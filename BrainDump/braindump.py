#!/usr/bin/env python3
"""
BrainDump: Daily Idea Collation System
Simple interface for capturing and organizing ideas with AI assistance.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

from agents.categorizer import CategorizerAgent
from agents.pattern_detector import PatternDetector
from agents.opportunity_suggester import OpportunitySuggester
from agents.trainer import TrainerAgent
from agents.ai_conversation import AIConversationAgent

class BrainDump:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.data_dir = self.base_dir / "data"
        self.ensure_data_structure()

        # Initialize agents
        self.categorizer = CategorizerAgent(self.data_dir)
        self.pattern_detector = PatternDetector(self.data_dir)
        self.opportunity_suggester = OpportunitySuggester(self.data_dir)
        self.trainer = TrainerAgent(self.data_dir)
        self.ai_conversation = AIConversationAgent(self.data_dir)

    def ensure_data_structure(self):
        """Create necessary data files if they don't exist."""
        self.data_dir.mkdir(exist_ok=True)

        default_files = {
            "ideas.json": [],
            "categories.json": {
                "Business": {"color": "green", "description": "Business ideas and strategies"},
                "Technical": {"color": "blue", "description": "Code projects and technical solutions"},
                "France-Move": {"color": "purple", "description": "Ideas related to moving to France"},
                "Life": {"color": "orange", "description": "Personal insights and life improvements"},
                "Montolieu-Shop": {"color": "red", "description": "Ideas for paper/book/coffee shop in Montolieu"}
            },
            "patterns.json": [],
            "feedback.json": [],
            "opportunities.json": []
        }

        for filename, default_content in default_files.items():
            filepath = self.data_dir / filename
            if not filepath.exists():
                with open(filepath, 'w') as f:
                    json.dump(default_content, f, indent=2)

    def add_idea(self, text, category_hint=None):
        """Add a new idea to the system."""
        idea = {
            "id": self.generate_id(),
            "text": text,
            "timestamp": datetime.now().isoformat(),
            "category": None,
            "confidence": None,
            "tags": []
        }

        # Auto-categorize
        category, confidence = self.categorizer.categorize(text, category_hint)
        idea["category"] = category
        idea["confidence"] = confidence

        # Save idea
        ideas_file = self.data_dir / "ideas.json"
        with open(ideas_file, 'r') as f:
            ideas = json.load(f)

        ideas.append(idea)

        with open(ideas_file, 'w') as f:
            json.dump(ideas, f, indent=2)

        # Only show categorization feedback in non-conversational mode
        if not hasattr(self, '_in_conversation'):
            print(f"✓ Idea saved and categorized as '{category}' (confidence: {confidence:.1%})")
        return idea

    def generate_id(self):
        """Generate a unique ID for ideas."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def daily_checkin(self):
        """Interactive daily AI-powered brain dump session."""
        print("\n🧠 BrainDump AI Conversation")
        print("=" * 40)

        # Show recent patterns and opportunities briefly
        self.show_recent_insights()
        print()

        # Start conversational brain dump
        self.conversational_brain_dump()

        # Run analysis after session
        self.run_analysis()

    def conversational_brain_dump(self):
        """AI-powered conversational brain dumping session."""
        all_captured_ideas = []
        conversation_rounds = 0

        # Get opening prompt
        opening = self.ai_conversation.get_opening_prompt()
        print(f"🤖 {opening}")
        print("\n(You can type 'done' anytime to finish, or just share whatever's on your mind)")

        while conversation_rounds < 10:  # Max 10 rounds
            user_response = input("\n💭 ").strip()

            if not user_response or user_response.lower() in ['done', 'finished', 'that\'s all']:
                break

            conversation_rounds += 1

            # Extract and process ideas from response
            ideas, follow_up = self.ai_conversation.analyze_response_and_follow_up(user_response)

            # Save each extracted idea
            for idea_text in ideas:
                if len(idea_text.strip()) > 10:  # Meaningful ideas only
                    saved_idea = self.add_idea(idea_text)
                    all_captured_ideas.append(saved_idea)

            # Show what was captured
            if ideas:
                print(f"\n✓ Captured {len(ideas)} idea(s) from that thought")

            # Ask follow-up question if conversation should continue
            if (conversation_rounds < 8 and
                self.ai_conversation.should_continue_conversation(conversation_rounds, user_response)):
                print(f"\n🤖 {follow_up}")
            else:
                break

        # Closing message
        closing = self.ai_conversation.get_closing_message(len(all_captured_ideas))
        print(f"\n🤖 {closing}")

        return all_captured_ideas

    def show_prompts(self):
        """Show helpful prompts for idea generation."""
        prompts = [
            "🏪 Business: What could improve your Montolieu shop concept?",
            "💻 Technical: Any coding projects or tools you need?",
            "🇫🇷 France Move: What's on your mind about the transition?",
            "📚 Shop Inventory: Ideas for books, papers, or antique desks?",
            "☕ Cafe Concept: Coffee service or atmosphere ideas?",
            "🎯 Life: Personal insights or improvements?",
            "🤝 Connections: Who could help with your goals?"
        ]

        print("\n" + "─" * 50)
        print("💭 Idea Prompts:")
        for prompt in prompts:
            print(f"   {prompt}")
        print("─" * 50)

    def show_recent_insights(self):
        """Display recent patterns and opportunities."""
        patterns = self.pattern_detector.get_recent_patterns(days=7)
        opportunities = self.opportunity_suggester.get_opportunities()

        if patterns:
            print("📊 Recent Patterns:")
            for pattern in patterns[:3]:
                print(f"   • {pattern['description']}")

        if opportunities:
            print("🎯 Opportunities:")
            for opp in opportunities[:2]:
                print(f"   • {opp['description']}")

    def request_feedback(self):
        """Ask user for feedback on the last categorization."""
        feedback = input("Was that categorization correct? (y/n/category_name): ").strip().lower()

        if feedback and feedback != 'y':
            self.trainer.record_feedback(feedback)

    def run_analysis(self):
        """Run pattern detection and opportunity analysis."""
        print("\n🔍 Analyzing ideas...")

        patterns = self.pattern_detector.detect_patterns()
        opportunities = self.opportunity_suggester.find_opportunities()

        if patterns:
            print(f"   Found {len(patterns)} new patterns")

        if opportunities:
            print(f"   Identified {len(opportunities)} opportunities")

        print("✓ Analysis complete")

    def quick_add(self, idea_text):
        """Quick add mode for single ideas."""
        idea = self.add_idea(idea_text)
        print(f"✓ Idea saved and categorized as '{idea['category']}' (confidence: {idea['confidence']:.1%})")
        self.run_analysis()
        return idea

def main():
    """Main entry point."""
    brain_dump = BrainDump()

    if len(sys.argv) > 1:
        # Quick add mode
        idea_text = " ".join(sys.argv[1:])
        brain_dump.quick_add(idea_text)
    else:
        # Interactive check-in mode
        brain_dump.daily_checkin()

if __name__ == "__main__":
    main()
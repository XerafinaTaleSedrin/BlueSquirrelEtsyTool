"""
AI Conversation Agent: Manages natural conversation flow for brain dumping sessions.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

class AIConversationAgent:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.conversation_starters = self._load_conversation_starters()
        self.follow_up_patterns = self._load_follow_up_patterns()

    def _load_conversation_starters(self) -> List[str]:
        """Load conversation starters for brain dumping sessions."""
        return [
            "What's been on your mind lately?",
            "What are you thinking about today?",
            "What's capturing your attention right now?",
            "What's been bouncing around in your head?",
            "What thoughts have been percolating?",
            "What's been occupying your mental space?",
            "What ideas have been brewing?",
            "What's been stirring in your thoughts today?",
        ]

    def _load_follow_up_patterns(self) -> Dict[str, List[str]]:
        """Load follow-up question patterns based on content themes."""
        return {
            "business": [
                "Tell me more about that business idea - what's the core concept?",
                "What's driving that business thought? Any specific opportunity you're seeing?",
                "How does that connect to your Montolieu shop vision?",
                "What would success look like for that idea?",
            ],
            "france": [
                "What aspect of the France move is on your mind?",
                "How are you feeling about that part of the transition?",
                "What's the timeline looking like for that?",
                "What would help you feel more prepared for that?",
            ],
            "montolieu": [
                "That sounds interesting for the shop - tell me more.",
                "How do you envision that fitting into the Montolieu experience?",
                "What inspired that shop-related thought?",
                "How would that enhance the customer experience?",
            ],
            "technical": [
                "What kind of technical solution are you envisioning?",
                "How would that tool or system work?",
                "What problem would that solve for you?",
                "Any specific technology you're thinking about using?",
            ],
            "challenge": [
                "What's making that challenging right now?",
                "What would need to happen to move that forward?",
                "Have you encountered something similar before?",
                "What resources might help with that?",
            ],
            "opportunity": [
                "What makes that opportunity exciting?",
                "What would be the first step to explore that?",
                "How does that align with your other goals?",
                "What's the potential impact of that idea?",
            ],
            "general": [
                "What else is connected to that thought?",
                "How long have you been thinking about this?",
                "What triggered that line of thinking?",
                "Is there more to explore there?",
            ]
        }

    def get_opening_prompt(self) -> str:
        """Get a natural conversation starter."""
        import random
        starter = random.choice(self.conversation_starters)

        # Add context based on recent activity
        context = self._get_conversation_context()
        if context:
            return f"{starter}\n\n{context}"

        return starter

    def _get_conversation_context(self) -> str:
        """Generate contextual opening based on recent patterns or opportunities."""
        try:
            # Check for recent patterns or opportunities to mention
            patterns_file = self.data_dir / "patterns.json"
            opportunities_file = self.data_dir / "opportunities.json"

            context_parts = []

            # Recent patterns
            if patterns_file.exists():
                with open(patterns_file, 'r') as f:
                    patterns = json.load(f)
                    recent_patterns = [p for p in patterns if self._is_recent(p.get('detected_at', ''))]
                    if recent_patterns:
                        latest_pattern = recent_patterns[0]
                        context_parts.append(f"I noticed you've been thinking a lot about {latest_pattern.get('description', '').lower()}")

            # Recent opportunities
            if opportunities_file.exists():
                with open(opportunities_file, 'r') as f:
                    opportunities = json.load(f)
                    if opportunities:
                        latest_opp = opportunities[0]
                        if latest_opp.get('priority') == 'high':
                            context_parts.append(f"There might be a good opportunity around {latest_opp.get('description', '')[:50]}...")

            return " • ".join(context_parts) if context_parts else ""

        except (FileNotFoundError, json.JSONDecodeError):
            return ""

    def analyze_response_and_follow_up(self, response: str) -> Tuple[List[str], str]:
        """Analyze user response and generate appropriate follow-up questions."""
        response_lower = response.lower()

        # Extract potential ideas from the response
        ideas = self._extract_ideas_from_response(response)

        # Determine the theme/category of the response
        theme = self._detect_response_theme(response_lower)

        # Generate follow-up question
        follow_up = self._generate_follow_up_question(theme, response)

        return ideas, follow_up

    def _extract_ideas_from_response(self, response: str) -> List[str]:
        """Extract individual ideas from a brain dump response."""
        ideas = []

        # Split by common separators
        separators = ['. ', '.\n', ', and ', ' and ', ' also ', ' plus ', ' another thing ']

        current_text = response
        for separator in separators:
            if separator in current_text:
                parts = current_text.split(separator)
                current_text = parts[0]  # Keep first part
                for part in parts[1:]:
                    if len(part.strip()) > 10:  # Meaningful length
                        ideas.append(part.strip())

        # Add the main/first idea
        if len(current_text.strip()) > 10:
            ideas.insert(0, current_text.strip())

        # Look for bullet points or numbered lists
        bullet_patterns = [r'^\d+\.', r'^[-•*]', r'^\([a-z]\)']
        lines = response.split('\n')
        for line in lines:
            line = line.strip()
            if any(re.match(pattern, line) for pattern in bullet_patterns):
                clean_line = re.sub(r'^(\d+\.|[-•*]|\([a-z]\))\s*', '', line).strip()
                if len(clean_line) > 10:
                    ideas.append(clean_line)

        # Remove duplicates while preserving order
        seen = set()
        unique_ideas = []
        for idea in ideas:
            if idea.lower() not in seen and len(idea) > 10:
                unique_ideas.append(idea)
                seen.add(idea.lower())

        return unique_ideas[:10]  # Limit to 10 ideas max

    def _detect_response_theme(self, response_lower: str) -> str:
        """Detect the main theme of the user's response."""
        theme_keywords = {
            "montolieu": ["montolieu", "shop", "bookstore", "cafe", "coffee", "paper", "stationery", "antique", "desk"],
            "france": ["france", "french", "move", "moving", "visa", "relocation", "housing", "bureaucracy"],
            "business": ["business", "revenue", "customer", "profit", "marketing", "sales", "strategy"],
            "technical": ["code", "programming", "website", "app", "tool", "software", "system"],
            "challenge": ["problem", "difficult", "challenge", "stuck", "confused", "worried", "concern"],
            "opportunity": ["opportunity", "idea", "could", "might", "potential", "exciting", "interesting"]
        }

        theme_scores = {}
        for theme, keywords in theme_keywords.items():
            score = sum(1 for keyword in keywords if keyword in response_lower)
            if score > 0:
                theme_scores[theme] = score

        if theme_scores:
            return max(theme_scores, key=theme_scores.get)

        return "general"

    def _generate_follow_up_question(self, theme: str, original_response: str) -> str:
        """Generate an appropriate follow-up question based on theme and content."""
        import random

        follow_ups = self.follow_up_patterns.get(theme, self.follow_up_patterns["general"])

        # Add some variety and personalization
        base_question = random.choice(follow_ups)

        # Add contextual elements for Montolieu-specific responses
        if theme == "montolieu" and "inventory" in original_response.lower():
            return "What kind of inventory items are you thinking about? Books, papers, or the antique desks?"
        elif theme == "france" and "timing" in original_response.lower():
            return "What's your ideal timeline looking like for that part of the move?"
        elif theme == "business" and "customer" in original_response.lower():
            return "What do you think customers would find most appealing about that idea?"

        return base_question

    def should_continue_conversation(self, responses_so_far: int, last_response: str) -> bool:
        """Determine if conversation should continue based on engagement."""
        if responses_so_far >= 10:  # Max conversation length
            return False

        if len(last_response.strip()) < 5:  # Very short responses suggest ending
            return False

        # Look for conversation ending signals
        ending_signals = ["that's all", "that's it", "nothing else", "i'm done", "no more", "finished"]
        if any(signal in last_response.lower() for signal in ending_signals):
            return False

        return True

    def get_closing_message(self, ideas_captured: int) -> str:
        """Generate a nice closing message."""
        messages = [
            f"Great brain dump! I captured {ideas_captured} ideas to organize and analyze.",
            f"Thanks for sharing your thoughts! {ideas_captured} ideas captured and categorized.",
            f"Perfect session - {ideas_captured} ideas collected. Let me analyze these for patterns and opportunities.",
            f"Excellent! {ideas_captured} ideas saved. I'll look for connections and opportunities in these thoughts."
        ]

        import random
        return random.choice(messages)

    def _is_recent(self, timestamp: str, days: int = 3) -> bool:
        """Check if timestamp is recent."""
        try:
            from datetime import timedelta
            if not timestamp:
                return False
            date = datetime.fromisoformat(timestamp)
            cutoff = datetime.now() - timedelta(days=days)
            return date >= cutoff
        except:
            return False
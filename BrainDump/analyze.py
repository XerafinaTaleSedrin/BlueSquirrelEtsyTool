#!/usr/bin/env python3
"""
BrainDump Analysis Script: Generate reports and insights from collected ideas.
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter

from agents.categorizer import CategorizerAgent
from agents.pattern_detector import PatternDetector
from agents.opportunity_suggester import OpportunitySuggester
from agents.trainer import TrainerAgent

class BrainDumpAnalyzer:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.data_dir = self.base_dir / "data"

        # Initialize agents
        self.categorizer = CategorizerAgent(self.data_dir)
        self.pattern_detector = PatternDetector(self.data_dir)
        self.opportunity_suggester = OpportunitySuggester(self.data_dir)
        self.trainer = TrainerAgent(self.data_dir)

    def generate_full_report(self):
        """Generate a comprehensive analysis report."""
        print("🧠 BrainDump Analysis Report")
        print("=" * 60)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Ideas overview
        self.show_ideas_overview()
        print()

        # Category analysis
        self.show_category_analysis()
        print()

        # Pattern analysis
        self.show_pattern_analysis()
        print()

        # Opportunity analysis
        self.show_opportunity_analysis()
        print()

        # Montolieu goal progress
        self.show_montolieu_progress()
        print()

        # Training status
        self.show_training_status()

    def show_ideas_overview(self):
        """Show overview of all ideas."""
        print("📊 Ideas Overview")
        print("-" * 30)

        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            if not ideas:
                print("No ideas captured yet.")
                return

            total_ideas = len(ideas)
            print(f"Total ideas: {total_ideas}")

            # Time analysis
            now = datetime.now()
            recent_ideas = [i for i in ideas if self._is_recent(i['timestamp'], 7)]
            print(f"Ideas this week: {len(recent_ideas)}")

            # Latest idea
            latest = max(ideas, key=lambda x: x['timestamp'])
            latest_date = datetime.fromisoformat(latest['timestamp']).strftime('%Y-%m-%d %H:%M')
            print(f"Latest idea: {latest_date}")
            print(f"  '{latest['text'][:80]}...'")

        except FileNotFoundError:
            print("No ideas file found.")

    def show_category_analysis(self):
        """Show category distribution and statistics."""
        print("📁 Category Analysis")
        print("-" * 30)

        stats = self.categorizer.get_category_stats()

        if not stats:
            print("No categorized ideas yet.")
            return

        total = sum(stats.values())
        for category, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total) * 100
            print(f"{category:15} {count:3d} ({percentage:5.1f}%)")

        # Suggest recategorizations
        suggestions = self.categorizer.suggest_recategorization()
        if suggestions:
            print("\n💡 Recategorization Suggestions:")
            for suggestion in suggestions[:3]:
                print(f"  • '{suggestion['text']}' → {suggestion['suggested_category']}")

    def show_pattern_analysis(self):
        """Show detected patterns."""
        print("🔍 Pattern Analysis")
        print("-" * 30)

        patterns = self.pattern_detector.get_recent_patterns(30)

        if not patterns:
            print("No patterns detected yet.")
            return

        # Group by type
        by_type = {}
        for pattern in patterns:
            pattern_type = pattern['type']
            if pattern_type not in by_type:
                by_type[pattern_type] = []
            by_type[pattern_type].append(pattern)

        for pattern_type, type_patterns in by_type.items():
            print(f"\n{pattern_type.title()} Patterns:")
            for pattern in type_patterns[:3]:  # Top 3 per type
                print(f"  • {pattern['description']}")

    def show_opportunity_analysis(self):
        """Show identified opportunities."""
        print("🎯 Opportunity Analysis")
        print("-" * 30)

        opportunities = self.opportunity_suggester.get_opportunities(10)

        if not opportunities:
            print("No opportunities identified yet.")
            return

        # Group by priority
        by_priority = {'high': [], 'medium': [], 'low': []}
        for opp in opportunities:
            priority = opp.get('priority', 'low')
            by_priority[priority].append(opp)

        for priority in ['high', 'medium', 'low']:
            if by_priority[priority]:
                print(f"\n{priority.title()} Priority:")
                for opp in by_priority[priority][:3]:
                    print(f"  • {opp['description']}")

    def show_montolieu_progress(self):
        """Show progress toward Montolieu shop goals."""
        print("🏪 Montolieu Shop Goal Progress")
        print("-" * 40)

        progress = self.opportunity_suggester.get_goal_progress()

        if not progress:
            print("No goal-related ideas yet.")
            return

        for goal_key, goal_data in progress.items():
            idea_count = goal_data['idea_count']
            priority = goal_data['priority']
            print(f"\n{goal_data['description']} ({priority} priority)")
            print(f"  Ideas: {idea_count}")

            if goal_data['related_ideas']:
                print("  Recent:")
                for idea in goal_data['related_ideas'][:2]:
                    print(f"    • {idea['text']}")

    def show_training_status(self):
        """Show training and feedback status."""
        print("🎓 Training Status")
        print("-" * 25)

        feedback_summary = self.trainer.get_feedback_summary()
        total_feedback = feedback_summary.get('total', 0)

        if total_feedback == 0:
            print("No feedback received yet.")
            print("💡 Provide feedback on categorizations to improve accuracy!")
            return

        print(f"Total feedback: {total_feedback}")

        by_type = feedback_summary.get('by_type', {})
        for feedback_type, count in by_type.items():
            print(f"  {feedback_type}: {count}")

        # Show improvement suggestions
        suggestions = self.trainer.suggest_improvements()
        if suggestions:
            print("\nSuggestions:")
            for suggestion in suggestions:
                print(f"  • {suggestion}")

    def _is_recent(self, timestamp: str, days: int) -> bool:
        """Check if timestamp is within recent days."""
        try:
            idea_date = datetime.fromisoformat(timestamp)
            cutoff = datetime.now() - timedelta(days=days)
            return idea_date >= cutoff
        except:
            return False

    def export_data(self, format_type: str = 'json'):
        """Export all data in specified format."""
        if format_type.lower() != 'json':
            print("Only JSON export currently supported.")
            return

        export_data = {
            'metadata': {
                'export_date': datetime.now().isoformat(),
                'version': '1.0'
            },
            'ideas': self._load_json_file('ideas.json'),
            'categories': self._load_json_file('categories.json'),
            'patterns': self._load_json_file('patterns.json'),
            'opportunities': self._load_json_file('opportunities.json'),
            'feedback': self._load_json_file('feedback.json'),
            'training_data': self.trainer.export_training_data()
        }

        export_file = self.data_dir / f"braindump_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(export_file, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"Data exported to: {export_file}")

    def _load_json_file(self, filename: str):
        """Safely load a JSON file."""
        try:
            with open(self.data_dir / filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def quick_stats(self):
        """Show quick statistics."""
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            total = len(ideas)
            recent = len([i for i in ideas if self._is_recent(i['timestamp'], 7)])

            categories = Counter(i.get('category', 'Unknown') for i in ideas)
            top_category = categories.most_common(1)[0] if categories else ('None', 0)

            print(f"Ideas: {total} total, {recent} this week")
            print(f"Top category: {top_category[0]} ({top_category[1]})")

            opportunities = self.opportunity_suggester.get_opportunities(3)
            print(f"Opportunities: {len(opportunities)}")

        except FileNotFoundError:
            print("No data found. Run 'python braindump.py' to start collecting ideas!")

def main():
    """Main entry point."""
    analyzer = BrainDumpAnalyzer()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == 'report':
            analyzer.generate_full_report()
        elif command == 'export':
            analyzer.export_data()
        elif command == 'stats':
            analyzer.quick_stats()
        else:
            print("Usage: python analyze.py [report|export|stats]")
    else:
        analyzer.quick_stats()

if __name__ == "__main__":
    main()
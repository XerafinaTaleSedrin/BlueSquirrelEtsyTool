"""
Trainer Agent: Learns from user feedback to improve categorization and suggestions.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

class TrainerAgent:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.feedback_file = data_dir / "feedback.json"

    def record_feedback(self, feedback: str, idea_id: str = None):
        """Record user feedback on categorization or suggestions."""
        timestamp = datetime.now().isoformat()

        feedback_entry = {
            'timestamp': timestamp,
            'feedback': feedback,
            'idea_id': idea_id,
            'type': self._classify_feedback(feedback)
        }

        # Load existing feedback
        try:
            with open(self.feedback_file, 'r') as f:
                all_feedback = json.load(f)
        except FileNotFoundError:
            all_feedback = []

        all_feedback.append(feedback_entry)

        # Save updated feedback
        with open(self.feedback_file, 'w') as f:
            json.dump(all_feedback, f, indent=2)

        # Apply feedback immediately if possible
        self._apply_feedback(feedback_entry)

    def _classify_feedback(self, feedback: str) -> str:
        """Classify the type of feedback."""
        feedback_lower = feedback.lower()

        if feedback_lower in ['n', 'no', 'wrong', 'incorrect']:
            return 'negative'
        elif feedback_lower in ['y', 'yes', 'correct', 'good']:
            return 'positive'
        elif any(cat in feedback_lower for cat in ['business', 'technical', 'france', 'life', 'montolieu']):
            return 'recategorization'
        else:
            return 'other'

    def _apply_feedback(self, feedback_entry: Dict):
        """Apply feedback to improve future categorizations."""
        feedback_type = feedback_entry['type']
        feedback_text = feedback_entry['feedback'].lower()

        if feedback_type == 'recategorization':
            self._learn_category_correction(feedback_entry)
        elif feedback_type == 'negative':
            self._record_categorization_error(feedback_entry)

    def _learn_category_correction(self, feedback_entry: Dict):
        """Learn from category corrections."""
        idea_id = feedback_entry.get('idea_id')
        if not idea_id:
            return

        # Find the original idea
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            idea = next((i for i in ideas if i['id'] == idea_id), None)
            if not idea:
                return

            # Update the idea's category based on feedback
            new_category = self._extract_category_from_feedback(feedback_entry['feedback'])
            if new_category:
                idea['category'] = new_category
                idea['confidence'] = 0.9  # High confidence from user correction
                idea['user_corrected'] = True

                # Save updated ideas
                with open(self.data_dir / "ideas.json", 'w') as f:
                    json.dump(ideas, f, indent=2)

                # Record this correction for future learning
                self._record_category_rule(idea['text'], new_category)

        except FileNotFoundError:
            pass

    def _extract_category_from_feedback(self, feedback: str) -> Optional[str]:
        """Extract category name from user feedback."""
        feedback_lower = feedback.lower()

        category_mappings = {
            'business': 'Business',
            'technical': 'Technical',
            'tech': 'Technical',
            'france': 'France-Move',
            'life': 'Life',
            'montolieu': 'Montolieu-Shop',
            'shop': 'Montolieu-Shop'
        }

        for key, category in category_mappings.items():
            if key in feedback_lower:
                return category

        return None

    def _record_categorization_error(self, feedback_entry: Dict):
        """Record when categorization was wrong to learn patterns."""
        # This could be used to identify systematic categorization errors
        pass

    def _record_category_rule(self, text: str, category: str):
        """Record a new categorization rule based on user correction."""
        rules_file = self.data_dir / "learned_rules.json"

        try:
            with open(rules_file, 'r') as f:
                rules = json.load(f)
        except FileNotFoundError:
            rules = []

        # Extract key phrases from the text that might be category indicators
        words = text.lower().split()
        key_phrases = []

        # Look for meaningful 2-3 word phrases
        for i in range(len(words) - 1):
            phrase = f"{words[i]} {words[i+1]}"
            if len(phrase) > 5:  # Meaningful length
                key_phrases.append(phrase)

        if key_phrases:
            rule = {
                'category': category,
                'indicators': key_phrases[:3],  # Top 3 phrases
                'learned_from': text[:100] + "..." if len(text) > 100 else text,
                'timestamp': datetime.now().isoformat()
            }

            rules.append(rule)

            with open(rules_file, 'w') as f:
                json.dump(rules, f, indent=2)

    def get_learned_rules(self) -> List[Dict]:
        """Get all learned categorization rules."""
        rules_file = self.data_dir / "learned_rules.json"

        try:
            with open(rules_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def get_feedback_summary(self) -> Dict:
        """Get a summary of all feedback received."""
        try:
            with open(self.feedback_file, 'r') as f:
                all_feedback = json.load(f)

            if not all_feedback:
                return {'total': 0}

            feedback_types = {}
            for feedback in all_feedback:
                feedback_type = feedback.get('type', 'unknown')
                feedback_types[feedback_type] = feedback_types.get(feedback_type, 0) + 1

            recent_feedback = [f for f in all_feedback if self._is_recent(f['timestamp'])]

            return {
                'total': len(all_feedback),
                'recent_count': len(recent_feedback),
                'by_type': feedback_types,
                'recent_feedback': recent_feedback[-5:]  # Last 5 feedback items
            }

        except FileNotFoundError:
            return {'total': 0}

    def _is_recent(self, timestamp: str, days: int = 7) -> bool:
        """Check if timestamp is within recent days."""
        try:
            feedback_date = datetime.fromisoformat(timestamp)
            cutoff = datetime.now() - datetime.timedelta(days=days)
            return feedback_date >= cutoff
        except:
            return False

    def suggest_improvements(self) -> List[str]:
        """Suggest improvements based on feedback patterns."""
        feedback_summary = self.get_feedback_summary()
        suggestions = []

        if feedback_summary.get('total', 0) == 0:
            return ["No feedback received yet. Use the system more to provide training data."]

        # Analyze feedback patterns
        negative_feedback = feedback_summary.get('by_type', {}).get('negative', 0)
        total_feedback = feedback_summary.get('total', 1)

        if negative_feedback / total_feedback > 0.3:
            suggestions.append("High rate of incorrect categorizations detected. Consider reviewing keyword patterns.")

        recategorizations = feedback_summary.get('by_type', {}).get('recategorization', 0)
        if recategorizations > 0:
            suggestions.append(f"Learned {recategorizations} new categorization rules from your corrections.")

        recent_count = feedback_summary.get('recent_count', 0)
        if recent_count < 5:
            suggestions.append("More feedback would help improve accuracy. Consider correcting categorizations when they're wrong.")

        learned_rules = self.get_learned_rules()
        if len(learned_rules) > 10:
            suggestions.append("System has learned many rules. Consider reviewing learned patterns for accuracy.")

        return suggestions if suggestions else ["System is learning well from your feedback!"]

    def export_training_data(self) -> Dict:
        """Export all training data for analysis or backup."""
        data = {
            'feedback': self.get_feedback_summary(),
            'learned_rules': self.get_learned_rules(),
            'export_timestamp': datetime.now().isoformat()
        }

        return data
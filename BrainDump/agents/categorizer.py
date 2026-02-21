"""
Categorizer Agent: Auto-categorizes ideas based on content and context.
"""

import json
import re
from pathlib import Path
from typing import Tuple, List, Dict

class CategorizerAgent:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.load_categories()
        self.load_keywords()

    def load_categories(self):
        """Load category definitions."""
        with open(self.data_dir / "categories.json", 'r') as f:
            self.categories = json.load(f)

    def load_keywords(self):
        """Define keyword patterns for each category."""
        self.keywords = {
            "Business": [
                r'\b(?:business|revenue|profit|customers|marketing|sales|pricing|strategy|competition|market)\b',
                r'\b(?:income|money|financial|investment|roi|budget|cost|pricing)\b',
                r'\b(?:service|product|offering|value|proposition)\b'
            ],
            "Technical": [
                r'\b(?:code|programming|python|javascript|html|css|database|api|software|app)\b',
                r'\b(?:framework|library|tool|algorithm|debug|optimize|refactor)\b',
                r'\b(?:server|deployment|hosting|git|version|testing)\b'
            ],
            "France-Move": [
                r'\b(?:france|french|visa|immigration|residency|citizenship|relocation)\b',
                r'\b(?:moving|relocating|transition|settling|adaptation)\b',
                r'\b(?:language|culture|bureaucracy|paperwork|legal)\b',
                r'\b(?:house|apartment|rental|neighborhood|area)\b'
            ],
            "Montolieu-Shop": [
                r'\b(?:montolieu|shop|store|bookstore|cafe|coffee|paper|stationery)\b',
                r'\b(?:antique|vintage|desk|furniture|restoration|books|used books)\b',
                r'\b(?:inventory|supplies|vendors|suppliers|local|artisan)\b',
                r'\b(?:customer|atmosphere|ambiance|cozy|charm|experience)\b'
            ],
            "Life": [
                r'\b(?:personal|health|wellness|habits|routine|goals|self-improvement)\b',
                r'\b(?:family|friends|relationships|social|community)\b',
                r'\b(?:hobbies|interests|learning|skills|education|growth)\b'
            ]
        }

    def categorize(self, text: str, hint: str = None) -> Tuple[str, float]:
        """Categorize an idea based on its content."""
        text_lower = text.lower()

        # If user provided a hint, try to match it first
        if hint:
            if hint.title() in self.categories:
                return hint.title(), 0.9

        # Score each category
        scores = {}
        for category, patterns in self.keywords.items():
            score = 0
            for pattern in patterns:
                matches = len(re.findall(pattern, text_lower, re.IGNORECASE))
                score += matches

            # Normalize score
            if score > 0:
                scores[category] = min(score / len(patterns), 1.0)

        # Apply context-based boosting
        scores = self._apply_context_boosting(text_lower, scores)

        if not scores:
            return "Life", 0.3  # Default category

        # Get best match
        best_category = max(scores, key=scores.get)
        confidence = scores[best_category]

        return best_category, confidence

    def _apply_context_boosting(self, text: str, scores: Dict[str, float]) -> Dict[str, float]:
        """Apply contextual boosting based on common idea patterns."""

        # Boost France-related ideas that mention practical concerns
        if any(word in text for word in ['need to', 'must', 'important', 'urgent', 'deadline']):
            if 'France-Move' in scores:
                scores['France-Move'] *= 1.3

        # Boost business ideas that mention the shop specifically
        if any(word in text for word in ['shop', 'store', 'customer', 'sell', 'buy']):
            if 'Montolieu-Shop' in scores:
                scores['Montolieu-Shop'] *= 1.2
            elif 'Business' in scores:
                scores['Business'] *= 1.1

        # Boost technical ideas that mention building or creating
        if any(word in text for word in ['build', 'create', 'make', 'develop', 'implement']):
            if 'Technical' in scores:
                scores['Technical'] *= 1.1

        # Cross-category connections
        if 'france' in text and 'shop' in text:
            # Ideas that combine France and shop concerns
            scores['Montolieu-Shop'] = scores.get('Montolieu-Shop', 0) + 0.5

        return scores

    def get_category_stats(self) -> Dict[str, int]:
        """Get statistics on idea categories."""
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            stats = {}
            for idea in ideas:
                category = idea.get('category', 'Unknown')
                stats[category] = stats.get(category, 0) + 1

            return stats
        except FileNotFoundError:
            return {}

    def suggest_recategorization(self) -> List[Dict]:
        """Suggest ideas that might be miscategorized."""
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            suggestions = []
            for idea in ideas:
                current_category = idea.get('category')
                confidence = idea.get('confidence', 0)

                # Re-analyze with current rules
                new_category, new_confidence = self.categorize(idea['text'])

                if (new_category != current_category and
                    new_confidence > confidence + 0.2):
                    suggestions.append({
                        'id': idea['id'],
                        'text': idea['text'][:100] + "..." if len(idea['text']) > 100 else idea['text'],
                        'current_category': current_category,
                        'suggested_category': new_category,
                        'confidence_improvement': new_confidence - confidence
                    })

            return sorted(suggestions, key=lambda x: x['confidence_improvement'], reverse=True)

        except FileNotFoundError:
            return []
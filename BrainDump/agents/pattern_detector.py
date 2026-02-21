"""
Pattern Detector Agent: Identifies recurring themes and connections between ideas.
"""

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Set

class PatternDetector:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def detect_patterns(self) -> List[Dict]:
        """Detect patterns in recent ideas."""
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            patterns = []

            # Detect frequency patterns
            patterns.extend(self._detect_frequency_patterns(ideas))

            # Detect keyword clusters
            patterns.extend(self._detect_keyword_clusters(ideas))

            # Detect category trends
            patterns.extend(self._detect_category_trends(ideas))

            # Detect temporal patterns
            patterns.extend(self._detect_temporal_patterns(ideas))

            # Save patterns
            self._save_patterns(patterns)

            return patterns

        except FileNotFoundError:
            return []

    def _detect_frequency_patterns(self, ideas: List[Dict]) -> List[Dict]:
        """Detect frequently mentioned concepts."""
        patterns = []

        # Extract key phrases (2-3 words)
        all_text = " ".join([idea['text'].lower() for idea in ideas])
        words = re.findall(r'\b\w+\b', all_text)

        # Find common bigrams and trigrams
        bigrams = []
        trigrams = []

        for i in range(len(words) - 1):
            bigrams.append(f"{words[i]} {words[i+1]}")

        for i in range(len(words) - 2):
            trigrams.append(f"{words[i]} {words[i+1]} {words[i+2]}")

        # Count frequencies
        bigram_counts = Counter(bigrams)
        trigram_counts = Counter(trigrams)

        # Filter out common/meaningless phrases
        stop_phrases = {
            'i think', 'i need', 'i want', 'i should', 'i could',
            'it would', 'would be', 'need to', 'want to', 'have to'
        }

        for phrase, count in bigram_counts.items():
            if count >= 3 and phrase not in stop_phrases:
                patterns.append({
                    'type': 'frequency',
                    'description': f"'{phrase}' mentioned {count} times",
                    'frequency': count,
                    'phrase': phrase,
                    'significance': 'high' if count >= 5 else 'medium'
                })

        return patterns[:5]  # Top 5 patterns

    def _detect_keyword_clusters(self, ideas: List[Dict]) -> List[Dict]:
        """Detect clusters of related keywords."""
        patterns = []

        # France/Business clusters
        france_keywords = ['france', 'french', 'visa', 'move', 'relocate', 'montolieu']
        business_keywords = ['shop', 'business', 'customer', 'sell', 'revenue', 'profit']
        tech_keywords = ['code', 'python', 'app', 'website', 'database', 'api']

        clusters = {
            'France Transition': france_keywords,
            'Business Development': business_keywords,
            'Technical Projects': tech_keywords
        }

        for cluster_name, keywords in clusters.items():
            cluster_ideas = []
            for idea in ideas:
                text_lower = idea['text'].lower()
                if any(keyword in text_lower for keyword in keywords):
                    cluster_ideas.append(idea)

            if len(cluster_ideas) >= 3:
                patterns.append({
                    'type': 'cluster',
                    'description': f"{cluster_name}: {len(cluster_ideas)} related ideas",
                    'cluster_name': cluster_name,
                    'idea_count': len(cluster_ideas),
                    'significance': 'high' if len(cluster_ideas) >= 5 else 'medium'
                })

        return patterns

    def _detect_category_trends(self, ideas: List[Dict]) -> List[Dict]:
        """Detect trends in category distribution over time."""
        patterns = []

        # Group ideas by category and time
        now = datetime.now()
        recent_cutoff = now - timedelta(days=7)
        older_cutoff = now - timedelta(days=14)

        recent_categories = Counter()
        older_categories = Counter()

        for idea in ideas:
            idea_date = datetime.fromisoformat(idea['timestamp'])
            category = idea.get('category', 'Unknown')

            if idea_date >= recent_cutoff:
                recent_categories[category] += 1
            elif idea_date >= older_cutoff:
                older_categories[category] += 1

        # Find growing categories
        for category in recent_categories:
            recent_count = recent_categories[category]
            older_count = older_categories.get(category, 0)

            if recent_count > older_count and recent_count >= 3:
                growth = recent_count - older_count
                patterns.append({
                    'type': 'trend',
                    'description': f"Increased focus on {category} ({growth} more ideas this week)",
                    'category': category,
                    'growth': growth,
                    'significance': 'high' if growth >= 3 else 'medium'
                })

        return patterns

    def _detect_temporal_patterns(self, ideas: List[Dict]) -> List[Dict]:
        """Detect patterns in when ideas are generated."""
        patterns = []

        if len(ideas) < 10:
            return patterns

        # Analyze time of day patterns
        hours = []
        for idea in ideas:
            idea_date = datetime.fromisoformat(idea['timestamp'])
            hours.append(idea_date.hour)

        hour_counts = Counter(hours)
        peak_hour = hour_counts.most_common(1)[0]

        if peak_hour[1] >= 3:
            time_desc = self._get_time_description(peak_hour[0])
            patterns.append({
                'type': 'temporal',
                'description': f"Most ideas generated in the {time_desc} ({peak_hour[1]} ideas)",
                'peak_hour': peak_hour[0],
                'count': peak_hour[1],
                'significance': 'medium'
            })

        return patterns

    def _get_time_description(self, hour: int) -> str:
        """Convert hour to descriptive time period."""
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 21:
            return "evening"
        else:
            return "night"

    def _save_patterns(self, patterns: List[Dict]):
        """Save detected patterns to file."""
        pattern_file = self.data_dir / "patterns.json"

        # Add timestamp to each pattern
        timestamp = datetime.now().isoformat()
        for pattern in patterns:
            pattern['detected_at'] = timestamp

        try:
            with open(pattern_file, 'r') as f:
                existing_patterns = json.load(f)
        except FileNotFoundError:
            existing_patterns = []

        # Add new patterns
        existing_patterns.extend(patterns)

        # Keep only recent patterns (last 30 days)
        cutoff = datetime.now() - timedelta(days=30)
        recent_patterns = [
            p for p in existing_patterns
            if datetime.fromisoformat(p['detected_at']) >= cutoff
        ]

        with open(pattern_file, 'w') as f:
            json.dump(recent_patterns, f, indent=2)

    def get_recent_patterns(self, days: int = 7) -> List[Dict]:
        """Get patterns detected in the last N days."""
        try:
            with open(self.data_dir / "patterns.json", 'r') as f:
                patterns = json.load(f)

            cutoff = datetime.now() - timedelta(days=days)
            recent = [
                p for p in patterns
                if datetime.fromisoformat(p['detected_at']) >= cutoff
            ]

            return sorted(recent, key=lambda x: x['detected_at'], reverse=True)

        except FileNotFoundError:
            return []

    def get_pattern_summary(self) -> Dict:
        """Get a summary of all detected patterns."""
        patterns = self.get_recent_patterns(30)

        summary = {
            'total_patterns': len(patterns),
            'by_type': Counter(p['type'] for p in patterns),
            'by_significance': Counter(p['significance'] for p in patterns),
            'most_recent': patterns[:3] if patterns else []
        }

        return summary
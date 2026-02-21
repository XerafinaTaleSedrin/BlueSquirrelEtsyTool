"""
Opportunity Suggester Agent: Identifies actionable opportunities that align with Montolieu shop goals.
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Set

class OpportunitySuggester:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.montolieu_goals = self._define_montolieu_goals()

    def _define_montolieu_goals(self) -> Dict[str, Dict]:
        """Define key goals and success metrics for the Montolieu shop."""
        return {
            "inventory_sourcing": {
                "keywords": ["books", "paper", "stationery", "antique", "desk", "vintage", "supplier", "vendor"],
                "priority": "high",
                "description": "Finding reliable sources for shop inventory"
            },
            "customer_experience": {
                "keywords": ["atmosphere", "cozy", "coffee", "experience", "customer", "ambiance", "charm"],
                "priority": "high",
                "description": "Creating an appealing customer experience"
            },
            "local_connections": {
                "keywords": ["montolieu", "local", "community", "french", "artisan", "network", "collaborate"],
                "priority": "high",
                "description": "Building local community connections"
            },
            "business_operations": {
                "keywords": ["revenue", "pricing", "cost", "profit", "inventory", "accounting", "legal", "permits"],
                "priority": "medium",
                "description": "Establishing solid business operations"
            },
            "digital_presence": {
                "keywords": ["website", "online", "social", "marketing", "instagram", "facebook", "etsy"],
                "priority": "medium",
                "description": "Building online presence and marketing"
            },
            "personal_preparation": {
                "keywords": ["french", "language", "visa", "housing", "move", "relocation", "adaptation"],
                "priority": "medium",
                "description": "Personal preparation for France transition"
            }
        }

    def find_opportunities(self) -> List[Dict]:
        """Identify actionable opportunities from recent ideas."""
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            opportunities = []

            # Find direct goal alignment opportunities
            opportunities.extend(self._find_goal_alignment_opportunities(ideas))

            # Find connection opportunities
            opportunities.extend(self._find_connection_opportunities(ideas))

            # Find timing-sensitive opportunities
            opportunities.extend(self._find_timing_opportunities(ideas))

            # Find resource gap opportunities
            opportunities.extend(self._find_resource_gaps(ideas))

            # Remove duplicates and sort by priority
            opportunities = self._deduplicate_and_prioritize(opportunities)

            # Save opportunities
            self._save_opportunities(opportunities)

            return opportunities

        except FileNotFoundError:
            return []

    def _find_goal_alignment_opportunities(self, ideas: List[Dict]) -> List[Dict]:
        """Find ideas that directly align with Montolieu shop goals."""
        opportunities = []

        for idea in ideas:
            text_lower = idea['text'].lower()

            for goal_key, goal_info in self.montolieu_goals.items():
                matches = sum(1 for keyword in goal_info['keywords'] if keyword in text_lower)

                if matches >= 2:  # Strong alignment
                    opportunities.append({
                        'type': 'goal_alignment',
                        'description': f"Pursue: {idea['text'][:100]}... (Supports {goal_info['description']})",
                        'goal': goal_key,
                        'priority': goal_info['priority'],
                        'idea_id': idea['id'],
                        'alignment_score': matches,
                        'actionable': True
                    })

        return opportunities

    def _find_connection_opportunities(self, ideas: List[Dict]) -> List[Dict]:
        """Find opportunities to connect seemingly unrelated ideas."""
        opportunities = []

        # Look for ideas that could be combined
        business_ideas = [i for i in ideas if i.get('category') == 'Business' or i.get('category') == 'Montolieu-Shop']
        tech_ideas = [i for i in ideas if i.get('category') == 'Technical']

        for business_idea in business_ideas:
            for tech_idea in tech_ideas:
                if self._could_ideas_connect(business_idea, tech_idea):
                    opportunities.append({
                        'type': 'connection',
                        'description': f"Combine tech solution with business need: '{tech_idea['text'][:50]}...' + '{business_idea['text'][:50]}...'",
                        'priority': 'medium',
                        'idea_ids': [business_idea['id'], tech_idea['id']],
                        'actionable': True
                    })

        return opportunities[:3]  # Limit to top 3 connections

    def _could_ideas_connect(self, idea1: Dict, idea2: Dict) -> bool:
        """Check if two ideas could be connected."""
        text1 = idea1['text'].lower()
        text2 = idea2['text'].lower()

        # Look for common themes
        common_keywords = ['customer', 'online', 'inventory', 'tracking', 'organize', 'manage', 'automate']

        return any(keyword in text1 and keyword in text2 for keyword in common_keywords)

    def _find_timing_opportunities(self, ideas: List[Dict]) -> List[Dict]:
        """Find opportunities that are time-sensitive or seasonal."""
        opportunities = []

        current_month = datetime.now().month
        current_season = self._get_season(current_month)

        seasonal_opportunities = {
            'winter': ['planning', 'research', 'online', 'preparation', 'learning'],
            'spring': ['networking', 'sourcing', 'connecting', 'exploring', 'testing'],
            'summer': ['travel', 'visit', 'experience', 'market research', 'vacation'],
            'autumn': ['implementation', 'launch', 'execution', 'action', 'moving']
        }

        season_keywords = seasonal_opportunities.get(current_season, [])

        for idea in ideas:
            text_lower = idea['text'].lower()
            if any(keyword in text_lower for keyword in season_keywords):
                opportunities.append({
                    'type': 'timing',
                    'description': f"Perfect timing for {current_season}: {idea['text'][:80]}...",
                    'season': current_season,
                    'priority': 'high',
                    'idea_id': idea['id'],
                    'actionable': True
                })

        return opportunities[:2]  # Limit to top 2 timing opportunities

    def _get_season(self, month: int) -> str:
        """Get current season based on month."""
        if month in [12, 1, 2]:
            return 'winter'
        elif month in [3, 4, 5]:
            return 'spring'
        elif month in [6, 7, 8]:
            return 'summer'
        else:
            return 'autumn'

    def _find_resource_gaps(self, ideas: List[Dict]) -> List[Dict]:
        """Identify gaps where additional resources or knowledge might be needed."""
        opportunities = []

        # Common resource needs for the Montolieu shop
        resource_patterns = {
            'funding': ['expensive', 'cost', 'invest', 'money', 'budget', 'loan'],
            'knowledge': ['learn', 'understand', 'research', 'study', 'figure out'],
            'connections': ['contact', 'know someone', 'need help', 'expert', 'advisor'],
            'tools': ['need', 'tool', 'software', 'system', 'platform']
        }

        resource_mentions = {resource: 0 for resource in resource_patterns}

        for idea in ideas:
            text_lower = idea['text'].lower()
            for resource, keywords in resource_patterns.items():
                if any(keyword in text_lower for keyword in keywords):
                    resource_mentions[resource] += 1

        for resource, count in resource_mentions.items():
            if count >= 2:
                opportunities.append({
                    'type': 'resource_gap',
                    'description': f"Consider addressing {resource} needs (mentioned {count} times)",
                    'resource_type': resource,
                    'priority': 'medium',
                    'frequency': count,
                    'actionable': True
                })

        return opportunities

    def _deduplicate_and_prioritize(self, opportunities: List[Dict]) -> List[Dict]:
        """Remove duplicates and sort by priority and relevance."""
        # Simple deduplication by description similarity
        unique_opportunities = []
        seen_descriptions = set()

        for opp in opportunities:
            desc_key = opp['description'][:50]  # First 50 chars as key
            if desc_key not in seen_descriptions:
                unique_opportunities.append(opp)
                seen_descriptions.add(desc_key)

        # Sort by priority and actionability
        priority_order = {'high': 3, 'medium': 2, 'low': 1}

        return sorted(unique_opportunities,
                     key=lambda x: (priority_order.get(x.get('priority', 'low'), 1),
                                   x.get('actionable', False)),
                     reverse=True)[:10]  # Top 10 opportunities

    def _save_opportunities(self, opportunities: List[Dict]):
        """Save opportunities to file."""
        opp_file = self.data_dir / "opportunities.json"

        # Add timestamp
        timestamp = datetime.now().isoformat()
        for opp in opportunities:
            opp['generated_at'] = timestamp

        try:
            with open(opp_file, 'r') as f:
                existing_opportunities = json.load(f)
        except FileNotFoundError:
            existing_opportunities = []

        # Add new opportunities
        existing_opportunities.extend(opportunities)

        # Keep only recent opportunities (last 14 days)
        cutoff = datetime.now() - timedelta(days=14)
        recent_opportunities = [
            o for o in existing_opportunities
            if datetime.fromisoformat(o['generated_at']) >= cutoff
        ]

        with open(opp_file, 'w') as f:
            json.dump(recent_opportunities, f, indent=2)

    def get_opportunities(self, limit: int = 5) -> List[Dict]:
        """Get recent opportunities."""
        try:
            with open(self.data_dir / "opportunities.json", 'r') as f:
                opportunities = json.load(f)

            # Get most recent opportunities
            recent = sorted(opportunities,
                          key=lambda x: x.get('generated_at', ''),
                          reverse=True)

            return recent[:limit]

        except FileNotFoundError:
            return []

    def get_goal_progress(self) -> Dict[str, Dict]:
        """Analyze progress toward Montolieu shop goals."""
        try:
            with open(self.data_dir / "ideas.json", 'r') as f:
                ideas = json.load(f)

            progress = {}

            for goal_key, goal_info in self.montolieu_goals.items():
                related_ideas = []
                for idea in ideas:
                    text_lower = idea['text'].lower()
                    matches = sum(1 for keyword in goal_info['keywords'] if keyword in text_lower)
                    if matches >= 1:
                        related_ideas.append({
                            'id': idea['id'],
                            'text': idea['text'][:80] + "..." if len(idea['text']) > 80 else idea['text'],
                            'matches': matches
                        })

                progress[goal_key] = {
                    'description': goal_info['description'],
                    'priority': goal_info['priority'],
                    'idea_count': len(related_ideas),
                    'related_ideas': sorted(related_ideas, key=lambda x: x['matches'], reverse=True)[:3]
                }

            return progress

        except FileNotFoundError:
            return {}
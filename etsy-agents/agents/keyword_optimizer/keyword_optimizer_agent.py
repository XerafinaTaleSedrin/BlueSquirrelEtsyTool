#!/usr/bin/env python3
"""
Keyword Optimization Agent for EcureuilBleu Etsy Shop
Analyzes existing keywords and suggests replacements/removals
"""

import json
import csv
from collections import Counter
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple, Optional

@dataclass
class KeywordAnalysis:
    keyword: str
    frequency_across_listings: int
    estimated_competition: str  # High/Medium/Low
    relevance_score: float  # 1-10
    replacement_suggestions: List[str]
    action_recommendation: str  # Keep/Replace/Remove
    reasoning: str

@dataclass
class KeywordOptimization:
    listing_title: str
    current_keywords: List[str]
    keywords_to_remove: List[str]
    keywords_to_replace: Dict[str, str]  # old_keyword: new_keyword
    keywords_to_add: List[str]
    optimization_priority: str  # High/Medium/Low
    expected_improvement: str

class KeywordOptimizerAgent:
    def __init__(self):
        self.keyword_performance_db = self._initialize_keyword_database()
        self.competitor_keywords = self._load_competitor_insights()

    def _initialize_keyword_database(self):
        """Initialize database of keyword performance insights"""
        return {
            # Political/Protest Keywords
            "resist": {"competition": "High", "relevance": 9, "trend": "stable"},
            "protest": {"competition": "High", "relevance": 8, "trend": "declining"},
            "political": {"competition": "High", "relevance": 7, "trend": "stable"},
            "government": {"competition": "Medium", "relevance": 9, "trend": "rising"},
            "bureaucrat": {"competition": "Low", "relevance": 10, "trend": "rising"},
            "civil servant": {"competition": "Low", "relevance": 9, "trend": "rising"},
            "federal employee": {"competition": "Medium", "relevance": 10, "trend": "rising"},

            # Product Type Keywords
            "t shirt": {"competition": "High", "relevance": 6, "trend": "stable"},
            "tshirt": {"competition": "High", "relevance": 6, "trend": "stable"},
            "shirt": {"competition": "High", "relevance": 7, "trend": "stable"},
            "tee": {"competition": "Medium", "relevance": 8, "trend": "rising"},
            "apparel": {"competition": "Medium", "relevance": 6, "trend": "stable"},
            "clothing": {"competition": "High", "relevance": 5, "trend": "declining"},
            "sticker": {"competition": "Medium", "relevance": 9, "trend": "rising"},
            "decal": {"competition": "Low", "relevance": 8, "trend": "stable"},
            "mug": {"competition": "High", "relevance": 7, "trend": "stable"},
            "cup": {"competition": "High", "relevance": 6, "trend": "declining"},
            "hat": {"competition": "Medium", "relevance": 8, "trend": "stable"},
            "cap": {"competition": "Medium", "relevance": 7, "trend": "stable"},

            # Gift Keywords
            "gift": {"competition": "High", "relevance": 8, "trend": "stable"},
            "present": {"competition": "Medium", "relevance": 6, "trend": "declining"},
            "birthday gift": {"competition": "High", "relevance": 7, "trend": "stable"},
            "retirement gift": {"competition": "Medium", "relevance": 9, "trend": "rising"},
            "coworker gift": {"competition": "Medium", "relevance": 8, "trend": "rising"},

            # Humor Keywords
            "funny": {"competition": "High", "relevance": 8, "trend": "stable"},
            "humor": {"competition": "Medium", "relevance": 9, "trend": "rising"},
            "sarcastic": {"competition": "Low", "relevance": 9, "trend": "rising"},
            "satire": {"competition": "Low", "relevance": 10, "trend": "rising"},
            "witty": {"competition": "Low", "relevance": 8, "trend": "stable"},

            # Quality Descriptors (often low value)
            "beautiful": {"competition": "High", "relevance": 2, "trend": "declining"},
            "perfect": {"competition": "High", "relevance": 2, "trend": "declining"},
            "amazing": {"competition": "High", "relevance": 2, "trend": "declining"},
            "awesome": {"competition": "High", "relevance": 3, "trend": "declining"},
            "great": {"competition": "High", "relevance": 2, "trend": "declining"},
            "best": {"competition": "High", "relevance": 3, "trend": "stable"},
            "quality": {"competition": "Medium", "relevance": 4, "trend": "stable"},

            # Trending Niche Keywords
            "deep state": {"competition": "Low", "relevance": 10, "trend": "rising"},
            "rogue": {"competition": "Low", "relevance": 10, "trend": "rising"},
            "opsec": {"competition": "Low", "relevance": 10, "trend": "rising"},
            "nato": {"competition": "Low", "relevance": 9, "trend": "rising"},
            "cybersecurity": {"competition": "Medium", "relevance": 9, "trend": "rising"},
            "classified": {"competition": "Low", "relevance": 8, "trend": "rising"}
        }

    def _load_competitor_insights(self):
        """Load insights about competitor keyword usage"""
        return {
            "overused_keywords": ["political", "resist", "protest", "funny"],
            "underutilized_gems": ["bureaucrat", "civil servant", "deep state", "opsec"],
            "seasonal_opportunities": ["election", "voting", "democracy", "transparency"],
            "niche_dominance": ["rogue bureaucrat", "federal humor", "government satire"]
        }

    def analyze_keyword_portfolio(self, listings_data: List[Dict]) -> List[KeywordAnalysis]:
        """Analyze all keywords across the portfolio"""
        all_keywords = []
        keyword_frequency = Counter()

        # Collect all keywords and count frequency
        for listing in listings_data:
            keywords = listing.get('tags', [])
            all_keywords.extend(keywords)
            for keyword in keywords:
                keyword_frequency[keyword.lower()] += 1

        # Analyze each unique keyword
        unique_keywords = set(k.lower() for k in all_keywords)
        keyword_analyses = []

        for keyword in unique_keywords:
            analysis = self._analyze_single_keyword(
                keyword,
                keyword_frequency[keyword],
                len(listings_data)
            )
            keyword_analyses.append(analysis)

        # Sort by priority (relevance score + frequency consideration)
        keyword_analyses.sort(
            key=lambda x: (x.relevance_score, -x.frequency_across_listings),
            reverse=True
        )

        return keyword_analyses

    def _analyze_single_keyword(self, keyword: str, frequency: int, total_listings: int) -> KeywordAnalysis:
        """Analyze a single keyword and provide recommendations"""
        keyword_clean = keyword.lower().strip()

        # Get keyword data from database
        keyword_data = self.keyword_performance_db.get(
            keyword_clean,
            {"competition": "Unknown", "relevance": 5, "trend": "stable"}
        )

        # Calculate relevance score
        relevance_score = keyword_data["relevance"]

        # Adjust relevance based on frequency (over-usage penalty)
        frequency_ratio = frequency / total_listings
        if frequency_ratio > 0.7:  # Used in >70% of listings
            relevance_score *= 0.8  # Penalty for overuse

        # Generate replacement suggestions
        replacements = self._get_replacement_suggestions(keyword_clean)

        # Determine action recommendation
        action, reasoning = self._determine_action(keyword_clean, keyword_data, frequency_ratio)

        return KeywordAnalysis(
            keyword=keyword,
            frequency_across_listings=frequency,
            estimated_competition=keyword_data["competition"],
            relevance_score=relevance_score,
            replacement_suggestions=replacements,
            action_recommendation=action,
            reasoning=reasoning
        )

    def _get_replacement_suggestions(self, keyword: str) -> List[str]:
        """Suggest better alternatives for a keyword"""
        replacements = {
            "political": ["government humor", "civic satire", "bureaucrat gift"],
            "funny": ["witty", "sarcastic", "humor"],
            "protest": ["resistance gear", "activist apparel", "dissent"],
            "t shirt": ["tee", "shirt design", "apparel"],
            "tshirt": ["tee", "graphic shirt", "statement shirt"],
            "beautiful": [],  # Remove, no replacement needed
            "perfect": [],  # Remove, no replacement needed
            "amazing": [],  # Remove, no replacement needed
            "awesome": ["witty", "clever"],
            "great": ["quality", "premium"],
            "clothing": ["apparel", "shirt", "tee"],
            "cup": ["mug", "drinkware", "tumbler"],
            "present": ["gift", "coworker gift", "retirement gift"],
            "resist": ["resistance gear", "activist", "dissent"],
            "save democracy": ["democracy defender", "civic engagement", "voting rights"]
        }

        return replacements.get(keyword, [])

    def _determine_action(self, keyword: str, keyword_data: Dict, frequency_ratio: float) -> Tuple[str, str]:
        """Determine what action to take with a keyword"""
        relevance = keyword_data["relevance"]
        competition = keyword_data["competition"]
        trend = keyword_data["trend"]

        # Remove low-value keywords
        if relevance <= 3:
            return "Remove", f"Low relevance ({relevance}/10). Wasting valuable tag space."

        # Remove overused quality descriptors
        if keyword in ["beautiful", "perfect", "amazing", "awesome", "great"] and relevance <= 4:
            return "Remove", "Quality descriptor adds no search value. Focus on specific product features."

        # Replace declining high-competition keywords
        if competition == "High" and trend == "declining" and relevance <= 7:
            return "Replace", f"High competition, declining trend. Better alternatives available."

        # Replace overused keywords (used in >80% of listings)
        if frequency_ratio > 0.8 and relevance <= 8:
            return "Replace", f"Overused across {frequency_ratio*100:.0f}% of listings. Diversify keyword portfolio."

        # Keep high-performing keywords
        if relevance >= 8 and trend in ["stable", "rising"]:
            return "Keep", f"High relevance ({relevance}/10), {trend} trend. Strong performer."

        # Default to keep with optimization
        return "Keep", "Moderate performance. Monitor and optimize placement."

    def optimize_listing_keywords(self, listing: Dict) -> KeywordOptimization:
        """Provide specific optimization recommendations for a single listing"""
        title = listing.get('title', 'Unknown Listing')
        current_keywords = listing.get('tags', [])

        # Analyze current keywords
        keywords_to_remove = []
        keywords_to_replace = {}
        keywords_to_add = []

        for keyword in current_keywords:
            analysis = self._analyze_single_keyword(keyword, 1, 1)  # Single listing context

            if analysis.action_recommendation == "Remove":
                keywords_to_remove.append(keyword)
            elif analysis.action_recommendation == "Replace" and analysis.replacement_suggestions:
                best_replacement = analysis.replacement_suggestions[0]
                keywords_to_replace[keyword] = best_replacement

        # Suggest additions based on listing content
        additional_keywords = self._suggest_additional_keywords(title, current_keywords)
        keywords_to_add = additional_keywords[:3]  # Top 3 suggestions

        # Calculate priority
        total_changes = len(keywords_to_remove) + len(keywords_to_replace) + len(keywords_to_add)
        if total_changes >= 5:
            priority = "High"
            improvement = "25-40% improvement expected"
        elif total_changes >= 3:
            priority = "Medium"
            improvement = "15-25% improvement expected"
        else:
            priority = "Low"
            improvement = "5-15% improvement expected"

        return KeywordOptimization(
            listing_title=title,
            current_keywords=current_keywords,
            keywords_to_remove=keywords_to_remove,
            keywords_to_replace=keywords_to_replace,
            keywords_to_add=keywords_to_add,
            optimization_priority=priority,
            expected_improvement=improvement
        )

    def _suggest_additional_keywords(self, title: str, current_keywords: List[str]) -> List[str]:
        """Suggest additional keywords based on listing title and current tags"""
        title_lower = title.lower()
        current_lower = [k.lower() for k in current_keywords]

        suggestions = []

        # Product-specific suggestions
        if "opsec" in title_lower and "cybersecurity" not in current_lower:
            suggestions.extend(["cybersecurity", "IT security", "security humor"])

        if "foxtrot" in title_lower or "delta" in title_lower or "tango" in title_lower:
            suggestions.extend(["military alphabet", "nato phonetic", "diplomat gift"])

        if "bureaucrat" in title_lower:
            suggestions.extend(["civil servant", "federal worker", "government humor"])

        if "public service" in title_lower:
            suggestions.extend(["civic engagement", "democracy defender", "public sector"])

        # General political merchandise
        if any(word in title_lower for word in ["political", "protest", "resist"]):
            suggestions.extend(["activist gear", "statement piece", "political art"])

        # Product type additions
        if "sticker" in title_lower and "decal" not in current_lower:
            suggestions.append("decal")

        if "shirt" in title_lower or "tee" in title_lower:
            suggestions.extend(["graphic tee", "statement shirt", "political apparel"])

        if "hat" in title_lower or "cap" in title_lower:
            suggestions.extend(["political hat", "statement cap", "protest gear"])

        # Remove duplicates and current keywords
        unique_suggestions = []
        for suggestion in suggestions:
            if suggestion.lower() not in current_lower and suggestion not in unique_suggestions:
                unique_suggestions.append(suggestion)

        return unique_suggestions[:5]  # Top 5 suggestions

    def generate_portfolio_report(self, listings_data: List[Dict]) -> Dict:
        """Generate comprehensive keyword optimization report"""
        keyword_analyses = self.analyze_keyword_portfolio(listings_data)
        listing_optimizations = []

        for listing in listings_data:
            optimization = self.optimize_listing_keywords(listing)
            listing_optimizations.append(optimization)

        # Portfolio-level insights
        total_keywords = sum(len(listing.get('tags', [])) for listing in listings_data)
        avg_keywords_per_listing = total_keywords / len(listings_data) if listings_data else 0

        high_priority_listings = [opt for opt in listing_optimizations if opt.optimization_priority == "High"]

        # Identify portfolio gaps
        portfolio_gaps = self._identify_portfolio_gaps(listings_data)

        return {
            "portfolio_summary": {
                "total_listings": len(listings_data),
                "total_unique_keywords": len(set(k.lower() for listing in listings_data for k in listing.get('tags', []))),
                "avg_keywords_per_listing": round(avg_keywords_per_listing, 1),
                "high_priority_optimizations": len(high_priority_listings)
            },
            "keyword_analyses": [asdict(analysis) for analysis in keyword_analyses],
            "listing_optimizations": [asdict(opt) for opt in listing_optimizations],
            "portfolio_gaps": portfolio_gaps,
            "quick_wins": self._identify_quick_wins(listing_optimizations),
            "strategic_recommendations": self._generate_strategic_recommendations(keyword_analyses)
        }

    def _identify_portfolio_gaps(self, listings_data: List[Dict]) -> List[str]:
        """Identify missing keyword opportunities across the portfolio"""
        all_keywords = set(k.lower() for listing in listings_data for k in listing.get('tags', []))

        # High-value keywords missing from portfolio
        valuable_missing = []
        high_value_keywords = [
            "deep state", "transparency", "accountability", "oversight",
            "whistleblower", "classified", "security clearance", "insider",
            "diplomatic", "intelligence", "briefing", "memo"
        ]

        for keyword in high_value_keywords:
            if keyword not in all_keywords:
                valuable_missing.append(keyword)

        return valuable_missing[:8]  # Top 8 gaps

    def _identify_quick_wins(self, optimizations: List[KeywordOptimization]) -> List[Dict]:
        """Identify easy optimization opportunities"""
        quick_wins = []

        for opt in optimizations:
            if opt.optimization_priority in ["High", "Medium"] and len(opt.keywords_to_remove) > 0:
                quick_wins.append({
                    "listing": opt.listing_title[:50] + "..." if len(opt.listing_title) > 50 else opt.listing_title,
                    "action": f"Remove {len(opt.keywords_to_remove)} low-value keywords",
                    "impact": opt.expected_improvement,
                    "effort": "5 minutes"
                })

        return quick_wins[:5]  # Top 5 quick wins

    def _generate_strategic_recommendations(self, keyword_analyses: List[KeywordAnalysis]) -> List[str]:
        """Generate high-level strategic recommendations"""
        recommendations = []

        # Count actions needed
        remove_count = sum(1 for analysis in keyword_analyses if analysis.action_recommendation == "Remove")
        replace_count = sum(1 for analysis in keyword_analyses if analysis.action_recommendation == "Replace")

        if remove_count > 5:
            recommendations.append(f"Portfolio Cleanup: Remove {remove_count} low-value keywords to free up tag space")

        if replace_count > 3:
            recommendations.append(f"Keyword Modernization: Replace {replace_count} underperforming keywords with trending alternatives")

        # Check for overused keywords
        overused = [analysis for analysis in keyword_analyses if analysis.frequency_across_listings > 10]
        if overused:
            recommendations.append("Keyword Diversification: Reduce overuse of common terms across listings")

        # Check for trend alignment
        recommendations.append("Trend Alignment: Focus on government/bureaucrat niche keywords with rising trends")

        return recommendations

def main():
    """Test the keyword optimizer agent"""
    # This would normally load from the CSV or JSON data
    print("Keyword Optimizer Agent initialized successfully!")
    print("Ready to analyze keyword portfolios and suggest optimizations.")

if __name__ == "__main__":
    main()
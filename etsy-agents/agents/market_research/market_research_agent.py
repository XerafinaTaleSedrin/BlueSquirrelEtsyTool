#!/usr/bin/env python3
"""
Market Research Subagent for Etsy Opportunity Analysis
Implements capability-aware opportunity identification and prioritization
"""

import json
import datetime
from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from pathlib import Path
import requests
import re

@dataclass
class MarketOpportunity:
    name: str
    category: str
    search_volume: int
    competition_level: str  # "Low", "Medium", "High"
    avg_price: float
    seasonal_factor: float
    keywords: List[str]
    skill_requirements: List[str]
    resource_requirements: List[str]
    effort_score: int  # 1-5 scale
    impact_score: int  # 1-5 scale
    confidence_score: int  # 1-5 scale
    timeline: str  # "Quick Win", "Weekend Project", "Major Initiative", "Long-term Strategy"

@dataclass
class CapabilityProfile:
    skills: Set[str]
    tools_available: Set[str]
    tools_not_available: Set[str]
    time_availability: Dict[str, int]  # hours per category
    budget: float
    learning_capacity: str  # "High", "Medium", "Low"

class EtsyMarketResearcher:
    def __init__(self, config_path: str = "../../config/market_config.json"):
        self.config = self._load_config(config_path)
        self.capability_profile = self._load_capability_profile()
        self.opportunity_history = {}

    def _load_config(self, config_path: str) -> Dict:
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._default_config()

    def _default_config(self) -> Dict:
        return {
            "excluded_categories": [
                "woodworking", "metalworking", "glass blowing", "pottery wheel",
                "jewelry casting", "leather working", "screen printing"
            ],
            "preferred_categories": [
                "digital products", "printables", "simple crafts", "planning",
                "stickers", "cards", "simple sewing", "knitting", "crochet"
            ],
            "effort_weights": {
                "research_time": 0.2,
                "skill_learning": 0.3,
                "material_cost": 0.2,
                "production_time": 0.3
            },
            "impact_factors": {
                "market_size": 0.4,
                "competition": 0.3,
                "profit_margin": 0.3
            }
        }

    def _load_capability_profile(self) -> CapabilityProfile:
        """
        Load user's capability profile - this would be customized per user
        """
        return CapabilityProfile(
            skills={"digital_design", "basic_sewing", "writing", "planning", "organization"},
            tools_available={"computer", "printer", "basic_sewing_supplies", "design_software"},
            tools_not_available={"woodworking_tools", "pottery_wheel", "metalworking", "advanced_machinery"},
            time_availability={"quick_wins": 2, "weekend_projects": 8, "major_initiatives": 40},
            budget=200.0,
            learning_capacity="Medium"
        )

    def research_market_opportunities(self, focus_areas: List[str] = None) -> List[MarketOpportunity]:
        """
        Research market opportunities based on capability constraints
        """
        opportunities = []

        # Simulated market research data - in practice, this would use Etsy API or web scraping
        potential_opportunities = [
            {
                "name": "Digital Planning Printables",
                "category": "digital_products",
                "search_volume": 5000,
                "competition_level": "Medium",
                "avg_price": 12.50,
                "seasonal_factor": 1.2,
                "keywords": ["digital planner", "printable planner", "goal setting", "productivity"],
                "skill_requirements": ["digital_design", "planning"],
                "resource_requirements": ["design_software", "time"]
            },
            {
                "name": "Custom Wedding Stickers",
                "category": "stickers",
                "search_volume": 3200,
                "competition_level": "High",
                "avg_price": 8.75,
                "seasonal_factor": 1.5,
                "keywords": ["wedding stickers", "custom labels", "bridal shower"],
                "skill_requirements": ["digital_design", "customer_service"],
                "resource_requirements": ["design_software", "printer", "sticker_paper"]
            },
            {
                "name": "Handmade Baby Bibs",
                "category": "sewing",
                "search_volume": 2100,
                "competition_level": "Low",
                "avg_price": 15.00,
                "seasonal_factor": 1.0,
                "keywords": ["baby bib", "handmade", "personalized", "organic"],
                "skill_requirements": ["basic_sewing", "pattern_following"],
                "resource_requirements": ["sewing_machine", "fabric", "thread"]
            },
            {
                "name": "Wooden Cutting Boards",
                "category": "woodworking",
                "search_volume": 4500,
                "competition_level": "Medium",
                "avg_price": 35.00,
                "seasonal_factor": 1.3,
                "keywords": ["cutting board", "wooden", "handmade", "kitchen"],
                "skill_requirements": ["woodworking", "finishing"],
                "resource_requirements": ["woodworking_tools", "wood", "workspace"]
            }
        ]

        for opp_data in potential_opportunities:
            # Filter out opportunities that require unavailable capabilities
            if self._is_opportunity_feasible(opp_data):
                opportunity = self._create_market_opportunity(opp_data)
                opportunities.append(opportunity)

        return sorted(opportunities, key=lambda x: self._calculate_priority_score(x), reverse=True)

    def _is_opportunity_feasible(self, opp_data: Dict) -> bool:
        """
        Check if opportunity aligns with user capabilities and constraints
        """
        # Check if category is excluded
        if opp_data["category"] in self.config["excluded_categories"]:
            return False

        # Check skill requirements
        required_skills = set(opp_data["skill_requirements"])
        if not required_skills.issubset(self.capability_profile.skills):
            # Check if skills can be learned given learning capacity
            if self.capability_profile.learning_capacity == "Low" and len(required_skills - self.capability_profile.skills) > 1:
                return False

        # Check tool requirements
        required_tools = set(opp_data["resource_requirements"])
        if any(tool in self.capability_profile.tools_not_available for tool in required_tools):
            return False

        return True

    def _create_market_opportunity(self, opp_data: Dict) -> MarketOpportunity:
        """
        Create MarketOpportunity object with calculated scores
        """
        effort_score = self._calculate_effort_score(opp_data)
        impact_score = self._calculate_impact_score(opp_data)
        confidence_score = self._calculate_confidence_score(opp_data)
        timeline = self._determine_timeline(effort_score, opp_data)

        return MarketOpportunity(
            name=opp_data["name"],
            category=opp_data["category"],
            search_volume=opp_data["search_volume"],
            competition_level=opp_data["competition_level"],
            avg_price=opp_data["avg_price"],
            seasonal_factor=opp_data["seasonal_factor"],
            keywords=opp_data["keywords"],
            skill_requirements=opp_data["skill_requirements"],
            resource_requirements=opp_data["resource_requirements"],
            effort_score=effort_score,
            impact_score=impact_score,
            confidence_score=confidence_score,
            timeline=timeline
        )

    def _calculate_effort_score(self, opp_data: Dict) -> int:
        """
        Calculate effort score (1-5, lower is easier)
        """
        base_effort = 2

        # Skill gap penalty
        required_skills = set(opp_data["skill_requirements"])
        missing_skills = required_skills - self.capability_profile.skills
        base_effort += len(missing_skills)

        # Competition adjustment
        if opp_data["competition_level"] == "High":
            base_effort += 1
        elif opp_data["competition_level"] == "Low":
            base_effort -= 1

        # Category preference bonus
        if opp_data["category"] in self.config["preferred_categories"]:
            base_effort -= 1

        return max(1, min(5, base_effort))

    def _calculate_impact_score(self, opp_data: Dict) -> int:
        """
        Calculate impact score (1-5, higher is better)
        """
        # Normalize search volume to 1-5 scale
        volume_score = min(5, max(1, opp_data["search_volume"] // 1000 + 1))

        # Price impact
        price_score = min(5, max(1, int(opp_data["avg_price"] // 10)))

        # Seasonal boost
        seasonal_score = min(5, int(opp_data["seasonal_factor"] * 3))

        # Competition penalty
        competition_penalty = {"Low": 0, "Medium": -1, "High": -2}[opp_data["competition_level"]]

        impact = (volume_score + price_score + seasonal_score) // 3 + competition_penalty

        return max(1, min(5, impact))

    def _calculate_confidence_score(self, opp_data: Dict) -> int:
        """
        Calculate confidence in the opportunity assessment (1-5)
        """
        confidence = 3  # Base confidence

        # Higher confidence for areas with existing skills
        required_skills = set(opp_data["skill_requirements"])
        skill_overlap = len(required_skills.intersection(self.capability_profile.skills))
        confidence += min(2, skill_overlap)

        # Lower confidence for highly competitive markets
        if opp_data["competition_level"] == "High":
            confidence -= 1

        return max(1, min(5, confidence))

    def _determine_timeline(self, effort_score: int, opp_data: Dict) -> str:
        """
        Determine timeline category based on effort and complexity
        """
        if effort_score <= 2:
            return "Quick Win"
        elif effort_score == 3:
            return "Weekend Project"
        elif effort_score == 4:
            return "Major Initiative"
        else:
            return "Long-term Strategy"

    def _calculate_priority_score(self, opportunity: MarketOpportunity) -> float:
        """
        Calculate RICE priority score: (Reach × Impact × Confidence) ÷ Effort
        """
        reach = opportunity.search_volume / 1000  # Normalize search volume
        impact = opportunity.impact_score
        confidence = opportunity.confidence_score
        effort = opportunity.effort_score

        return (reach * impact * confidence) / effort

    def generate_opportunity_report(self, opportunities: List[MarketOpportunity]) -> Dict:
        """
        Generate comprehensive opportunity assessment report
        """
        now = datetime.datetime.now()

        # Categorize opportunities by timeline
        categorized = {
            "Quick Win": [],
            "Weekend Project": [],
            "Major Initiative": [],
            "Long-term Strategy": []
        }

        for opp in opportunities:
            categorized[opp.timeline].append(opp)

        # Generate seasonal recommendations
        current_month = now.month
        seasonal_opps = [opp for opp in opportunities if opp.seasonal_factor > 1.1]

        report = {
            "generated_date": now.isoformat(),
            "total_opportunities": len(opportunities),
            "categorized_opportunities": {
                timeline: [{
                    "name": opp.name,
                    "priority_score": self._calculate_priority_score(opp),
                    "effort_score": opp.effort_score,
                    "impact_score": opp.impact_score,
                    "confidence_score": opp.confidence_score,
                    "avg_price": opp.avg_price,
                    "competition": opp.competition_level,
                    "skills_needed": opp.skill_requirements,
                    "resources_needed": opp.resource_requirements
                } for opp in opps[:5]]  # Top 5 in each category
                for timeline, opps in categorized.items()
            },
            "seasonal_recommendations": [{
                "name": opp.name,
                "seasonal_factor": opp.seasonal_factor,
                "keywords": opp.keywords
            } for opp in seasonal_opps[:3]],
            "capability_gaps": self._identify_capability_gaps(opportunities),
            "next_actions": self._generate_next_actions(opportunities[:5])
        }

        return report

    def _identify_capability_gaps(self, opportunities: List[MarketOpportunity]) -> List[Dict]:
        """
        Identify what capabilities would unlock more opportunities
        """
        all_skills = set()
        all_tools = set()

        for opp in opportunities:
            all_skills.update(opp.skill_requirements)
            all_tools.update(opp.resource_requirements)

        missing_skills = all_skills - self.capability_profile.skills
        missing_tools = all_tools - self.capability_profile.tools_available

        gaps = []

        for skill in missing_skills:
            # Count how many opportunities this skill would unlock
            unlock_count = sum(1 for opp in opportunities if skill in opp.skill_requirements)
            gaps.append({
                "type": "skill",
                "name": skill,
                "opportunities_unlocked": unlock_count,
                "learning_effort": "Medium"  # Could be made more sophisticated
            })

        for tool in missing_tools:
            if tool not in self.capability_profile.tools_not_available:
                unlock_count = sum(1 for opp in opportunities if tool in opp.resource_requirements)
                gaps.append({
                    "type": "tool",
                    "name": tool,
                    "opportunities_unlocked": unlock_count,
                    "acquisition_cost": "Variable"
                })

        return sorted(gaps, key=lambda x: x["opportunities_unlocked"], reverse=True)

    def _generate_next_actions(self, top_opportunities: List[MarketOpportunity]) -> List[Dict]:
        """
        Generate specific next action recommendations
        """
        actions = []

        for i, opp in enumerate(top_opportunities[:3]):
            actions.append({
                "priority": i + 1,
                "opportunity": opp.name,
                "action": f"Research {opp.name} market in detail",
                "timeline": "This week",
                "estimated_time": "2-3 hours"
            })

            if opp.timeline == "Quick Win":
                actions.append({
                    "priority": i + 1,
                    "opportunity": opp.name,
                    "action": f"Create prototype/sample for {opp.name}",
                    "timeline": "Next week",
                    "estimated_time": "4-6 hours"
                })

        return actions

    def save_report(self, report: Dict, report_type: str):
        """
        Save reports to the outputs directory
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"../../outputs/{report_type}_{timestamp}.json"

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

if __name__ == "__main__":
    # Example usage
    researcher = EtsyMarketResearcher()

    opportunities = researcher.research_market_opportunities()
    report = researcher.generate_opportunity_report(opportunities)
    researcher.save_report(report, "market_research_report")

    print(f"Found {len(opportunities)} feasible opportunities")
    print("Top 3 opportunities:")
    for i, opp in enumerate(opportunities[:3]):
        priority_score = researcher._calculate_priority_score(opp)
        print(f"{i+1}. {opp.name} (Priority: {priority_score:.2f}, {opp.timeline})")
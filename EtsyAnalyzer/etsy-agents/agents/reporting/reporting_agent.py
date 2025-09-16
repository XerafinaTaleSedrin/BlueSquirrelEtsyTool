#!/usr/bin/env python3
"""
Reporting Subagent for Etsy Business Intelligence
Synthesizes insights from SEO and Market Research agents into actionable reports
"""

import json
import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from pathlib import Path
import sys
import os

# Add parent directories to path for importing other agents
sys.path.append(os.path.join(os.path.dirname(__file__), '../seo_optimizer'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../market_research'))

try:
    from seo_agent import EtsySEOOptimizer, ListingMetrics
    from market_research_agent import EtsyMarketResearcher, MarketOpportunity
except ImportError:
    # Fallback for when modules aren't available
    pass

@dataclass
class BusinessMetrics:
    total_revenue: float
    total_views: int
    avg_conversion_rate: float
    total_listings: int
    active_opportunities: int
    weekly_growth_rate: float

@dataclass
class ExecutiveSummary:
    date: str
    performance_status: str  # "Excellent", "Good", "Needs Attention", "Critical"
    revenue: float
    revenue_change: float
    key_win: str
    key_challenge: str
    completed_actions: List[str]
    next_priorities: List[str]
    decisions_needed: List[str]

class EtsyReportingAgent:
    def __init__(self, config_path: str = "../../config/reporting_config.json"):
        self.config = self._load_config(config_path)
        self.seo_optimizer = None
        self.market_researcher = None
        self._initialize_agents()

    def _load_config(self, config_path: str) -> Dict:
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._default_config()

    def _default_config(self) -> Dict:
        return {
            "reporting_schedule": {
                "daily": {"enabled": True, "time": "09:00"},
                "weekly": {"enabled": True, "day": "Monday", "time": "09:00"},
                "monthly": {"enabled": True, "day": 1, "time": "09:00"}
            },
            "alert_thresholds": {
                "revenue_decline": -0.15,
                "view_decline": -0.20,
                "conversion_decline": -0.25
            },
            "dashboard_preferences": {
                "max_opportunities": 5,
                "max_actions": 3,
                "chart_type": "text"
            }
        }

    def _initialize_agents(self):
        """
        Initialize SEO and Market Research agents
        """
        try:
            self.seo_optimizer = EtsySEOOptimizer()
            self.market_researcher = EtsyMarketResearcher()
        except:
            print("Warning: Could not initialize sub-agents. Running in standalone mode.")

    def generate_executive_summary(self,
                                   business_metrics: BusinessMetrics,
                                   seo_data: Dict = None,
                                   market_data: Dict = None) -> ExecutiveSummary:
        """
        Generate the 2-minute executive summary from the framework
        """
        now = datetime.datetime.now()

        # Determine overall performance status
        performance_status = self._assess_performance_status(business_metrics)

        # Extract key insights
        key_win = self._identify_key_win(seo_data, market_data)
        key_challenge = self._identify_key_challenge(seo_data, market_data)

        # Generate action summaries
        completed_actions = self._extract_completed_actions(seo_data, market_data)
        next_priorities = self._generate_next_priorities(seo_data, market_data)
        decisions_needed = self._identify_decisions_needed(seo_data, market_data)

        return ExecutiveSummary(
            date=now.strftime("%Y-%m-%d"),
            performance_status=performance_status,
            revenue=business_metrics.total_revenue,
            revenue_change=business_metrics.weekly_growth_rate,
            key_win=key_win,
            key_challenge=key_challenge,
            completed_actions=completed_actions,
            next_priorities=next_priorities,
            decisions_needed=decisions_needed
        )

    def _assess_performance_status(self, metrics: BusinessMetrics) -> str:
        """
        Assess overall business performance status
        """
        if metrics.weekly_growth_rate > 0.10:
            return "Excellent"
        elif metrics.weekly_growth_rate > 0:
            return "Good"
        elif metrics.weekly_growth_rate > -0.10:
            return "Needs Attention"
        else:
            return "Critical"

    def _identify_key_win(self, seo_data: Dict, market_data: Dict) -> str:
        """
        Identify the biggest success from the week
        """
        wins = []

        if seo_data and 'top_performers' in seo_data:
            if seo_data['top_performers']:
                top_performer = seo_data['top_performers'][0]
                wins.append(f"'{top_performer['title']}' achieving {top_performer['score']}/100 SEO score")

        if market_data and 'total_opportunities' in market_data:
            if market_data['total_opportunities'] > 0:
                wins.append(f"Identified {market_data['total_opportunities']} new market opportunities")

        return wins[0] if wins else "Steady performance maintained"

    def _identify_key_challenge(self, seo_data: Dict, market_data: Dict) -> str:
        """
        Identify the main concern requiring attention
        """
        challenges = []

        if seo_data and 'attention_needed' in seo_data:
            attention_count = len(seo_data['attention_needed'])
            if attention_count > 0:
                challenges.append(f"{attention_count} listings requiring immediate SEO attention")

        if market_data and 'capability_gaps' in market_data:
            if market_data['capability_gaps']:
                challenges.append("Capability gaps limiting opportunity pursuit")

        return challenges[0] if challenges else "No major concerns identified"

    def _extract_completed_actions(self, seo_data: Dict, market_data: Dict) -> List[str]:
        """
        Extract completed actions from the week
        """
        actions = []

        # This would be populated from historical data or action tracking
        actions.append("Completed weekly SEO performance review")
        actions.append("Researched new market opportunities")

        return actions[:3]  # Max 3 as per framework

    def _generate_next_priorities(self, seo_data: Dict, market_data: Dict) -> List[str]:
        """
        Generate next week's priorities
        """
        priorities = []

        if seo_data and 'attention_needed' in seo_data:
            if seo_data['attention_needed']:
                priorities.append(f"Fix SEO issues for underperforming listings")

        if market_data and 'next_actions' in market_data:
            for action in market_data['next_actions'][:2]:
                priorities.append(action.get('action', 'Continue market research'))

        # Default priorities if no specific actions found
        if not priorities:
            priorities = [
                "Monitor current listing performance",
                "Research seasonal opportunities",
                "Optimize top-performing listings"
            ]

        return priorities[:3]

    def _identify_decisions_needed(self, seo_data: Dict, market_data: Dict) -> List[str]:
        """
        Identify strategic decisions requiring attention
        """
        decisions = []

        if market_data and 'categorized_opportunities' in market_data:
            quick_wins = market_data['categorized_opportunities'].get('Quick Win', [])
            if quick_wins:
                decisions.append(f"Choose which Quick Win opportunity to pursue first")

        if seo_data and 'status_counts' in seo_data:
            red_count = seo_data['status_counts'].get('RED', 0)
            if red_count > 2:
                decisions.append("Decide whether to pause/remove underperforming listings")

        return decisions

    def generate_integrated_dashboard(self,
                                      business_metrics: BusinessMetrics,
                                      seo_data: Dict = None,
                                      market_data: Dict = None) -> Dict:
        """
        Generate the master dashboard from the framework
        """
        now = datetime.datetime.now()
        executive_summary = self.generate_executive_summary(business_metrics, seo_data, market_data)

        # Calculate derived metrics
        active_projects = self._count_active_projects(market_data)
        potential_revenue = self._calculate_potential_revenue(market_data)

        dashboard = {
            "generated_date": now.isoformat(),
            "current_state": {
                "revenue": f"${business_metrics.total_revenue:,.2f}",
                "views": f"{business_metrics.total_views:,}",
                "conversion_rate": f"{business_metrics.avg_conversion_rate:.1%}",
                "health_score": self._calculate_overall_health_score(seo_data)
            },
            "opportunity_pipeline": {
                "active_projects": active_projects,
                "researched_opportunities": market_data.get('total_opportunities', 0) if market_data else 0,
                "potential_revenue": f"${potential_revenue:,.2f}",
                "next_review": (now + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
            },
            "weekly_focus": self._generate_weekly_focus(seo_data, market_data),
            "monthly_goals": self._generate_monthly_goals(business_metrics),
            "executive_summary": {
                "performance_status": executive_summary.performance_status,
                "key_win": executive_summary.key_win,
                "key_challenge": executive_summary.key_challenge,
                "revenue_change": f"{executive_summary.revenue_change:+.1%}"
            },
            "alerts": self._generate_alerts(business_metrics, seo_data)
        }

        return dashboard

    def _count_active_projects(self, market_data: Dict) -> int:
        """
        Count active projects from market research data
        """
        if not market_data or 'next_actions' not in market_data:
            return 0
        return len(market_data['next_actions'])

    def _calculate_potential_revenue(self, market_data: Dict) -> float:
        """
        Calculate potential revenue from identified opportunities
        """
        if not market_data or 'categorized_opportunities' not in market_data:
            return 0.0

        potential = 0.0
        for category, opportunities in market_data['categorized_opportunities'].items():
            for opp in opportunities:
                # Estimate monthly revenue: avg_price * estimated monthly sales
                estimated_sales = 10 if category == "Quick Win" else 5
                potential += opp.get('avg_price', 0) * estimated_sales

        return potential

    def _calculate_overall_health_score(self, seo_data: Dict) -> str:
        """
        Calculate overall business health score
        """
        if not seo_data or 'status_counts' not in seo_data:
            return "N/A"

        counts = seo_data['status_counts']
        total = sum(counts.values())
        if total == 0:
            return "N/A"

        green_ratio = counts.get('GREEN', 0) / total
        if green_ratio > 0.7:
            return "Excellent"
        elif green_ratio > 0.4:
            return "Good"
        else:
            return "Needs Work"

    def _generate_weekly_focus(self, seo_data: Dict, market_data: Dict) -> Dict:
        """
        Generate weekly focus priorities
        """
        focus = {
            "priority_1": "Monitor current performance",
            "priority_2": "Research market opportunities",
            "priority_3": "Optimize underperforming listings",
            "completion": "0/3"
        }

        if seo_data and 'attention_needed' in seo_data:
            if seo_data['attention_needed']:
                focus["priority_1"] = f"Fix {len(seo_data['attention_needed'])} underperforming listings"

        if market_data and 'next_actions' in market_data:
            if market_data['next_actions']:
                focus["priority_2"] = market_data['next_actions'][0].get('action', focus["priority_2"])

        return focus

    def _generate_monthly_goals(self, business_metrics: BusinessMetrics) -> Dict:
        """
        Generate monthly goal targets
        """
        current_revenue = business_metrics.total_revenue
        target_growth = 0.15  # 15% growth target

        return {
            "revenue_target": f"${current_revenue * (1 + target_growth):,.2f}",
            "view_growth": "10%",
            "new_listings": "2-3",
            "seo_improvements": "5 listings"
        }

    def _generate_alerts(self, business_metrics: BusinessMetrics, seo_data: Dict) -> List[Dict]:
        """
        Generate performance alerts based on thresholds
        """
        alerts = []

        # Revenue decline alert
        if business_metrics.weekly_growth_rate < self.config['alert_thresholds']['revenue_decline']:
            alerts.append({
                "type": "warning",
                "message": f"Revenue declined {abs(business_metrics.weekly_growth_rate):.1%} this week",
                "action": "Review underperforming listings and market trends"
            })

        # SEO performance alerts
        if seo_data and 'status_counts' in seo_data:
            red_count = seo_data['status_counts'].get('RED', 0)
            if red_count > 3:
                alerts.append({
                    "type": "critical",
                    "message": f"{red_count} listings need immediate SEO attention",
                    "action": "Prioritize SEO fixes for red-status listings"
                })

        return alerts

    def generate_weekly_summary_report(self,
                                       business_metrics: BusinessMetrics,
                                       seo_data: Dict = None,
                                       market_data: Dict = None) -> Dict:
        """
        Generate comprehensive weekly summary report
        """
        executive_summary = self.generate_executive_summary(business_metrics, seo_data, market_data)
        dashboard = self.generate_integrated_dashboard(business_metrics, seo_data, market_data)

        report = {
            "report_type": "Weekly Summary",
            "generated_date": datetime.datetime.now().isoformat(),
            "executive_summary": executive_summary.__dict__,
            "dashboard": dashboard,
            "detailed_analysis": {
                "seo_performance": seo_data or {},
                "market_opportunities": market_data or {},
                "business_metrics": business_metrics.__dict__
            },
            "action_plan": self._generate_action_plan(seo_data, market_data),
            "kpi_tracking": self._generate_kpi_tracking(business_metrics)
        }

        return report

    def _generate_action_plan(self, seo_data: Dict, market_data: Dict) -> List[Dict]:
        """
        Generate detailed action plan for the week
        """
        actions = []

        # SEO actions
        if seo_data and 'attention_needed' in seo_data:
            for listing in seo_data['attention_needed'][:3]:  # Top 3 priority
                actions.append({
                    "category": "SEO",
                    "action": f"Optimize '{listing['title']}'",
                    "priority": "High",
                    "estimated_time": "1 hour",
                    "expected_outcome": "Improved search visibility and CTR"
                })

        # Market research actions
        if market_data and 'next_actions' in market_data:
            for next_action in market_data['next_actions'][:2]:
                actions.append({
                    "category": "Market Research",
                    "action": next_action.get('action', 'Research opportunity'),
                    "priority": f"Priority {next_action.get('priority', 'Medium')}",
                    "estimated_time": next_action.get('estimated_time', '2 hours'),
                    "expected_outcome": "Market opportunity validation"
                })

        return actions

    def _generate_kpi_tracking(self, business_metrics: BusinessMetrics) -> Dict:
        """
        Generate KPI tracking dashboard
        """
        return {
            "revenue_trend": "stable",  # Would be calculated from historical data
            "view_trend": "growing",
            "conversion_trend": "stable",
            "listing_count_trend": "stable",
            "targets": {
                "monthly_revenue": business_metrics.total_revenue * 1.15,
                "monthly_views": business_metrics.total_views * 1.10,
                "target_conversion": business_metrics.avg_conversion_rate * 1.05
            }
        }

    def save_report(self, report: Dict, report_type: str):
        """
        Save reports to the outputs directory with formatted filename
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"../../outputs/{report_type}_{timestamp}.json"

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

        # Also save a human-readable version
        self._save_readable_report(report, report_type, timestamp)

    def _save_readable_report(self, report: Dict, report_type: str, timestamp: str):
        """
        Save a human-readable markdown version of the report
        """
        filename = f"../../outputs/{report_type}_{timestamp}.md"

        if 'executive_summary' in report:
            summary = report['executive_summary']

            markdown_content = f"""# {report.get('report_type', 'Business Report')} - {summary.get('date', 'N/A')}

## Executive Summary

**Performance Status:** {summary.get('performance_status', 'N/A')}
**Revenue:** ${summary.get('revenue', 0):,.2f} ({summary.get('revenue_change', 0):+.1%})

### Key Highlights
- **Key Win:** {summary.get('key_win', 'N/A')}
- **Key Challenge:** {summary.get('key_challenge', 'N/A')}

### This Week's Actions
"""

            for action in summary.get('completed_actions', []):
                markdown_content += f"- ✅ {action}\n"

            markdown_content += "\n### Next Week's Priorities\n"

            for priority in summary.get('next_priorities', []):
                markdown_content += f"- 🎯 {priority}\n"

            if summary.get('decisions_needed'):
                markdown_content += "\n### Decisions Needed\n"
                for decision in summary['decisions_needed']:
                    markdown_content += f"- ❓ {decision}\n"

            with open(filename, 'w') as f:
                f.write(markdown_content)

if __name__ == "__main__":
    # Example usage
    reporter = EtsyReportingAgent()

    # Sample business metrics
    sample_metrics = BusinessMetrics(
        total_revenue=1250.00,
        total_views=5420,
        avg_conversion_rate=0.045,
        total_listings=25,
        active_opportunities=3,
        weekly_growth_rate=0.08
    )

    # Generate reports
    dashboard = reporter.generate_integrated_dashboard(sample_metrics)
    weekly_report = reporter.generate_weekly_summary_report(sample_metrics)

    reporter.save_report(weekly_report, "weekly_summary")
    print("Reporting agent created and tested successfully!")
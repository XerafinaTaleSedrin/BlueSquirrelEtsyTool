#!/usr/bin/env python3
"""
Multi-Agent Etsy Business Intelligence System
Integrates Keyword Optimization, Trends Research, and Product Expansion agents
"""

import json
import sys
import os
from datetime import datetime

# Get the current directory and set up paths
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'etsy-agents/agents/keyword_optimizer'))
sys.path.append(os.path.join(current_dir, 'etsy-agents/agents/trend_researcher'))
sys.path.append(os.path.join(current_dir, 'etsy-agents/agents/product_expander'))
sys.path.append(current_dir)

from keyword_optimizer_agent import KeywordOptimizerAgent
from trend_researcher_agent import EtsyTrendsResearchAgent
from product_expander_agent import ProductExpanderAgent
from ecureuil_bleu_analysis_framework import EtsyAnalyzer

class MultiAgentAnalyzer:
    def __init__(self):
        self.keyword_agent = KeywordOptimizerAgent()
        self.trends_agent = EtsyTrendsResearchAgent()
        self.product_agent = ProductExpanderAgent()
        self.base_analyzer = EtsyAnalyzer()

    def run_comprehensive_analysis(self, csv_path="etsy-agents/EtsyListingsDownload.csv"):
        """Run comprehensive multi-agent analysis"""
        print("Starting Multi-Agent Business Intelligence Analysis...")
        print("=" * 60)

        # Load shop data
        shop_data = self._load_shop_data(csv_path)
        if not shop_data:
            print("❌ Failed to load shop data")
            return None

        print(f"Analyzing {len(shop_data['listings'])} listings...")

        # Run base analysis
        print("\n1. Running base SEO analysis...")
        base_analysis = self.base_analyzer.generate_comprehensive_analysis(shop_data)

        # Run keyword optimization analysis
        print("\n2. Running keyword optimization analysis...")
        keyword_analysis = self.keyword_agent.generate_portfolio_report(shop_data['listings'])

        # Run trends research
        print("\n3. Researching current market trends...")
        trends_analysis = self.trends_agent.generate_trend_report()

        # Run product expansion analysis
        print("\n4. Analyzing product expansion opportunities...")
        product_analysis = self.product_agent.generate_expansion_roadmap(shop_data['listings'])

        # Integrate all analyses
        print("\n5. Integrating multi-agent insights...")
        integrated_analysis = self._integrate_analyses(
            base_analysis, keyword_analysis, trends_analysis, product_analysis
        )

        print("\nMulti-agent analysis complete!")
        return integrated_analysis

    def _load_shop_data(self, csv_path):
        """Load shop data from CSV using existing parser"""
        try:
            # Import and use existing CSV parser
            from etsy_csv_analyzer import EtsyCSVParser
            parser = EtsyCSVParser(csv_path)
            listings = parser.parse_etsy_csv()

            if not listings:
                return None

            return {
                "total_listings": len(listings),
                "total_sales": 0,  # To be updated manually
                "avg_rating": 0.0,  # To be updated manually
                "listings": [
                    {
                        "title": listing.title,
                        "price": listing.price,
                        "views": listing.views,
                        "favorites": listing.favorites,
                        "sales": listing.sales,
                        "tags": listing.tags,
                        "category": listing.category,
                        "photos_count": listing.photos_count,
                        "description_length": listing.description_length
                    }
                    for listing in listings
                ]
            }
        except Exception as e:
            print(f"Error loading shop data: {e}")
            return None

    def _integrate_analyses(self, base_analysis, keyword_analysis, trends_analysis, product_analysis):
        """Integrate insights from all agents"""
        integration_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Cross-reference insights
        cross_insights = self._generate_cross_insights(
            keyword_analysis, trends_analysis, product_analysis
        )

        # Priority recommendations
        priority_actions = self._generate_priority_actions(
            keyword_analysis, trends_analysis, product_analysis
        )

        # Strategic roadmap
        strategic_roadmap = self._generate_strategic_roadmap(
            keyword_analysis, trends_analysis, product_analysis
        )

        integrated_report = {
            "analysis_metadata": {
                "generated_timestamp": integration_timestamp,
                "agents_used": ["base_seo", "keyword_optimizer", "trends_researcher", "product_expander"],
                "total_listings_analyzed": base_analysis.total_listings,
                "analysis_scope": "comprehensive_multi_agent"
            },
            "executive_summary": {
                "overall_shop_health": self._assess_shop_health(base_analysis, keyword_analysis),
                "key_opportunities": cross_insights["top_opportunities"],
                "immediate_actions": priority_actions["immediate"],
                "strategic_focus": strategic_roadmap["primary_focus"]
            },
            "agent_analyses": {
                "base_seo_analysis": self._serialize_base_analysis(base_analysis),
                "keyword_optimization": keyword_analysis,
                "trends_research": trends_analysis,
                "product_expansion": product_analysis
            },
            "cross_agent_insights": cross_insights,
            "priority_action_plan": priority_actions,
            "strategic_roadmap": strategic_roadmap,
            "integrated_recommendations": self._generate_integrated_recommendations(
                keyword_analysis, trends_analysis, product_analysis
            )
        }

        return integrated_report

    def _serialize_base_analysis(self, base_analysis):
        """Convert base analysis to serializable format"""
        try:
            from dataclasses import asdict
            return asdict(base_analysis)
        except:
            # Fallback serialization
            return {
                "shop_name": base_analysis.shop_name,
                "analysis_date": base_analysis.analysis_date,
                "total_listings": base_analysis.total_listings,
                "total_sales": base_analysis.total_sales,
                "avg_rating": base_analysis.avg_rating,
                "listings_count": len(base_analysis.listings),
                "seo_optimizations_count": len(base_analysis.seo_optimizations),
                "market_opportunities_count": len(base_analysis.market_opportunities)
            }

    def _generate_cross_insights(self, keyword_analysis, trends_analysis, product_analysis):
        """Generate insights by cross-referencing agent analyses"""

        # Find keyword-trend alignments
        hot_keywords_data = trends_analysis["detailed_findings"]["hot_keywords_last_90_days"]
        trending_keywords = []
        for trend in hot_keywords_data:
            if hasattr(trend, 'keyword'):
                trending_keywords.append(trend.keyword)
            elif isinstance(trend, dict):
                trending_keywords.append(trend.get("keyword", ""))
        current_keywords = [kw["keyword"] for kw in keyword_analysis["keyword_analyses"]]

        keyword_trend_gaps = []
        for trending_kw in trending_keywords:
            if not any(trending_kw.lower() in current_kw.lower() for current_kw in current_keywords):
                keyword_trend_gaps.append(trending_kw)

        # Find product-trend alignments
        category_trends_data = trends_analysis["detailed_findings"]["category_trends"]
        trending_categories = []
        for cat in category_trends_data:
            if hasattr(cat, 'category_name'):
                trending_categories.append(cat)
            elif isinstance(cat, dict):
                # Convert dict to object-like structure
                class CategoryTrend:
                    def __init__(self, **kwargs):
                        for k, v in kwargs.items():
                            setattr(self, k, v)
                trending_categories.append(CategoryTrend(**cat))
        current_product_categories = product_analysis["current_portfolio_analysis"]["current_categories"]

        category_expansion_opportunities = []
        for category_trend in trending_categories:
            category_name = category_trend.category_name.lower().replace(" ", "_")
            if category_name not in current_product_categories:
                category_expansion_opportunities.append({
                    "category": category_trend.category_name,
                    "growth_rate": category_trend.growth_rate,
                    "opportunity_score": category_trend.opportunity_score
                })

        # Find keyword-product synergies
        product_keyword_synergies = []
        immediate_products_data = product_analysis["expansion_priorities"]["immediate_launch"]
        immediate_products = []
        for prod in immediate_products_data:
            if hasattr(prod, 'product_name'):
                immediate_products.append(prod)
            elif isinstance(prod, dict):
                # Convert dict to object-like structure
                class ProductOpportunity:
                    def __init__(self, **kwargs):
                        for k, v in kwargs.items():
                            setattr(self, k, v)
                immediate_products.append(ProductOpportunity(**prod))
        keyword_recs = keyword_analysis["quick_wins"]

        for product in immediate_products:
            related_keywords = []
            for kw_rec in keyword_recs:
                if any(word in product.product_name.lower() for word in kw_rec["action"].lower().split()):
                    related_keywords.append(kw_rec)

            if related_keywords:
                product_keyword_synergies.append({
                    "product": product.product_name,
                    "supporting_keywords": related_keywords
                })

        return {
            "keyword_trend_gaps": keyword_trend_gaps[:5],  # Top 5 gaps
            "category_expansion_opportunities": sorted(
                category_expansion_opportunities,
                key=lambda x: x["opportunity_score"],
                reverse=True
            )[:3],  # Top 3 opportunities
            "product_keyword_synergies": product_keyword_synergies,
            "top_opportunities": [
                f"Add trending keyword: {keyword_trend_gaps[0] if keyword_trend_gaps else 'No major gaps'}",
                f"Expand into: {category_expansion_opportunities[0]['category'] if category_expansion_opportunities else 'Current categories optimal'}",
                f"Launch: {immediate_products[0].product_name if immediate_products else 'Focus on current optimization'}"
            ]
        }

    def _generate_priority_actions(self, keyword_analysis, trends_analysis, product_analysis):
        """Generate prioritized action plan across all agents"""

        # Immediate actions (this week)
        immediate = []

        # From keyword analysis
        if keyword_analysis["quick_wins"]:
            immediate.extend([
                f"🔧 {win['action']} - {win['effort']}"
                for win in keyword_analysis["quick_wins"][:2]
            ])

        # From trends analysis
        trending_keywords = trends_analysis["keyword_recommendations"]["immediate_add"]
        if trending_keywords:
            immediate.append(f"📈 Add trending keywords: {', '.join(trending_keywords[:3])}")

        # Short-term actions (next month)
        short_term = []

        # From product analysis
        immediate_products = product_analysis["expansion_priorities"]["immediate_launch"][:2]
        short_term.extend([
            f"🚀 Launch: {product.product_name} - {product.time_to_market}"
            for product in immediate_products
        ])

        # From trends analysis
        seasonal_prep = trends_analysis["detailed_findings"]["seasonal_forecasts"]
        if seasonal_prep:
            short_term.append(f"🗓️ Prepare for: {seasonal_prep[0].season}")

        # Medium-term actions (next quarter)
        medium_term = []

        # Strategic keyword overhaul
        if keyword_analysis["strategic_recommendations"]:
            medium_term.extend(keyword_analysis["strategic_recommendations"][:2])

        # Product portfolio expansion
        medium_products = product_analysis["expansion_priorities"]["medium_term"][:3]
        medium_term.extend([
            f"📦 Develop: {product.product_name}"
            for product in medium_products
        ])

        return {
            "immediate": immediate[:5],  # Top 5 immediate actions
            "short_term": short_term[:5],  # Top 5 short-term actions
            "medium_term": medium_term[:5]  # Top 5 medium-term actions
        }

    def _generate_strategic_roadmap(self, keyword_analysis, trends_analysis, product_analysis):
        """Generate long-term strategic roadmap"""

        # Determine primary strategic focus
        digital_opportunities = [p for p in product_analysis["expansion_priorities"]["immediate_launch"]
                               if "Digital" in p.product_category]

        if len(digital_opportunities) >= 3:
            primary_focus = "Digital Product Expansion"
        elif trends_analysis["detailed_findings"]["political_niche_insights"]["niche_health"] == "Strong and growing":
            primary_focus = "Niche Market Domination"
        else:
            primary_focus = "Portfolio Optimization"

        # Strategic phases
        phases = {
            "phase_1_optimization": {
                "timeline": "Next 2 months",
                "focus": "Optimize existing portfolio",
                "key_actions": [
                    "Complete keyword optimization across all listings",
                    "Implement top trending keywords",
                    "Launch 2-3 high-priority digital products"
                ]
            },
            "phase_2_expansion": {
                "timeline": "Months 3-6",
                "focus": "Strategic product expansion",
                "key_actions": [
                    "Launch POD product line",
                    "Develop digital product suites",
                    "Enter trending categories"
                ]
            },
            "phase_3_scaling": {
                "timeline": "Months 7-12",
                "focus": "Scale and diversify",
                "key_actions": [
                    "Expand to new customer segments",
                    "Develop premium product lines",
                    "Build brand recognition in niche"
                ]
            }
        }

        return {
            "primary_focus": primary_focus,
            "strategic_phases": phases,
            "success_metrics": {
                "revenue_target": "100% increase in 12 months",
                "product_diversity": "Double current category count",
                "market_position": "Top 3 in government humor niche"
            }
        }

    def _assess_shop_health(self, base_analysis, keyword_analysis):
        """Assess overall shop health using multiple metrics"""

        # SEO health
        avg_seo_score = sum(listing.seo_score for listing in base_analysis.listings) / len(base_analysis.listings)

        # Keyword health
        portfolio_health = keyword_analysis["portfolio_summary"]
        keyword_efficiency = portfolio_health["avg_keywords_per_listing"] / 13  # Max tags is 13

        # Overall assessment
        if avg_seo_score >= 75 and keyword_efficiency >= 0.8:
            health_status = "Excellent"
        elif avg_seo_score >= 60 and keyword_efficiency >= 0.6:
            health_status = "Good"
        elif avg_seo_score >= 45 and keyword_efficiency >= 0.4:
            health_status = "Fair"
        else:
            health_status = "Needs Improvement"

        return {
            "status": health_status,
            "seo_score": f"{avg_seo_score:.1f}/100",
            "keyword_efficiency": f"{keyword_efficiency*100:.1f}%",
            "optimization_potential": "High" if health_status in ["Fair", "Needs Improvement"] else "Medium"
        }

    def _generate_integrated_recommendations(self, keyword_analysis, trends_analysis, product_analysis):
        """Generate integrated recommendations combining all agent insights"""

        recommendations = {
            "seo_keyword_strategy": {
                "immediate_keywords_to_add": trends_analysis["keyword_recommendations"]["immediate_add"],
                "keywords_to_remove": [kw["keyword"] for kw in keyword_analysis["keyword_analyses"]
                                     if kw["action_recommendation"] == "Remove"][:5],
                "long_tail_opportunities": ["government worker gift", "cyber security humor", "federal employee"],
                "seasonal_timing": "Add election/holiday keywords by October 1st"
            },
            "product_development_strategy": {
                "digital_first_approach": "Launch 3 digital products before POD expansion",
                "pod_priorities": [p.product_name for p in product_analysis["expansion_priorities"]["immediate_launch"][:3]],
                "bundle_opportunities": [suite.suite_name for suite in product_analysis["digital_product_suites"]],
                "variation_strategy": "Create agency-specific versions of successful products"
            },
            "market_positioning": {
                "niche_focus": "Government employee humor and cybersecurity",
                "competitive_advantage": "Insider knowledge and workplace-appropriate designs",
                "target_expansion": ["government contractors", "policy professionals", "IT security workers"],
                "pricing_strategy": "Premium pricing for specialized knowledge"
            },
            "growth_timeline": {
                "30_days": "Complete keyword optimization, launch 2 digital products",
                "60_days": "Add 3 POD products, implement trending keywords",
                "90_days": "Launch product bundles, expand to new categories",
                "6_months": "Achieve portfolio diversification and market position goals"
            }
        }

        return recommendations

    def export_multi_agent_report(self, analysis_data, filename="multi_agent_analysis_report.json"):
        """Export comprehensive multi-agent analysis to JSON"""

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False, default=str)

        print(f"Multi-agent analysis exported to: {filename}")

def main():
    """Run multi-agent analysis"""
    analyzer = MultiAgentAnalyzer()

    print("EcureuilBleu Multi-Agent Business Intelligence System")
    print("=" * 60)

    # Run comprehensive analysis
    analysis_results = analyzer.run_comprehensive_analysis()

    if analysis_results:
        # Export results
        analyzer.export_multi_agent_report(analysis_results)

        # Print executive summary
        print("\n" + "=" * 60)
        print("EXECUTIVE SUMMARY")
        print("=" * 60)

        summary = analysis_results["executive_summary"]
        print(f"Shop Health: {summary['overall_shop_health']['status']}")
        print(f"SEO Score: {summary['overall_shop_health']['seo_score']}")
        print(f"Keyword Efficiency: {summary['overall_shop_health']['keyword_efficiency']}")

        print("\nTOP OPPORTUNITIES:")
        for i, opp in enumerate(summary["key_opportunities"], 1):
            print(f"  {i}. {opp}")

        print("\nIMMEDIATE ACTIONS:")
        for i, action in enumerate(summary["immediate_actions"], 1):
            print(f"  {i}. {action}")

        print(f"\nSTRATEGIC FOCUS: {summary['strategic_focus']}")

        print("\nMulti-agent analysis complete! Check the JSON file for detailed insights.")

    else:
        print("Analysis failed. Please check your data files and try again.")

if __name__ == "__main__":
    main()
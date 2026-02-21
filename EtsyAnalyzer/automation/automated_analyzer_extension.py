#!/usr/bin/env python3
"""
Automated EtsyAnalyzer Extension
Adds automation triggers and workflow orchestration to the existing EtsyAnalyzer system
"""

import json
import os
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import existing analyzer components
try:
    from multi_agent_analyzer import MultiAgentAnalyzer
except ImportError:
    MultiAgentAnalyzer = None

# Import our automation components
try:
    from design_generation_system import DesignWorkflowManager
    from listing_content_generator import ListingWorkflowManager
    from printful_catalog import PrintfulCatalogManager, validate_printful_products, get_available_products
except ImportError:
    DesignWorkflowManager = None
    ListingWorkflowManager = None
    PrintfulCatalogManager = None

@dataclass
class AutomationTrigger:
    """Defines when and how to trigger automation workflows"""
    trigger_type: str  # trend_detected, opportunity_found, schedule_based
    condition: str     # Specific condition that triggers automation
    threshold: float   # Numerical threshold for triggering
    action: str        # What action to take
    priority: int      # 1-5, 5 being highest priority
    last_triggered: Optional[str] = None
    enabled: bool = True

@dataclass
class WorkflowExecution:
    """Records workflow execution details"""
    execution_id: str
    trigger_type: str
    timestamp: str
    actions_taken: List[str]
    outputs_generated: List[str]
    success: bool
    error_message: Optional[str] = None
    metrics: Dict = None

class AutomatedAnalyzerOrchestrator:
    """Orchestrates automated workflows based on market intelligence"""

    def __init__(self, config_file: str = "automation_config.json"):
        self.config_file = config_file
        self.config = self._load_config()
        self.triggers = self._initialize_triggers()
        self.execution_history = []

        # Initialize workflow managers
        self.design_manager = DesignWorkflowManager() if DesignWorkflowManager else None
        self.listing_manager = ListingWorkflowManager() if ListingWorkflowManager else None
        self.analyzer = MultiAgentAnalyzer() if MultiAgentAnalyzer else None

    def _load_config(self) -> Dict:
        """Load automation configuration"""
        default_config = {
            "automation_enabled": True,
            "max_daily_executions": 10,
            "output_directory": "DESIGNS/automated_outputs",
            "notification_settings": {
                "email_enabled": False,
                "email_address": "",
                "webhook_url": ""
            },
            "workflow_settings": {
                "auto_generate_designs": True,
                "auto_create_listings": True,
                "auto_pricing": True,
                "quality_checks": True
            }
        }

        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        else:
            # Create default config
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=2)
            return default_config

    def _initialize_triggers(self) -> List[AutomationTrigger]:
        """Initialize automation triggers based on your business intelligence"""
        return [
            # Trend-based triggers
            AutomationTrigger(
                trigger_type="trending_keyword_detected",
                condition="keyword_trend_gap_count > threshold",
                threshold=3.0,
                action="generate_trend_based_designs",
                priority=5
            ),
            AutomationTrigger(
                trigger_type="category_growth_detected",
                condition="category_growth_rate > threshold",
                threshold=30.0,  # 30% growth
                action="create_category_expansion_products",
                priority=4
            ),
            AutomationTrigger(
                trigger_type="seo_opportunity_found",
                condition="seo_score < threshold",
                threshold=75.0,
                action="optimize_existing_listings",
                priority=3
            ),

            # Seasonal triggers
            AutomationTrigger(
                trigger_type="seasonal_preparation",
                condition="days_until_season < threshold",
                threshold=45.0,  # 45 days before season
                action="create_seasonal_products",
                priority=4
            ),

            # Performance triggers
            AutomationTrigger(
                trigger_type="low_performing_listings",
                condition="avg_listing_performance < threshold",
                threshold=2.0,  # Low views/favorites
                action="refresh_underperforming_content",
                priority=2
            ),

            # Opportunity triggers
            AutomationTrigger(
                trigger_type="new_market_opportunity",
                condition="opportunity_score > threshold",
                threshold=7.0,  # High opportunity score
                action="rapid_product_development",
                priority=5
            ),

            # Schedule-based triggers
            AutomationTrigger(
                trigger_type="weekly_analysis",
                condition="days_since_last_analysis > threshold",
                threshold=7.0,
                action="run_comprehensive_analysis",
                priority=1
            ),
            AutomationTrigger(
                trigger_type="monthly_portfolio_review",
                condition="days_since_portfolio_review > threshold",
                threshold=30.0,
                action="comprehensive_portfolio_optimization",
                priority=2
            )
        ]

    def run_automated_analysis_cycle(self) -> Dict:
        """Run complete automated analysis and trigger appropriate workflows"""

        if not self.config["automation_enabled"]:
            return {"status": "disabled", "message": "Automation is disabled in config"}

        print("AUTOMATION Starting Automated Analysis Cycle...")
        cycle_start = datetime.now()

        # Step 1: Run market intelligence analysis
        analysis_results = self._run_market_analysis()
        if not analysis_results:
            return {"status": "failed", "message": "Market analysis failed"}

        # Step 2: Evaluate triggers
        triggered_actions = self._evaluate_triggers(analysis_results)

        # Step 3: Execute triggered workflows
        execution_results = []
        for action in triggered_actions:
            result = self._execute_workflow(action, analysis_results)
            execution_results.append(result)

        # Step 4: Generate summary report
        summary = self._generate_cycle_summary(cycle_start, analysis_results, execution_results)

        # Step 5: Save results and update history
        self._save_cycle_results(summary, execution_results)

        return summary

    def _run_market_analysis(self) -> Optional[Dict]:
        """Run the multi-agent market analysis"""
        if not self.analyzer:
            print("ERROR MultiAgentAnalyzer not available")
            return None

        try:
            print("ANALYSIS Running market intelligence analysis...")
            analysis_results = self.analyzer.run_comprehensive_analysis()

            if analysis_results:
                # Save analysis results
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                analysis_file = f"automated_analysis_{timestamp}.json"

                with open(analysis_file, 'w', encoding='utf-8') as f:
                    json.dump(analysis_results, f, indent=2, default=str)

                print(f"SUCCESS Analysis complete: {analysis_file}")
                return analysis_results

        except Exception as e:
            print(f"ERROR Analysis failed: {e}")
            return None

    def _evaluate_triggers(self, analysis_data: Dict) -> List[Dict]:
        """Evaluate which automation triggers should fire"""
        triggered_actions = []

        for trigger in self.triggers:
            if not trigger.enabled:
                continue

            should_trigger = False
            trigger_context = {}

            try:
                # Evaluate different trigger types
                if trigger.trigger_type == "trending_keyword_detected":
                    gap_count = len(analysis_data.get("cross_agent_insights", {}).get("keyword_trend_gaps", []))
                    should_trigger = gap_count > trigger.threshold
                    trigger_context = {"gap_count": gap_count, "gaps": analysis_data.get("cross_agent_insights", {}).get("keyword_trend_gaps", [])}

                elif trigger.trigger_type == "category_growth_detected":
                    opportunities = analysis_data.get("cross_agent_insights", {}).get("category_expansion_opportunities", [])
                    for opp in opportunities:
                        growth_rate = float(opp.get("growth_rate", "0").replace("%", "").replace("+", ""))
                        if growth_rate > trigger.threshold:
                            should_trigger = True
                            trigger_context = {"opportunity": opp, "growth_rate": growth_rate}
                            break

                elif trigger.trigger_type == "seo_opportunity_found":
                    seo_score = float(analysis_data.get("executive_summary", {}).get("overall_shop_health", {}).get("seo_score", "0/100").split("/")[0])
                    should_trigger = seo_score < trigger.threshold
                    trigger_context = {"current_seo_score": seo_score}

                elif trigger.trigger_type == "new_market_opportunity":
                    opportunities = analysis_data.get("cross_agent_insights", {}).get("category_expansion_opportunities", [])
                    for opp in opportunities:
                        if opp.get("opportunity_score", 0) > trigger.threshold:
                            should_trigger = True
                            trigger_context = {"opportunity": opp}
                            break

                elif trigger.trigger_type == "weekly_analysis":
                    # Check if last analysis was more than threshold days ago
                    if trigger.last_triggered:
                        last_trigger = datetime.fromisoformat(trigger.last_triggered)
                        days_since = (datetime.now() - last_trigger).days
                        should_trigger = days_since > trigger.threshold
                    else:
                        should_trigger = True  # First time

                # Add trigger to action list if conditions met
                if should_trigger:
                    triggered_actions.append({
                        "trigger": trigger,
                        "context": trigger_context,
                        "timestamp": datetime.now().isoformat()
                    })

                    # Update last triggered time
                    trigger.last_triggered = datetime.now().isoformat()

                    print(f"TARGET Triggered: {trigger.action} (Priority: {trigger.priority})")

            except Exception as e:
                print(f"WARNING: Error evaluating trigger {trigger.trigger_type}: {e}")
                continue

        # Sort by priority (highest first)
        triggered_actions.sort(key=lambda x: x["trigger"].priority, reverse=True)

        return triggered_actions

    def _execute_workflow(self, action_data: Dict, analysis_results: Dict) -> WorkflowExecution:
        """Execute a specific automation workflow"""

        trigger = action_data["trigger"]
        context = action_data["context"]
        execution_id = f"{trigger.action}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        print(f"STARTING Executing: {trigger.action}")

        try:
            actions_taken = []
            outputs_generated = []

            if trigger.action == "generate_trend_based_designs":
                outputs = self._generate_trend_designs(analysis_results, context)
                actions_taken.append("Generated trending keyword-based designs")
                outputs_generated.extend(outputs)

            elif trigger.action == "create_category_expansion_products":
                outputs = self._create_expansion_products(analysis_results, context)
                actions_taken.append("Created category expansion products")
                outputs_generated.extend(outputs)

            elif trigger.action == "optimize_existing_listings":
                outputs = self._optimize_listings(analysis_results, context)
                actions_taken.append("Optimized existing listing content")
                outputs_generated.extend(outputs)

            elif trigger.action == "create_seasonal_products":
                outputs = self._create_seasonal_products(analysis_results, context)
                actions_taken.append("Created seasonal product variations")
                outputs_generated.extend(outputs)

            elif trigger.action == "rapid_product_development":
                outputs = self._rapid_product_development(analysis_results, context)
                actions_taken.append("Rapid development of high-opportunity products")
                outputs_generated.extend(outputs)

            else:
                actions_taken.append(f"Unknown action: {trigger.action}")

            return WorkflowExecution(
                execution_id=execution_id,
                trigger_type=trigger.trigger_type,
                timestamp=datetime.now().isoformat(),
                actions_taken=actions_taken,
                outputs_generated=outputs_generated,
                success=True,
                metrics={"outputs_count": len(outputs_generated)}
            )

        except Exception as e:
            print(f"ERROR Workflow execution failed: {e}")
            return WorkflowExecution(
                execution_id=execution_id,
                trigger_type=trigger.trigger_type,
                timestamp=datetime.now().isoformat(),
                actions_taken=[],
                outputs_generated=[],
                success=False,
                error_message=str(e)
            )

    def _generate_trend_designs(self, analysis_results: Dict, context: Dict) -> List[str]:
        """Generate designs based on trending keywords"""
        if not self.design_manager:
            return []

        try:
            # Create temporary analysis file for design manager
            temp_analysis = "DESIGNS/temp/temp_analysis_for_design.json"
            os.makedirs(os.path.dirname(temp_analysis), exist_ok=True)
            with open(temp_analysis, 'w', encoding='utf-8') as f:
                json.dump(analysis_results, f, indent=2, default=str)

            # Generate design prompts
            prompts = self.design_manager.process_market_analysis(temp_analysis)

            # Clean up temp file
            if os.path.exists(temp_analysis):
                os.remove(temp_analysis)

            return prompts

        except Exception as e:
            print(f"Error generating trend designs: {e}")
            return []

    def _create_expansion_products(self, analysis_results: Dict, context: Dict) -> List[str]:
        """Create products for category expansion opportunities"""
        if not self.design_manager or not self.listing_manager:
            return []

        try:
            # Focus on the specific opportunity from context
            opportunity = context.get("opportunity", {})
            category = opportunity.get("category", "")

            # Create focused design brief for this category
            focused_brief = {
                "concept_name": f"expansion_{category.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "target_keywords": [category.lower(), "professional", "gift"],
                "design_theme": "government_humor" if "government" in category.lower() else "professional",
                "target_audience": f"{category} professionals",
                "style_preferences": ["professional", "clean", "humorous"],
                "printful_products": self._get_validated_printful_products(category, "apparel"),
                "priority_score": opportunity.get("opportunity_score", 5.0)
            }

            # Generate design and listing content
            outputs = []

            # Save the focused brief
            brief_file = f"DESIGNS/briefs/expansion_brief_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            os.makedirs(os.path.dirname(brief_file), exist_ok=True)
            with open(brief_file, 'w', encoding='utf-8') as f:
                json.dump(focused_brief, f, indent=2)
            outputs.append(brief_file)

            return outputs

        except Exception as e:
            print(f"Error creating expansion products: {e}")
            return []

    def _optimize_listings(self, analysis_results: Dict, context: Dict) -> List[str]:
        """Optimize existing listings based on SEO analysis"""
        if not self.listing_manager:
            return []

        try:
            # Generate optimization recommendations
            recommendations_file = f"DESIGNS/seo_recommendations/seo_optimization_recommendations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

            current_seo = context.get("current_seo_score", 0)

            recommendations = {
                "current_seo_score": current_seo,
                "target_seo_score": 85.0,
                "optimization_actions": [
                    "Add trending keywords to existing titles",
                    "Enhance product descriptions with SEO keywords",
                    "Update tags with high-performing keywords",
                    "Optimize for seasonal search terms"
                ],
                "trending_keywords": analysis_results.get("cross_agent_insights", {}).get("keyword_trend_gaps", []),
                "immediate_keywords": analysis_results.get("integrated_recommendations", {}).get("seo_keyword_strategy", {}).get("immediate_keywords_to_add", [])
            }

            os.makedirs(os.path.dirname(recommendations_file), exist_ok=True)
            with open(recommendations_file, 'w', encoding='utf-8') as f:
                json.dump(recommendations, f, indent=2)

            return [recommendations_file]

        except Exception as e:
            print(f"Error optimizing listings: {e}")
            return []

    def _create_seasonal_products(self, analysis_results: Dict, context: Dict) -> List[str]:
        """Create seasonal product variations"""
        # Implementation for seasonal products
        season_file = f"DESIGNS/seasonal/seasonal_products_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        seasonal_data = {
            "season": "Q4 2025",
            "seasonal_keywords": ["holiday", "election", "year-end", "government budget"],
            "product_variations": [
                "Holiday Government Humor Collection",
                "Election Season Professional Wear",
                "Year-End Budget Jokes Apparel"
            ],
            "timing": "Launch 45 days before season peak"
        }

        os.makedirs(os.path.dirname(season_file), exist_ok=True)
        with open(season_file, 'w', encoding='utf-8') as f:
            json.dump(seasonal_data, f, indent=2)

        return [season_file]

    def _rapid_product_development(self, analysis_results: Dict, context: Dict) -> List[str]:
        """Rapid development for high-opportunity products"""
        opportunity = context.get("opportunity", {})

        rapid_dev_file = f"DESIGNS/rapid_dev/rapid_development_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        rapid_plan = {
            "opportunity": opportunity,
            "development_timeline": "7-14 days",
            "priority_products": [
                "High-opportunity category lead product",
                "Complementary product variations",
                "Bundle opportunities"
            ],
            "go_to_market_strategy": "Fast launch with A/B testing"
        }

        os.makedirs(os.path.dirname(rapid_dev_file), exist_ok=True)
        with open(rapid_dev_file, 'w', encoding='utf-8') as f:
            json.dump(rapid_plan, f, indent=2)

        return [rapid_dev_file]

    def _generate_cycle_summary(self, start_time: datetime, analysis_results: Dict, execution_results: List[WorkflowExecution]) -> Dict:
        """Generate summary of automation cycle"""

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        successful_executions = [ex for ex in execution_results if ex.success]
        failed_executions = [ex for ex in execution_results if not ex.success]

        summary = {
            "cycle_id": f"auto_cycle_{start_time.strftime('%Y%m%d_%H%M%S')}",
            "timestamp": start_time.isoformat(),
            "duration_seconds": duration,
            "status": "completed",
            "analysis_summary": {
                "shop_health": analysis_results.get("executive_summary", {}).get("overall_shop_health", {}),
                "key_opportunities": analysis_results.get("executive_summary", {}).get("key_opportunities", []),
                "immediate_actions": analysis_results.get("executive_summary", {}).get("immediate_actions", [])
            },
            "automation_results": {
                "total_workflows_executed": len(execution_results),
                "successful_workflows": len(successful_executions),
                "failed_workflows": len(failed_executions),
                "total_outputs_generated": sum(len(ex.outputs_generated) for ex in successful_executions)
            },
            "workflow_details": [asdict(ex) for ex in execution_results],
            "next_recommended_actions": self._generate_next_actions(analysis_results, execution_results)
        }

        return summary

    def _generate_next_actions(self, analysis_results: Dict, execution_results: List[WorkflowExecution]) -> List[str]:
        """Generate recommended next actions based on automation results"""

        actions = []

        # Check if any workflows failed
        failed_workflows = [ex for ex in execution_results if not ex.success]
        if failed_workflows:
            actions.append("Review and fix failed automation workflows")

        # Check for outputs that need manual review
        total_outputs = sum(len(ex.outputs_generated) for ex in execution_results if ex.success)
        if total_outputs > 0:
            actions.append(f"Review {total_outputs} generated outputs for quality and accuracy")

        # Check for immediate opportunities
        immediate_actions = analysis_results.get("executive_summary", {}).get("immediate_actions", [])
        if immediate_actions:
            actions.append("Implement immediate market opportunities identified")

        # Standard follow-up actions
        actions.extend([
            "Create actual designs from generated concepts",
            "Upload optimized content to Etsy",
            "Monitor performance of new listings"
        ])

        return actions

    def _save_cycle_results(self, summary: Dict, execution_results: List[WorkflowExecution]):
        """Save automation cycle results"""

        # Ensure output directory exists
        os.makedirs(self.config["output_directory"], exist_ok=True)

        # Save summary
        summary_file = os.path.join(
            self.config["output_directory"],
            f"automation_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, default=str)

        # Update execution history
        self.execution_history.append(summary)

        # Keep only last 50 executions in memory
        if len(self.execution_history) > 50:
            self.execution_history = self.execution_history[-50:]

        print(f"FILE Automation results saved: {summary_file}")

    def _get_validated_printful_products(self, theme_or_category: str, product_type: str = "apparel") -> List[str]:
        """Get validated Printful products based on theme/category and type"""
        try:
            if PrintfulCatalogManager is None:
                # Fallback to safe defaults if catalog manager not available
                print("Warning: Printful catalog not available, using fallback products")
                return ["t-shirt", "hoodie"]

            # Get available products from catalog
            available_products = get_available_products(product_type)

            if not available_products:
                # If no catalog data, use validated defaults
                return ["unisex-basic-softstyle-t-shirt", "unisex-heavy-cotton-hoodie"]

            # Map theme/category to appropriate product types
            product_mapping = {
                "government": ["t-shirt", "hoodie", "mug", "embroidered-hat"],
                "cybersecurity": ["t-shirt", "hoodie", "laptop-sleeve", "mug"],
                "political": ["t-shirt", "hoodie", "tote-bag", "sticker"],
                "professional": ["polo-shirt", "embroidered-shirt", "mug", "notebook"],
                "humor": ["t-shirt", "hoodie", "mug", "sticker"],
                "apparel": ["t-shirt", "hoodie", "sweatshirt"],
                "accessories": ["mug", "tote-bag", "sticker", "phone-case"],
                "home": ["mug", "pillow", "poster", "canvas"]
            }

            # Determine products based on theme/category
            theme_lower = theme_or_category.lower()
            suggested_products = []

            for key, products in product_mapping.items():
                if key in theme_lower:
                    suggested_products.extend(products)
                    break

            if not suggested_products:
                # Default based on product type
                if product_type == "apparel":
                    suggested_products = ["t-shirt", "hoodie"]
                elif product_type == "accessories":
                    suggested_products = ["mug", "tote-bag"]
                else:
                    suggested_products = ["t-shirt", "mug"]

            # Validate against Printful catalog
            validated_products = []
            for product in suggested_products:
                # Check if product exists in catalog (case-insensitive partial match)
                matches = [p for p in available_products
                          if product.lower().replace('-', ' ') in p['name'].lower()
                          or product.lower() in p['type_name'].lower()]

                if matches:
                    # Use the actual Printful product name
                    validated_products.append(matches[0]['name'])
                else:
                    # Try to find a close alternative
                    alternatives = [p for p in available_products
                                  if any(word in p['name'].lower()
                                        for word in product.lower().split('-'))]
                    if alternatives:
                        validated_products.append(alternatives[0]['name'])

            # Ensure we have at least 2 products
            if len(validated_products) < 2:
                # Add popular defaults if needed
                defaults = [p for p in available_products
                           if any(term in p['name'].lower()
                                 for term in ['t-shirt', 'shirt', 'tee'])]
                if defaults and defaults[0]['name'] not in validated_products:
                    validated_products.append(defaults[0]['name'])

                # Add mug as backup
                mugs = [p for p in available_products
                       if 'mug' in p['name'].lower()]
                if mugs and len(validated_products) < 2:
                    validated_products.append(mugs[0]['name'])

            # Limit to top 3 products
            return validated_products[:3] if validated_products else ["t-shirt", "mug"]

        except Exception as e:
            print(f"Error validating Printful products: {e}")
            # Safe fallback
            return ["t-shirt", "hoodie", "mug"]

    def get_automation_status(self) -> Dict:
        """Get current automation status and recent history"""

        return {
            "automation_enabled": self.config["automation_enabled"],
            "active_triggers": len([t for t in self.triggers if t.enabled]),
            "total_triggers": len(self.triggers),
            "recent_executions": self.execution_history[-5:] if self.execution_history else [],
            "last_execution": self.execution_history[-1] if self.execution_history else None,
            "next_scheduled_analysis": "Every 7 days (weekly trigger)"
        }

def main():
    """Example usage of the automated analyzer extension"""

    print("AUTOMATION EtsyAnalyzer Automation System")
    print("=" * 50)

    # Initialize orchestrator
    orchestrator = AutomatedAnalyzerOrchestrator()

    # Show current status
    status = orchestrator.get_automation_status()
    print(f"Automation Status: {'Enabled' if status['automation_enabled'] else 'Disabled'}")
    print(f"Active Triggers: {status['active_triggers']}/{status['total_triggers']}")

    # Run automated cycle
    print("\nRunning automated analysis cycle...")
    results = orchestrator.run_automated_analysis_cycle()

    if results["status"] == "completed":
        print(f"\nSUCCESS Automation cycle completed successfully!")
        print(f"Duration: {results.get('duration_seconds', 0):.1f} seconds")
        print(f"Workflows executed: {results['automation_results']['total_workflows_executed']}")
        print(f"Outputs generated: {results['automation_results']['total_outputs_generated']}")

        if results.get('next_recommended_actions'):
            print("\nINFO Next Recommended Actions:")
            for i, action in enumerate(results['next_recommended_actions'][:5], 1):
                print(f"  {i}. {action}")
    else:
        print(f"\nERROR Automation cycle failed: {results.get('message', 'Unknown error')}")

if __name__ == "__main__":
    main()
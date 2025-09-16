#!/usr/bin/env python3
"""
Shared data models for Etsy Business Intelligence agents
Provides common data structures and utilities across all agents
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Any
from datetime import datetime
from enum import Enum
import json

class PerformanceStatus(Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"

class OpportunityTimeline(Enum):
    QUICK_WIN = "Quick Win"
    WEEKEND_PROJECT = "Weekend Project"
    MAJOR_INITIATIVE = "Major Initiative"
    LONG_TERM_STRATEGY = "Long-term Strategy"

class CompetitionLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

@dataclass
class ListingData:
    """Core listing information from Etsy"""
    listing_id: str
    title: str
    description: str
    price: float
    category: str
    shop_section: str
    tags: List[str]
    materials: List[str]
    photos: List[str]
    created_date: datetime
    last_updated: datetime

@dataclass
class PerformanceMetrics:
    """Performance metrics for a listing"""
    views: int = 0
    visits: int = 0
    favorites: int = 0
    orders: int = 0
    revenue: float = 0.0
    conversion_rate: float = 0.0
    click_through_rate: float = 0.0
    favorite_rate: float = 0.0
    search_visibility: float = 0.0
    avg_position: float = 0.0
    period_start: datetime = field(default_factory=datetime.now)
    period_end: datetime = field(default_factory=datetime.now)

@dataclass
class SEOMetrics:
    """SEO-specific metrics and scores"""
    overall_score: int = 0
    title_score: int = 0
    tag_score: int = 0
    photo_score: int = 0
    description_score: int = 0
    keyword_density: float = 0.0
    keyword_ranking: Dict[str, int] = field(default_factory=dict)
    competitor_analysis: Dict[str, Any] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)

@dataclass
class MarketOpportunity:
    """Market opportunity data structure"""
    id: str
    name: str
    category: str
    subcategory: str = ""
    description: str = ""
    keywords: List[str] = field(default_factory=list)
    search_volume: int = 0
    competition_level: CompetitionLevel = CompetitionLevel.MEDIUM
    avg_price: float = 0.0
    price_range: tuple = (0.0, 0.0)
    seasonal_factor: float = 1.0
    trend_direction: str = "stable"  # "growing", "stable", "declining"

    # Feasibility analysis
    skill_requirements: Set[str] = field(default_factory=set)
    tool_requirements: Set[str] = field(default_factory=set)
    material_requirements: List[str] = field(default_factory=list)
    time_investment: str = ""  # From OpportunityTimeline

    # Scoring
    effort_score: int = 3  # 1-5 scale
    impact_score: int = 3  # 1-5 scale
    confidence_score: int = 3  # 1-5 scale
    priority_score: float = 0.0  # Calculated RICE score

    # Analysis metadata
    analyzed_date: datetime = field(default_factory=datetime.now)
    data_sources: List[str] = field(default_factory=list)
    notes: str = ""

@dataclass
class UserCapabilities:
    """User's skills, tools, and constraints"""
    # Skills and expertise
    skills: Set[str] = field(default_factory=set)
    skill_levels: Dict[str, str] = field(default_factory=dict)  # skill -> "Beginner", "Intermediate", "Advanced"
    learning_capacity: str = "Medium"  # "High", "Medium", "Low"

    # Tools and equipment
    tools_available: Set[str] = field(default_factory=set)
    tools_not_available: Set[str] = field(default_factory=set)
    workspace_type: str = "home"  # "home", "studio", "shared", etc.

    # Constraints
    time_availability: Dict[str, int] = field(default_factory=dict)  # hours per time period
    budget_constraints: Dict[str, float] = field(default_factory=dict)  # budget limits
    physical_limitations: List[str] = field(default_factory=list)

    # Preferences
    preferred_categories: Set[str] = field(default_factory=set)
    excluded_categories: Set[str] = field(default_factory=set)
    risk_tolerance: str = "Medium"  # "High", "Medium", "Low"

    last_updated: datetime = field(default_factory=datetime.now)

@dataclass
class BusinessGoals:
    """Business objectives and targets"""
    monthly_revenue_target: float = 0.0
    monthly_view_target: int = 0
    conversion_rate_target: float = 0.0
    new_listing_target: int = 0
    market_expansion_goals: List[str] = field(default_factory=list)
    timeline: str = "monthly"  # "weekly", "monthly", "quarterly", "yearly"
    priority_level: str = "medium"  # "high", "medium", "low"

@dataclass
class ActionItem:
    """Trackable action item with priority and status"""
    id: str
    title: str
    description: str
    category: str  # "seo", "market_research", "operations", "strategy"
    priority: str  # "high", "medium", "low"
    status: str = "pending"  # "pending", "in_progress", "completed", "blocked", "cancelled"

    # Timing
    created_date: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None
    estimated_time: str = ""  # "30 minutes", "2 hours", etc.
    actual_time: str = ""

    # Tracking
    assigned_to: str = "user"  # Could be "seo_agent", "market_agent", etc.
    dependencies: List[str] = field(default_factory=list)  # IDs of other actions
    tags: List[str] = field(default_factory=list)

    # Outcomes
    expected_outcome: str = ""
    actual_outcome: str = ""
    impact_measurement: Dict[str, Any] = field(default_factory=dict)

    # Metadata
    source_agent: str = ""  # Which agent generated this action
    notes: str = ""

@dataclass
class BusinessSnapshot:
    """Point-in-time snapshot of business performance"""
    date: datetime

    # Core metrics
    total_revenue: float = 0.0
    total_views: int = 0
    total_visits: int = 0
    total_orders: int = 0
    total_listings: int = 0
    active_listings: int = 0

    # Calculated metrics
    avg_conversion_rate: float = 0.0
    avg_order_value: float = 0.0
    revenue_per_listing: float = 0.0

    # Growth metrics
    revenue_growth: float = 0.0
    view_growth: float = 0.0
    listing_growth: int = 0

    # SEO health
    overall_seo_health: str = "unknown"  # "excellent", "good", "needs_work", "critical"
    listings_by_status: Dict[str, int] = field(default_factory=dict)  # GREEN, YELLOW, RED counts

    # Opportunities
    active_opportunities: int = 0
    completed_opportunities: int = 0
    total_potential_revenue: float = 0.0

    # Goals tracking
    monthly_progress: Dict[str, float] = field(default_factory=dict)  # goal -> progress percentage

class EtsyDataValidator:
    """Validation utilities for Etsy data models"""

    @staticmethod
    def validate_listing_data(data: ListingData) -> List[str]:
        """Validate listing data and return list of errors"""
        errors = []

        if not data.listing_id or not data.listing_id.strip():
            errors.append("Listing ID is required")

        if not data.title or len(data.title.strip()) < 3:
            errors.append("Title must be at least 3 characters")

        if data.price <= 0:
            errors.append("Price must be positive")

        if len(data.tags) > 13:
            errors.append("Cannot have more than 13 tags")

        return errors

    @staticmethod
    def validate_performance_metrics(metrics: PerformanceMetrics) -> List[str]:
        """Validate performance metrics"""
        errors = []

        if metrics.views < 0:
            errors.append("Views cannot be negative")

        if metrics.visits > metrics.views:
            errors.append("Visits cannot exceed views")

        if metrics.orders > metrics.visits:
            errors.append("Orders cannot exceed visits")

        if metrics.conversion_rate < 0 or metrics.conversion_rate > 1:
            errors.append("Conversion rate must be between 0 and 1")

        return errors

class EtsyDataTransformer:
    """Utility class for transforming and aggregating Etsy data"""

    @staticmethod
    def aggregate_metrics(metrics_list: List[PerformanceMetrics]) -> PerformanceMetrics:
        """Aggregate multiple performance metrics into a summary"""
        if not metrics_list:
            return PerformanceMetrics()

        total_views = sum(m.views for m in metrics_list)
        total_visits = sum(m.visits for m in metrics_list)
        total_orders = sum(m.orders for m in metrics_list)
        total_revenue = sum(m.revenue for m in metrics_list)

        return PerformanceMetrics(
            views=total_views,
            visits=total_visits,
            orders=total_orders,
            revenue=total_revenue,
            conversion_rate=total_orders / total_visits if total_visits > 0 else 0,
            click_through_rate=total_visits / total_views if total_views > 0 else 0
        )

    @staticmethod
    def calculate_growth_rate(current: float, previous: float) -> float:
        """Calculate growth rate between two values"""
        if previous == 0:
            return 1.0 if current > 0 else 0.0
        return (current - previous) / previous

    @staticmethod
    def opportunities_to_dict(opportunities: List[MarketOpportunity]) -> Dict[str, List[Dict]]:
        """Group opportunities by timeline for reporting"""
        grouped = {timeline.value: [] for timeline in OpportunityTimeline}

        for opp in opportunities:
            timeline = opp.time_investment or OpportunityTimeline.WEEKEND_PROJECT.value
            if timeline not in grouped:
                grouped[timeline] = []

            grouped[timeline].append({
                'name': opp.name,
                'category': opp.category,
                'priority_score': opp.priority_score,
                'effort_score': opp.effort_score,
                'impact_score': opp.impact_score,
                'avg_price': opp.avg_price,
                'search_volume': opp.search_volume,
                'competition': opp.competition_level.value
            })

        return grouped

def save_data_model(obj: Any, filepath: str):
    """Save data model to JSON file"""
    def json_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, (set, frozenset)):
            return list(obj)
        elif isinstance(obj, Enum):
            return obj.value
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        return str(obj)

    with open(filepath, 'w') as f:
        json.dump(obj, f, default=json_serializer, indent=2)

def load_data_model(filepath: str, model_class) -> Any:
    """Load data model from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)

    # This would need more sophisticated deserialization logic
    # for complex nested objects and datetime parsing
    return model_class(**data)

if __name__ == "__main__":
    # Example usage and testing
    sample_listing = ListingData(
        listing_id="12345",
        title="Handmade Coffee Mug",
        description="Beautiful ceramic coffee mug",
        price=24.99,
        category="Kitchen & Dining",
        shop_section="Drinkware",
        tags=["coffee", "mug", "ceramic", "handmade"],
        materials=["ceramic", "glaze"],
        photos=["photo1.jpg", "photo2.jpg"],
        created_date=datetime.now(),
        last_updated=datetime.now()
    )

    print("Data models created successfully!")

    # Validate the sample data
    errors = EtsyDataValidator.validate_listing_data(sample_listing)
    if errors:
        print(f"Validation errors: {errors}")
    else:
        print("Sample data is valid!")
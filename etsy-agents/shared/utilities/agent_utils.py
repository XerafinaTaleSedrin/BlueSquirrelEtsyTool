#!/usr/bin/env python3
"""
Shared utilities for Etsy Business Intelligence agents
Common functions, helpers, and integrations used across all agents
"""

import json
import csv
import datetime
import logging
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from dataclasses import asdict
import requests
from urllib.parse import urlencode
import time
import os

class EtsyAPIClient:
    """
    Simplified Etsy API client wrapper
    Note: This would need proper API keys and OAuth implementation
    """

    def __init__(self, api_key: str = None, shop_id: str = None):
        self.api_key = api_key or os.environ.get('ETSY_API_KEY')
        self.shop_id = shop_id or os.environ.get('ETSY_SHOP_ID')
        self.base_url = "https://openapi.etsy.com/v3"
        self.session = requests.Session()

    def get_shop_listings(self, limit: int = 100) -> List[Dict]:
        """Get all listings for a shop"""
        if not self.api_key or not self.shop_id:
            return self._mock_listings_data()

        # Real API call would go here
        # return self._api_request(f"/application/shops/{self.shop_id}/listings/active")
        return self._mock_listings_data()

    def get_shop_stats(self, start_date: str, end_date: str) -> Dict:
        """Get shop statistics for a date range"""
        if not self.api_key or not self.shop_id:
            return self._mock_stats_data()

        # Real API call would go here
        return self._mock_stats_data()

    def _api_request(self, endpoint: str, params: Dict = None) -> Dict:
        """Make authenticated API request"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        url = f"{self.base_url}{endpoint}"
        if params:
            url += f"?{urlencode(params)}"

        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def _mock_listings_data(self) -> List[Dict]:
        """Mock data for testing when API isn't available"""
        return [
            {
                "listing_id": "12345",
                "title": "Handmade Ceramic Coffee Mug - Blue Glaze",
                "price": 24.99,
                "views": 450,
                "num_favorers": 23,
                "tags": ["coffee", "mug", "ceramic", "handmade", "blue"],
                "created_timestamp": int(datetime.datetime.now().timestamp())
            },
            {
                "listing_id": "12346",
                "title": "Custom Wedding Planning Printable Set",
                "price": 15.50,
                "views": 320,
                "num_favorers": 18,
                "tags": ["wedding", "planning", "printable", "digital", "custom"],
                "created_timestamp": int(datetime.datetime.now().timestamp())
            }
        ]

    def _mock_stats_data(self) -> Dict:
        """Mock shop statistics data"""
        return {
            "views": 1250,
            "visits": 340,
            "orders": 15,
            "revenue": 312.50,
            "conversion_rate": 0.044
        }

class DataProcessor:
    """Utility class for processing and analyzing Etsy data"""

    @staticmethod
    def calculate_performance_trends(historical_data: List[Dict]) -> Dict:
        """Calculate performance trends from historical data"""
        if len(historical_data) < 2:
            return {"trend": "insufficient_data"}

        recent = historical_data[-1]
        previous = historical_data[-2]

        trends = {}
        for key in ['views', 'visits', 'orders', 'revenue']:
            if key in recent and key in previous and previous[key] > 0:
                change = (recent[key] - previous[key]) / previous[key]
                trends[f"{key}_trend"] = change

        return trends

    @staticmethod
    def identify_seasonal_patterns(data: List[Dict], date_field: str = 'date') -> Dict:
        """Identify seasonal patterns in data"""
        monthly_data = {}

        for entry in data:
            if date_field in entry:
                try:
                    date_obj = datetime.datetime.fromisoformat(entry[date_field])
                    month = date_obj.month
                    if month not in monthly_data:
                        monthly_data[month] = []
                    monthly_data[month].append(entry)
                except (ValueError, TypeError):
                    continue

        # Calculate average performance by month
        seasonal_averages = {}
        for month, entries in monthly_data.items():
            if entries:
                avg_revenue = sum(e.get('revenue', 0) for e in entries) / len(entries)
                seasonal_averages[month] = avg_revenue

        return seasonal_averages

    @staticmethod
    def extract_keywords_from_title(title: str) -> List[str]:
        """Extract potential keywords from a listing title"""
        # Simple keyword extraction - could be enhanced with NLP
        import re

        # Remove common stop words
        stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'a', 'an'}

        words = re.findall(r'\b[a-zA-Z]{3,}\b', title.lower())
        keywords = [word for word in words if word not in stop_words]

        return keywords[:10]  # Return top 10 potential keywords

class ReportGenerator:
    """Generate various report formats from agent data"""

    @staticmethod
    def generate_csv_report(data: List[Dict], filename: str):
        """Generate CSV report from data"""
        if not data:
            return

        filepath = Path(filename)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def generate_html_dashboard(dashboard_data: Dict, template_path: str = None) -> str:
        """Generate HTML dashboard from data"""
        if template_path and Path(template_path).exists():
            with open(template_path, 'r') as f:
                template = f.read()
                # Simple template substitution - could use proper templating engine
                for key, value in dashboard_data.items():
                    template = template.replace(f"{{{{ {key} }}}}", str(value))
                return template

        # Simple HTML generation
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Etsy Business Intelligence Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .metric {{ display: inline-block; margin: 10px; padding: 15px;
                          border: 1px solid #ddd; border-radius: 5px; }}
                .green {{ background-color: #d4edda; }}
                .yellow {{ background-color: #fff3cd; }}
                .red {{ background-color: #f8d7da; }}
            </style>
        </head>
        <body>
            <h1>Etsy Business Dashboard</h1>
            <div class="metrics">
        """

        for key, value in dashboard_data.items():
            html += f'<div class="metric"><strong>{key}:</strong> {value}</div>'

        html += """
            </div>
        </body>
        </html>
        """

        return html

class CacheManager:
    """Simple caching system for API responses and computed data"""

    def __init__(self, cache_dir: str = "../../logs/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_cache_key(self, *args, **kwargs) -> str:
        """Generate cache key from arguments"""
        key_string = f"{args}{kwargs}"
        return hashlib.md5(key_string.encode()).hexdigest()

    def get(self, key: str, max_age_hours: int = 24) -> Optional[Any]:
        """Get cached data if it exists and is not expired"""
        cache_file = self.cache_dir / f"{key}.json"

        if not cache_file.exists():
            return None

        # Check if cache is expired
        file_age = time.time() - cache_file.stat().st_mtime
        if file_age > (max_age_hours * 3600):
            cache_file.unlink()  # Delete expired cache
            return None

        try:
            with open(cache_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None

    def set(self, key: str, data: Any):
        """Cache data"""
        cache_file = self.cache_dir / f"{key}.json"

        with open(cache_file, 'w') as f:
            json.dump(data, f, default=str, indent=2)

class ConfigManager:
    """Manage configuration across all agents"""

    def __init__(self, config_dir: str = "../../config"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self, config_name: str) -> Dict:
        """Load configuration file"""
        config_file = self.config_dir / f"{config_name}.json"

        if config_file.exists():
            with open(config_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_config(self, config_name: str, config_data: Dict):
        """Save configuration file"""
        config_file = self.config_dir / f"{config_name}.json"

        with open(config_file, 'w') as f:
            json.dump(config_data, f, indent=2)

    def get_user_capabilities(self) -> Dict:
        """Get user capability configuration"""
        return self.load_config("user_capabilities")

    def get_api_credentials(self) -> Dict:
        """Get API credentials (should be encrypted in production)"""
        return self.load_config("api_credentials")

class Logger:
    """Centralized logging for all agents"""

    def __init__(self, agent_name: str, log_dir: str = "../../logs"):
        self.agent_name = agent_name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Set up logging
        log_file = self.log_dir / f"{agent_name}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(agent_name)

    def info(self, message: str, **kwargs):
        """Log info message"""
        self.logger.info(f"{message} {kwargs if kwargs else ''}")

    def warning(self, message: str, **kwargs):
        """Log warning message"""
        self.logger.warning(f"{message} {kwargs if kwargs else ''}")

    def error(self, message: str, **kwargs):
        """Log error message"""
        self.logger.error(f"{message} {kwargs if kwargs else ''}")

    def log_agent_action(self, action: str, data: Dict = None):
        """Log specific agent actions"""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "agent": self.agent_name,
            "action": action,
            "data": data or {}
        }
        self.info(f"Agent Action: {action}", **log_entry)

class PerformanceMonitor:
    """Monitor and track agent performance"""

    def __init__(self):
        self.start_times = {}
        self.performance_log = []

    def start_timer(self, operation_name: str):
        """Start timing an operation"""
        self.start_times[operation_name] = time.time()

    def end_timer(self, operation_name: str) -> float:
        """End timing and return duration"""
        if operation_name in self.start_times:
            duration = time.time() - self.start_times[operation_name]
            del self.start_times[operation_name]

            self.performance_log.append({
                "operation": operation_name,
                "duration": duration,
                "timestamp": datetime.datetime.now().isoformat()
            })

            return duration
        return 0.0

    def get_performance_summary(self) -> Dict:
        """Get performance summary statistics"""
        if not self.performance_log:
            return {}

        operations = {}
        for entry in self.performance_log:
            op = entry["operation"]
            if op not in operations:
                operations[op] = []
            operations[op].append(entry["duration"])

        summary = {}
        for op, durations in operations.items():
            summary[op] = {
                "count": len(durations),
                "avg_duration": sum(durations) / len(durations),
                "min_duration": min(durations),
                "max_duration": max(durations)
            }

        return summary

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format currency amount"""
    return f"${amount:,.2f}"

def format_percentage(value: float, decimal_places: int = 1) -> str:
    """Format percentage"""
    return f"{value * 100:.{decimal_places}f}%"

def format_large_number(number: int) -> str:
    """Format large numbers with appropriate suffixes"""
    if number >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.1f}K"
    else:
        return str(number)

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divide two numbers, returning default if denominator is zero"""
    return numerator / denominator if denominator != 0 else default

def date_range_generator(start_date: datetime.datetime, end_date: datetime.datetime, delta: datetime.timedelta):
    """Generate date range"""
    current = start_date
    while current <= end_date:
        yield current
        current += delta

if __name__ == "__main__":
    # Example usage and testing
    print("Testing utilities...")

    # Test API client
    api_client = EtsyAPIClient()
    listings = api_client.get_shop_listings()
    print(f"Found {len(listings)} mock listings")

    # Test cache manager
    cache = CacheManager()
    cache.set("test_key", {"test": "data"})
    cached_data = cache.get("test_key")
    print(f"Cache test: {cached_data}")

    # Test logger
    logger = Logger("test_agent")
    logger.info("Utilities test completed successfully")

    print("All utilities loaded and tested!")
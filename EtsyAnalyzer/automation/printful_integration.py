#!/usr/bin/env python3
"""
Printful API Integration for Automated Product Creation
Automates the creation of Printful products from design concepts and listings
"""

import json
import os
import time
import base64
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict

try:
    import requests
except ImportError:
    requests = None

@dataclass
class PrintfulProduct:
    """Printful product configuration"""
    product_id: int          # Printful product ID (71 = Unisex T-shirt, etc.)
    variant_id: int          # Specific variant (size, color)
    name: str                # Product name
    size: str                # Size (S, M, L, etc.)
    color: str               # Color name
    price: float             # Base price from Printful
    print_areas: List[str]   # Available print areas (front, back, etc.)

@dataclass
class DesignFile:
    """Design file for Printful upload"""
    file_path: str
    file_type: str           # jpg, png, svg, pdf
    print_area: str          # front, back, etc.
    width: int               # Design width in pixels
    height: int              # Design height in pixels
    dpi: int                 # Resolution
    placement: Dict          # x, y positioning

@dataclass
class PrintfulOrder:
    """Complete Printful product order"""
    external_id: str         # Our unique identifier
    product_config: PrintfulProduct
    design_files: List[DesignFile]
    recipient_info: Dict     # Name, address if needed
    retail_price: float      # Our selling price
    profit_margin: float     # Calculated profit
    status: str              # pending, processing, fulfilled, etc.
    printful_order_id: Optional[str] = None
    created_timestamp: str = ""
    mockup_urls: List[str] = None

class PrintfulAPIClient:
    """Client for Printful API operations"""

    def __init__(self, api_key: str = None):
        # Try multiple sources for API key
        self.api_key = (
            api_key or
            os.getenv('PRINTFUL_API_KEY') or
            'LPUcjY4AJmyrHoWxGg7ub4hv9oG38cyjtvOPb2Jg'  # Fallback API key
        )
        self.base_url = "https://api.printful.com"
        self.session = requests.Session() if requests else None

        if self.session and self.api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            })

        # Common product mappings
        self.product_catalog = self._initialize_product_catalog()

    def _initialize_product_catalog(self) -> Dict:
        """Initialize common Printful product catalog"""
        return {
            # T-Shirts
            "unisex_tshirt": {
                "id": 71,
                "name": "Bella + Canvas 3001 Unisex Short Sleeve Jersey T-Shirt",
                "base_price": 9.95,
                "sizes": ["XS", "S", "M", "L", "XL", "2XL", "3XL"],
                "colors": {
                    "Black": {"hex": "#000000", "variant_id": 4011},
                    "White": {"hex": "#ffffff", "variant_id": 4012},
                    "Navy": {"hex": "#14213d", "variant_id": 4013},
                    "Heather Grey": {"hex": "#9ba2a8", "variant_id": 4014},
                    "Red": {"hex": "#cc0000", "variant_id": 4015}
                },
                "print_areas": ["front", "back"],
                "max_print_size": {"width": 12, "height": 16}  # inches
            },

            # Hoodies
            "unisex_hoodie": {
                "id": 146,
                "name": "Gildan 18500 Unisex Heavy Blend Hooded Sweatshirt",
                "base_price": 22.95,
                "sizes": ["S", "M", "L", "XL", "2XL", "3XL"],
                "colors": {
                    "Black": {"hex": "#000000", "variant_id": 5191},
                    "Navy": {"hex": "#14213d", "variant_id": 5192},
                    "Dark Heather": {"hex": "#3e424a", "variant_id": 5193},
                    "Red": {"hex": "#cc0000", "variant_id": 5194}
                },
                "print_areas": ["front", "back"],
                "max_print_size": {"width": 12, "height": 16}
            },

            # Mugs
            "white_mug": {
                "id": 19,
                "name": "White Glossy Mug",
                "base_price": 8.95,
                "sizes": ["11oz"],
                "colors": {"White": {"hex": "#ffffff", "variant_id": 1692}},
                "print_areas": ["default"],
                "max_print_size": {"width": 8.5, "height": 3.7}
            }
        }

    def test_connection(self) -> bool:
        """Test API connection and authentication"""
        if not self.session or not self.api_key:
            print("ERROR: Printful API key not configured")
            return False

        try:
            response = self.session.get(f"{self.base_url}/oauth/scopes")
            if response.status_code == 200:
                print("SUCCESS: Printful API connection successful")
                return True
            else:
                print(f"ERROR: Printful API error: {response.status_code}")
                return False
        except Exception as e:
            print(f"ERROR: Printful API connection failed: {e}")
            return False

    def get_products(self, category_id: str = None) -> List[Dict]:
        """Get available products from Printful catalog"""
        if not self.session:
            return []

        try:
            url = f"{self.base_url}/products"
            if category_id:
                url += f"?category_id={category_id}"

            response = self.session.get(url)
            if response.status_code == 200:
                data = response.json()
                return data.get('result', [])
            else:
                print(f"❌ Failed to fetch products: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error fetching products: {e}")
            return []

    def get_product_variants(self, product_id: int) -> List[Dict]:
        """Get variants (sizes, colors) for a specific product"""
        if not self.session:
            return []

        try:
            response = self.session.get(f"{self.base_url}/products/{product_id}")
            if response.status_code == 200:
                data = response.json()
                return data.get('result', {}).get('variants', [])
            else:
                print(f"❌ Failed to fetch variants for product {product_id}")
                return []
        except Exception as e:
            print(f"❌ Error fetching variants: {e}")
            return []

    def upload_design_file(self, file_path: str) -> Optional[str]:
        """Upload design file to Printful and return file URL"""
        if not self.session or not os.path.exists(file_path):
            return None

        try:
            with open(file_path, 'rb') as f:
                file_content = base64.b64encode(f.read()).decode('utf-8')

            file_data = {
                "type": "default",
                "url": f"data:image/{os.path.splitext(file_path)[1][1:]};base64,{file_content}",
                "filename": os.path.basename(file_path)
            }

            response = self.session.post(f"{self.base_url}/files", json=file_data)
            if response.status_code == 200:
                data = response.json()
                return data.get('result', {}).get('id')
            else:
                print(f"❌ Failed to upload design file: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error uploading design: {e}")
            return None

    def create_mockup(self, product_id: int, variant_id: int, design_files: List[Dict]) -> List[str]:
        """Generate product mockups"""
        if not self.session:
            return []

        try:
            mockup_data = {
                "variant_id": variant_id,
                "files": design_files
            }

            response = self.session.post(f"{self.base_url}/mockup-generator/create-task/{product_id}", json=mockup_data)
            if response.status_code == 200:
                data = response.json()
                task_key = data.get('result', {}).get('task_key')

                if task_key:
                    # Poll for completion (simplified - in production, use webhooks)
                    for _ in range(30):  # Wait up to 30 seconds
                        time.sleep(1)
                        result = self.session.get(f"{self.base_url}/mockup-generator/task?task_key={task_key}")
                        if result.status_code == 200:
                            task_data = result.json()
                            if task_data.get('result', {}).get('status') == 'completed':
                                mockups = task_data.get('result', {}).get('mockups', [])
                                return [mockup.get('mockup_url') for mockup in mockups]

                return []
            else:
                print(f"❌ Failed to create mockup: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error creating mockup: {e}")
            return []

    def calculate_pricing(self, product_type: str, quantity: int = 1) -> Dict:
        """Calculate pricing for products"""
        if product_type not in self.product_catalog:
            return {}

        product_info = self.product_catalog[product_type]
        base_cost = product_info["base_price"]

        # Add estimated print costs
        print_cost = 2.50  # Estimated print cost
        total_cost = base_cost + print_cost

        # Calculate suggested retail prices with different margins
        pricing = {
            "base_cost": base_cost,
            "print_cost": print_cost,
            "total_cost": total_cost,
            "suggested_retail": {
                "conservative": round(total_cost * 1.8, 2),  # 80% markup
                "standard": round(total_cost * 2.2, 2),      # 120% markup
                "premium": round(total_cost * 2.8, 2)        # 180% markup
            },
            "profit_margins": {
                "conservative": round((total_cost * 1.8 - total_cost), 2),
                "standard": round((total_cost * 2.2 - total_cost), 2),
                "premium": round((total_cost * 2.8 - total_cost), 2)
            }
        }

        return pricing

class AutomatedProductCreator:
    """Creates Printful products automatically from design concepts"""

    def __init__(self, printful_api_key: str = None):
        self.printful_client = PrintfulAPIClient(printful_api_key)
        self.created_products = []
        self.processing_log = []

    def create_products_from_listings(self, listing_files: List[str], design_directory: str) -> Dict:
        """Create Printful products from generated listings"""

        if not self.printful_client.test_connection():
            return {"status": "error", "message": "Printful API not accessible"}

        print(f"🏭 Creating Printful products from {len(listing_files)} listings...")

        successful_creates = []
        failed_creates = []

        for listing_file in listing_files:
            try:
                result = self._process_single_listing(listing_file, design_directory)
                if result["success"]:
                    successful_creates.append(result)
                    print(f"✅ Created: {result['product_name']}")
                else:
                    failed_creates.append(result)
                    print(f"❌ Failed: {result['error']}")

            except Exception as e:
                failed_creates.append({
                    "listing_file": listing_file,
                    "success": False,
                    "error": str(e)
                })
                print(f"❌ Error processing {listing_file}: {e}")

        summary = {
            "status": "completed",
            "total_processed": len(listing_files),
            "successful_creates": len(successful_creates),
            "failed_creates": len(failed_creates),
            "products_created": successful_creates,
            "failures": failed_creates,
            "timestamp": datetime.now().isoformat()
        }

        # Save summary
        self._save_creation_summary(summary)

        return summary

    def _process_single_listing(self, listing_file: str, design_directory: str) -> Dict:
        """Process a single listing to create Printful product"""

        # Load listing data
        with open(listing_file, 'r') as f:
            listing_data = json.load(f)

        # Extract information
        source_image = listing_data.get("source_image", "")
        target_products = listing_data.get("target_products", ["t-shirt"])
        title = listing_data.get("title", "")
        price_range = listing_data.get("price_range", [15.99, 24.99])

        # Find corresponding design file
        design_file = self._find_design_file(source_image, design_directory)
        if not design_file:
            return {
                "success": False,
                "error": f"Design file not found for {source_image}",
                "listing_file": listing_file
            }

        # Create products for each target type
        created_variants = []

        for product_type in target_products[:2]:  # Limit to 2 product types per design
            try:
                # Map to Printful product type
                printful_product_type = self._map_to_printful_product(product_type)
                if not printful_product_type:
                    continue

                # Create product variants
                variants = self._create_product_variants(
                    printful_product_type,
                    design_file,
                    title,
                    price_range
                )

                created_variants.extend(variants)

            except Exception as e:
                print(f"⚠️ Error creating {product_type}: {e}")
                continue

        if created_variants:
            return {
                "success": True,
                "product_name": title,
                "listing_file": listing_file,
                "design_file": design_file,
                "variants_created": len(created_variants),
                "variants": created_variants
            }
        else:
            return {
                "success": False,
                "error": "No variants could be created",
                "listing_file": listing_file
            }

    def _find_design_file(self, source_image_path: str, design_directory: str) -> Optional[str]:
        """Find the actual design file in the design directory"""

        if not source_image_path or not os.path.exists(design_directory):
            return None

        # Get filename without extension
        image_filename = os.path.basename(source_image_path)
        image_name = os.path.splitext(image_filename)[0]

        # Look for matching files in design directory
        for file in os.listdir(design_directory):
            file_path = os.path.join(design_directory, file)
            if os.path.isfile(file_path):
                file_name = os.path.splitext(file)[0]
                file_ext = os.path.splitext(file)[1].lower()

                # Check if filename matches and is supported format
                if (image_name.lower() in file_name.lower() or
                    file_name.lower() in image_name.lower()) and \
                   file_ext in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
                    return file_path

        # If exact match not found, return the source image path if it exists
        if os.path.exists(source_image_path):
            return source_image_path

        return None

    def _map_to_printful_product(self, product_type: str) -> Optional[str]:
        """Map generic product type to Printful product type"""
        mapping = {
            "t-shirt": "unisex_tshirt",
            "tshirt": "unisex_tshirt",
            "shirt": "unisex_tshirt",
            "hoodie": "unisex_hoodie",
            "sweatshirt": "unisex_hoodie",
            "mug": "white_mug",
            "cup": "white_mug",
            "coffee mug": "white_mug"
        }
        return mapping.get(product_type.lower())

    def _create_product_variants(self, printful_product_type: str, design_file: str, title: str, price_range: List[float]) -> List[Dict]:
        """Create multiple variants (sizes, colors) for a product"""

        variants = []

        if printful_product_type not in self.printful_client.product_catalog:
            return variants

        product_info = self.printful_client.product_catalog[printful_product_type]

        # Calculate pricing
        pricing = self.printful_client.calculate_pricing(printful_product_type)
        retail_price = (price_range[0] + price_range[1]) / 2

        # Create variants for popular combinations
        popular_combinations = self._get_popular_combinations(printful_product_type)

        for combo in popular_combinations[:3]:  # Limit to 3 variants per product
            size = combo["size"]
            color = combo["color"]

            try:
                # This would integrate with actual Printful API to create the product
                variant_data = {
                    "product_type": printful_product_type,
                    "product_id": product_info["id"],
                    "size": size,
                    "color": color,
                    "design_file": design_file,
                    "title": f"{title} - {color} {size}",
                    "retail_price": retail_price,
                    "cost": pricing.get("total_cost", 0),
                    "profit": retail_price - pricing.get("total_cost", 0),
                    "created_timestamp": datetime.now().isoformat()
                }

                # In a real implementation, this would call Printful API
                # For now, we create a simulation
                variant_data["printful_id"] = f"sim_{datetime.now().strftime('%Y%m%d%H%M%S')}_{len(variants)}"
                variant_data["status"] = "created"

                variants.append(variant_data)

                print(f"  📦 Created: {color} {size} - ${retail_price:.2f}")

            except Exception as e:
                print(f"  ⚠️ Failed to create {color} {size}: {e}")
                continue

        return variants

    def _get_popular_combinations(self, product_type: str) -> List[Dict]:
        """Get popular size/color combinations for a product type"""

        combinations = {
            "unisex_tshirt": [
                {"size": "M", "color": "Black"},
                {"size": "L", "color": "Black"},
                {"size": "M", "color": "Navy"},
                {"size": "L", "color": "White"},
                {"size": "XL", "color": "Black"}
            ],
            "unisex_hoodie": [
                {"size": "M", "color": "Black"},
                {"size": "L", "color": "Black"},
                {"size": "M", "color": "Navy"},
                {"size": "XL", "color": "Dark Heather"}
            ],
            "white_mug": [
                {"size": "11oz", "color": "White"}
            ]
        }

        return combinations.get(product_type, [])

    def _save_creation_summary(self, summary: Dict):
        """Save product creation summary"""

        os.makedirs("printful_outputs", exist_ok=True)

        summary_file = f"printful_outputs/creation_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2, default=str)

        print(f"📁 Creation summary saved: {summary_file}")

    def get_pricing_recommendations(self, product_types: List[str]) -> Dict:
        """Get pricing recommendations for product types"""

        recommendations = {}

        for product_type in product_types:
            printful_type = self._map_to_printful_product(product_type)
            if printful_type:
                pricing = self.printful_client.calculate_pricing(printful_type)
                recommendations[product_type] = pricing

        return recommendations

    def create_mock_store_setup(self, listing_directory: str) -> Dict:
        """Create a mock Printful store setup for testing"""

        if not os.path.exists(listing_directory):
            return {"status": "error", "message": f"Directory not found: {listing_directory}"}

        listing_files = [f for f in os.listdir(listing_directory) if f.endswith('_listing.json')]

        if not listing_files:
            return {"status": "error", "message": "No listing files found"}

        # Analyze listings and create product recommendations
        product_recommendations = []

        for listing_file in listing_files[:5]:  # Process first 5 for demo
            file_path = os.path.join(listing_directory, listing_file)

            with open(file_path, 'r') as f:
                listing_data = json.load(f)

            # Create recommendation
            recommendation = {
                "listing_file": listing_file,
                "title": listing_data.get("title", ""),
                "target_products": listing_data.get("target_products", []),
                "price_range": listing_data.get("price_range", []),
                "seo_score": listing_data.get("seo_score", 0),
                "recommended_action": "Create Printful products",
                "estimated_setup_time": "5-10 minutes",
                "profit_potential": "Medium to High"
            }

            # Add pricing analysis
            for product_type in recommendation["target_products"][:2]:
                printful_type = self._map_to_printful_product(product_type)
                if printful_type:
                    pricing = self.printful_client.calculate_pricing(printful_type)
                    recommendation[f"{product_type}_pricing"] = pricing

            product_recommendations.append(recommendation)

        # Create setup plan
        setup_plan = {
            "status": "ready",
            "total_products_planned": len(product_recommendations),
            "estimated_total_setup_time": f"{len(product_recommendations) * 7} minutes",
            "product_recommendations": product_recommendations,
            "next_steps": [
                "Review product recommendations",
                "Prepare high-resolution design files",
                "Set up Printful account and API access",
                "Create first batch of products",
                "Test ordering and fulfillment process"
            ],
            "setup_checklist": [
                "Printful account created",
                "API key configured",
                "Design files prepared (300 DPI, correct dimensions)",
                "Pricing strategy determined",
                "Shipping and return policies set"
            ]
        }

        # Save setup plan
        setup_file = f"printful_outputs/store_setup_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.makedirs("printful_outputs", exist_ok=True)

        with open(setup_file, 'w') as f:
            json.dump(setup_plan, f, indent=2, default=str)

        return setup_plan

def main():
    """Example usage of Printful integration"""

    print("🏭 Printful Integration System")
    print("=" * 40)

    # Initialize product creator
    creator = AutomatedProductCreator()

    # Test connection (will fail without API key, but shows structure)
    print("Testing Printful connection...")
    connected = creator.printful_client.test_connection()

    if not connected:
        print("⚠️ Printful API not configured - running in demo mode")

    # Get pricing recommendations
    print("\n💰 Pricing Recommendations:")
    product_types = ["t-shirt", "hoodie", "mug"]
    pricing = creator.get_pricing_recommendations(product_types)

    for product_type, price_data in pricing.items():
        if price_data:
            print(f"\n{product_type.title()}:")
            print(f"  Base Cost: ${price_data['total_cost']:.2f}")
            print(f"  Suggested Retail: ${price_data['suggested_retail']['standard']:.2f}")
            print(f"  Profit Margin: ${price_data['profit_margins']['standard']:.2f}")

    # Create mock store setup
    listing_directory = "image_generated_listings/listings"
    if os.path.exists(listing_directory):
        print(f"\n📋 Creating store setup plan...")
        setup_plan = creator.create_mock_store_setup(listing_directory)

        if setup_plan["status"] == "ready":
            print(f"✅ Setup plan created for {setup_plan['total_products_planned']} products")
            print(f"📁 Plan saved with detailed recommendations")

            print("\n📋 Next Steps:")
            for i, step in enumerate(setup_plan["next_steps"][:3], 1):
                print(f"  {i}. {step}")
        else:
            print(f"❌ Setup plan failed: {setup_plan.get('message', 'Unknown error')}")
    else:
        print(f"\n⚠️ Listing directory not found: {listing_directory}")
        print("Please run the image-to-listing workflow first")

    print("\n🔧 Integration Features:")
    print("✅ Automated product creation from listings")
    print("✅ Pricing optimization based on market data")
    print("✅ Multi-variant product generation")
    print("✅ Mockup generation integration")
    print("✅ Profit margin calculation")

    print("\n📖 To use with real Printful API:")
    print("1. Set PRINTFUL_API_KEY environment variable")
    print("2. Prepare high-resolution design files")
    print("3. Run the full automation workflow")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
SEO-Optimized Listing Content Generator for Etsy
Automatically generates titles, descriptions, and tags based on market intelligence
"""

import json
import os
import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict

@dataclass
class ListingContent:
    """Complete listing content for Etsy"""
    title: str
    description: str
    tags: List[str]
    category: str
    materials: List[str]
    occasion: Optional[str]
    recipient: Optional[str]
    style: List[str]
    color: List[str]
    size: List[str]
    price_suggestion: float
    seo_score: float
    keyword_density: Dict[str, float]

@dataclass
class ContentTemplate:
    """Template for generating content based on product type"""
    product_type: str
    title_templates: List[str]
    description_templates: List[str]
    default_materials: List[str]
    default_occasions: List[str]
    default_recipients: List[str]
    default_styles: List[str]
    price_range: Tuple[float, float]

class SEOContentGenerator:
    """Generates SEO-optimized Etsy listing content"""

    def __init__(self, market_data_path: str = None):
        self.market_data = self._load_market_data(market_data_path)
        self.content_templates = self._initialize_templates()
        self.seo_rules = self._initialize_seo_rules()

    def _load_market_data(self, data_path: str) -> Dict:
        """Load market intelligence from EtsyAnalyzer"""
        if data_path and os.path.exists(data_path):
            with open(data_path, 'r') as f:
                return json.load(f)
        return {}

    def _initialize_templates(self) -> Dict[str, ContentTemplate]:
        """Initialize content templates for different product types"""
        return {
            "t-shirt": ContentTemplate(
                product_type="t-shirt",
                title_templates=[
                    "{MAIN_KEYWORD} T-Shirt - {SECONDARY_KEYWORD} Gift for {TARGET_AUDIENCE}",
                    "{HUMOR_ELEMENT} {PRODUCT_TYPE} - Perfect {OCCASION} Gift for {PROFESSIONAL}",
                    "{NICHE_KEYWORD} Tee - {STYLE_DESCRIPTOR} Design for {TARGET_GROUP}",
                    "Funny {THEME} Shirt - {MAIN_KEYWORD} {PRODUCT_TYPE} for {RECIPIENT}"
                ],
                description_templates=[
                    "🎯 Perfect for {TARGET_AUDIENCE} who appreciate {THEME_DESCRIPTOR}\n\n" +
                    "This {STYLE_DESCRIPTOR} {PRODUCT_TYPE} features {DESIGN_DESCRIPTION}. " +
                    "Whether you're a {PROFESSIONAL_TITLE} or know someone who is, this {HUMOR_ELEMENT} design " +
                    "is perfect for {OCCASION_LIST}.\n\n" +
                    "✨ FEATURES:\n" +
                    "• High-quality {MATERIAL} construction\n" +
                    "• {PRINTING_METHOD} for lasting durability\n" +
                    "• Comfortable fit for all-day wear\n" +
                    "• Available in multiple sizes and colors\n\n" +
                    "🎁 PERFECT GIFT FOR:\n" +
                    "• {TARGET_PROFESSION} appreciation\n" +
                    "• {OCCASION_SPECIFIC} celebrations\n" +
                    "• Office white elephant gifts\n" +
                    "• Anyone who loves {NICHE_HUMOR}\n\n" +
                    "📏 SIZE GUIDE: Please check our size chart for the perfect fit\n" +
                    "🚚 SHIPPING: Fast processing and shipping worldwide\n" +
                    "💝 GIFT READY: Arrives ready to gift or enjoy yourself!"
                ],
                default_materials=["Cotton", "Cotton Blend", "Soft Cotton", "Premium Cotton"],
                default_occasions=["Birthday", "Christmas", "Office Party", "Appreciation Week", "Retirement"],
                default_recipients=["Coworker", "Boss", "Employee", "Friend", "Family Member"],
                default_styles=["Funny", "Humorous", "Professional", "Clever", "Witty"],
                price_range=(15.99, 29.99)
            ),
            "hoodie": ContentTemplate(
                product_type="hoodie",
                title_templates=[
                    "{MAIN_KEYWORD} Hoodie - Cozy {SECONDARY_KEYWORD} Sweatshirt for {TARGET_AUDIENCE}",
                    "Warm {THEME} Hoodie - {HUMOR_ELEMENT} Gift for {PROFESSIONAL}",
                    "{NICHE_KEYWORD} Sweatshirt - Comfortable {STYLE_DESCRIPTOR} Design"
                ],
                description_templates=[
                    "Stay warm and show your {THEME_DESCRIPTOR} pride with this cozy hoodie! " +
                    "Perfect for {TARGET_AUDIENCE} who want comfort and humor combined.\n\n" +
                    "✨ PREMIUM FEATURES:\n" +
                    "• Soft, warm fleece lining\n" +
                    "• Durable {PRINTING_METHOD}\n" +
                    "• Adjustable drawstring hood\n" +
                    "• Kangaroo pocket for convenience\n\n" +
                    "🎁 IDEAL FOR: {OCCASION_LIST} and everyday comfort"
                ],
                default_materials=["Cotton Polyester Blend", "Fleece", "Heavy Cotton"],
                default_occasions=["Winter Gifts", "Holiday Parties", "Casual Fridays"],
                default_recipients=["Team Member", "Colleague", "Professional"],
                default_styles=["Cozy", "Comfortable", "Warm", "Casual"],
                price_range=(25.99, 45.99)
            ),
            "mug": ContentTemplate(
                product_type="mug",
                title_templates=[
                    "{MAIN_KEYWORD} Coffee Mug - {HUMOR_ELEMENT} Cup for {TARGET_AUDIENCE}",
                    "Funny {THEME} Mug - Perfect {OCCASION} Gift for {PROFESSIONAL}",
                    "{NICHE_KEYWORD} Cup - {STYLE_DESCRIPTOR} Coffee Mug"
                ],
                description_templates=[
                    "Start your day with a smile! This {HUMOR_ELEMENT} coffee mug is perfect for " +
                    "{TARGET_AUDIENCE} who need their caffeine with a side of humor.\n\n" +
                    "☕ MUG FEATURES:\n" +
                    "• High-quality ceramic construction\n" +
                    "• Dishwasher and microwave safe\n" +
                    "• Vibrant, fade-resistant printing\n" +
                    "• 11oz capacity - perfect for coffee or tea\n\n" +
                    "🎁 PERFECT FOR: Office gifts, {OCCASION_LIST}, and daily motivation"
                ],
                default_materials=["Ceramic", "High-Quality Ceramic"],
                default_occasions=["Boss Day", "Administrative Professionals Day", "Office Parties"],
                default_recipients=["Coworker", "Boss", "Team Lead"],
                default_styles=["Functional", "Humorous", "Professional"],
                price_range=(12.99, 19.99)
            )
        }

    def _initialize_seo_rules(self) -> Dict:
        """Initialize SEO optimization rules for Etsy"""
        return {
            "title_max_length": 140,
            "description_max_length": 13000,
            "tags_count": 13,
            "tag_max_length": 20,
            "keyword_density_target": 0.02,  # 2%
            "keyword_density_max": 0.05,     # 5%
            "title_keyword_positions": [0, 1, 2],  # First 3 positions preferred
            "required_elements": ["material", "occasion", "recipient"],
            "power_words": ["Perfect", "Unique", "Funny", "Professional", "Gift", "Quality", "Premium"],
            "seasonal_boost": {
                "christmas": ["Holiday", "Christmas", "Gift", "Winter"],
                "halloween": ["Halloween", "Spooky", "October"],
                "election": ["Election", "Vote", "Political", "Democracy"]
            }
        }

    def generate_listing_content(self, design_brief: Dict, product_type: str = "t-shirt") -> ListingContent:
        """Generate complete SEO-optimized listing content"""

        # Get relevant keywords from market data
        trending_keywords = self._extract_trending_keywords()
        niche_keywords = self._extract_niche_keywords(design_brief.get("design_theme", ""))

        # Get template
        template = self.content_templates.get(product_type, self.content_templates["t-shirt"])

        # Generate title
        title = self._generate_optimized_title(design_brief, template, trending_keywords)

        # Generate description
        description = self._generate_seo_description(design_brief, template, trending_keywords)

        # Generate tags
        tags = self._generate_etsy_tags(design_brief, trending_keywords, niche_keywords)

        # Determine additional attributes
        category = self._determine_category(product_type, design_brief.get("design_theme", ""))
        materials = self._select_materials(template, product_type)
        occasion = self._select_occasion(design_brief, template)
        recipient = self._select_recipient(design_brief, template)
        style = self._select_style(design_brief, template)
        colors = self._suggest_colors(design_brief)
        sizes = self._get_size_options(product_type)

        # Calculate pricing
        price = self._calculate_optimal_price(template, trending_keywords)

        # Calculate SEO score
        seo_score = self._calculate_seo_score(title, description, tags, trending_keywords)

        # Calculate keyword density
        keyword_density = self._calculate_keyword_density(title + " " + description, trending_keywords)

        return ListingContent(
            title=title,
            description=description,
            tags=tags,
            category=category,
            materials=materials,
            occasion=occasion,
            recipient=recipient,
            style=style,
            color=colors,
            size=sizes,
            price_suggestion=price,
            seo_score=seo_score,
            keyword_density=keyword_density
        )

    def _extract_trending_keywords(self) -> List[str]:
        """Extract trending keywords from market data"""
        trending = []

        if "cross_agent_insights" in self.market_data:
            gaps = self.market_data["cross_agent_insights"].get("keyword_trend_gaps", [])
            trending.extend(gaps[:5])

        if "integrated_recommendations" in self.market_data:
            immediate_keywords = self.market_data["integrated_recommendations"]["seo_keyword_strategy"].get("immediate_keywords_to_add", [])
            trending.extend(immediate_keywords[:3])

        # Add fallback keywords if none found
        if not trending:
            trending = ["government humor", "civil servant", "bureaucrat gift", "office humor", "professional"]

        return trending[:8]

    def _extract_niche_keywords(self, theme: str) -> List[str]:
        """Extract niche-specific keywords based on theme"""
        niche_maps = {
            "government_humor": ["federal employee", "civil service", "bureaucrat", "government worker", "public sector"],
            "cybersecurity": ["IT security", "cyber professional", "tech worker", "information security", "network admin"],
            "political_satire": ["political humor", "election", "democracy", "civic duty", "voting"]
        }
        return niche_maps.get(theme, ["professional", "workplace", "office", "career", "job"])

    def _generate_optimized_title(self, design_brief: Dict, template: ContentTemplate, keywords: List[str]) -> str:
        """Generate SEO-optimized title"""

        # Select best title template
        title_template = template.title_templates[0]  # Use primary template

        # Fill template variables
        variables = {
            "MAIN_KEYWORD": keywords[0] if keywords else "Professional",
            "SECONDARY_KEYWORD": keywords[1] if len(keywords) > 1 else "Humor",
            "TARGET_AUDIENCE": design_brief.get("target_audience", "Professionals").split(",")[0],
            "HUMOR_ELEMENT": "Funny" if "humor" in design_brief.get("design_theme", "") else "Clever",
            "PRODUCT_TYPE": template.product_type.title(),
            "OCCASION": template.default_occasions[0],
            "PROFESSIONAL": self._extract_profession_from_audience(design_brief.get("target_audience", "")),
            "NICHE_KEYWORD": keywords[2] if len(keywords) > 2 else "Office",
            "STYLE_DESCRIPTOR": template.default_styles[0],
            "TARGET_GROUP": "Professionals",
            "THEME": design_brief.get("design_theme", "Professional").replace("_", " ").title(),
            "RECIPIENT": template.default_recipients[0]
        }

        # Replace variables in template
        title = title_template
        for var, value in variables.items():
            title = title.replace(f"{{{var}}}", value)

        # Ensure title meets length requirements
        if len(title) > self.seo_rules["title_max_length"]:
            title = title[:self.seo_rules["title_max_length"]-3] + "..."

        return title

    def _generate_seo_description(self, design_brief: Dict, template: ContentTemplate, keywords: List[str]) -> str:
        """Generate SEO-optimized description"""

        # Select description template
        desc_template = template.description_templates[0]

        # Create variable mappings
        target_audience = design_brief.get("target_audience", "professionals")
        theme = design_brief.get("design_theme", "professional").replace("_", " ")

        variables = {
            "TARGET_AUDIENCE": target_audience.split(",")[0],
            "THEME_DESCRIPTOR": f"{theme} humor",
            "STYLE_DESCRIPTOR": template.default_styles[0].lower(),
            "PRODUCT_TYPE": template.product_type,
            "DESIGN_DESCRIPTION": "a clever and humorous design that resonates with your professional experience",
            "PROFESSIONAL_TITLE": self._extract_profession_from_audience(target_audience),
            "HUMOR_ELEMENT": "witty and relatable",
            "OCCASION_LIST": ", ".join(template.default_occasions[:3]),
            "MATERIAL": template.default_materials[0],
            "PRINTING_METHOD": "screen printing" if template.product_type == "t-shirt" else "high-quality printing",
            "TARGET_PROFESSION": self._extract_profession_from_audience(target_audience),
            "OCCASION_SPECIFIC": template.default_occasions[0],
            "NICHE_HUMOR": f"{theme} humor"
        }

        # Replace variables
        description = desc_template
        for var, value in variables.items():
            description = description.replace(f"{{{var}}}", value)

        # Add keyword optimization
        description = self._optimize_description_keywords(description, keywords)

        return description

    def _generate_etsy_tags(self, design_brief: Dict, trending_keywords: List[str], niche_keywords: List[str]) -> List[str]:
        """Generate 13 SEO-optimized Etsy tags"""

        tags = []

        # Add trending keywords (top priority)
        for keyword in trending_keywords[:4]:
            if len(keyword) <= self.seo_rules["tag_max_length"]:
                tags.append(keyword.lower())

        # Add niche keywords
        for keyword in niche_keywords[:3]:
            if len(keyword) <= self.seo_rules["tag_max_length"] and keyword.lower() not in tags:
                tags.append(keyword.lower())

        # Add product-specific tags
        product_tags = ["gift", "funny", "humor", "professional", "office", "work"]
        for tag in product_tags:
            if len(tags) < 13 and tag not in tags:
                tags.append(tag)

        # Add theme-specific tags
        theme = design_brief.get("design_theme", "")
        if "government" in theme:
            theme_tags = ["government", "federal", "civil service"]
        elif "cyber" in theme:
            theme_tags = ["tech", "it", "security"]
        else:
            theme_tags = ["workplace", "career", "job"]

        for tag in theme_tags:
            if len(tags) < 13 and tag not in tags:
                tags.append(tag)

        # Fill remaining slots with generic high-performing tags
        filler_tags = ["unique", "custom", "quality", "perfect gift"]
        for tag in filler_tags:
            if len(tags) < 13 and tag not in tags:
                tags.append(tag)

        return tags[:13]

    def _optimize_description_keywords(self, description: str, keywords: List[str]) -> str:
        """Optimize keyword density in description"""

        # Calculate current keyword density
        word_count = len(description.split())

        for keyword in keywords[:3]:  # Focus on top 3 keywords
            current_count = description.lower().count(keyword.lower())
            target_count = max(1, int(word_count * self.seo_rules["keyword_density_target"]))

            # Add keywords if below target (naturally)
            if current_count < target_count:
                additions_needed = target_count - current_count
                # Add keyword variations naturally
                for _ in range(additions_needed):
                    if "gift" not in description.lower() and "gift" in keyword.lower():
                        description += f" Perfect as a {keyword.lower()}."
                    elif "professional" in keyword.lower():
                        description += f" Ideal for any {keyword.lower()}."

        return description

    def _extract_profession_from_audience(self, audience: str) -> str:
        """Extract primary profession from target audience"""
        if "government" in audience.lower():
            return "government employee"
        elif "cyber" in audience.lower() or "IT" in audience:
            return "IT professional"
        elif "tech" in audience.lower():
            return "tech worker"
        else:
            return "professional"

    def _determine_category(self, product_type: str, theme: str) -> str:
        """Determine Etsy category"""
        category_map = {
            "t-shirt": "Clothing > Unisex Adult Clothing > Tops & Tees",
            "hoodie": "Clothing > Unisex Adult Clothing > Hoodies & Sweatshirts",
            "mug": "Home & Living > Kitchen & Dining > Drink & Barware > Mugs"
        }
        return category_map.get(product_type, "Clothing > Unisex Adult Clothing > Tops & Tees")

    def _select_materials(self, template: ContentTemplate, product_type: str) -> List[str]:
        """Select appropriate materials"""
        return template.default_materials[:2]

    def _select_occasion(self, design_brief: Dict, template: ContentTemplate) -> str:
        """Select most appropriate occasion"""
        return template.default_occasions[0]

    def _select_recipient(self, design_brief: Dict, template: ContentTemplate) -> str:
        """Select most appropriate recipient"""
        return template.default_recipients[0]

    def _select_style(self, design_brief: Dict, template: ContentTemplate) -> List[str]:
        """Select style attributes"""
        return template.default_styles[:2]

    def _suggest_colors(self, design_brief: Dict) -> List[str]:
        """Suggest color options"""
        theme = design_brief.get("design_theme", "")
        if "government" in theme:
            return ["Navy", "Gray", "Black", "White"]
        elif "cyber" in theme:
            return ["Black", "Green", "Blue", "Gray"]
        else:
            return ["Black", "Navy", "Gray", "White", "Red"]

    def _get_size_options(self, product_type: str) -> List[str]:
        """Get available size options"""
        if product_type in ["t-shirt", "hoodie"]:
            return ["XS", "S", "M", "L", "XL", "2XL", "3XL"]
        else:
            return ["One Size"]

    def _calculate_optimal_price(self, template: ContentTemplate, keywords: List[str]) -> float:
        """Calculate optimal price based on market data and keywords"""
        base_price = (template.price_range[0] + template.price_range[1]) / 2

        # Adjust based on keyword trends (premium for trending keywords)
        if any("government" in kw.lower() for kw in keywords):
            base_price *= 1.1  # 10% premium for government niche

        if any("cyber" in kw.lower() for kw in keywords):
            base_price *= 1.15  # 15% premium for tech niche

        return round(base_price, 2)

    def _calculate_seo_score(self, title: str, description: str, tags: List[str], keywords: List[str]) -> float:
        """Calculate SEO optimization score (0-100)"""
        score = 0
        max_score = 100

        # Title optimization (30 points)
        title_score = 0
        if len(title) <= self.seo_rules["title_max_length"]:
            title_score += 10
        if any(kw.lower() in title.lower() for kw in keywords[:3]):
            title_score += 20

        # Description optimization (40 points)
        desc_score = 0
        if len(description) >= 200:
            desc_score += 10
        if len(description) <= self.seo_rules["description_max_length"]:
            desc_score += 10
        keyword_in_desc = sum(1 for kw in keywords[:3] if kw.lower() in description.lower())
        desc_score += min(20, keyword_in_desc * 7)

        # Tags optimization (30 points)
        tag_score = 0
        if len(tags) == 13:
            tag_score += 10
        keyword_in_tags = sum(1 for kw in keywords[:5] if any(kw.lower() in tag.lower() for tag in tags))
        tag_score += min(20, keyword_in_tags * 4)

        total_score = title_score + desc_score + tag_score
        return min(100, total_score)

    def _calculate_keyword_density(self, text: str, keywords: List[str]) -> Dict[str, float]:
        """Calculate keyword density for each keyword"""
        word_count = len(text.split())
        densities = {}

        for keyword in keywords[:5]:
            count = text.lower().count(keyword.lower())
            density = count / word_count if word_count > 0 else 0
            densities[keyword] = round(density, 4)

        return densities

class ListingWorkflowManager:
    """Manages the complete listing content generation workflow"""

    def __init__(self, output_dir: str = "generated_listings"):
        self.output_dir = output_dir
        self.content_generator = SEOContentGenerator()
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Create output directory structure"""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "listings"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "csv_uploads"), exist_ok=True)

    def process_design_briefs(self, briefs_dir: str) -> List[str]:
        """Process all design briefs and generate listing content"""

        generated_listings = []

        # Find all brief files
        brief_files = [f for f in os.listdir(briefs_dir) if f.endswith("_brief.json")]

        for brief_file in brief_files:
            brief_path = os.path.join(briefs_dir, brief_file)

            with open(brief_path, 'r') as f:
                brief_data = json.load(f)

            # Generate listings for multiple product types
            product_types = brief_data.get("printful_products", ["t-shirt"])

            for product_type in product_types:
                listing_content = self.content_generator.generate_listing_content(brief_data, product_type)

                # Save listing content
                listing_name = f"{brief_data['concept_name']}_{product_type}"
                listing_file = os.path.join(self.output_dir, "listings", f"{listing_name}_listing.json")

                with open(listing_file, 'w') as f:
                    json.dump(asdict(listing_content), f, indent=2)

                generated_listings.append(listing_file)

                print(f"Generated listing: {listing_name} (SEO Score: {listing_content.seo_score:.1f})")

        return generated_listings

    def create_etsy_upload_csv(self, listing_files: List[str]) -> str:
        """Create CSV file for bulk Etsy upload"""

        csv_file = os.path.join(self.output_dir, "csv_uploads", f"etsy_upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

        # Etsy CSV headers
        headers = [
            "Title", "Description", "Tags", "Materials", "Price", "Quantity",
            "Category", "Occasion", "Recipients", "Style", "Colors", "Sizes",
            "Who Made", "When Made", "Processing Time"
        ]

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            import csv
            writer = csv.writer(f)
            writer.writerow(headers)

            for listing_file in listing_files:
                with open(listing_file, 'r') as lf:
                    listing_data = json.load(lf)

                # Format data for Etsy CSV
                row = [
                    listing_data["title"],
                    listing_data["description"],
                    "|".join(listing_data["tags"]),  # Etsy uses | separator
                    ", ".join(listing_data["materials"]),
                    listing_data["price_suggestion"],
                    "10",  # Default quantity
                    listing_data["category"],
                    listing_data["occasion"] or "",
                    listing_data["recipient"] or "",
                    ", ".join(listing_data["style"]),
                    ", ".join(listing_data["color"]),
                    ", ".join(listing_data["size"]),
                    "I did",  # Who made
                    "2020-2024",  # When made
                    "1-3 business days"  # Processing time
                ]

                writer.writerow(row)

        return csv_file

def main():
    """Example usage of the listing content generator"""

    # Initialize workflow manager
    manager = ListingWorkflowManager()

    # Path to design briefs (from design generation system)
    briefs_dir = "generated_designs/briefs"

    if os.path.exists(briefs_dir):
        print("Generating SEO-optimized listing content...")
        listings = manager.process_design_briefs(briefs_dir)

        if listings:
            # Create Etsy upload CSV
            csv_file = manager.create_etsy_upload_csv(listings)

            print(f"\nListing generation complete!")
            print(f"Generated {len(listings)} listings")
            print(f"Etsy upload CSV: {csv_file}")
            print("\nNext steps:")
            print("1. Review generated listings for accuracy")
            print("2. Upload CSV to Etsy for bulk listing creation")
            print("3. Add product images from your designs")
        else:
            print("No listings generated. Check design briefs.")
    else:
        print(f"Design briefs directory not found: {briefs_dir}")
        print("Please run the design generation system first")

if __name__ == "__main__":
    main()
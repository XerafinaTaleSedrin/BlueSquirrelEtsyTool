#!/usr/bin/env python3
"""
Etsy Listing Generation with SEO Optimization
Generates SEO-optimized Etsy listings from design briefs and market intelligence
"""

import os
# Force UTF-8 encoding for all operations
os.environ['PYTHONIOENCODING'] = 'utf-8'

import json
import re
from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class EtsyListingSpec:
    """Specification for an Etsy listing"""
    title: str
    description: str
    tags: List[str]
    category_id: int
    price: float
    quantity: int
    processing_time: str
    shipping_profile: str
    materials: List[str]
    images: List[str]
    variations: Dict[str, Any]
    seo_score: float
    target_keywords: List[str]

@dataclass
class ListingGenerationResult:
    """Result of listing generation"""
    success: bool
    listing_id: str
    listing_spec: Optional[EtsyListingSpec]
    seo_analysis: Dict[str, Any]
    optimization_suggestions: List[str]
    error_message: Optional[str]
    generated_timestamp: str

class EtsyListingGenerator:
    """Generates SEO-optimized Etsy listings from design briefs"""

    def __init__(self):
        # Etsy category mappings
        self.category_mapping = {
            "government_humor": 150,  # Clothing > T-shirts
            "cybersecurity": 150,     # Clothing > T-shirts
            "political_satire": 150,  # Clothing > T-shirts
            "apparel": 150,           # Clothing > T-shirts
            "accessories": 1050,      # Accessories
            "home_decor": 1003        # Home & Living
        }

        # SEO keyword templates by theme
        self.seo_templates = {
            "government_humor": {
                "primary_keywords": ["government", "funny", "office", "bureaucrat", "federal", "civil servant"],
                "secondary_keywords": ["workplace", "humor", "professional", "admin", "public service"],
                "long_tail": ["funny government shirt", "federal employee gift", "office humor tee"],
                "trending": ["remote work", "public service", "election year", "civic duty"]
            },
            "cybersecurity": {
                "primary_keywords": ["cybersecurity", "IT", "hacker", "tech", "programming", "security"],
                "secondary_keywords": ["network", "data", "cyber", "digital", "information security"],
                "long_tail": ["cybersecurity professional shirt", "IT security gift", "hacker humor tee"],
                "trending": ["data privacy", "cyber awareness", "remote security", "digital protection"]
            },
            "political_satire": {
                "primary_keywords": ["political", "democracy", "voting", "civic", "election", "patriotic"],
                "secondary_keywords": ["government", "politics", "citizen", "freedom", "liberty"],
                "long_tail": ["political humor shirt", "democracy supporter gift", "voting rights tee"],
                "trending": ["civic engagement", "voter registration", "democracy defender", "political awareness"]
            }
        }

        # High-performing title templates
        self.title_templates = {
            "government_humor": [
                "{concept} - Funny Government Employee Shirt | Federal Worker Gift",
                "{concept} - Bureaucrat Humor Tee | Office Professional Apparel",
                "{concept} - Civil Servant Gift | Government Worker T-Shirt",
                "Funny {concept} Shirt | Government Office Humor | Federal Employee Tee"
            ],
            "cybersecurity": [
                "{concept} - Cybersecurity Professional Shirt | IT Security Gift",
                "{concept} - Hacker Humor Tee | Tech Professional Apparel",
                "{concept} - Information Security Shirt | Cyber Expert Gift",
                "Funny {concept} Shirt | Cybersecurity Humor | IT Professional Tee"
            ],
            "political_satire": [
                "{concept} - Political Humor Shirt | Democracy Supporter Gift",
                "{concept} - Voting Rights Tee | Civic Engagement Apparel",
                "{concept} - Political Satire Shirt | Election Humor Gift",
                "Funny {concept} Shirt | Political Awareness | Democracy Tee"
            ]
        }

    def generate_listing_from_brief(self, brief_data: Dict, market_intelligence: Dict = None) -> ListingGenerationResult:
        """Generate a complete Etsy listing from a design brief"""

        try:
            print(f"🏪 Generating Etsy listing for: {brief_data.get('concept_name', 'Unknown')}")

            # Extract brief information
            concept_name = brief_data.get('concept_name', '')
            theme = brief_data.get('design_theme', 'government_humor')
            target_keywords = brief_data.get('target_keywords', [])
            printful_products = brief_data.get('printful_products', ['t-shirt'])

            # Generate SEO-optimized title
            title = self._generate_seo_title(concept_name, theme, target_keywords)

            # Generate comprehensive description
            description = self._generate_listing_description(brief_data, market_intelligence)

            # Generate optimized tags
            tags = self._generate_seo_tags(theme, target_keywords, market_intelligence)

            # Generate pricing strategy
            price = self._calculate_optimal_price(theme, printful_products, market_intelligence)

            # Generate materials list
            materials = self._get_materials_for_products(printful_products)

            # Create listing specification
            listing_spec = EtsyListingSpec(
                title=title,
                description=description,
                tags=tags[:13],  # Etsy allows max 13 tags
                category_id=self.category_mapping.get(theme, 150),
                price=price,
                quantity=100,  # Standard inventory
                processing_time="1-3 business days",
                shipping_profile="standard",
                materials=materials,
                images=[],  # Will be populated with actual design files
                variations=self._generate_product_variations(printful_products),
                seo_score=0.0,  # Will be calculated
                target_keywords=target_keywords
            )

            # Calculate SEO score
            seo_analysis = self._analyze_seo_performance(listing_spec, theme)
            listing_spec.seo_score = seo_analysis['overall_score']

            # Generate optimization suggestions
            optimization_suggestions = self._generate_optimization_suggestions(seo_analysis)

            listing_id = f"listing_{concept_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

            return ListingGenerationResult(
                success=True,
                listing_id=listing_id,
                listing_spec=listing_spec,
                seo_analysis=seo_analysis,
                optimization_suggestions=optimization_suggestions,
                error_message=None,
                generated_timestamp=datetime.now().isoformat()
            )

        except Exception as e:
            print(f"❌ Error generating listing: {e}")
            return ListingGenerationResult(
                success=False,
                listing_id="",
                listing_spec=None,
                seo_analysis={},
                optimization_suggestions=[],
                error_message=str(e),
                generated_timestamp=datetime.now().isoformat()
            )

    def _generate_seo_title(self, concept_name: str, theme: str, target_keywords: List[str]) -> str:
        """Generate SEO-optimized title"""

        # Clean concept name
        clean_concept = concept_name.replace('_', ' ').title()

        # Get theme-specific templates
        templates = self.title_templates.get(theme, self.title_templates["government_humor"])

        # Choose template based on keyword inclusion
        best_template = templates[0]  # Default

        for template in templates:
            # Count how many target keywords would fit in this template
            template_lower = template.lower()
            keyword_matches = sum(1 for kw in target_keywords if kw.lower() in template_lower)
            if keyword_matches > 0:
                best_template = template
                break

        # Format template with concept
        title = best_template.format(concept=clean_concept)

        # Ensure title is within Etsy's 140 character limit
        if len(title) > 140:
            # Truncate and add ellipsis
            title = title[:137] + "..."

        return title

    def _generate_listing_description(self, brief_data: Dict, market_intelligence: Dict = None) -> str:
        """Generate comprehensive listing description with SEO optimization"""

        concept_name = brief_data.get('concept_name', '').replace('_', ' ').title()
        theme = brief_data.get('design_theme', 'government_humor')
        target_audience = brief_data.get('target_audience', 'Professionals')
        target_keywords = brief_data.get('target_keywords', [])
        printful_products = brief_data.get('printful_products', ['t-shirt'])

        # Theme-specific opening hooks
        opening_hooks = {
            "government_humor": "Perfect for government employees, federal workers, and anyone who appreciates the lighter side of public service!",
            "cybersecurity": "Ideal for cybersecurity professionals, IT experts, and anyone passionate about digital security!",
            "political_satire": "Great for civic-minded individuals, political enthusiasts, and democracy supporters!"
        }

        opening = opening_hooks.get(theme, "Perfect for professionals who appreciate quality and humor!")

        description = f"""🎯 {concept_name} - {opening}

📋 WHAT YOU GET:
• High-quality design printed on premium materials
• Perfect fit and comfort for everyday wear
• Professional yet fun design that starts conversations
• Ideal gift for colleagues, friends, and family

👔 PERFECT FOR:
• {target_audience}
• Office environments and casual settings
• Gifts for coworkers and professionals
• Anyone who appreciates clever humor

📏 PRODUCT DETAILS:
"""

        # Add product-specific details
        for product in printful_products[:3]:  # Limit to 3 products
            if 't-shirt' in product.lower() or 'tee' in product.lower():
                description += "• Unisex T-Shirt: 100% cotton, sizes S-3XL available\n"
            elif 'hoodie' in product.lower():
                description += "• Comfortable Hoodie: Cotton blend, sizes S-3XL available\n"
            elif 'mug' in product.lower():
                description += "• 11oz Ceramic Mug: Dishwasher and microwave safe\n"

        description += f"""
🚀 WHY CHOOSE US:
• Fast processing and shipping
• Excellent customer service
• High-quality printing that lasts
• Satisfaction guaranteed

🏷️ KEYWORDS: {', '.join(target_keywords[:8])}

💝 Makes a great gift for birthdays, holidays, promotions, or just because!

📞 Questions? We're here to help! Message us anytime.

#ProfessionalHumor #{theme.replace('_', '').title()} #QualityApparel #UniqueGifts
"""

        return description.strip()

    def _generate_seo_tags(self, theme: str, target_keywords: List[str], market_intelligence: Dict = None) -> List[str]:
        """Generate SEO-optimized tags"""

        tags = []

        # Get theme-specific SEO templates
        seo_template = self.seo_templates.get(theme, self.seo_templates["government_humor"])

        # Add primary keywords (highest priority)
        tags.extend(seo_template["primary_keywords"][:4])

        # Add target keywords from brief
        for keyword in target_keywords[:3]:
            if keyword not in tags and len(keyword) <= 20:  # Etsy tag length limit
                tags.append(keyword)

        # Add secondary keywords
        for keyword in seo_template["secondary_keywords"]:
            if len(tags) < 10 and keyword not in tags:
                tags.append(keyword)

        # Add long-tail keywords (high conversion)
        for keyword in seo_template["long_tail"]:
            if len(tags) < 12 and keyword not in tags and len(keyword) <= 20:
                tags.append(keyword)

        # Add trending keywords if available
        if market_intelligence and "trending_keywords" in market_intelligence:
            trending = market_intelligence["trending_keywords"][:2]
            for keyword in trending:
                if len(tags) < 13 and keyword not in tags and len(keyword) <= 20:
                    tags.append(keyword)

        # Fill remaining slots with theme trending keywords
        for keyword in seo_template["trending"]:
            if len(tags) < 13 and keyword not in tags and len(keyword) <= 20:
                tags.append(keyword)

        return tags[:13]  # Etsy maximum

    def _calculate_optimal_price(self, theme: str, products: List[str], market_intelligence: Dict = None) -> float:
        """Calculate optimal pricing based on market intelligence"""

        # Base pricing by product type
        base_prices = {
            "t-shirt": 19.99,
            "hoodie": 34.99,
            "mug": 16.99,
            "tote-bag": 22.99
        }

        # Get base price for primary product
        primary_product = products[0] if products else "t-shirt"
        base_price = base_prices.get(primary_product.lower(), base_prices["t-shirt"])

        # Theme-specific adjustments
        theme_multipliers = {
            "government_humor": 1.1,     # Slightly premium for niche humor
            "cybersecurity": 1.2,        # Higher value for professional market
            "political_satire": 1.0      # Standard pricing for broader appeal
        }

        multiplier = theme_multipliers.get(theme, 1.0)
        optimized_price = base_price * multiplier

        # Market intelligence adjustments
        if market_intelligence and "price_analysis" in market_intelligence:
            market_avg = market_intelligence["price_analysis"].get("average_price", base_price)
            # Stay competitive but not lowest
            optimized_price = min(optimized_price, market_avg * 1.1)

        return round(optimized_price, 2)

    def _get_materials_for_products(self, products: List[str]) -> List[str]:
        """Get materials list for products"""

        materials = []

        for product in products:
            if 't-shirt' in product.lower() or 'tee' in product.lower():
                materials.extend(["Cotton", "Polyester"])
            elif 'hoodie' in product.lower():
                materials.extend(["Cotton", "Polyester Blend"])
            elif 'mug' in product.lower():
                materials.append("Ceramic")
            elif 'tote' in product.lower():
                materials.append("Canvas")

        # Remove duplicates while preserving order
        return list(dict.fromkeys(materials))

    def _generate_product_variations(self, products: List[str]) -> Dict[str, Any]:
        """Generate product variations for Etsy listing"""

        variations = {}

        # Size variations for apparel
        if any(p in products[0].lower() for p in ['shirt', 'hoodie', 'tee']):
            variations["Size"] = {
                "options": ["S", "M", "L", "XL", "2XL"],
                "prices": {}  # Same price for all sizes
            }

        # Color variations if multiple products
        if len(products) > 1:
            variations["Color"] = {
                "options": ["Black", "Navy", "White", "Heather Grey"],
                "prices": {}
            }

        return variations

    def _analyze_seo_performance(self, listing_spec: EtsyListingSpec, theme: str) -> Dict[str, Any]:
        """Analyze SEO performance of the listing"""

        analysis = {
            "title_score": 0,
            "description_score": 0,
            "tags_score": 0,
            "keyword_density": 0,
            "overall_score": 0,
            "strengths": [],
            "weaknesses": []
        }

        # Analyze title (30% of score)
        title_lower = listing_spec.title.lower()
        title_points = 0

        # Check for target keywords in title
        keyword_in_title = sum(1 for kw in listing_spec.target_keywords if kw.lower() in title_lower)
        title_points += min(keyword_in_title * 20, 60)  # Max 60 points

        # Check title length (optimal 60-80 characters)
        title_len = len(listing_spec.title)
        if 60 <= title_len <= 80:
            title_points += 20
        elif 40 <= title_len < 60 or 80 < title_len <= 100:
            title_points += 10

        # Check for power words
        power_words = ["funny", "perfect", "professional", "quality", "unique", "gift"]
        title_points += min(sum(1 for word in power_words if word in title_lower) * 5, 20)

        analysis["title_score"] = min(title_points, 100)

        # Analyze description (25% of score)
        desc_lower = listing_spec.description.lower()
        desc_points = 0

        # Check description length (optimal 1000-2000 characters)
        desc_len = len(listing_spec.description)
        if 1000 <= desc_len <= 2000:
            desc_points += 30
        elif 500 <= desc_len < 1000:
            desc_points += 20
        elif desc_len >= 2000:
            desc_points += 15

        # Check for keyword usage
        keyword_usage = sum(1 for kw in listing_spec.target_keywords if kw.lower() in desc_lower)
        desc_points += min(keyword_usage * 15, 45)

        # Check for call-to-action
        cta_phrases = ["perfect for", "great gift", "order now", "message us", "questions"]
        if any(phrase in desc_lower for phrase in cta_phrases):
            desc_points += 15

        # Check for structured content
        if "•" in listing_spec.description or "📋" in listing_spec.description:
            desc_points += 10

        analysis["description_score"] = min(desc_points, 100)

        # Analyze tags (25% of score)
        tags_points = 0

        # Tag count (optimal 11-13 tags)
        tag_count = len(listing_spec.tags)
        if tag_count >= 11:
            tags_points += 40
        elif tag_count >= 8:
            tags_points += 30
        elif tag_count >= 5:
            tags_points += 20

        # Long-tail keywords in tags
        long_tail_count = sum(1 for tag in listing_spec.tags if len(tag.split()) > 1)
        tags_points += min(long_tail_count * 10, 30)

        # Theme relevance
        theme_keywords = self.seo_templates.get(theme, {}).get("primary_keywords", [])
        theme_coverage = sum(1 for kw in theme_keywords if any(kw in tag.lower() for tag in listing_spec.tags))
        tags_points += min(theme_coverage * 10, 30)

        analysis["tags_score"] = min(tags_points, 100)

        # Calculate keyword density (20% of score)
        total_text = (listing_spec.title + " " + listing_spec.description + " " + " ".join(listing_spec.tags)).lower()
        total_words = len(total_text.split())
        keyword_mentions = sum(total_text.count(kw.lower()) for kw in listing_spec.target_keywords)

        if total_words > 0:
            density = (keyword_mentions / total_words) * 100
            # Optimal density 2-5%
            if 2 <= density <= 5:
                density_score = 100
            elif 1 <= density < 2 or 5 < density <= 8:
                density_score = 70
            else:
                density_score = 40
        else:
            density_score = 0

        analysis["keyword_density"] = density

        # Calculate overall score
        analysis["overall_score"] = (
            analysis["title_score"] * 0.30 +
            analysis["description_score"] * 0.25 +
            analysis["tags_score"] * 0.25 +
            density_score * 0.20
        )

        # Generate strengths and weaknesses
        if analysis["title_score"] >= 80:
            analysis["strengths"].append("Strong SEO title with good keyword placement")
        elif analysis["title_score"] < 60:
            analysis["weaknesses"].append("Title needs more relevant keywords")

        if analysis["description_score"] >= 80:
            analysis["strengths"].append("Well-structured description with good keyword usage")
        elif analysis["description_score"] < 60:
            analysis["weaknesses"].append("Description could be more detailed and keyword-rich")

        if analysis["tags_score"] >= 80:
            analysis["strengths"].append("Excellent tag optimization")
        elif analysis["tags_score"] < 60:
            analysis["weaknesses"].append("Need more relevant and long-tail tags")

        return analysis

    def _generate_optimization_suggestions(self, seo_analysis: Dict[str, Any]) -> List[str]:
        """Generate specific optimization suggestions"""

        suggestions = []

        if seo_analysis["title_score"] < 70:
            suggestions.append("Add more target keywords to the title while keeping it readable")
            suggestions.append("Consider including power words like 'perfect', 'professional', or 'funny'")

        if seo_analysis["description_score"] < 70:
            suggestions.append("Expand description to 1000-2000 characters for better SEO")
            suggestions.append("Add more structured content with bullet points and emojis")
            suggestions.append("Include more target keywords naturally in the description")

        if seo_analysis["tags_score"] < 70:
            suggestions.append("Use all 13 available tag slots")
            suggestions.append("Add more long-tail keywords as tags")
            suggestions.append("Include trending keywords relevant to your niche")

        if seo_analysis["keyword_density"] < 2:
            suggestions.append("Increase keyword density to 2-5% for better search visibility")
        elif seo_analysis["keyword_density"] > 5:
            suggestions.append("Reduce keyword density to avoid keyword stuffing")

        if seo_analysis["overall_score"] >= 80:
            suggestions.append("Great SEO optimization! Consider A/B testing different titles")

        return suggestions

    def save_listing_to_file(self, result: ListingGenerationResult, output_dir: str = "DESIGNS/etsy_listings") -> str:
        """Save listing to file"""

        os.makedirs(output_dir, exist_ok=True)

        # Create comprehensive listing file
        listing_data = {
            "listing_id": result.listing_id,
            "success": result.success,
            "generated_timestamp": result.generated_timestamp,
            "listing_specification": asdict(result.listing_spec) if result.listing_spec else None,
            "seo_analysis": result.seo_analysis,
            "optimization_suggestions": result.optimization_suggestions,
            "error_message": result.error_message
        }

        filename = f"{output_dir}/{result.listing_id}_etsy_listing.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(listing_data, f, indent=2, ensure_ascii=False)

        print(f"💾 Listing saved to: {filename}")
        return filename

def main():
    """Test the Etsy listing generator"""

    print("🏪 Etsy Listing Generator Test")
    print("=" * 40)

    # Sample brief data
    sample_brief = {
        "concept_name": "government_humor_test_20250930",
        "target_keywords": ["government", "humor", "office", "federal", "bureaucrat"],
        "design_theme": "government_humor",
        "target_audience": "Government employees, federal workers, and civil servants",
        "printful_products": ["t-shirt", "hoodie"],
        "style_preferences": ["professional", "humorous", "vintage"]
    }

    # Sample market intelligence
    sample_market_intel = {
        "trending_keywords": ["remote work", "public service"],
        "price_analysis": {
            "average_price": 22.50
        }
    }

    # Generate listing
    generator = EtsyListingGenerator()
    result = generator.generate_listing_from_brief(sample_brief, sample_market_intel)

    if result.success:
        print(f"✅ Listing generated successfully!")
        print(f"📋 Title: {result.listing_spec.title}")
        print(f"💰 Price: ${result.listing_spec.price}")
        print(f"🏷️ Tags: {', '.join(result.listing_spec.tags)}")
        print(f"📊 SEO Score: {result.seo_analysis['overall_score']:.1f}/100")

        # Save listing
        filename = generator.save_listing_to_file(result)
        print(f"💾 Saved to: {filename}")

        print(f"\n🎯 Optimization Suggestions:")
        for i, suggestion in enumerate(result.optimization_suggestions[:3], 1):
            print(f"  {i}. {suggestion}")

    else:
        print(f"❌ Listing generation failed: {result.error_message}")

if __name__ == "__main__":
    main()
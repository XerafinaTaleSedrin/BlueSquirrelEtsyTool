#!/usr/bin/env python3
"""
Image-to-Listing Workflow using Claude Vision
Automatically generates Etsy listings from design images using AI vision analysis
"""

import json
import os
import base64
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class ImageAnalysis:
    """Results from Claude vision analysis of design image"""
    image_path: str
    image_hash: str
    design_description: str
    text_elements: List[str]
    style_analysis: str
    color_palette: List[str]
    target_audience_suggestion: str
    product_type_suggestions: List[str]
    theme_classification: str
    humor_level: str  # none, mild, moderate, strong
    professionalism_level: str  # casual, business_casual, professional, formal
    suggested_keywords: List[str]
    estimated_appeal: Dict[str, float]  # demographics with appeal scores
    technical_notes: str

@dataclass
class GeneratedListing:
    """Complete listing generated from image analysis"""
    source_image: str
    image_analysis: ImageAnalysis
    title: str
    description: str
    tags: List[str]
    category: str
    price_range: Tuple[float, float]
    target_products: List[str]
    seo_score: float
    generation_timestamp: str
    claude_prompt_used: str
    quality_score: float

class ImageAnalysisEngine:
    """Analyzes design images using Claude vision capabilities"""

    def __init__(self):
        self.analysis_cache = {}
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.webp', '.gif']
        self.prompt_templates = self._initialize_prompts()

    def _initialize_prompts(self) -> Dict[str, str]:
        """Initialize Claude vision prompts for different analysis types"""
        return {
            "comprehensive_analysis": """
Analyze this t-shirt/product design image for Etsy marketplace optimization. Provide detailed analysis in the following areas:

1. DESIGN DESCRIPTION:
   - What is the main visual concept?
   - Describe the layout, typography, and imagery
   - What message or theme does it convey?

2. TEXT ELEMENTS:
   - List all readable text in the design
   - Identify main text, subtitles, and supporting text
   - Assess text readability and hierarchy

3. STYLE ANALYSIS:
   - Design style (minimalist, vintage, modern, illustrated, etc.)
   - Typography style (bold, script, serif, sans-serif)
   - Overall aesthetic approach

4. COLOR PALETTE:
   - Primary colors used
   - Secondary/accent colors
   - Color scheme type (monochromatic, complementary, etc.)

5. TARGET AUDIENCE:
   - Who would this design appeal to?
   - What profession/interest group is targeted?
   - Age range and demographics

6. PRODUCT SUGGESTIONS:
   - What products would this design work best on? (t-shirt, hoodie, mug, etc.)
   - Any size or placement considerations?

7. THEME CLASSIFICATION:
   - What category does this fit? (humor, professional, political, hobby, etc.)
   - Specific niche or subcategory

8. PROFESSIONALISM LEVEL:
   - Is this workplace appropriate?
   - Formality level (casual to professional)

9. HUMOR ASSESSMENT:
   - How funny/humorous is the design? (none/mild/moderate/strong)
   - Type of humor (witty, sarcastic, observational, etc.)

10. KEYWORD SUGGESTIONS:
    - What search terms would customers use to find this?
    - Include both broad and specific keywords

11. MARKET APPEAL:
    - Estimated appeal to different demographics
    - Potential market size

12. TECHNICAL NOTES:
    - Print quality considerations
    - Any design limitations or requirements

Please provide detailed, specific responses for each category to help optimize this design for Etsy sales.
""",

            "quick_analysis": """
Quickly analyze this design image and provide:
1. Main concept (1-2 sentences)
2. Target audience
3. 5-7 relevant keywords for Etsy
4. Suggested product types
5. Professional appropriateness level
6. Estimated market appeal (1-10 scale)
""",

            "seo_focused": """
Analyze this design image specifically for Etsy SEO optimization:

1. PRIMARY KEYWORDS: What are the 3-5 most important search terms?
2. LONG-TAIL KEYWORDS: What specific phrases would customers search?
3. CATEGORY KEYWORDS: What Etsy category keywords apply?
4. DEMOGRAPHIC KEYWORDS: What audience-specific terms are relevant?
5. SEASONAL/OCCASION KEYWORDS: Any time-specific relevance?
6. STYLE KEYWORDS: What style/aesthetic descriptors apply?
7. NICHE KEYWORDS: Any specialized/professional terms?

Focus on actual search terms customers would use to find this product on Etsy.
""",

            "listing_optimization": """
Based on this design image, create optimized Etsy listing content:

1. TITLE: Create an SEO-optimized title (under 140 characters)
2. DESCRIPTION: Write a compelling product description (include benefits, features, target audience)
3. TAGS: Provide 13 Etsy tags for maximum searchability
4. CATEGORY: Suggest appropriate Etsy category
5. PRICE RANGE: Suggest competitive pricing range
6. TARGET PRODUCTS: Which Printful products would work best?

Make the content compelling for both search engines and human buyers.
"""
        }

    def analyze_image(self, image_path: str, analysis_type: str = "comprehensive_analysis") -> Optional[ImageAnalysis]:
        """Analyze design image using Claude vision"""

        if not os.path.exists(image_path):
            print(f"❌ Image not found: {image_path}")
            return None

        # Check if already analyzed (cache)
        image_hash = self._calculate_image_hash(image_path)
        cache_key = f"{image_hash}_{analysis_type}"

        if cache_key in self.analysis_cache:
            print(f"📋 Using cached analysis for {os.path.basename(image_path)}")
            return self.analysis_cache[cache_key]

        # Check file format
        file_ext = os.path.splitext(image_path)[1].lower()
        if file_ext not in self.supported_formats:
            print(f"❌ Unsupported image format: {file_ext}")
            return None

        try:
            print(f"🔍 Analyzing image: {os.path.basename(image_path)}")

            # In a real implementation, this would use Claude's vision API
            # For now, we'll create a structured framework for when that's available
            analysis_result = self._simulate_claude_vision_analysis(image_path, analysis_type)

            if analysis_result:
                # Cache the result
                self.analysis_cache[cache_key] = analysis_result
                return analysis_result

        except Exception as e:
            print(f"❌ Error analyzing image: {e}")
            return None

    def _simulate_claude_vision_analysis(self, image_path: str, analysis_type: str) -> ImageAnalysis:
        """
        Simulates Claude vision analysis - replace with actual Claude API call
        This provides the structure for when Claude vision API is integrated
        """

        # This is a placeholder that shows the expected structure
        # In practice, you would:
        # 1. Encode image to base64
        # 2. Send to Claude vision API with prompt
        # 3. Parse structured response

        filename = os.path.basename(image_path).lower()
        image_hash = self._calculate_image_hash(image_path)

        # Basic analysis based on filename and common patterns
        # This would be replaced by actual Claude vision analysis
        if "government" in filename or "civil" in filename or "federal" in filename:
            theme = "government_humor"
            target_audience = "Government employees, civil servants, federal workers"
            keywords = ["government humor", "civil servant", "federal employee", "bureaucrat", "office humor"]
            humor_level = "moderate"
            professionalism = "business_casual"
        elif "cyber" in filename or "security" in filename or "tech" in filename:
            theme = "cybersecurity"
            target_audience = "IT professionals, cybersecurity experts, tech workers"
            keywords = ["cybersecurity", "IT humor", "tech professional", "security expert", "network admin"]
            humor_level = "mild"
            professionalism = "professional"
        elif "political" in filename or "election" in filename:
            theme = "political_satire"
            target_audience = "Political enthusiasts, civic-minded individuals"
            keywords = ["political humor", "election", "democracy", "voting", "civic duty"]
            humor_level = "moderate"
            professionalism = "casual"
        else:
            theme = "general_humor"
            target_audience = "General audience, professionals"
            keywords = ["funny", "humor", "professional", "gift", "workplace"]
            humor_level = "mild"
            professionalism = "business_casual"

        return ImageAnalysis(
            image_path=image_path,
            image_hash=image_hash,
            design_description=f"Professional {theme.replace('_', ' ')} design with text-based humor",
            text_elements=["Main text element", "Supporting text"],  # Would be extracted by vision
            style_analysis="Clean, professional design with bold typography",
            color_palette=["Black", "White", "Navy"],  # Would be detected by vision
            target_audience_suggestion=target_audience,
            product_type_suggestions=["t-shirt", "hoodie", "mug"],
            theme_classification=theme,
            humor_level=humor_level,
            professionalism_level=professionalism,
            suggested_keywords=keywords,
            estimated_appeal={
                "professionals": 0.8,
                "young_adults": 0.6,
                "middle_aged": 0.7,
                "seniors": 0.4
            },
            technical_notes="High contrast design suitable for various print methods"
        )

    def _calculate_image_hash(self, image_path: str) -> str:
        """Calculate hash of image file for caching"""
        with open(image_path, 'rb') as f:
            content = f.read()
            return hashlib.md5(content).hexdigest()

    def batch_analyze_images(self, image_directory: str, analysis_type: str = "comprehensive_analysis") -> List[ImageAnalysis]:
        """Analyze all images in a directory"""

        if not os.path.exists(image_directory):
            print(f"❌ Directory not found: {image_directory}")
            return []

        image_files = []
        for file in os.listdir(image_directory):
            file_path = os.path.join(image_directory, file)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in self.supported_formats:
                    image_files.append(file_path)

        if not image_files:
            print(f"❌ No supported image files found in {image_directory}")
            return []

        print(f"📊 Analyzing {len(image_files)} images...")

        analyses = []
        for image_path in image_files:
            analysis = self.analyze_image(image_path, analysis_type)
            if analysis:
                analyses.append(analysis)

        print(f"✅ Completed analysis of {len(analyses)} images")
        return analyses

class ImageToListingGenerator:
    """Generates complete Etsy listings from image analysis"""

    def __init__(self, market_data_path: str = None):
        self.image_analyzer = ImageAnalysisEngine()
        self.market_data = self._load_market_data(market_data_path)

    def _load_market_data(self, data_path: str) -> Dict:
        """Load market intelligence for optimization"""
        if data_path and os.path.exists(data_path):
            with open(data_path, 'r') as f:
                return json.load(f)
        return {}

    def generate_listing_from_image(self, image_path: str, product_type: str = "t-shirt") -> Optional[GeneratedListing]:
        """Generate complete Etsy listing from single image"""

        # Analyze image
        analysis = self.image_analyzer.analyze_image(image_path, "comprehensive_analysis")
        if not analysis:
            return None

        # Generate optimized content
        title = self._generate_seo_title(analysis, product_type)
        description = self._generate_description(analysis, product_type)
        tags = self._generate_tags(analysis)
        category = self._determine_category(analysis, product_type)
        price_range = self._calculate_price_range(analysis, product_type)
        target_products = self._suggest_target_products(analysis)

        # Calculate quality scores
        seo_score = self._calculate_seo_score(title, description, tags, analysis.suggested_keywords)
        quality_score = self._assess_listing_quality(analysis, title, description, tags)

        # Create Claude prompt used (for reference)
        claude_prompt = self._create_generation_prompt(analysis, product_type)

        return GeneratedListing(
            source_image=image_path,
            image_analysis=analysis,
            title=title,
            description=description,
            tags=tags,
            category=category,
            price_range=price_range,
            target_products=target_products,
            seo_score=seo_score,
            generation_timestamp=datetime.now().isoformat(),
            claude_prompt_used=claude_prompt,
            quality_score=quality_score
        )

    def _generate_seo_title(self, analysis: ImageAnalysis, product_type: str) -> str:
        """Generate SEO-optimized title"""

        # Get primary keywords
        primary_kw = analysis.suggested_keywords[0] if analysis.suggested_keywords else "Professional"
        secondary_kw = analysis.suggested_keywords[1] if len(analysis.suggested_keywords) > 1 else "Gift"

        # Extract main profession from target audience
        audience_parts = analysis.target_audience_suggestion.split(",")
        target_group = audience_parts[0].strip() if audience_parts else "Professionals"

        # Determine humor element
        humor_element = ""
        if analysis.humor_level in ["moderate", "strong"]:
            humor_element = "Funny "
        elif analysis.humor_level == "mild":
            humor_element = "Clever "

        # Build title
        if product_type == "mug":
            title = f"{humor_element}{primary_kw} Coffee Mug - {secondary_kw} Cup for {target_group}"
        elif product_type == "hoodie":
            title = f"{humor_element}{primary_kw} Hoodie - {secondary_kw} Sweatshirt for {target_group}"
        else:  # t-shirt
            title = f"{humor_element}{primary_kw} T-Shirt - {secondary_kw} Gift for {target_group}"

        # Ensure under 140 characters
        if len(title) > 140:
            title = title[:137] + "..."

        return title

    def _generate_description(self, analysis: ImageAnalysis, product_type: str) -> str:
        """Generate compelling product description"""

        # Extract key elements
        theme = analysis.theme_classification.replace("_", " ").title()
        target_audience = analysis.target_audience_suggestion.split(",")[0].strip()
        professionalism = analysis.professionalism_level.replace("_", " ")

        # Build description sections
        intro = f"Perfect for {target_audience.lower()} who appreciate {theme.lower()}! "
        intro += f"This {analysis.style_analysis.lower()} design features {analysis.design_description.lower()}."

        features = f"""
✨ PREMIUM FEATURES:
• High-quality {self._get_material(product_type)} construction
• Durable, fade-resistant printing
• Comfortable fit for all-day wear
• Available in multiple sizes and colors"""

        if product_type == "mug":
            features = f"""
☕ MUG FEATURES:
• High-quality ceramic construction
• Dishwasher and microwave safe
• Vibrant, fade-resistant printing
• 11oz capacity - perfect for coffee or tea"""

        occasions = """
🎁 PERFECT FOR:
• Professional appreciation gifts
• Office white elephant exchanges
• Birthday and holiday presents
• Anyone who loves workplace humor"""

        practical = f"""
📏 SIZING: Please check our size chart for the perfect fit
🚚 SHIPPING: Fast processing and shipping worldwide
💝 GIFT READY: Arrives ready to gift or enjoy yourself!"""

        if product_type == "mug":
            practical = """
🎁 PERFECT GIFT: Ideal for office gifts, appreciation days, and daily motivation
🚚 SHIPPING: Carefully packaged for safe delivery
💝 GIFT READY: Arrives ready to bring smiles to coffee breaks!"""

        description = f"{intro}\n{features}\n{occasions}\n{practical}"

        # Add keywords naturally
        description = self._optimize_description_keywords(description, analysis.suggested_keywords[:3])

        return description

    def _generate_tags(self, analysis: ImageAnalysis) -> List[str]:
        """Generate 13 optimized Etsy tags"""

        tags = []

        # Add main keywords
        for keyword in analysis.suggested_keywords[:5]:
            if len(keyword) <= 20 and keyword.lower() not in [t.lower() for t in tags]:
                tags.append(keyword.lower())

        # Add theme-specific tags
        theme_tags = {
            "government_humor": ["government", "federal", "civil service", "bureaucrat"],
            "cybersecurity": ["tech", "it security", "cyber", "network"],
            "political_satire": ["political", "election", "democracy", "civic"],
            "general_humor": ["funny", "humor", "workplace", "office"]
        }

        theme = analysis.theme_classification
        if theme in theme_tags:
            for tag in theme_tags[theme]:
                if len(tags) < 13 and tag not in tags:
                    tags.append(tag)

        # Add universal tags
        universal_tags = ["gift", "professional", "unique", "quality"]
        for tag in universal_tags:
            if len(tags) < 13 and tag not in tags:
                tags.append(tag)

        # Fill remaining with color/style tags
        style_tags = ["custom", "personalized", "trendy"]
        for tag in style_tags:
            if len(tags) < 13 and tag not in tags:
                tags.append(tag)

        return tags[:13]

    def _determine_category(self, analysis: ImageAnalysis, product_type: str) -> str:
        """Determine appropriate Etsy category"""
        categories = {
            "t-shirt": "Clothing > Unisex Adult Clothing > Tops & Tees",
            "hoodie": "Clothing > Unisex Adult Clothing > Hoodies & Sweatshirts",
            "mug": "Home & Living > Kitchen & Dining > Drink & Barware > Mugs"
        }
        return categories.get(product_type, categories["t-shirt"])

    def _calculate_price_range(self, analysis: ImageAnalysis, product_type: str) -> Tuple[float, float]:
        """Calculate competitive price range"""

        base_prices = {
            "t-shirt": (15.99, 24.99),
            "hoodie": (25.99, 39.99),
            "mug": (12.99, 18.99)
        }

        base_range = base_prices.get(product_type, base_prices["t-shirt"])

        # Adjust for niche markets
        if analysis.theme_classification in ["government_humor", "cybersecurity"]:
            # Premium pricing for niche markets
            multiplier = 1.15
            return (base_range[0] * multiplier, base_range[1] * multiplier)

        return base_range

    def _suggest_target_products(self, analysis: ImageAnalysis) -> List[str]:
        """Suggest best product types for this design"""
        return analysis.product_type_suggestions[:3]

    def _get_material(self, product_type: str) -> str:
        """Get material description for product type"""
        materials = {
            "t-shirt": "cotton blend",
            "hoodie": "cotton-polyester blend",
            "mug": "ceramic"
        }
        return materials.get(product_type, "premium")

    def _optimize_description_keywords(self, description: str, keywords: List[str]) -> str:
        """Add keywords naturally to description"""
        # Simple implementation - would be more sophisticated in practice
        for keyword in keywords[:2]:
            if keyword.lower() not in description.lower():
                description += f" Great for anyone looking for {keyword.lower()} merchandise."
        return description

    def _calculate_seo_score(self, title: str, description: str, tags: List[str], keywords: List[str]) -> float:
        """Calculate SEO optimization score"""
        score = 0

        # Title optimization (30 points)
        if len(title) <= 140:
            score += 10
        keywords_in_title = sum(1 for kw in keywords[:3] if kw.lower() in title.lower())
        score += min(20, keywords_in_title * 7)

        # Description optimization (40 points)
        if len(description) >= 200:
            score += 10
        if len(description) <= 13000:
            score += 10
        keywords_in_desc = sum(1 for kw in keywords[:3] if kw.lower() in description.lower())
        score += min(20, keywords_in_desc * 7)

        # Tags optimization (30 points)
        if len(tags) == 13:
            score += 10
        keywords_in_tags = sum(1 for kw in keywords[:5] if any(kw.lower() in tag.lower() for tag in tags))
        score += min(20, keywords_in_tags * 4)

        return min(100, score)

    def _assess_listing_quality(self, analysis: ImageAnalysis, title: str, description: str, tags: List[str]) -> float:
        """Assess overall listing quality"""

        quality_score = 0

        # Image analysis quality (40 points)
        if analysis.design_description and len(analysis.design_description) > 20:
            quality_score += 10
        if analysis.suggested_keywords and len(analysis.suggested_keywords) >= 5:
            quality_score += 10
        if analysis.target_audience_suggestion and len(analysis.target_audience_suggestion) > 10:
            quality_score += 10
        if analysis.professionalism_level in ["business_casual", "professional"]:
            quality_score += 10

        # Content quality (60 points)
        if title and len(title) > 30:
            quality_score += 15
        if description and len(description) > 300:
            quality_score += 15
        if tags and len(tags) == 13:
            quality_score += 15
        if any(len(tag) > 3 for tag in tags):
            quality_score += 15

        return min(100, quality_score)

    def _create_generation_prompt(self, analysis: ImageAnalysis, product_type: str) -> str:
        """Create the Claude prompt that would be used for generation"""
        return f"""
Generate Etsy listing content for a {product_type} with this design:

Design Analysis:
- Theme: {analysis.theme_classification}
- Target Audience: {analysis.target_audience_suggestion}
- Style: {analysis.style_analysis}
- Humor Level: {analysis.humor_level}
- Keywords: {', '.join(analysis.suggested_keywords[:5])}

Requirements:
- SEO-optimized title under 140 characters
- Compelling description with benefits and features
- 13 relevant Etsy tags
- Professional tone appropriate for {analysis.professionalism_level}

Focus on converting browsers to buyers while maintaining search visibility.
"""

class ImageWorkflowManager:
    """Manages the complete image-to-listing workflow"""

    def __init__(self, output_dir: str = "image_generated_listings"):
        self.output_dir = output_dir
        self.generator = ImageToListingGenerator()
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Create output directory structure"""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "analyses"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "listings"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "csv_uploads"), exist_ok=True)

    def process_images_to_listings(self, image_directory: str, product_types: List[str] = None) -> Dict:
        """Process all images in directory to complete listings"""

        if product_types is None:
            product_types = ["t-shirt"]

        if not os.path.exists(image_directory):
            return {"status": "error", "message": f"Directory not found: {image_directory}"}

        # Find all images
        image_files = []
        for file in os.listdir(image_directory):
            file_path = os.path.join(image_directory, file)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
                    image_files.append(file_path)

        if not image_files:
            return {"status": "error", "message": "No image files found"}

        print(f"🖼️ Processing {len(image_files)} images for {len(product_types)} product types...")

        generated_listings = []
        failed_images = []

        for image_path in image_files:
            for product_type in product_types:
                try:
                    listing = self.generator.generate_listing_from_image(image_path, product_type)

                    if listing:
                        # Save listing
                        image_name = os.path.splitext(os.path.basename(image_path))[0]
                        listing_file = os.path.join(
                            self.output_dir, "listings",
                            f"{image_name}_{product_type}_listing.json"
                        )

                        with open(listing_file, 'w') as f:
                            json.dump(asdict(listing), f, indent=2, default=str)

                        generated_listings.append(listing_file)

                        print(f"✅ Generated: {image_name} ({product_type}) - SEO: {listing.seo_score:.1f}, Quality: {listing.quality_score:.1f}")
                    else:
                        failed_images.append(f"{image_path} ({product_type})")

                except Exception as e:
                    print(f"❌ Failed to process {image_path} ({product_type}): {e}")
                    failed_images.append(f"{image_path} ({product_type})")

        # Create CSV for bulk upload
        csv_file = None
        if generated_listings:
            csv_file = self._create_bulk_upload_csv(generated_listings)

        # Generate summary
        summary = {
            "status": "completed",
            "total_images_processed": len(image_files),
            "total_listings_generated": len(generated_listings),
            "failed_items": len(failed_images),
            "csv_upload_file": csv_file,
            "listing_files": generated_listings,
            "failed_items_list": failed_images,
            "timestamp": datetime.now().isoformat()
        }

        # Save summary
        summary_file = os.path.join(self.output_dir, f"processing_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2, default=str)

        return summary

    def _create_bulk_upload_csv(self, listing_files: List[str]) -> str:
        """Create CSV file for bulk Etsy upload"""

        csv_file = os.path.join(self.output_dir, "csv_uploads", f"image_listings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

        headers = [
            "Title", "Description", "Tags", "Category", "Price", "Quantity",
            "Materials", "Occasion", "Recipients", "Style", "Colors", "Sizes",
            "Who Made", "When Made", "Processing Time", "Source Image"
        ]

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            import csv
            writer = csv.writer(f)
            writer.writerow(headers)

            for listing_file in listing_files:
                with open(listing_file, 'r') as lf:
                    listing_data = json.load(lf)

                # Extract pricing (use middle of range)
                price_range = listing_data["price_range"]
                price = (price_range[0] + price_range[1]) / 2

                row = [
                    listing_data["title"],
                    listing_data["description"],
                    "|".join(listing_data["tags"]),
                    listing_data["category"],
                    f"{price:.2f}",
                    "10",  # Default quantity
                    "Cotton Blend",  # Default material
                    "Birthday",  # Default occasion
                    "Friend",  # Default recipient
                    "Funny",  # Default style
                    "Multiple",  # Default colors
                    "S,M,L,XL,2XL",  # Default sizes
                    "I did",
                    "2020-2024",
                    "1-3 business days",
                    os.path.basename(listing_data["source_image"])
                ]

                writer.writerow(row)

        return csv_file

def main():
    """Example usage of image-to-listing workflow"""

    print("🖼️ Image-to-Listing Automation Workflow")
    print("=" * 50)

    # Initialize workflow manager
    manager = ImageWorkflowManager()

    # Example usage
    image_directory = "design_images"  # Directory containing your design images
    product_types = ["t-shirt", "hoodie", "mug"]

    if os.path.exists(image_directory):
        print(f"Processing images from: {image_directory}")
        results = manager.process_images_to_listings(image_directory, product_types)

        if results["status"] == "completed":
            print(f"\n✅ Processing completed successfully!")
            print(f"Images processed: {results['total_images_processed']}")
            print(f"Listings generated: {results['total_listings_generated']}")
            print(f"Failed items: {results['failed_items']}")

            if results["csv_upload_file"]:
                print(f"📄 Bulk upload CSV: {results['csv_upload_file']}")

            print("\n📋 Next steps:")
            print("1. Review generated listings for accuracy")
            print("2. Add actual product images to listings")
            print("3. Upload to Etsy using the CSV file")
            print("4. Monitor performance and optimize")

        else:
            print(f"❌ Processing failed: {results['message']}")

    else:
        print(f"❌ Image directory not found: {image_directory}")
        print("Please create the directory and add your design images")
        print("\nSupported formats: .jpg, .jpeg, .png, .webp, .gif")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
EcureuilBleu Data Collection Template
Step-by-step guide for manual data entry
"""

# Import the analyzer
from ecureuil_bleu_analysis_framework import EtsyAnalyzer

def create_data_template():
    """Template for manual data entry"""

    # STEP 1: Get these numbers from your Etsy Stats dashboard
    shop_overview = {
        "total_listings": 0,     # From Shop Manager → Listings
        "total_sales": 0,        # From Stats → Overview (all time)
        "avg_rating": 0.0,       # From your shop's main page
    }

    # STEP 2: For each listing, collect this data manually
    # You can start with just your top 5-10 performing listings
    listing_template = {
        "title": "Copy exact title from listing",
        "price": 0.00,          # Current listing price
        "views": 0,             # From Stats → Listings (past 30 days)
        "favorites": 0,         # From listing page or stats
        "sales": 0,             # From Stats → Listings (all time)
        "tags": [],             # Copy all 13 tags from listing
        "category": "",         # Main category from listing
        "photos_count": 0,      # Count photos in listing
        "description_length": 0  # Approximate character count
    }

    return {
        **shop_overview,
        "listings": [
            # Add your actual listings here using the template above
            # Example:
            # {
            #     "title": "Handmade Ceramic Mug with Blue Glaze",
            #     "price": 28.50,
            #     "views": 150,
            #     "favorites": 12,
            #     "sales": 8,
            #     "tags": ["ceramic mug", "handmade pottery", "blue glaze", "coffee cup"],
            #     "category": "Home & Living",
            #     "photos_count": 6,
            #     "description_length": 250
            # }
        ]
    }

def quick_start_analysis():
    """Run analysis with minimal data to test the system"""

    # Simple test data - replace with your actual data
    test_data = {
        "total_listings": 25,
        "total_sales": 150,
        "avg_rating": 4.8,
        "listings": [
            {
                "title": "Beautiful Handmade Ceramic Mug Perfect Gift",  # Poor SEO example
                "price": 25.00,
                "views": 200,
                "favorites": 15,
                "sales": 8,
                "tags": ["mug", "ceramic", "handmade"],  # Only 3 tags - should be 13
                "category": "Home & Living",
                "photos_count": 3,  # Could be more
                "description_length": 80   # Too short
            }
        ]
    }

    analyzer = EtsyAnalyzer()
    analysis = analyzer.generate_comprehensive_analysis(test_data)

    # Print results
    print("=== SHOP ANALYSIS RESULTS ===")
    print(f"Shop: {analysis.shop_name}")
    print(f"Analysis Date: {analysis.analysis_date}")
    print(f"Total Listings: {analysis.total_listings}")

    print("\n=== LISTING ANALYSIS ===")
    for i, listing in enumerate(analysis.listings):
        print(f"Listing {i+1}: {listing.title}")
        print(f"  SEO Score: {listing.seo_score:.1f}/100")
        print(f"  Conversion Rate: {listing.conversion_rate:.2f}%")

    print("\n=== SEO RECOMMENDATIONS ===")
    for i, seo in enumerate(analysis.seo_optimizations):
        print(f"Listing {i+1} - Priority: {seo.priority.value}")
        print(f"  Current Title: {seo.current_title}")
        print(f"  Suggested Title: {seo.optimized_title}")
        print(f"  Impact: {seo.estimated_impact}")
        print()

    print("=== MARKET OPPORTUNITIES ===")
    for opp in analysis.market_opportunities:
        print(f"• {opp.product_idea}")
        print(f"  Category: {opp.category}")
        print(f"  Priority: {opp.priority.value}")
        print(f"  Opportunity Score: {opp.calculate_opportunity_score():.1f}/10")
        print(f"  Estimated Revenue: {opp.estimated_revenue}")
        print()

    return analysis

if __name__ == "__main__":
    print("EcureuilBleu Data Collection Guide")
    print("=" * 50)
    print("\nTo use this analysis tool:")
    print("1. Collect your shop data using the template above")
    print("2. Replace the test_data with your actual shop data")
    print("3. Run: python data_collection_template.py")
    print("\nFor now, let's run a demo with sample data:\n")

    # Run demo analysis
    analysis = quick_start_analysis()

    print("\n" + "="*50)
    print("Next steps:")
    print("1. Replace test_data with your actual Etsy shop data")
    print("2. Focus on your top 5-10 listings first")
    print("3. Export results: analyzer.export_to_json(analysis, 'my_shop_analysis.json')")
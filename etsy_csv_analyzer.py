#!/usr/bin/env python3
"""
EcureuilBleu Etsy CSV Analyzer
Reads directly from Etsy CSV export and performs comprehensive analysis
"""

import csv
import os
from ecureuil_bleu_analysis_framework import EtsyAnalyzer, Listing

class EtsyCSVParser:
    def __init__(self, csv_path="etsy-agents/EtsyListingsDownload.csv"):
        self.csv_path = csv_path
        self.analyzer = EtsyAnalyzer()

    def parse_etsy_csv(self):
        """Parse Etsy CSV export into our analysis format"""
        if not os.path.exists(self.csv_path):
            print(f"Error: CSV file not found at {self.csv_path}")
            return None

        listings = []

        try:
            with open(self.csv_path, 'r', encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    # Skip empty rows
                    if not row.get('TITLE'):
                        continue

                    # Count images
                    photo_count = 0
                    for i in range(1, 11):  # IMAGE1 through IMAGE10
                        if row.get(f'IMAGE{i}'):
                            photo_count += 1

                    # Parse tags (usually comma or pipe separated)
                    tags = []
                    if row.get('TAGS'):
                        # Handle different tag formats
                        tag_string = row['TAGS']
                        if ',' in tag_string:
                            tags = [tag.strip() for tag in tag_string.split(',')]
                        elif '|' in tag_string:
                            tags = [tag.strip() for tag in tag_string.split('|')]
                        else:
                            tags = [tag_string.strip()]

                    # Create listing object
                    listing = Listing(
                        title=row.get('TITLE', ''),
                        price=float(row.get('PRICE', 0) or 0),
                        views=0,  # Not in CSV - needs manual addition
                        favorites=0,  # Not in CSV - needs manual addition
                        sales=0,  # Not in CSV - needs manual addition
                        tags=tags,
                        category="General",  # Not in CSV - could be inferred
                        photos_count=photo_count,
                        description_length=len(row.get('DESCRIPTION', ''))
                    )

                    listings.append(listing)

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return None

        print(f"Successfully parsed {len(listings)} listings from CSV")
        return listings

    def analyze_from_csv(self):
        """Run complete analysis using CSV data"""
        listings = self.parse_etsy_csv()

        if not listings:
            print("No listings found in CSV. Make sure your CSV has data rows.")
            return None

        # Create shop data structure
        shop_data = {
            "total_listings": len(listings),
            "total_sales": 0,  # Will need manual update
            "avg_rating": 0.0,  # Will need manual update
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

        # Run analysis
        analysis = self.analyzer.generate_comprehensive_analysis(shop_data)

        return analysis

    def display_results(self, analysis):
        """Display analysis results in readable format"""
        if not analysis:
            return

        print("\n" + "="*60)
        print(f"ECUREUILBLEU ETSY SHOP ANALYSIS - {analysis.analysis_date}")
        print("="*60)

        print(f"\nSHOP OVERVIEW:")
        print(f"  Total Listings: {analysis.total_listings}")
        print(f"  Total Sales: {analysis.total_sales} (update manually)")
        print(f"  Average Rating: {analysis.avg_rating} (update manually)")

        print(f"\nLISTING PERFORMANCE:")
        for i, listing in enumerate(analysis.listings[:5]):  # Show top 5
            print(f"  {i+1}. {listing.title[:50]}...")
            print(f"     SEO Score: {listing.seo_score:.1f}/100")
            print(f"     Photos: {listing.photos_count}")
            print(f"     Tags: {len(listing.tags)}/13")

        if len(analysis.listings) > 5:
            print(f"  ... and {len(analysis.listings) - 5} more listings")

        print(f"\nTOP SEO RECOMMENDATIONS:")
        high_priority_seo = [seo for seo in analysis.seo_optimizations if seo.priority.value == "High"]
        for i, seo in enumerate(high_priority_seo[:3]):  # Top 3 priorities
            print(f"  {i+1}. {seo.current_title[:40]}...")
            print(f"     Priority: {seo.priority.value}")
            print(f"     Expected Impact: {seo.estimated_impact}")
            print(f"     Effort: {seo.implementation_effort}")
            print()

        print(f"MARKET OPPORTUNITIES:")
        for i, opp in enumerate(analysis.market_opportunities):
            print(f"  {i+1}. {opp.product_idea}")
            print(f"     Category: {opp.category}")
            print(f"     Priority: {opp.priority.value}")
            print(f"     Score: {opp.calculate_opportunity_score():.1f}/10")
            print(f"     Revenue Potential: {opp.estimated_revenue}")
            print()

    def export_enhanced_csv(self, analysis, filename="enhanced_listings_analysis.csv"):
        """Export analysis results to enhanced CSV"""
        if not analysis:
            return

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'title', 'price', 'seo_score', 'photos_count', 'tags_count',
                'description_length', 'priority', 'estimated_impact',
                'keyword_opportunities'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i, listing in enumerate(analysis.listings):
                seo = analysis.seo_optimizations[i] if i < len(analysis.seo_optimizations) else None

                writer.writerow({
                    'title': listing.title,
                    'price': listing.price,
                    'seo_score': f"{listing.seo_score:.1f}",
                    'photos_count': listing.photos_count,
                    'tags_count': len(listing.tags),
                    'description_length': listing.description_length,
                    'priority': seo.priority.value if seo else 'N/A',
                    'estimated_impact': seo.estimated_impact if seo else 'N/A',
                    'keyword_opportunities': '; '.join(seo.keyword_opportunities) if seo else 'N/A'
                })

        print(f"\nEnhanced analysis exported to: {filename}")

def main():
    """Main function to run the analysis"""
    print("EcureuilBleu Etsy CSV Analyzer")
    print("="*40)

    parser = EtsyCSVParser()

    # Check if CSV exists
    if not os.path.exists(parser.csv_path):
        print(f"CSV file not found at: {parser.csv_path}")
        print("Please ensure your Etsy CSV export is in the etsy-agents folder")
        return

    # Run analysis
    print(f"Reading CSV from: {parser.csv_path}")
    analysis = parser.analyze_from_csv()

    if analysis:
        # Display results
        parser.display_results(analysis)

        # Export enhanced CSV
        parser.export_enhanced_csv(analysis)

        # Export JSON for further processing
        parser.analyzer.export_to_json(analysis, "ecureuil_bleu_full_analysis.json")
        print("Full analysis exported to: ecureuil_bleu_full_analysis.json")

        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("1. Add performance data (views, favorites, sales) to your listings")
        print("2. Implement high-priority SEO recommendations")
        print("3. Explore market opportunities for expansion")
        print("4. Re-run analysis monthly to track improvements")

    else:
        print("Analysis failed. Please check your CSV file format.")

if __name__ == "__main__":
    main()
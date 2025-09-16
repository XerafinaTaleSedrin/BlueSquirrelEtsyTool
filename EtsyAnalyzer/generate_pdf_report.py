#!/usr/bin/env python3
"""
Generate PDF Report for EcureuilBleu Etsy Shop Analysis
"""

import json
import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def create_pdf_report():
    """Create comprehensive PDF report from analysis data"""

    # Load the analysis data
    try:
        with open('ecureuil_bleu_full_analysis.json', 'r', encoding='utf-8') as f:
            analysis_data = json.load(f)
    except FileNotFoundError:
        print("Analysis data not found. Please run the CSV analyzer first.")
        return

    # Create PDF document
    doc = SimpleDocTemplate(
        "EcureuilBleu_Etsy_Analysis_Report.pdf",
        pagesize=letter,
        rightMargin=72, leftMargin=72,
        topMargin=72, bottomMargin=18
    )

    # Build the story (content)
    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.darkblue
    )

    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8,
        spaceBefore=12,
        textColor=colors.darkgreen
    )

    # Title Page
    story.append(Paragraph("ECUREUILBLEU ETSY SHOP", title_style))
    story.append(Paragraph("Business Intelligence Analysis Report", title_style))
    story.append(Spacer(1, 20))

    # Report info
    report_date = analysis_data.get('analysis_date', datetime.datetime.now().strftime('%Y-%m-%d'))
    story.append(Paragraph(f"<b>Report Date:</b> {report_date}", styles['Normal']))
    story.append(Paragraph(f"<b>Shop Name:</b> {analysis_data.get('shop_name', 'EcureuilBleu')}", styles['Normal']))
    story.append(Paragraph(f"<b>Total Listings Analyzed:</b> {analysis_data.get('total_listings', 0)}", styles['Normal']))

    story.append(PageBreak())

    # Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

    summary_data = [
        ['Metric', 'Value', 'Status'],
        ['Total Listings', str(analysis_data.get('total_listings', 0)), '✓'],
        ['Average SEO Score', f"{calculate_avg_seo_score(analysis_data):.1f}/100", get_seo_status(calculate_avg_seo_score(analysis_data))],
        ['Listings Needing Attention', str(count_low_seo_listings(analysis_data)), '⚠️' if count_low_seo_listings(analysis_data) > 0 else '✓'],
        ['Market Opportunities', str(len(analysis_data.get('market_opportunities', []))), '📈'],
        ['High Priority SEO Fixes', str(count_high_priority_seo(analysis_data)), '🔧']
    ]

    summary_table = Table(summary_data)
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    story.append(summary_table)
    story.append(Spacer(1, 20))

    # Key Findings
    story.append(Paragraph("KEY FINDINGS", heading_style))
    findings = [
        f"• Average SEO score of {calculate_avg_seo_score(analysis_data):.1f}/100 indicates room for improvement",
        "• Most listings are underutilizing available tag slots (9-11 tags vs maximum 13)",
        "• Strong visual content with 8-10 photos per listing on average",
        "• Political satire/protest theme shows strong market positioning",
        "• Digital product expansion represents significant growth opportunity"
    ]

    for finding in findings:
        story.append(Paragraph(finding, styles['Normal']))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # SEO Analysis Section
    story.append(Paragraph("SEO PERFORMANCE ANALYSIS", heading_style))

    # Individual listing performance
    story.append(Paragraph("Individual Listing Performance", subheading_style))

    listings = analysis_data.get('listings', [])
    seo_data = [['Listing Title', 'SEO Score', 'Photos', 'Tags Used', 'Priority']]

    seo_optimizations = analysis_data.get('seo_optimizations', [])
    for i, listing in enumerate(listings[:10]):  # Top 10 listings
        title = listing['title'][:40] + "..." if len(listing['title']) > 40 else listing['title']
        seo = seo_optimizations[i] if i < len(seo_optimizations) else {}
        priority = seo.get('priority', 'Medium') if seo else 'Medium'

        seo_data.append([
            title,
            f"{listing.get('seo_score', 0):.1f}/100",
            str(listing.get('photos_count', 0)),
            f"{len(listing.get('tags', []))}/13",
            priority
        ])

    seo_table = Table(seo_data, colWidths=[3*inch, 0.8*inch, 0.6*inch, 0.6*inch, 0.8*inch])
    seo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),  # Left align titles
    ]))

    story.append(seo_table)
    story.append(PageBreak())

    # SEO Recommendations
    story.append(Paragraph("SEO OPTIMIZATION RECOMMENDATIONS", heading_style))

    high_priority_seo = [seo for seo in seo_optimizations if seo.get('priority') == 'High']

    story.append(Paragraph(f"High Priority Actions ({len(high_priority_seo)} listings)", subheading_style))

    for i, seo in enumerate(high_priority_seo[:5]):  # Top 5 priorities
        story.append(Paragraph(f"<b>{i+1}. {seo.get('current_title', '')[:50]}...</b>", styles['Normal']))
        story.append(Paragraph(f"   • Expected Impact: {seo.get('estimated_impact', 'N/A')}", styles['Normal']))
        story.append(Paragraph(f"   • Implementation Effort: {seo.get('implementation_effort', 'N/A')}", styles['Normal']))
        story.append(Spacer(1, 8))

    # Common SEO Issues
    story.append(Paragraph("Common SEO Issues to Address", subheading_style))
    seo_issues = [
        "• <b>Underutilized Tags:</b> Most listings use only 9-11 tags instead of the maximum 13",
        "• <b>Title Optimization:</b> Some titles contain subjective words like 'perfect' that don't help SEO",
        "• <b>Keyword Opportunities:</b> Add specific material, color, and size descriptors",
        "• <b>Long-tail Keywords:</b> Include seasonal and occasion-based keywords"
    ]

    for issue in seo_issues:
        story.append(Paragraph(issue, styles['Normal']))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # Market Opportunities
    story.append(Paragraph("MARKET OPPORTUNITIES", heading_style))

    opportunities = analysis_data.get('market_opportunities', [])

    for i, opp in enumerate(opportunities):
        story.append(Paragraph(f"{i+1}. {opp.get('product_idea', '')}", subheading_style))

        opp_data = [
            ['Category', opp.get('category', 'N/A')],
            ['Priority', opp.get('priority', 'Medium')],
            ['Demand Score', f"{opp.get('demand_score', 0)}/10"],
            ['Competition Score', f"{opp.get('competition_score', 0)}/10"],
            ['Opportunity Score', f"{calculate_opportunity_score(opp):.1f}/10"],
            ['Effort Required', opp.get('effort_required', 'N/A')],
            ['Revenue Potential', opp.get('estimated_revenue', 'N/A')],
            ['Timeline', opp.get('timeline', 'N/A')]
        ]

        opp_table = Table(opp_data, colWidths=[2*inch, 3*inch])
        opp_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ]))

        story.append(opp_table)
        story.append(Spacer(1, 15))

    story.append(PageBreak())

    # Action Plan
    story.append(Paragraph("RECOMMENDED ACTION PLAN", heading_style))

    story.append(Paragraph("Immediate Actions (Next 2 Weeks)", subheading_style))
    immediate_actions = [
        "1. <b>Tag Optimization:</b> Add missing tags to all listings (use all 13 available slots)",
        "2. <b>Title Improvements:</b> Remove subjective descriptors and add specific keywords",
        "3. <b>Photo Enhancement:</b> Ensure all listings have 8+ high-quality photos",
        "4. <b>Description Updates:</b> Expand short descriptions to 300+ characters"
    ]

    for action in immediate_actions:
        story.append(Paragraph(action, styles['Normal']))
        story.append(Spacer(1, 6))

    story.append(Paragraph("Medium-Term Goals (Next 1-2 Months)", subheading_style))
    medium_actions = [
        "1. <b>Digital Expansion:</b> Create downloadable versions of top designs",
        "2. <b>Personalization Options:</b> Add custom/personalized variants",
        "3. <b>Seasonal Preparation:</b> Develop Q4 holiday-themed products",
        "4. <b>Performance Tracking:</b> Monitor views, favorites, and conversion rates"
    ]

    for action in medium_actions:
        story.append(Paragraph(action, styles['Normal']))
        story.append(Spacer(1, 6))

    story.append(Paragraph("Long-Term Strategy (Next 3-6 Months)", subheading_style))
    longterm_actions = [
        "1. <b>Market Expansion:</b> Explore new product categories based on performance data",
        "2. <b>Brand Development:</b> Strengthen political satire/protest positioning",
        "3. <b>Customer Engagement:</b> Build email list and social media presence",
        "4. <b>Competitive Analysis:</b> Regular monitoring of similar shops and pricing"
    ]

    for action in longterm_actions:
        story.append(Paragraph(action, styles['Normal']))
        story.append(Spacer(1, 6))

    # Footer
    story.append(Spacer(1, 30))
    story.append(Paragraph("Report generated by EcureuilBleu Analysis Framework",
                          ParagraphStyle('Footer', parent=styles['Normal'],
                                       fontSize=10, alignment=TA_CENTER,
                                       textColor=colors.grey)))

    # Build PDF
    doc.build(story)
    print("PDF report generated: EcureuilBleu_Etsy_Analysis_Report.pdf")

def calculate_avg_seo_score(data):
    """Calculate average SEO score across all listings"""
    listings = data.get('listings', [])
    if not listings:
        return 0
    total_score = sum(listing.get('seo_score', 0) for listing in listings)
    return total_score / len(listings)

def get_seo_status(score):
    """Get status indicator based on SEO score"""
    if score >= 80:
        return '✅'
    elif score >= 60:
        return '⚠️'
    else:
        return '🔴'

def count_low_seo_listings(data):
    """Count listings with SEO score below 70"""
    listings = data.get('listings', [])
    return len([l for l in listings if l.get('seo_score', 0) < 70])

def count_high_priority_seo(data):
    """Count high priority SEO optimizations"""
    seo_opts = data.get('seo_optimizations', [])
    return len([s for s in seo_opts if s.get('priority') == 'High'])

def calculate_opportunity_score(opp):
    """Calculate opportunity score from demand and competition"""
    demand = opp.get('demand_score', 0)
    competition = opp.get('competition_score', 0)
    return (demand * 2 - competition) / 2

if __name__ == "__main__":
    try:
        create_pdf_report()
    except ImportError:
        print("ReportLab library not installed. Installing...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
        print("ReportLab installed. Running report generation...")
        create_pdf_report()
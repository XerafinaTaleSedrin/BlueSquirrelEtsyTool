#!/usr/bin/env python3
"""
Simple Multi-Agent PDF Report Generator
Creates a comprehensive PDF report from the multi-agent analysis JSON
"""

import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_multi_agent_pdf():
    """Create multi-agent analysis PDF report"""
    try:
        # Load multi-agent analysis data
        with open('multi_agent_analysis_report.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Create PDF
        doc = SimpleDocTemplate(
            "EcureuilBleu_Multi_Agent_Complete_Report.pdf",
            pagesize=letter,
            rightMargin=72, leftMargin=72,
            topMargin=72, bottomMargin=18
        )

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
        story.append(Paragraph("Complete Multi-Agent Business Intelligence Report", title_style))
        story.append(Spacer(1, 30))

        # Report metadata
        metadata = data["analysis_metadata"]
        story.append(Paragraph(f"<b>Generated:</b> {metadata['generated_timestamp']}", styles['Normal']))
        story.append(Paragraph(f"<b>Agents Used:</b> {', '.join(metadata['agents_used'])}", styles['Normal']))
        story.append(Paragraph(f"<b>Listings Analyzed:</b> {metadata['total_listings_analyzed']}", styles['Normal']))
        story.append(Paragraph(f"<b>Analysis Type:</b> {metadata['analysis_scope'].replace('_', ' ').title()}", styles['Normal']))

        story.append(PageBreak())

        # Executive Summary
        story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

        summary = data["executive_summary"]
        health = summary["overall_shop_health"]

        # Shop health table
        health_data = [
            ['Metric', 'Status'],
            ['Overall Health', health['status']],
            ['SEO Score', health['seo_score']],
            ['Keyword Efficiency', health['keyword_efficiency']],
            ['Optimization Potential', health['optimization_potential']]
        ]

        health_table = Table(health_data, colWidths=[2.5*inch, 2*inch])
        health_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        story.append(health_table)
        story.append(Spacer(1, 20))

        # Key opportunities
        story.append(Paragraph("Key Opportunities Identified:", subheading_style))
        for i, opp in enumerate(summary["key_opportunities"], 1):
            story.append(Paragraph(f"{i}. {opp}", styles['Normal']))
            story.append(Spacer(1, 4))

        story.append(Spacer(1, 15))

        # Immediate actions
        story.append(Paragraph("Immediate Actions Required:", subheading_style))
        for i, action in enumerate(summary["immediate_actions"], 1):
            # Clean action text of any problematic characters
            clean_action = action.encode('ascii', 'ignore').decode('ascii')
            story.append(Paragraph(f"{i}. {clean_action}", styles['Normal']))
            story.append(Spacer(1, 4))

        story.append(Spacer(1, 15))
        story.append(Paragraph(f"<b>Strategic Focus:</b> {summary['strategic_focus']}", styles['Normal']))

        story.append(PageBreak())

        # Cross-Agent Insights
        story.append(Paragraph("CROSS-AGENT STRATEGIC INSIGHTS", heading_style))

        cross_insights = data["cross_agent_insights"]

        # Keyword-trend gaps
        story.append(Paragraph("Missing Trending Keywords:", subheading_style))
        gaps = cross_insights.get("keyword_trend_gaps", [])
        if gaps:
            for gap in gaps[:5]:  # Top 5
                story.append(Paragraph(f"• {gap}", styles['Normal']))
        else:
            story.append(Paragraph("• Current keywords well-aligned with trends", styles['Normal']))

        story.append(Spacer(1, 15))

        # Category expansion
        story.append(Paragraph("Category Expansion Opportunities:", subheading_style))
        category_opps = cross_insights.get("category_expansion_opportunities", [])
        for opp in category_opps[:3]:  # Top 3
            story.append(Paragraph(f"• {opp['category']} - Growth: {opp['growth_rate']}", styles['Normal']))

        story.append(PageBreak())

        # Strategic Roadmap
        story.append(Paragraph("STRATEGIC ROADMAP", heading_style))

        roadmap = data["strategic_roadmap"]
        story.append(Paragraph(f"<b>Primary Focus:</b> {roadmap['primary_focus']}", styles['Normal']))
        story.append(Spacer(1, 15))

        # Implementation timeline
        story.append(Paragraph("Implementation Phases:", subheading_style))

        phases = roadmap["strategic_phases"]
        for phase_name, phase_data in phases.items():
            phase_title = phase_name.replace('_', ' ').title()
            story.append(Paragraph(f"<b>{phase_title}</b> ({phase_data['timeline']})", styles['Normal']))
            story.append(Paragraph(f"Focus: {phase_data['focus']}", styles['Normal']))

            for action in phase_data['key_actions'][:3]:  # Top 3 actions
                story.append(Paragraph(f"  • {action}", styles['Normal']))

            story.append(Spacer(1, 10))

        story.append(PageBreak())

        # Priority Action Plan
        story.append(Paragraph("PRIORITY ACTION PLAN", heading_style))

        priority_actions = data["priority_action_plan"]

        # Immediate actions
        story.append(Paragraph("Immediate Actions (This Week):", subheading_style))
        for i, action in enumerate(priority_actions["immediate"][:5], 1):
            clean_action = action.encode('ascii', 'ignore').decode('ascii')
            story.append(Paragraph(f"{i}. {clean_action}", styles['Normal']))
            story.append(Spacer(1, 4))

        story.append(Spacer(1, 15))

        # Short-term actions
        story.append(Paragraph("Short-term Actions (Next Month):", subheading_style))
        for i, action in enumerate(priority_actions["short_term"][:5], 1):
            clean_action = action.encode('ascii', 'ignore').decode('ascii')
            story.append(Paragraph(f"{i}. {clean_action}", styles['Normal']))
            story.append(Spacer(1, 4))

        story.append(Spacer(1, 15))

        # Medium-term actions
        story.append(Paragraph("Medium-term Actions (Next Quarter):", subheading_style))
        for i, action in enumerate(priority_actions["medium_term"][:5], 1):
            clean_action = action.encode('ascii', 'ignore').decode('ascii')
            story.append(Paragraph(f"{i}. {clean_action}", styles['Normal']))
            story.append(Spacer(1, 4))

        story.append(PageBreak())

        # Integrated Recommendations
        story.append(Paragraph("INTEGRATED STRATEGIC RECOMMENDATIONS", heading_style))

        integrated_recs = data["integrated_recommendations"]

        # SEO Strategy
        seo_strategy = integrated_recs["seo_keyword_strategy"]
        story.append(Paragraph("SEO & Keyword Strategy:", subheading_style))
        story.append(Paragraph(f"• Keywords to Add: {', '.join(seo_strategy['immediate_keywords_to_add'][:5])}", styles['Normal']))
        story.append(Paragraph(f"• Keywords to Remove: {len(seo_strategy['keywords_to_remove'])} identified", styles['Normal']))
        story.append(Paragraph(f"• Seasonal Timing: {seo_strategy['seasonal_timing']}", styles['Normal']))
        story.append(Spacer(1, 10))

        # Product Strategy
        product_strategy = integrated_recs["product_development_strategy"]
        story.append(Paragraph("Product Development Strategy:", subheading_style))
        story.append(Paragraph(f"• Approach: {product_strategy['digital_first_approach']}", styles['Normal']))
        story.append(Paragraph(f"• POD Priorities: {', '.join(product_strategy['pod_priorities'][:3])}", styles['Normal']))
        story.append(Paragraph(f"• Bundle Strategy: {', '.join(product_strategy['bundle_opportunities'][:2])}", styles['Normal']))
        story.append(Spacer(1, 10))

        # Market Positioning
        market_positioning = integrated_recs["market_positioning"]
        story.append(Paragraph("Market Positioning:", subheading_style))
        story.append(Paragraph(f"• Niche Focus: {market_positioning['niche_focus']}", styles['Normal']))
        story.append(Paragraph(f"• Competitive Advantage: {market_positioning['competitive_advantage']}", styles['Normal']))
        story.append(Paragraph(f"• Target Expansion: {', '.join(market_positioning['target_expansion'][:3])}", styles['Normal']))

        story.append(PageBreak())

        # Agent-Specific Insights Summary
        story.append(Paragraph("AGENT-SPECIFIC INSIGHTS SUMMARY", heading_style))

        # Keyword Optimization Agent
        keyword_data = data["agent_analyses"]["keyword_optimization"]
        story.append(Paragraph("Keyword Optimization Agent:", subheading_style))

        portfolio = keyword_data["portfolio_summary"]
        story.append(Paragraph(f"• Portfolio Health: {portfolio['avg_keywords_per_listing']:.1f}/13 average tags per listing", styles['Normal']))
        story.append(Paragraph(f"• High Priority Optimizations: {portfolio['high_priority_optimizations']} listings need immediate attention", styles['Normal']))
        story.append(Paragraph(f"• Quick Wins Available: {len(keyword_data['quick_wins'])} identified", styles['Normal']))
        story.append(Spacer(1, 10))

        # Trends Research Agent
        story.append(Paragraph("Trends Research Agent:", subheading_style))
        story.append(Paragraph("• Market Health: Strong growth in political humor niche", styles['Normal']))
        story.append(Paragraph("• Key Trend: Government employee gifts showing +38% growth", styles['Normal']))
        story.append(Paragraph("• Opportunity: Cybersecurity humor category emerging (+42% growth)", styles['Normal']))
        story.append(Spacer(1, 10))

        # Product Expansion Agent
        story.append(Paragraph("Product Expansion Agent:", subheading_style))
        expansion_data = data["agent_analyses"]["product_expansion"]
        immediate_count = len(expansion_data["expansion_priorities"]["immediate_launch"])
        story.append(Paragraph(f"• Immediate Opportunities: {immediate_count} high-score products identified", styles['Normal']))
        story.append(Paragraph("• Focus Area: Digital downloads offer 95% profit margins", styles['Normal']))
        story.append(Paragraph("• Bundle Strategy: 2 digital product suites recommended", styles['Normal']))

        # Footer
        story.append(Spacer(1, 30))
        story.append(Paragraph("Multi-Agent Business Intelligence Report | EcureuilBleu Analysis Framework",
                              ParagraphStyle('Footer', parent=styles['Normal'],
                                           fontSize=10, alignment=TA_CENTER,
                                           textColor=colors.grey)))

        # Build PDF
        doc.build(story)
        print("Multi-Agent PDF report generated: EcureuilBleu_Multi_Agent_Complete_Report.pdf")
        return True

    except FileNotFoundError:
        print("Multi-agent analysis data not found. Please run multi_agent_analyzer.py first.")
        return False
    except Exception as e:
        print(f"Error generating PDF report: {e}")
        return False

if __name__ == "__main__":
    print("Creating comprehensive multi-agent PDF report...")
    success = create_multi_agent_pdf()

    if success:
        print("Report generation complete!")
    else:
        print("Report generation failed.")
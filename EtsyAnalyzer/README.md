# EcureuilBleu Etsy Shop Business Intelligence Analyzer

Complete multi-agent business intelligence system for Etsy shop optimization and expansion.

## Quick Start

### Master Command (Run This First)
```bash
python multi_agent_analyzer.py
```

### Generate PDF Report
```bash
python simple_multi_agent_report.py
```

## System Architecture

### 🤖 Multi-Agent System
- **Keyword Optimization Agent** - Analyzes existing keywords for removal/replacement
- **Trends Research Agent** - Researches Etsy trends from specialized sources
- **Product Expansion Agent** - Suggests POD and digital product opportunities
- **Integration Engine** - Cross-references insights for strategic recommendations

### 📁 File Structure

#### Core System Files
- `multi_agent_analyzer.py` - **MASTER FILE** - Runs complete analysis
- `ecureuil_bleu_analysis_framework.py` - Base SEO analysis framework
- `etsy_csv_analyzer.py` - CSV data parser for Etsy listings

#### Report Generators
- `simple_multi_agent_report.py` - **RECOMMENDED** - Clean comprehensive PDF
- `final_enhanced_report.py` - Detailed PDF with individual listing analysis
- `enhanced_pdf_report.py` - Enhanced PDF with trending keywords
- `generate_pdf_report.py` - Basic PDF report generator
- `ultimate_pdf_report.py` - Full-featured PDF (complex)

#### Utility Files
- `data_collection_template.py` - Manual data entry template
- `etsy-bi-reporting-framework.md` - Business intelligence framework documentation

### 🗂️ Data Structure

#### Input Data
- `etsy-agents/EtsyListingsDownload.csv` - Your Etsy shop data (UPDATE THIS)

#### Generated Reports
- `multi_agent_analysis_report.json` - Complete analysis data
- `ecureuil_bleu_full_analysis.json` - Base analysis results
- `enhanced_listings_analysis.csv` - Listing-by-listing recommendations
- `EcureuilBleu_Multi_Agent_Complete_Report.pdf` - Final PDF report

#### Agent System
- `etsy-agents/agents/` - Three specialized AI agents
  - `keyword_optimizer/` - Keyword analysis agent
  - `trend_researcher/` - Market trends agent
  - `product_expander/` - Product opportunity agent
- `etsy-agents/config/` - Agent configuration files

## Usage Workflow

### 1. Update Your Data
Replace your Etsy shop data in: `etsy-agents/EtsyListingsDownload.csv`

### 2. Run Master Analysis
```bash
python multi_agent_analyzer.py
```
This generates: `multi_agent_analysis_report.json`

### 3. Generate PDF Report
```bash
python simple_multi_agent_report.py
```
This creates: `EcureuilBleu_Multi_Agent_Complete_Report.pdf`

### 4. Review & Implement
- Executive summary shows shop health and opportunities
- Priority actions list immediate steps to take
- Strategic roadmap provides 3-phase implementation plan
- Individual listing analysis gives specific recommendations

## Key Features

### ✅ What The System Provides
- **SEO Analysis** - Keyword optimization recommendations (Etsy-compliant ≤20 chars)
- **Market Intelligence** - Trending categories and keywords from last 90 days
- **Product Opportunities** - POD and digital expansion recommendations
- **Cross-Agent Insights** - Strategic synergies between keyword trends and products
- **Implementation Roadmap** - Prioritized action plan with timelines

### 📊 Analysis Outputs
- Shop health assessment (SEO score, keyword efficiency)
- 25+ trending keyword recommendations
- 15+ product expansion opportunities
- Individual analysis for all listings
- Strategic 3-phase roadmap (optimization → expansion → scaling)

## Requirements

- Python 3.x
- ReportLab library: `pip install reportlab`
- Your Etsy shop data in CSV format

## Troubleshooting

### Unicode Issues (Windows)
If you see Unicode errors, the system will still work - it's just emoji display issues in Windows Command Prompt.

### Missing Data
Update your CSV file with actual Etsy shop data from Shop Manager → Listings → Export

### Agent Errors
Each agent is independent - if one fails, others will continue to work.

---

**🎯 Start Here:** Run `python multi_agent_analyzer.py` to begin your complete shop analysis!
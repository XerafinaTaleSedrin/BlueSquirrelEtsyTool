# 🎯 EtsyAnalyzer Workflow Dashboard

A Flask-based GUI management system for your AI-powered Etsy product creation workflow.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install flask requests
```

### 2. Start the Dashboard
```bash
python workflow_dashboard.py
```

### 3. Access the Dashboard
Open your browser and go to: **http://localhost:5000**

## 📋 Workflow Process

### Phase 1: Market Analysis
- **Page**: Market Analysis
- **Action**: Click "Start Analysis" to run market intelligence
- **Output**: Design briefs and prompts generated automatically
- **Time**: ~30 seconds

### Phase 2: Design Brief Review
- **Page**: Design Pipeline
- **Action**: Review generated briefs and approve/reject each one
- **Features**:
  - View detailed design prompts with Printful DPI requirements
  - Add approval notes
  - Bulk approve functionality
- **Output**: Approved briefs ready for image creation

### Phase 3: Design Creation (Manual)
- Use approved design prompts with Claude, ChatGPT, or Midjourney
- **Requirements**: 300 DPI PNG with transparent background
- **Specifications**:
  - T-shirt/Hoodie: 12" x 16" max
  - Mug: 8.5" x 3.5" max
  - Single-color design preferred

### Phase 4: Design Upload
- **Page**: Design Assets
- **Action**: Upload your created PNG files
- **Features**:
  - Drag & drop file upload
  - Automatic brief matching
  - File validation (PNG, 20MB max, 300 DPI)
- **Output**: Ready for Printful integration

### Phase 5: Product Setup (Coming Soon)
- **Page**: Printful Setup
- **Action**: One-click product creation on Printful
- **Features**: Automated mockup generation, profit calculation

### Phase 6: Etsy Integration (Coming Soon)
- **Page**: Etsy Management
- **Action**: Generate CSV and bulk upload to Etsy
- **Features**: SEO-optimized listings, bulk management

## 🎨 Generated Design Prompts Include:

- **Printful Technical Requirements** (300 DPI, PNG, transparent background)
- **Print Area Specifications** (T-shirt: 12"x16", Mug: 8.5"x3.5")
- **Color and Style Guidelines**
- **Target Audience Details**
- **SEO Keywords**
- **Design Constraints**

## 📁 File Structure

```
EtsyAnalyzer/
├── workflow_dashboard.py          # Main Flask application
├── workflow_state.db              # SQLite database (auto-created)
├── templates/                     # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── market_analysis.html
│   ├── design_pipeline.html
│   └── design_assets.html
├── static/                        # CSS & JavaScript
│   ├── css/dashboard.css
│   └── js/dashboard.js
├── DESIGNS/                       # Unified design storage
│   ├── briefs/                    # Generated design briefs
│   ├── prompts/                   # Claude-ready prompts
│   ├── completed_designs/         # Your uploaded PNGs
│   ├── future_concepts/           # Future design ideas
│   └── upload_ready/             # CSV files for Etsy
└── automation/                    # Backend automation components
```

## 🔧 Key Features

### ✅ Human Oversight Gates
- Review every design brief before creation
- Approve/reject with notes
- Prevents automated generation of unwanted products

### ✅ Printful Integration Ready
- All prompts include proper DPI specifications
- Technical requirements built into workflow
- Profit margin calculations

### ✅ Visual Workflow Management
- Progress tracking across all stages
- Status indicators for each design
- Bulk actions for efficiency

### ✅ File Upload Management
- Drag & drop interface
- Automatic brief matching
- File validation and progress tracking

## 🎯 Your TPS Report Design

Your existing TPS Report design should be placed at:
`DESIGNS/completed_designs/png_files/tps_report_survivor_xerox_300dpi.png`

The system will recognize it and allow you to proceed with Printful setup.

## 🔄 Workflow State Tracking

The dashboard uses SQLite to track:
- Design brief approval status
- Uploaded design files
- Printful setup progress
- Etsy listing status

## ⚡ Next Steps

1. **Start the dashboard**: `python workflow_dashboard.py`
2. **Run market analysis** to generate new design briefs
3. **Review and approve** design concepts you want to create
4. **Use approved prompts** with Claude to create actual designs
5. **Upload PNG files** through the Design Assets page
6. **Set up Printful products** (coming in next update)
7. **Create Etsy listings** (coming in next update)

## 🎨 Design Creation Tips

When using the generated prompts with Claude:
- Copy the entire prompt including technical requirements
- Ask for specific dimensions (e.g., "create at 3600x4800 pixels for 300 DPI at 12x16 inches")
- Request transparent background PNG format
- Specify single-color design for cost effectiveness

## 🚨 Important Notes

- Always use 300 DPI for Printful compatibility
- PNG with transparent background required
- Single-color designs cost less to print
- File size limit: 20MB maximum
- The system prevents incomplete products from reaching Etsy

This dashboard gives you complete control over your automated pipeline with human approval at every critical decision point!
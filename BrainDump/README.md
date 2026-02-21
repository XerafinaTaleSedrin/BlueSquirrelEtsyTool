# BrainDump: Multi-Agent Idea Collation System

A sophisticated system for collecting, organizing, and analyzing your daily ideas with a focus on supporting your Montolieu shop goals and France transition.

## 🎯 Purpose

BrainDump helps you:
- Capture ideas quickly during daily check-ins
- Automatically categorize ideas using AI
- Detect patterns and recurring themes
- Identify opportunities that support your Montolieu paper/book/coffee shop vision
- Learn from your feedback to improve over time

## 🚀 Quick Start

### Daily Check-in (Interactive Mode)
```bash
python braindump.py
```

### Quick Add (Single Idea)
```bash
python braindump.py "Idea about sourcing vintage desks from local antique dealers"
```

### Analysis & Reports
```bash
python analyze.py stats     # Quick statistics
python analyze.py report    # Full analysis report
python analyze.py export    # Export all data
```

## 📁 System Architecture

### Core Components

- **braindump.py** - Main interface for idea capture
- **analyze.py** - Analysis and reporting tools
- **agents/** - Multi-agent system for processing

### Agents

1. **Categorizer Agent** - Auto-categorizes ideas into:
   - Business (general business ideas)
   - Technical (code projects, tools)
   - France-Move (transition planning)
   - Life (personal insights)
   - Montolieu-Shop (specific shop ideas)

2. **Pattern Detector** - Identifies:
   - Frequently mentioned concepts
   - Keyword clusters
   - Category trends over time
   - Temporal patterns

3. **Opportunity Suggester** - Finds:
   - Ideas supporting Montolieu shop goals
   - Connection opportunities between ideas
   - Timing-sensitive opportunities
   - Resource gaps to address

4. **Trainer Agent** - Learns from feedback:
   - Records categorization corrections
   - Improves accuracy over time
   - Suggests system improvements

## 🎯 Montolieu Shop Focus Areas

The system is specifically tuned to identify opportunities in:

- **Inventory Sourcing** - Books, paper, stationery, antique desks
- **Customer Experience** - Atmosphere, coffee service, charm
- **Local Connections** - Community building, artisan networks
- **Business Operations** - Revenue, costs, permits, logistics
- **Digital Presence** - Website, social media, online marketing
- **Personal Preparation** - Language, visa, housing, adaptation

## 💾 Data Storage

All data is stored locally in JSON format:

- `data/ideas.json` - All captured ideas
- `data/categories.json` - Category definitions
- `data/patterns.json` - Detected patterns
- `data/opportunities.json` - Identified opportunities
- `data/feedback.json` - Training feedback
- `data/learned_rules.json` - AI learning data

## 🔄 Typical Workflow

1. **Morning Check-in**: Run `python braindump.py`
2. **Capture Ideas**: Type ideas as they come to mind
3. **Provide Feedback**: Correct categorizations when wrong
4. **Review Insights**: Run `python analyze.py report` weekly
5. **Act on Opportunities**: Follow up on high-priority suggestions

## 📊 Sample Analysis Output

```
🧠 BrainDump Analysis Report
============================================================

📊 Ideas Overview
------------------------------
Total ideas: 47
Ideas this week: 12
Latest idea: 2024-09-16 09:15

📁 Category Analysis
------------------------------
Montolieu-Shop   15 ( 31.9%)
Business         12 ( 25.5%)
France-Move       8 ( 17.0%)
Technical         7 ( 14.9%)
Life              5 ( 10.6%)

🎯 Opportunity Analysis
------------------------------
High Priority:
  • Perfect timing for autumn: Research antique desk restoration...
  • Pursue: Contact local Montolieu artisans for collaboration...

🏪 Montolieu Shop Goal Progress
----------------------------------------
Inventory Sourcing (high priority)
  Ideas: 8
  Recent:
    • Research suppliers for fountain pens and quality paper
    • Visit antique markets in Toulouse for vintage desks
```

## 🎓 Training the System

The system learns from your feedback:

- When it miscategorizes, type the correct category name
- Say "n" or "wrong" if categorization is incorrect
- The system will remember patterns and improve

## 🔧 Customization

Edit `agents/categorizer.py` to:
- Add new categories
- Modify keyword patterns
- Adjust categorization rules

Edit `agents/opportunity_suggester.py` to:
- Change goal priorities
- Add new opportunity types
- Modify suggestion criteria

## 📈 Future Enhancements

Potential additions:
- Voice input for idea capture
- Image/photo idea storage
- Integration with calendar/reminders
- Export to project management tools
- Web interface for remote access

## 🔒 Privacy

All data remains local on your machine. No cloud services or external APIs are used for idea processing.
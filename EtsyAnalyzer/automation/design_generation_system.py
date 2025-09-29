#!/usr/bin/env python3
"""
AI-Powered Design Generation System for Etsy T-shirt Business
Uses Claude prompts to generate design concepts based on market intelligence
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict

@dataclass
class DesignBrief:
    """Structured design brief for AI generation"""
    concept_name: str
    target_keywords: List[str]
    design_theme: str  # government_humor, cybersecurity, political_satire
    target_audience: str
    style_preferences: List[str]  # minimal, vintage, bold, humorous
    color_scheme: Optional[str]
    text_elements: List[str]
    avoid_elements: List[str]
    printful_products: List[str]  # t-shirt, hoodie, mug, etc.
    priority_score: float  # 1-10 based on market opportunity

@dataclass
class GeneratedDesign:
    """AI-generated design concept"""
    design_id: str
    brief_id: str
    concept_description: str
    visual_prompt: str  # For image generation
    text_elements: Dict[str, str]  # main_text, subtitle, tagline
    style_notes: str
    target_products: List[str]
    estimated_appeal: str  # High/Medium/Low
    generated_timestamp: str

class DesignPromptEngine:
    """Generates AI prompts for design creation based on market intelligence"""

    def __init__(self, market_data_path: str = None):
        self.market_data = self._load_market_data(market_data_path)
        self.design_templates = self._initialize_templates()

    def _load_market_data(self, data_path: str) -> Dict:
        """Load market intelligence data from EtsyAnalyzer"""
        if data_path and os.path.exists(data_path):
            with open(data_path, 'r') as f:
                return json.load(f)
        return {}

    def _initialize_templates(self) -> Dict:
        """Initialize design prompt templates for different themes"""
        return {
            "government_humor": {
                "base_prompt": "Create a humorous t-shirt design that government employees would find relatable and funny. The design should be workplace-appropriate and capture the absurdities of bureaucracy.",
                "style_elements": ["minimalist", "vintage office", "retro government", "clean typography"],
                "common_phrases": ["Civil Servant", "Bureaucrat Life", "Government Speed", "Red Tape", "Meeting About Meetings"],
                "avoid": ["political party references", "controversial topics", "inappropriate language"]
            },
            "cybersecurity": {
                "base_prompt": "Design a tech-savvy t-shirt that cybersecurity professionals would appreciate. Include clever references to IT security concepts.",
                "style_elements": ["matrix-style", "hacker aesthetic", "clean tech", "monospace fonts"],
                "common_phrases": ["Security First", "Patch Tuesday", "Zero Trust", "Phishing Awareness", "Social Engineering"],
                "avoid": ["actual hacking references", "illegal activities", "security vulnerabilities"]
            },
            "political_satire": {
                "base_prompt": "Create a witty political satire design that's clever but non-partisan. Focus on general political processes rather than specific parties.",
                "style_elements": ["editorial cartoon", "vintage propaganda", "clean illustration", "bold typography"],
                "common_phrases": ["Democracy", "Voting Matters", "Political Process", "Civic Duty", "Election Season"],
                "avoid": ["specific politicians", "partisan messaging", "controversial symbols"]
            }
        }

    def generate_design_brief_from_trends(self, trending_keywords: List[str], theme: str) -> DesignBrief:
        """Generate a design brief based on trending keywords and theme"""

        # Get theme template
        template = self.design_templates.get(theme, self.design_templates["government_humor"])

        # Create design brief
        brief = DesignBrief(
            concept_name=f"{theme}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            target_keywords=trending_keywords[:5],  # Top 5 keywords
            design_theme=theme,
            target_audience=self._determine_target_audience(theme),
            style_preferences=template["style_elements"][:3],
            color_scheme=self._suggest_color_scheme(theme),
            text_elements=self._generate_text_concepts(trending_keywords, template),
            avoid_elements=template["avoid"],
            printful_products=["t-shirt", "hoodie", "mug"],
            priority_score=self._calculate_priority_score(trending_keywords, theme)
        )

        return brief

    def _determine_target_audience(self, theme: str) -> str:
        """Determine target audience based on theme"""
        audience_map = {
            "government_humor": "Government employees, civil servants, federal workers, contractors",
            "cybersecurity": "IT professionals, cybersecurity experts, tech workers, system administrators",
            "political_satire": "Political enthusiasts, civic-minded individuals, election workers, policy professionals"
        }
        return audience_map.get(theme, "General audience")

    def _suggest_color_scheme(self, theme: str) -> str:
        """Suggest appropriate color schemes for themes"""
        color_schemes = {
            "government_humor": "Navy blue and gray (professional), or red/white/blue (patriotic)",
            "cybersecurity": "Green and black (matrix), or blue and white (tech)",
            "political_satire": "Red/white/blue (patriotic), or black and white (editorial)"
        }
        return color_schemes.get(theme, "Flexible color scheme")

    def _generate_text_concepts(self, keywords: List[str], template: Dict) -> List[str]:
        """Generate text concept ideas for designs"""
        text_concepts = []

        # Add template phrases
        text_concepts.extend(template["common_phrases"][:3])

        # Generate concepts from keywords
        for keyword in keywords[:3]:
            # Create variations
            text_concepts.append(f"Professional {keyword}")
            text_concepts.append(f"{keyword} Expert")
            text_concepts.append(f"Powered by {keyword}")

        return text_concepts[:8]  # Limit to 8 concepts

    def _calculate_priority_score(self, keywords: List[str], theme: str) -> float:
        """Calculate priority score based on market data"""
        base_score = 5.0

        # Adjust based on market intelligence if available
        if self.market_data:
            # Check for trending themes
            if theme == "government_humor" and "government humor" in str(self.market_data):
                base_score += 2.0
            if theme == "cybersecurity" and "cybersecurity" in str(self.market_data):
                base_score += 1.5
            if theme == "political_satire" and "political satire" in str(self.market_data):
                base_score += 1.8

        # Adjust based on keyword count
        base_score += min(len(keywords) * 0.2, 1.0)

        return min(base_score, 10.0)

    def create_claude_design_prompt(self, brief: DesignBrief) -> str:
        """Create a detailed Claude prompt for design generation"""

        template = self.design_templates.get(brief.design_theme, self.design_templates["government_humor"])

        prompt = f"""
Design Brief: {brief.concept_name}

THEME: {brief.design_theme}
TARGET AUDIENCE: {brief.target_audience}
TARGET KEYWORDS: {', '.join(brief.target_keywords)}

PRINTFUL TECHNICAL REQUIREMENTS (CRITICAL):
- Resolution: 300 DPI minimum (required for print quality)
- Format: PNG with transparent background
- File size: Maximum 20 MB per file
- Color mode: RGB
- Print areas:
  * T-shirt: 12" x 16" maximum print area
  * Hoodie: 12" x 16" maximum print area
  * Mug: 8.5" x 3.5" maximum print area
- Design must be scalable and readable at different sizes
- Single-color design preferred for cost-effective printing

BASE CONCEPT:
{template['base_prompt']}

SPECIFIC REQUIREMENTS:
- Style: {', '.join(brief.style_preferences)}
- Colors: {brief.color_scheme}
- Products: {', '.join(brief.printful_products)}

TEXT CONCEPTS TO CONSIDER:
{chr(10).join(f"- {text}" for text in brief.text_elements)}

MUST AVOID:
{chr(10).join(f"- {avoid}" for avoid in brief.avoid_elements)}

DELIVERABLES NEEDED:
1. Main design concept description (2-3 sentences)
2. Visual layout description (placement, typography, imagery)
3. Text hierarchy (main message, supporting text, tagline)
4. Color palette recommendations
5. Adaptability notes for different products (t-shirt vs mug vs hoodie)
6. 300 DPI specifications for each product variant

CONSTRAINTS:
- Design must work in single color for cost-effective printing
- Text must be readable at small sizes
- Design should appeal to professional workplace environment
- Must be legally safe and non-controversial
- Must meet Printful's 300 DPI technical requirements

Please provide a detailed design concept that balances creativity with commercial viability and meets all Printful technical specifications.
"""

        return prompt.strip()

    def generate_batch_briefs(self, market_analysis: Dict, max_briefs: int = 5) -> List[DesignBrief]:
        """Generate multiple design briefs from market analysis"""
        briefs = []

        # Extract trending keywords from market analysis
        trending_keywords = []
        if "cross_agent_insights" in market_analysis:
            trending_keywords = market_analysis["cross_agent_insights"].get("keyword_trend_gaps", [])

        if not trending_keywords and "executive_summary" in market_analysis:
            # Fallback to immediate actions
            immediate_actions = market_analysis["executive_summary"].get("immediate_actions", [])
            for action in immediate_actions:
                if "keyword" in action.lower():
                    # Extract keywords from action text
                    keywords = action.split(":")[-1].strip().split(",")
                    trending_keywords.extend([kw.strip() for kw in keywords])

        # Generate briefs for each theme
        themes = ["government_humor", "cybersecurity", "political_satire"]

        for i, theme in enumerate(themes):
            if i >= max_briefs:
                break

            keyword_subset = trending_keywords[i*3:(i+1)*3] if trending_keywords else [theme.replace("_", " ")]
            brief = self.generate_design_brief_from_trends(keyword_subset, theme)
            briefs.append(brief)

        return briefs

class DesignWorkflowManager:
    """Manages the complete design generation workflow"""

    def __init__(self, output_dir: str = "generated_designs"):
        self.output_dir = output_dir
        self.prompt_engine = DesignPromptEngine()
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "briefs"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "prompts"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "designs"), exist_ok=True)

    def process_market_analysis(self, analysis_file: str) -> List[str]:
        """Process market analysis and generate design prompts"""

        # Load market analysis
        with open(analysis_file, 'r') as f:
            market_data = json.load(f)

        # Generate design briefs
        briefs = self.prompt_engine.generate_batch_briefs(market_data)

        # Create Claude prompts
        generated_prompts = []

        for brief in briefs:
            # Save brief
            brief_file = os.path.join(self.output_dir, "briefs", f"{brief.concept_name}_brief.json")
            with open(brief_file, 'w') as f:
                json.dump(asdict(brief), f, indent=2)

            # Generate Claude prompt
            claude_prompt = self.prompt_engine.create_claude_design_prompt(brief)

            # Save prompt
            prompt_file = os.path.join(self.output_dir, "prompts", f"{brief.concept_name}_prompt.txt")
            with open(prompt_file, 'w') as f:
                f.write(claude_prompt)

            generated_prompts.append(prompt_file)

            print(f"Generated design brief and prompt: {brief.concept_name}")

        return generated_prompts

    def create_design_summary(self, prompts: List[str]) -> str:
        """Create a summary of all generated design prompts"""

        summary_file = os.path.join(self.output_dir, "design_generation_summary.md")

        with open(summary_file, 'w') as f:
            f.write("# AI-Generated Design Concepts\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total concepts generated: {len(prompts)}\n\n")

            for i, prompt_file in enumerate(prompts, 1):
                concept_name = os.path.basename(prompt_file).replace("_prompt.txt", "")
                f.write(f"## {i}. {concept_name}\n\n")
                f.write(f"**Prompt file:** `{prompt_file}`\n\n")
                f.write(f"**Brief file:** `{prompt_file.replace('prompts', 'briefs').replace('_prompt.txt', '_brief.json')}`\n\n")
                f.write("---\n\n")

        return summary_file

def main():
    """Example usage of the design generation system"""

    # Initialize workflow manager
    manager = DesignWorkflowManager()

    # Path to your market analysis
    analysis_file = "multi_agent_analysis_report.json"

    if os.path.exists(analysis_file):
        print("Processing market analysis for design generation...")
        prompts = manager.process_market_analysis(analysis_file)
        summary = manager.create_design_summary(prompts)

        print(f"\nDesign generation complete!")
        print(f"Generated {len(prompts)} design concepts")
        print(f"Summary available at: {summary}")
        print("\nNext steps:")
        print("1. Review the generated prompts")
        print("2. Use Claude to develop the design concepts")
        print("3. Create actual designs based on the concepts")
        print("4. Upload to Printful for product creation")
    else:
        print(f"Market analysis file not found: {analysis_file}")
        print("Please run the EtsyAnalyzer first to generate market intelligence")

if __name__ == "__main__":
    main()
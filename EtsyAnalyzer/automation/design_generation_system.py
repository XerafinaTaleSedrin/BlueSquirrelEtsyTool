#!/usr/bin/env python3
"""
AI-Powered Design Generation System for Etsy T-shirt Business
Uses Claude prompts to generate design concepts based on market intelligence
"""

import os
# Force UTF-8 encoding for all operations
os.environ['PYTHONIOENCODING'] = 'utf-8'

import json
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict

# Import Printful catalog validation
try:
    from printful_catalog import get_available_products, validate_printful_products
except ImportError:
    get_available_products = None
    validate_printful_products = None

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
            with open(data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _initialize_templates(self) -> Dict:
        """Initialize highly differentiated design prompt templates for different themes"""
        return {
            "government_humor": {
                "base_prompt": "Design a witty federal workplace satire piece that captures the unique culture of government service. Think vintage office aesthetics meets bureaucratic irony - celebrating public service while poking fun at the system. Target federal employees who appreciate inside jokes about forms, clearances, and interdepartmental coordination.",
                "style_elements": ["vintage office memo", "retro government poster", "official document parody", "bureaucratic seal mockery"],
                "unique_concepts": [
                    "Form 404: Motivation Not Found",
                    "Classified: Coffee Break Schedule",
                    "Security Clearance Required for Bathroom Key",
                    "Democracy: Some Assembly Required",
                    "Federal Employee Bingo",
                    "Department of Redundancy Department"
                ],
                "visual_metaphors": ["rubber stamps", "filing cabinets", "org charts", "security badges", "memo folders"],
                "industry_references": ["GS pay scale", "FERS retirement", "telework", "continuing resolution", "OPM guidelines"],
                "avoid": ["political party references", "controversial policies", "specific agencies"]
            },
            "cybersecurity": {
                "base_prompt": "Create a sophisticated tech professional design that speaks to the cybersecurity mindset. Blend matrix aesthetics with enterprise security culture - celebrating the guardian role while acknowledging the constant vigilance required. Target InfoSec professionals who understand both technical depth and business reality.",
                "style_elements": ["matrix code overlay", "terminal interface", "network topology", "security dashboard"],
                "unique_concepts": [
                    "Trust But Verify (Zero Trust Edition)",
                    "Patch Tuesday Survivor",
                    "Social Engineer This!",
                    "Human Layer = Weakest Link",
                    "Multi-Factor Authentication Champion",
                    "Incident Response Team"
                ],
                "visual_metaphors": ["shields", "locks", "firewalls", "encryption symbols", "alert dashboards"],
                "industry_references": ["CVE numbers", "SIEM alerts", "penetration testing", "compliance frameworks", "threat intelligence"],
                "avoid": ["actual vulnerabilities", "hacking tools", "illegal activities"]
            },
            "political_satire": {
                "base_prompt": "Design an editorial-style democratic engagement piece that promotes civic participation through clever commentary. Think vintage propaganda meets modern political awareness - inspiring action while maintaining non-partisan appeal. Target civically-minded individuals who appreciate political process humor.",
                "style_elements": ["editorial cartoon style", "vintage civic poster", "ballot design parody", "campaign button aesthetic"],
                "unique_concepts": [
                    "Vote Early, Vote Often (Legally)",
                    "Democracy: Participation Required",
                    "Civic Duty Loading... Please Wait",
                    "Checks and Balances Champion",
                    "Constitutional Scholar in Training",
                    "Grassroots Democracy Advocate"
                ],
                "visual_metaphors": ["ballot boxes", "scales of justice", "capitol buildings", "voting booths", "civic symbols"],
                "industry_references": ["constituent services", "town halls", "public comment periods", "election integrity", "civic engagement"],
                "avoid": ["specific politicians", "partisan messaging", "controversial current events"]
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
            printful_products=self._get_validated_products_for_theme(theme),
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
        """Generate highly differentiated text concept ideas for designs"""
        text_concepts = []

        # Add unique template concepts (much more distinctive)
        text_concepts.extend(template.get("unique_concepts", [])[:4])

        # Generate niche-specific concepts from keywords
        for keyword in keywords[:2]:
            if "government" in keyword.lower():
                text_concepts.extend([
                    f"Cleared for {keyword.title()}",
                    f"{keyword.title()}: Above Your Pay Grade",
                    f"Form {keyword.title()}-001: Required"
                ])
            elif "cyber" in keyword.lower() or "security" in keyword.lower():
                text_concepts.extend([
                    f"{keyword.title()}: Access Denied",
                    f"Scanning for {keyword.title()}...",
                    f"{keyword.title()} Layer Activated"
                ])
            elif "political" in keyword.lower() or "democracy" in keyword.lower():
                text_concepts.extend([
                    f"{keyword.title()}: Your Vote Counts",
                    f"Certified {keyword.title()} Participant",
                    f"{keyword.title()}: Civic Duty Edition"
                ])
            else:
                # Fallback for other keywords
                text_concepts.extend([
                    f"Professional {keyword.title()}",
                    f"{keyword.title()} Specialist"
                ])

        return text_concepts[:8]  # Limit to 8 distinctive concepts

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

    def _generate_creative_direction(self, theme: str, template: Dict) -> str:
        """Generate unique creative direction for each theme"""
        directions = {
            "government_humor": "Focus on the insider perspective of federal service - celebrate the dedication while gently satirizing the process. Think vintage office nostalgia with modern frustrations.",
            "cybersecurity": "Capture the vigilant guardian mindset - blend technical sophistication with enterprise reality. Appeal to those who see security as both craft and calling.",
            "political_satire": "Promote civic engagement through intelligent commentary - inspire participation while maintaining broad appeal across political spectrum."
        }
        return directions.get(theme, "Professional niche appeal with authentic insider perspective")

    def _generate_visual_references(self, theme: str, template: Dict) -> str:
        """Generate visual style references for each theme"""
        references = {
            "government_humor": "Vintage government posters, official memo styles, bureaucratic seals, org chart aesthetics",
            "cybersecurity": "Matrix code overlays, terminal interfaces, network diagrams, security dashboard elements",
            "political_satire": "Editorial cartoons, civic campaign materials, vintage propaganda art, ballot design elements"
        }
        return references.get(theme, "Professional industry-specific visual language")

    def _generate_market_positioning(self, theme: str, audience: str) -> str:
        """Generate market positioning strategy for each niche"""
        positioning = {
            "government_humor": "The go-to brand for federal workplace humor - celebrating public service culture with insider authenticity",
            "cybersecurity": "Premium tech professional identity wear - for those who understand that security is everyone's job",
            "political_satire": "Intelligent civic engagement apparel - promoting democracy through thoughtful commentary"
        }
        return positioning.get(theme, "Specialized professional identity wear for niche audiences")

    def create_claude_design_prompt(self, brief: DesignBrief) -> str:
        """Create a highly detailed, niche-specific Claude prompt for design generation"""
        template = self.design_templates.get(brief.design_theme, self.design_templates["government_humor"])

        # Create theme-specific creative direction
        creative_direction = self._generate_creative_direction(brief.design_theme, template)
        visual_references = self._generate_visual_references(brief.design_theme, template)
        market_positioning = self._generate_market_positioning(brief.design_theme, brief.target_audience)

        prompt = f"""SPECIALIZED DESIGN BRIEF: {brief.concept_name}

═══════════════════════════════════════════════════════════════════════════
MARKET INTELLIGENCE & POSITIONING
═══════════════════════════════════════════════════════════════════════════

TARGET NICHE: {brief.design_theme.replace('_', ' ').title()}
AUDIENCE PSYCHOGRAPHICS: {brief.target_audience}
KEYWORD FOCUS: {', '.join(brief.target_keywords)}
MARKET POSITIONING: {market_positioning}

═══════════════════════════════════════════════════════════════════════════
CREATIVE DIRECTION & UNIQUE ANGLE
═══════════════════════════════════════════════════════════════════════════

CREATIVE CONCEPT:
{template['base_prompt']}

UNIQUE DIFFERENTIATION:
{creative_direction}

VISUAL STYLE IDENTITY:
- Primary Style: {', '.join(brief.style_preferences)}
- Color Psychology: {brief.color_scheme}
- Visual References: {visual_references}

═══════════════════════════════════════════════════════════════════════════
DISTINCTIVE TEXT CONCEPTS (NICHE-SPECIFIC)
═══════════════════════════════════════════════════════════════════════════

INSIDER TERMINOLOGY & CONCEPTS:
{chr(10).join(f"• {text}" for text in brief.text_elements)}

VISUAL METAPHORS TO CONSIDER:
{chr(10).join(f"• {metaphor}" for metaphor in template.get('visual_metaphors', []))}

INDUSTRY REFERENCES:
{chr(10).join(f"• {ref}" for ref in template.get('industry_references', []))}

═══════════════════════════════════════════════════════════════════════════
⚙️ PRINTFUL TECHNICAL SPECIFICATIONS (CRITICAL)
═══════════════════════════════════════════════════════════════════════════

MANDATORY REQUIREMENTS:
• Resolution: 300 DPI minimum (non-negotiable for print quality)
• Format: PNG with transparent background (required for versatility)
• File size: Maximum 20 MB per file
• Color mode: RGB (for screen-to-print accuracy)

PRINT AREA SPECIFICATIONS:
• T-shirt/Hoodie: 12" x 16" maximum print area
• Mug: 8.5" x 3.5" maximum print area
• Design scalability: Must remain readable at all sizes
• Cost optimization: Single-color design strongly preferred

═══════════════════════════════════════════════════════════════════════════
🚫 CONTENT RESTRICTIONS & COMPLIANCE
═══════════════════════════════════════════════════════════════════════════

STRICTLY AVOID:
{chr(10).join(f"• {avoid}" for avoid in brief.avoid_elements)}

LEGAL & COMMERCIAL SAFETY:
• Must be workplace-appropriate
• Cannot include copyrighted elements
• Must avoid controversial current events
• Should appeal to professional environment

═══════════════════════════════════════════════════════════════════════════
📋 DETAILED DELIVERABLES REQUIRED
═══════════════════════════════════════════════════════════════════════════

1. CONCEPT OVERVIEW (2-3 sentences)
   - Core visual concept and emotional appeal
   - How it connects with target niche

2. DETAILED VISUAL LAYOUT
   - Element placement and hierarchy
   - Typography style and sizing
   - Imagery/iconography integration

3. TEXT HIERARCHY SYSTEM
   - Primary message (main headline)
   - Secondary text (supporting message)
   - Tertiary elements (tagline/accent text)

4. PRODUCT-SPECIFIC ADAPTATIONS
   - T-shirt layout optimization
   - Hoodie placement considerations
   - Mug wrap-around design notes

5. COLOR PALETTE STRATEGY
   - Primary color selection rationale
   - Single-color print optimization
   - Background/foreground contrast

6. TECHNICAL IMPLEMENTATION NOTES
   - 300 DPI sizing for each product
   - Scalability testing requirements
   - Print production considerations

═══════════════════════════════════════════════════════════════════════════
🎖️ SUCCESS METRICS & VALIDATION
═══════════════════════════════════════════════════════════════════════════

DESIGN SUCCESS CRITERIA:
• Immediate niche recognition and appeal
• Professional yet memorable aesthetic
• Clear differentiation from generic designs
• Strong commercial viability for Etsy marketplace
• Technical excellence for Printful production

Please create a design concept that demonstrates deep understanding of the {brief.design_theme.replace('_', ' ')} niche while meeting all technical and commercial requirements. Focus on authenticity and insider appeal rather than generic themes.
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

    def _get_validated_products_for_theme(self, theme: str) -> List[str]:
        """Get validated Printful products for the given theme"""
        try:
            if get_available_products is None:
                # Fallback if catalog not available
                return ["t-shirt", "hoodie", "mug"]

            # Theme-specific product mappings
            theme_products = {
                "government_humor": ["t-shirt", "hoodie", "mug", "tote-bag"],
                "cybersecurity": ["t-shirt", "hoodie", "laptop-sleeve", "sticker"],
                "political_satire": ["t-shirt", "hoodie", "tote-bag", "poster"],
                "professional": ["polo-shirt", "button-shirt", "mug", "notebook"],
                "humor": ["t-shirt", "hoodie", "mug", "sticker"],
                "vintage": ["t-shirt", "hoodie", "tote-bag", "poster"],
                "minimalist": ["t-shirt", "tank-top", "mug", "poster"]
            }

            # Get suggested products for theme
            suggested = theme_products.get(theme, ["t-shirt", "hoodie", "mug"])

            # Get available products from catalog
            available_products = get_available_products("apparel")
            if not available_products:
                return suggested

            # Validate and map to actual Printful products
            validated = []
            for product in suggested:
                # Find matching products in catalog
                matches = [p for p in available_products
                          if product.lower().replace('-', ' ') in p['name'].lower()
                          or product.lower() in p['type_name'].lower()]

                if matches:
                    validated.append(matches[0]['name'])
                else:
                    # Try partial matching for alternatives
                    alternatives = [p for p in available_products
                                  if any(word in p['name'].lower()
                                        for word in product.lower().split('-'))]
                    if alternatives:
                        validated.append(alternatives[0]['name'])

            # Ensure minimum products
            if len(validated) < 2:
                defaults = [p for p in available_products
                           if 't-shirt' in p['name'].lower() or 'tee' in p['name'].lower()]
                if defaults:
                    validated.append(defaults[0]['name'])

            return validated[:3] if validated else ["t-shirt", "hoodie", "mug"]

        except Exception as e:
            print(f"Error validating products for theme {theme}: {e}")
            return ["t-shirt", "hoodie", "mug"]

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
        with open(analysis_file, 'r', encoding='utf-8') as f:
            market_data = json.load(f)

        # Generate design briefs
        briefs = self.prompt_engine.generate_batch_briefs(market_data)

        # Create Claude prompts
        generated_prompts = []

        for brief in briefs:
            # Save brief
            brief_file = os.path.join(self.output_dir, "briefs", f"{brief.concept_name}_brief.json")
            with open(brief_file, 'w', encoding='utf-8') as f:
                json.dump(asdict(brief), f, indent=2)

            # Generate Claude prompt
            claude_prompt = self.prompt_engine.create_claude_design_prompt(brief)

            # Save prompt
            prompt_file = os.path.join(self.output_dir, "prompts", f"{brief.concept_name}_prompt.txt")
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(claude_prompt)

            generated_prompts.append(prompt_file)

            print(f"Generated design brief and prompt: {brief.concept_name}")

        return generated_prompts

    def create_design_summary(self, prompts: List[str]) -> str:
        """Create a summary of all generated design prompts"""

        summary_file = os.path.join(self.output_dir, "design_generation_summary.md")

        with open(summary_file, 'w', encoding='utf-8') as f:
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
# MTG Arena Deck Optimizer - Initial Brainstorm

**Date Created**: 2026-02-28
**Status**: [Brainstorm]
**Priority**: Medium

---

## What's the Idea?

An AI-powered deck optimization tool for Magic: The Gathering Arena that takes a player's existing card collection and builds competitive decks from it. Uses statistical models from winning meta decks, win-rate data, and card synergy analysis to create the best possible decks from what you already own — bridging the gap between "fun jank" and "actually winning."

---

## What Problem Does It Solve?

**The Problem**:
Casual/mid-tier MTGA players build decks around fun concepts (token spam, shrine combos, etc.) but those decks underperform competitively. Building a competitive deck requires deep meta knowledge, tracking tournament results, understanding synergy math, and knowing which cards in your collection map to which archetypes. Most players don't have time or expertise for this.

**Who Experiences This Problem?**:
- Casual MTGA players who want to win more without netdecking blindly
- Players with large collections who don't know what competitive decks they can already build
- Players who want to minimize wildcard spending by maximizing their existing collection
- FTP (free-to-play) players who need to be strategic about crafting decisions

**How Acute Is the Pain?**:
- [x] Should-have (people want it but can work around)
- Players actively search for deck builders and meta trackers, but current tools don't solve the "what can I build with MY cards" problem well

---

## How Do People Solve It Today?

**Current Solutions**:
1. **Manual netdecking** - Browse MTGGoldfish/Moxfield/Untapped.gg for meta decks, manually check if you have the cards
2. **Tracker overlays** (Untapped.gg, MTGA Pro Tracker) - Track stats and show collection, but don't optimize decks
3. **Third-party deck builders** (Moxfield, Archidekt) - Build decks but no collection-aware optimization
4. **Arena's built-in suggest** - Very basic, not competitively optimized
5. **Reddit/Discord communities** - Ask for advice, get generic "craft Sheoldred" responses

**What's Inadequate About Current Solutions?**:
- No tool cross-references YOUR collection against statistical win-rate data
- Tracker tools show you data but don't prescribe action ("build this deck, you're 3 cards away")
- Deck builders assume you have every card — no collection-aware suggestions
- No tool quantifies "closest competitive deck you can build" or "best wildcard investment"

---

## Initial Viability Thoughts

**Why This Might Work**:
- Clear pain point with engaged user base (MTGA has millions of active players)
- Data is available: card databases (Scryfall API), meta data (MTGGoldfish, 17Lands), collection export exists
- AI/LLM synergy analysis is genuinely useful here — card interactions are complex
- Could start as a personal tool and validate with the community
- Existing tools leave the "collection-aware optimization" gap wide open
- MTG players are proven spenders (wildcards, gems, third-party tools)

**Why This Might Not Work**:
- Collection export from MTGA is clunky (log file parsing, requires login session)
- Meta shifts constantly (new sets every ~3 months) — requires ongoing data maintenance
- Wizards of the Coast could add this feature natively
- Competitive deck building is partially subjective (meta reads, play style preferences)
- Existing tools (Untapped.gg) have massive user bases and could add this feature
- MTG rules complexity makes automated synergy analysis genuinely hard

**Gut Feel** (before research):
- [x] Curious - worth exploring

---

## Questions to Answer

**Market Questions**:
- Does a collection-aware deck optimizer already exist?
- How big is the MTGA player base currently?
- What do existing MTG tools charge? (Untapped.gg premium, MTGA Pro, etc.)
- How do players currently export their collection?
- What meta data sources are available and accessible?
- Is 17Lands data open? MTGGoldfish API?

**Feasibility Questions**:
- Can collection data be reliably extracted from MTGA? (log parsing vs. API vs. overlay)
- What card databases exist? (Scryfall API is well-known)
- How would synergy scoring work? (co-occurrence in winning decks? card text analysis?)
- Can this be a CLI/local tool or does it need a web UI?
- How fast does the meta shift? How much maintenance is needed?
- Could an LLM (Claude) do the synergy analysis directly from card text?

**Personal Questions**:
- Am I the right person? (Yes - active MTGA player, software dev, direct user of the tool)
- Do I have relevant skills? (Yes - data analysis, API integration, AI/LLM experience)
- Am I excited to work on this? (Yes - would use it personally regardless)
- Unique advantage: building for myself first, dog-fooding immediately

---

## Technical Approach (Initial Thinking)

### Collection Export Options
1. **Player.log parsing** - Parse `%LOCALAPPDATA%Low/Wizards Of The Coast/MTGA/Player.log` after login. Collection appears as JSON blob from `PlayerInventory.GetPlayerCardsV3` response. Fragile but free.
2. **MTGA Pro Tracker / Untapped.gg export** - Use existing overlay tools that already parse the log and can export collection to text/CSV.
3. **Manual paste** - Player exports deck lists from Arena's deck builder (works per-deck, tedious for full collection).
4. **Build a lightweight log watcher** - Small script that tails the log file and extracts collection data on login.

### Data Sources for Meta Analysis
- **Scryfall API** - Complete card database with text, types, colors, sets (free, well-documented)
- **17Lands** - Draft and play data with win rates by card/archetype (limited format focused)
- **MTGGoldfish** - Tournament/meta deck lists with win rates
- **Untapped.gg** - Constructed win rate data (premium/API access unclear)
- **MTGA Zone / MTG Meta** - Community-curated tier lists

### Optimization Approach
1. Gather top meta decks with win rates (per format: Standard, Historic, Explorer)
2. Map user's collection against each meta deck
3. Score each deck by: (cards owned / cards needed) weighted by card importance
4. Rank "closest competitive decks" with specific craft recommendations
5. Bonus: synergy analysis for building around user's favorite cards competitively

---

## Personal Use Case (Immediate Value)

Even without building a product, the immediate workflow is:
1. Export collection from MTGA (log parse or tracker tool)
2. Paste into Claude with current meta deck lists
3. Get personalized deck recommendations based on what I own
4. Get wildcard priority recommendations

This can be done **right now** as a manual process, then potentially automated later.

---

## Dual-Track Opportunity

**Track 1: Personal Tool (Immediate)**
- Script to extract collection from Player.log
- Feed to Claude for deck building
- Use immediately, iterate based on results

**Track 2: Product Research (Parallel)**
- Research if this is a viable product/service
- Assess market, competition, monetization
- Decide go/no-go on building a proper tool

---

## Next Steps

- [ ] Look up competitors for this idea (collection-aware deck optimizers)
- [ ] Research MTGA collection export methods in detail
- [ ] Investigate available meta data APIs (Scryfall, 17Lands, MTGGoldfish)
- [ ] Test manual workflow: export collection → Claude → deck recommendations
- [ ] Research market size (MTGA player count, MTG tool market)
- [ ] Estimate build complexity for automated version

---

**Ready to Research?**
If this idea still feels worth exploring, proceed with: `"Look up competitors for MTG Arena deck optimizer"`

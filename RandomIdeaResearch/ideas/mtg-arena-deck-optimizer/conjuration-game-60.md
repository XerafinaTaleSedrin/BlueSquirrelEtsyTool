# Conjuration Game — Diamond Push Build (60 Cards)

**Format**: Historic
**Archetype**: Bant (G/W/U) Conjure & Blink
**Strategy**: Blink conjure creatures to flood your hand with random cards. Hold up 1-mana blink spells to PROTECT your creatures from removal — and get a free conjure when they come back. Distinguished Conjurer draws on every blink return, feeding Worldweave for even more conjures. Win through overwhelming card advantage or Omniscience + Ornate Imitations for massive chaos.

---

## What Changed (60-Card Tight Build)

The 70-card build had consistency problems — too many 1-ofs, pieces not connecting. This version:
- **60 cards**: Draw your engine pieces faster, every card matters
- **4x everything that matters**: Distinguished Conjurer x4, Cloudshift x4, Fear of Change x4, Emergent Haunting x4, Worldweave x4
- **6 protection blinks at 1 mana**: Cloudshift x4 + Essence Flux x2. Opponent tries to exile/destroy your creature? Blink it in response — creature saved, ETB re-triggers, you're ahead
- **Displacer Kitten**: Every noncreature spell = free blink. Cast Opt, Kitten blinks Fear of Change, conjure + draw + Worldweave. If you don't own it yet, Charming Prince fills the slot
- **Cut the dead weight**: No more Witching Well, Ichor Wellspring, Clay Bricks, One with the Multiverse, Enter the Infinite, Aetherflux. Those were sitting in hand while you died

---

## How to Not Die (Protection Guide)

This is the #1 thing to learn. Your blink spells are DEFENSIVE first, offensive second.

```
SCENARIO: Opponent casts removal on your Fear of Change
  YOU: Cast Cloudshift targeting Fear of Change (1 mana, instant)
  RESULT: Fear of Change exiles (dodges the removal), returns immediately
          -> Conjures a new random creature on re-entry
          -> Distinguished Conjurer draws you a card
          -> Worldweave conjures another random card
  YOU SPENT: 1 mana
  YOU GOT: Creature saved + 2-3 free cards
  OPPONENT SPENT: Their removal spell + their mana
  OPPONENT GOT: Nothing

RULE: Always hold up W or U when you have a blink spell in hand.
      Never tap out if you have creatures worth protecting.
```

| Threat | Answer |
|--------|--------|
| Targeted removal (destroy/exile) | Cloudshift / Essence Flux in response |
| Board wipe (Wrath of God) | Thassa survives (indestructible). Enchantments survive. Rebuild with conjured cards in hand |
| Counterspells on your key cards | Teferi makes your spells uncounterable. Dovin's Veto / Mystical Dispute counter back |
| Opponent going wide (aggro swarm) | Supreme Verdict — uncounterable board wipe |
| Planeswalker threats | Teferi bounces any nonland permanent |

---

## The Deck (60 cards)

### Creatures (16)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Fear of Change | GU | THE conjure card. Conjures a random creature on ETB. #1 blink target |
| 4x | Emergent Haunting | 1U | Second Fear of Change — always have a blink target available |
| 4x | Distinguished Conjurer | 1W | Draws a card whenever a creature enters from exile. THE glue piece — every blink = draw = Worldweave trigger |
| 1x | Oracle of the Alpha | 2U | ETB conjures a Power Nine card. Blink it = another Power Nine |
| 1x | Thassa, Deep-Dwelling | 3U | 6/5 indestructible. Blinks a creature every end step FOR FREE |
| 1x | Soulherder | 1WU | Blinks every end step like Thassa. Gets +1/+1 per exile. Grows into a finisher |
| 1x | Displacer Kitten | 3U | Every noncreature spell you cast = free blink. Turns every Opt/Cloudshift into double value. (If not owned: swap for Charming Prince) |

### Enchantments (6)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Worldweave | 2G | THE ENGINE. Every card you draw conjures a random card |
| 1x | Omniscience | 7UUU | Late-game finisher. Cast everything free. Ornate Imitations for X=20 |
| 1x | Sterling Grove | GW | All enchantments have shroud (protects Worldweave). Sac to tutor Omniscience or Worldweave |

### Planeswalkers (1)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Teferi, Time Raveler | 1WU | Bounces threats, draws, makes YOUR spells uncounterable |

### Instants (10)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Cloudshift | W | 1-MANA PROTECTION + BLINK. Save creature from removal AND re-trigger ETB. Always hold one up |
| 2x | Essence Flux | U | Same as Cloudshift but blue. 6 total blink spells = almost always have one |
| 2x | Opt | U | Scry 1, draw 1. Cheap Worldweave trigger. With Displacer Kitten: also a free blink |
| 1x | Dovin's Veto | WU | Uncounterable counter. Protects Omniscience or Worldweave from removal |
| 1x | Mystical Dispute | 2U | Cheap counter (1 mana vs blue spells) |

### Sorceries (3)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Supreme Verdict | 1WWU | Uncounterable board wipe. Your enchantments + Thassa (indestructible) survive |
| 1x | Ornate Imitations | XGU | Conjure X random cards. THE chaos card. With Omniscience, X = all your mana |
| 1x | Solve the Equation | 2U | Tutor any instant/sorcery. Finds Supreme Verdict, Ornate Imitations, or Cloudshift |

### Lands (24)

| Qty | Card | Notes |
|-----|------|-------|
| 4x | Fabled Passage | Fetch any basic, fixes colors |
| 4x | The World Tree | Fixes all colors at 6+ lands |
| 4x | Brokers Hideout | G/W/U fetch triland |
| 5x | Island | Primary color — blue blink + draw + conjure |
| 4x | Plains | Cloudshift, Distinguished Conjurer, Teferi, Supreme Verdict |
| 2x | Forest | Worldweave, Fear of Change |
| 1x | Hidden Cataract | Transforms into draw land late game |

---

## Mana Curve

```
1 CMC:  ████████ 8            Cloudshift x4, Essence Flux x2, Opt x2
2 CMC:  ██████████████████ 18 Fear x4, Emergent x4, Distinguished Conjurer x4,
                                    Dovin's Veto x1, Sterling Grove x1
                               (Deduce/Growth Spiral cut — blinks replaced them)
3 CMC:  ██████ 6              Worldweave x4, Oracle x1, Soulherder x1
                               (Teferi = 1WU = 3 CMC, Solve = 2U = 3 CMC)
       Recount:
3 CMC:  ████████ 8            Worldweave x4, Oracle x1, Soulherder x1, Teferi x1,
                                    Solve x1
4 CMC:  ████ 4                Thassa x1, Displacer Kitten x1, Supreme Verdict x1,
                                    Mystical Dispute x1
10 CMC: █ 1                   Omniscience x1
X CMC:  █ 1                   Ornate Imitations (scales with mana)
```

24 lands, 26 cards at 1-2 CMC. You always have a play turns 1-3. Hold up 1 mana for blink protection whenever possible.

---

## How It Plays

### Early Game (Turns 1-3) — SURVIVE AND SET UP
- **Turn 1**: Land, pass. Hold up W/U if you have a blink spell (you probably won't need it yet, but the habit matters)
- **Turn 2**: Fear of Change or Emergent Haunting (conjure immediately). Or Distinguished Conjurer if you already have a conjure creature to blink next turn. **Leave 1 mana open if possible**
- **Turn 3**: Worldweave if you have it — NOW every draw conjures. Or Soulherder (blinks every end step). Or Teferi to bounce their best threat

### Mid Game (Turns 4-6) — BLINK ENGINE ONLINE
- **Thassa / Soulherder / Displacer Kitten** — any one of these makes the engine automatic
- **The value chain**: End step blink Fear of Change -> conjure creature -> Conjurer draws -> Worldweave conjures another -> 3 cards per turn for FREE
- **Hold blink spells for defense** until you have a repeatable blinker (Thassa/Soulherder). Then use them offensively
- **Supreme Verdict** if you're behind on board — your enchantments + Thassa survive

### Late Game (Turn 7+) — CLOSE IT OUT
- **Option A**: Blink value has buried them in random creatures. Attack with your army of conjured stuff
- **Option B**: Omniscience (Sterling Grove tutors it) -> Ornate Imitations for X = everything -> conjure 20 random cards -> cast them all free
- **Option C**: Solve the Equation finds whatever you need to close

### Key Play Patterns
```
DEFENSIVE BLINK (most important play in the deck):
  Opponent targets your creature -> Cloudshift in response
  = Creature saved + ETB re-triggers + you're up cards

OFFENSIVE BLINK (when you have the engine running):
  Your turn: Cast Opt -> Displacer Kitten blinks Fear of Change
  = Opt draws (Worldweave trigger) + conjure creature (Conjurer draws)
  = 1 mana, 3-4 cards generated

END STEP VALUE (every turn once Thassa/Soulherder is out):
  Their end step: Thassa blinks Fear of Change automatically
  = Conjure + Conjurer draw + Worldweave conjure
  = Free cards every single turn, no mana spent
```

---

## Toolbox: Finding What You Need

| Need | Find it with |
|------|-------------|
| Omniscience (finisher) | Sterling Grove (sac to tutor) |
| Worldweave (engine) | Sterling Grove (sac to tutor) |
| Supreme Verdict (survival) | Solve the Equation |
| Ornate Imitations (chaos) | Solve the Equation |
| Cloudshift (protection) | Solve the Equation (it's an instant!) |

---

## Synergy Map

```
THE BLINK LOOP (the deck's core engine):

  Cloudshift / Essence Flux (1 mana) --> exile your creature, it returns
       |
       +---> Fear of Change returns --> CONJURE a creature
       |
       +---> Distinguished Conjurer sees creature enter from exile --> DRAW
       |         |
       |         +---> Worldweave sees a draw --> CONJURE another random card
       |
       +---> Soulherder sees something exiled --> gets +1/+1 counter

  RESULT: 1 mana = conjure + draw + Worldweave conjure = 3 CARDS

Displacer Kitten --> every noncreature spell = FREE blink
    +---> Cast Opt --> Kitten blinks Fear of Change --> conjure + draw
    +---> Cast Cloudshift --> creature blinks --> Kitten blinks ANOTHER creature
    +---> With Omniscience, every free spell chains more blinks

Thassa / Soulherder --> blink a creature every end step FOR FREE
    +---> Same loop as above but automatic, every single turn
    +---> Blink Oracle of the Alpha = Power Nine EVERY TURN

Sterling Grove --> shroud on Worldweave + Omniscience
    +---> sacrifice to tutor either one

Teferi --> bounces threats + YOUR SPELLS CAN'T BE COUNTERED
    +---> safely resolve Omniscience or Worldweave

Cloudshift ALSO --> saves creatures from removal (blink in response)
    +---> defensive AND offensive -- never a dead card
```

---

## Matchups

| Matchup | Your Plan |
|---------|-----------|
| **Aggro** | Hold up blink spells, block with conjured creatures, Supreme Verdict if desperate. Thassa is indestructible blocker |
| **Control** | Teferi = uncounterable. Dovin's Veto protects key spells. Cloudshift dodges targeted removal. Blink engine out-values them |
| **Midrange** | Blink engine generates 3 cards/turn for 1 mana. No fair deck can keep up |
| **Combo** | Mystical Dispute + Dovin's Veto to disrupt. Race with blink value. Supreme Verdict if they go creature-based |

---

## Mulligan Guide

**Keep**: 2-3 lands (need W and U/G) + conjure creature + blink spell or Worldweave
**Dream hand**: Plains + Island + Fear of Change + Cloudshift + Distinguished Conjurer = protection online turn 2, blink value turn 3
**Also great**: Any 2 lands + Emergent Haunting + Cloudshift = creature turn 2 with protection backup
**Sterling Grove** + 2 lands = tutor for whatever you need
**Mulligan**: No white/blue source, all big spells, no creatures, 5+ lands

---

## Arena Import

```
4 Fear of Change
4 Emergent Haunting
4 Distinguished Conjurer
1 Oracle of the Alpha
1 Thassa, Deep-Dwelling
1 Soulherder
1 Displacer Kitten
1 Teferi, Time Raveler
4 Worldweave
1 Omniscience
1 Sterling Grove
4 Cloudshift
2 Essence Flux
2 Opt
1 Dovin's Veto
1 Mystical Dispute
1 Supreme Verdict
1 Solve the Equation
1 Ornate Imitations
4 Fabled Passage
4 The World Tree
4 Brokers Hideout
5 Island
4 Plains
2 Forest
1 Hidden Cataract
```

**Total: 60 cards** (36 spells + 24 lands)

---

## If You Don't Have Displacer Kitten

Swap `1 Displacer Kitten` for `1 Charming Prince`. Prince is weaker but still blinks creatures on ETB and is already in your collection. Craft the Kitten when you get a rare wildcard — it's the single best upgrade for this deck.

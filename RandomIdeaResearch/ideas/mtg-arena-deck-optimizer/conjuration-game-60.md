# Conjuration Game — Diamond Push Build (60 Cards)

**Format**: Historic
**Archetype**: Bant (G/W/U) Conjure & Combo
**Strategy**: Draw cards to fuel Worldweave conjures, protect your engine with counters and board wipes, ramp to Omniscience, then cast Enter the Infinite to draw your entire deck — every draw conjures a random card via Worldweave — and Aetherflux Reservoir lasers them for 50. Deterministic combo kill instead of hoping the chaos works.

---

## What Changed (Diamond Upgrade)

The old build had a clue/artifact subtheme (Novice Inspector, Forensic Gadgeteer, Thoughtcast) that was too slow and fragile for Diamond. This version replaces that with:
- **Interaction**: Supreme Verdict, Teferi, Dovin's Veto, Mystical Dispute — you survive aggro and protect your combo
- **Better draw**: Brainstorm (3 Worldweave triggers for 1 mana), Growth Spiral (ramp + draw)
- **Deterministic win**: Enter the Infinite + Omniscience = draw entire deck, not "hope for good conjures"
- **Engine protection**: Sterling Grove gives Worldweave/Omniscience shroud, or sac to tutor either one
- **Mana doubling**: Wilderness Reclamation untaps lands on end step — cast interaction on their turn, develop on yours

---

## The Deck (60 cards)

### Creatures (6)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Fear of Change | GU | THE conjure card. Conjures a random creature on ETB. Blocks early, generates value |
| 2x | Alaundo the Seer | 2GU | Suspend cards from hand, cast them free over time. Backup Omniscience that starts working immediately |

### Enchantments (10)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Worldweave | 2G | THE ENGINE. Every card you draw conjures a random card that shares a type. Brainstorm = 3 conjures for 1 mana |
| 2x | Omniscience | 7UUU | Cast everything free. With Worldweave + Enter the Infinite = deterministic combo kill |
| 1x | One with the Multiverse | 6UU | Play cards off the top free. Backup Omniscience, 2 mana cheaper |
| 1x | Wilderness Reclamation | 3G | Untaps ALL your lands on end step. Double your mana every turn. Cast Deduce/Brainstorm on their turn, still have mana on yours |
| 1x | Sterling Grove | GW | All your enchantments have shroud — Worldweave, Omniscience, Wilderness Rec can't be targeted. Sac to tutor any enchantment (find Omniscience or Worldweave on demand) |
| 1x | Shark Typhoon | 5U | Cycle for XU: draw a card (Worldweave trigger) + create X/X flying shark. Or hardcast as enchantment for free off Omniscience |

### Artifacts (5)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Clay-Fired Bricks | 1W | Transforms into a land — ramp toward Omniscience. Cheap early play |
| 1x | Aetherflux Reservoir | 4 | WIN CONDITION. Cast 10+ spells with Omniscience, gain 50+ life, laser opponent for 50 |

### Planeswalkers (2)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Teferi, Time Raveler | 1WU | Bounces any threat, draws a card, makes YOUR spells uncounterable. Protects your Omniscience turn — they can't counter it |
| 1x | Narset, Parter of Veils | 1UU | Look at top 4, take a noncreature spell (finds Omniscience, Enter the Infinite, Supreme Verdict). ALSO: opponents can't draw more than 1 card per turn — shuts down their card advantage |

### Instants (8)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Brainstorm | U | Draw 3, put back 2. With Worldweave out = 3 conjured cards for 1 mana. Best cantrip in Historic |
| 1x | Growth Spiral | GU | Instant speed ramp + draw. Triggers Worldweave AND gets you closer to Omniscience |
| 3x | Deduce | 1U | Draw + make a Clue. Triggers Worldweave on draw, clue is another future draw |
| 1x | Dovin's Veto | WU | Uncounterable counter for noncreature spells. Protects Omniscience from removal/counters |
| 1x | Mystical Dispute | 2U | Counter any spell (1 mana vs blue spells). Cheap protection early |
| 1x | Supreme Verdict | 1WWU | Uncounterable board wipe. Keeps you alive against aggro. Your enchantments survive |

### Sorceries (5)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | They Went This Way | 2G | Make 2 Clue tokens = 2 future Worldweave triggers. With Wilderness Rec, crack them on opponent's end step |
| 1x | Solve the Equation | 2U | Tutor ANY instant or sorcery. Find Enter the Infinite (combo), Supreme Verdict (survival), or Brainstorm (draw) |
| 1x | Ornate Imitations | XGU | Conjure X random cards. With Omniscience, X = all your mana = absurd |
| 1x | Enter the Infinite | 8UUUU | With Omniscience: draw your ENTIRE deck. Every draw triggers Worldweave. Cast everything for free. Aetherflux kills. Game over |

### Lands (24)

| Qty | Card | Notes |
|-----|------|-------|
| 4x | Fabled Passage | Fetch any basic, fixes colors |
| 4x | The World Tree | Fixes all colors at 6+ lands |
| 4x | Brokers Hideout | G/W/U fetch triland |
| 5x | Island | Primary color |
| 3x | Forest | Worldweave, Growth Spiral, Fear of Change |
| 3x | Plains | Supreme Verdict WW, Teferi, Sterling Grove, Clay Bricks |
| 1x | Hidden Cataract | Transforms into draw land late game |

---

## Mana Curve

```
1 CMC: ███ 3           (Brainstorm, Dovin's Veto... effective 1-mana plays)
2 CMC: █████████ 9     (Fear of Change x4, Deduce x3, Growth Spiral, Clay Bricks counted at 2)
        Actually:
1 CMC: ██ 2            (Brainstorm x1, Clay-Fired Bricks... Bricks are 1W = 2 CMC)
2 CMC: ████████████ 12 (Fear of Change x4, Deduce x3, Clay Bricks x4, Dovin's Veto x1)
3 CMC: ████████████ 12 (Worldweave x4, They Went This Way x2, Teferi x1, Narset x1,
                         Mystical Dispute x1, Solve the Equation x1, Sterling Grove x1,
                         Growth Spiral... GS is 2 CMC)
        Recount:
2 CMC: █████████████ 13 (Fear x4, Deduce x3, Bricks x4, Dovin's Veto x1, Growth Spiral x1)
3 CMC: ██████████ 10    (Worldweave x4, They Went x2, Teferi x1, Narset x1,
                          Solve x1, Sterling Grove x1... wait, Sterling is 2 CMC)
2 CMC: ██████████████ 14 (Fear x4, Deduce x3, Bricks x4, Dovin's Veto x1,
                           Growth Spiral x1, Sterling Grove x1)
3 CMC: ████████ 8        (Worldweave x4, They Went x2, Solve x1, Mystical Dispute x1)
4 CMC: █████ 5           (Alaundo x2, Wilderness Rec x1, Aetherflux x1, Supreme Verdict x1)
5+ CMC: █████ 5          (Omniscience x2, One with Multiverse x1, Enter the Infinite x1,
                           Shark Typhoon x1... Ornate Imitations is X)
```

24 lands with Clay-Fired Bricks ramp + Growth Spiral = consistently hitting 7-10 mana by turn 6-8.

---

## How It Plays

### Early Game (Turns 1-3)
- **Turn 1**: Land, pass. Or Brainstorm on their end step if Worldweave isn't out yet (still finds pieces)
- **Turn 2**: Fear of Change (conjure a creature) or Clay-Fired Bricks (ramp) or Sterling Grove (protect everything you play after)
- **Turn 3**: Worldweave — NOW every card draw conjures something. Or Teferi to bounce their best threat + draw

### Mid Game (Turns 4-6)
- **Wilderness Reclamation** doubles your mana — cast Deduce/Brainstorm on their end step, still have full mana on your turn
- **Narset** digs 4 deep for Omniscience or Enter the Infinite, while shutting down their card draw
- **Supreme Verdict** if aggro is swarming — uncounterable, your enchantments survive
- **Alaundo** starts suspending expensive cards for future free casts
- Crack clues on opponent's end step (Wilderness Rec untaps your mana)

### Late Game (Turn 7+)
- **Teferi on board = your spells can't be countered** → safely resolve Omniscience
- **Omniscience → Enter the Infinite** → draw your entire deck
- Every draw triggers Worldweave → conjure your whole library worth of random cards
- Cast everything for free → Aetherflux Reservoir counts spells → gain 50+ life → **laser for 50**
- If no Enter the Infinite: Solve the Equation finds it. If no Omniscience: Sterling Grove tutors it

### The Combo Kill
```
Board: Omniscience + Worldweave + Aetherflux Reservoir

1. Cast Enter the Infinite for free (draw entire deck)
   → Every card drawn triggers Worldweave
   → 30+ cards drawn = 30+ conjured random cards added to hand
2. Cast every card in hand for free (Omniscience)
   → Each spell triggers Aetherflux: +1, +2, +3... +10 = 55 life gained by spell 10
3. Pay 50 life → Aetherflux deals 50 damage
4. They're dead. Deterministic. No luck needed.

Backup: even without Enter the Infinite, Worldweave + Omniscience
chains free spells → conjures → free spells → eventually hits critical mass
```

---

## Toolbox: Finding What You Need

This build has powerful 1-ofs connected by tutors:

| Need | Find it with |
|------|-------------|
| Omniscience (combo) | Sterling Grove (sac to tutor), Narset (dig 4) |
| Enter the Infinite (win) | Solve the Equation (tutor instant/sorcery) |
| Supreme Verdict (survival) | Solve the Equation |
| Worldweave (engine) | Sterling Grove (sac to tutor), Narset (dig 4) |
| Any answer | Brainstorm (dig 3), Deduce (draw + clue), Narset (dig 4) |

---

## Synergy Map

```
Worldweave ──→ every card draw conjures a random card
    ↑               ↑               ↑                ↑
Brainstorm      Deduce          Growth Spiral    Crack Clues
(draw 3 = 3     (draw + clue)   (draw + ramp)    (Wilderness Rec
 conjures!)                                       untaps mana to crack)

Sterling Grove ──→ shroud on Worldweave + Omniscience + Wilderness Rec
    │                (opponents can't target ANY of your enchantments)
    └──→ sacrifice to tutor Omniscience or Worldweave

Teferi ──→ bounces threats + draws + YOUR SPELLS CAN'T BE COUNTERED
    └──→ safely resolve Omniscience without fear of countermagic

Wilderness Reclamation ──→ untap ALL lands on end step
    └──→ cast Brainstorm/Deduce on their turn + still have mana on yours
    └──→ effectively DOUBLES your mana every turn

Omniscience ──→ cast everything free
    + Enter the Infinite ──→ draw entire deck ──→ 30+ Worldweave triggers
    + Aetherflux Reservoir ──→ count spells ──→ gain 50+ life ──→ 50 DAMAGE LASER

Narset ──→ dig for combo pieces + SHUTS DOWN opponent card draw
    └──→ they draw 1 per turn max while you're drawing 5+
```

---

## Matchup Improvements (vs Old Build)

| Matchup | Old Build | Diamond Build |
|---------|-----------|---------------|
| **Aggro** | Die before Omniscience | Supreme Verdict wipes board, Teferi bounces, Fear of Change blocks |
| **Control** | They counter Omniscience, you lose | Teferi = uncounterable spells, Dovin's Veto protects combo, Sterling Grove = shroud on engine |
| **Midrange** | Race them poorly | Wilderness Rec doubles mana, Narset shuts down their draw, you combo faster |
| **Combo** | No interaction, just hope | Mystical Dispute + Dovin's Veto disrupt them, Supreme Verdict clears creatures |

---

## Mulligan Guide

**Keep**: 2-3 lands (must include blue or green source) + Worldweave or draw spell + any interaction
**Great keeps**: Forest/Island + Worldweave + Deduce = engine online turn 3, drawing cards turn 2
**Also great**: Sterling Grove + any lands = tutor for whatever you need
**Mulligan**: No blue or green source, all big spells, 5+ lands

---

## Arena Import

```
4 Fear of Change
2 Alaundo the Seer
1 Teferi, Time Raveler
1 Narset, Parter of Veils
4 Worldweave
2 Omniscience
1 One with the Multiverse
1 Wilderness Reclamation
1 Sterling Grove
1 Shark Typhoon
4 Clay-Fired Bricks
1 Aetherflux Reservoir
1 Brainstorm
1 Growth Spiral
3 Deduce
1 Dovin's Veto
1 Mystical Dispute
1 Supreme Verdict
2 They Went This Way
1 Solve the Equation
1 Ornate Imitations
1 Enter the Infinite
4 Fabled Passage
4 The World Tree
4 Brokers Hideout
5 Island
3 Forest
3 Plains
1 Hidden Cataract
```

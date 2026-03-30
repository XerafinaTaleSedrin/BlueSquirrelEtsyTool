# Thopterist Engine — Bant Worldweave 60

**Format**: Historic
**Archetype**: Bant (W/U/G) Conjure Engine
**Strategy**: Emporium Thopterist conjures a free Ornithopter to your hand every upkeep. Worldweave turns each conjure into additional random cards. The Ornithopters cost 0 to cast and become 2/2 fliers (or bigger with multiple Thopterists). Blink package protects key pieces and re-triggers Fear of Change for extra conjures. Win by Thopter beatdown or Omniscience + Ornate Imitations for massive conjure payoff.

**Built from**: Your collection (all cards owned)

---

## The Engine

```
EVERY UPKEEP (automatic, no mana):
  Emporium Thopterist → conjures Ornithopter into your hand
       |
       +→ Worldweave sees conjure → conjures ANOTHER random card
       |
       +→ Cast Ornithopter for FREE (0 mana) → 2/2 flier (Thopterist +2/+0)
       |
       +→ With 2 Thopterists: 2 Ornithopters/turn, each is 4/2 flier (+2/+0 stacks)

BLINK BONUS (when you blink Fear of Change):
  Cloudshift on Fear of Change → conjures random creature on re-entry
       |
       +→ Distinguished Conjurer draws a card (creature entered from exile)
       |
       +→ Worldweave sees the draw/conjure → conjures another card
       |
       RESULT: 1 mana = creature saved + 2-3 free cards

ENDGAME:
  Sterling Grove → sac to tutor Omniscience
  Omniscience → cast everything free
  Ornate Imitations for X = 15+ → conjure 15 random cards → cast them all free
```

---

## The Deck (60 cards)

### Creatures (16)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Emporium Thopterist | 1U | **THE ENGINE.** Conjures Ornithopter each upkeep. Thopters get +2/+0. Multiple copies stack — 2 Thopterists = 2 Ornithopters/turn, each gets +4/+0 |
| 4x | Fear of Change | GU | Conjures a random creature on ETB. #1 blink target — every blink = another conjure |
| 4x | Distinguished Conjurer | 1W | Draws a card whenever a creature enters from exile. Every blink = draw = potential Worldweave trigger |
| 2x | Emergent Haunting | 1U | Second conjure creature. Backup blink target when Fear of Change isn't available |
| 1x | Thassa, Deep-Dwelling | 3U | 6/5 indestructible. Blinks a creature every end step for FREE. Set-and-forget engine piece |
| 1x | Displacer Kitten | 3U | Every noncreature spell = free blink. Cast Opt → Kitten blinks Fear of Change → conjure + draw. Cast Ornithopter (artifact, not creature spell for this purpose — NOTE: Ornithopter IS a creature, so Kitten won't trigger. But your instants/sorceries still chain) |

### Enchantments (6)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Worldweave | 2G | **THE AMPLIFIER.** Every conjure generates another conjure. Turns Emporium Thopterist's single Ornithopter into 2+ cards per turn |
| 1x | Omniscience | 7UUU | Cast everything free. Ornate Imitations for X = all your mana. The finisher |
| 1x | Sterling Grove | GW | All enchantments have shroud (protects Worldweave + Omniscience). Sacrifice to tutor either one |

### Instants (10)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Cloudshift | W | 1-mana protection + blink. Save any creature from removal AND re-trigger its ETB. Always hold one up |
| 2x | Essence Flux | U | Same as Cloudshift in blue. 6 total protection blinks |
| 2x | Opt | U | Scry 1, draw 1. Cheap Worldweave trigger. With Displacer Kitten = also a free blink |
| 1x | Dovin's Veto | WU | Uncounterable counter. Protects Omniscience or Worldweave resolution |
| 1x | Growth Spiral | GU | Instant-speed ramp + draw. Accelerates to Worldweave on turn 2, triggers Worldweave if it's already out |

### Sorceries (2)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Ornate Imitations | XGU | **THE PAYOFF.** Conjure random creatures at each MV from 1 to X directly onto the battlefield. With Omniscience, X = all your mana. Does NOT trigger Worldweave (conjured, not cast), but still floods the board with random creatures |
| 1x | Solve the Equation | 2U | Tutor any instant/sorcery. Finds Ornate Imitations to close, or Cloudshift/Growth Spiral in a pinch |

### Planeswalkers (1)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Teferi, Time Raveler | 1WU | Your spells can't be countered (protects Omniscience resolution). Bounces threats. Draws a card |

### Board Control (1)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Supreme Verdict | 1WWU | Uncounterable board wipe. Your enchantments + Thassa (indestructible) survive. Emergency reset |

### Lands (24)

| Qty | Card | Notes |
|-----|------|-------|
| 4x | Brokers Hideout | G/W/U fetch — fixes all three colors |
| 4x | Fabled Passage | Fetch any basic |
| 4x | The World Tree | Taps for G; at 6+ lands taps for any color |
| 5x | Island | Primary color — Thopterist, blinks, draw, counters |
| 4x | Plains | Cloudshift, Distinguished Conjurer, Teferi |
| 2x | Forest | Worldweave, Fear of Change, Growth Spiral |
| 1x | Hidden Cataract | Transforms into draw land late game |

---

## Mana Curve

```
0 CMC:  ∞              Ornithopter tokens (conjured free, cast free)
1 CMC:  ██████████ 10   Cloudshift x4, Essence Flux x2, Opt x2,
                         Dovin's Veto x1, Growth Spiral x1
2 CMC:  ██████████████ 14  Emporium Thopterist x4, Fear of Change x4,
                            Distinguished Conjurer x4, Emergent Haunting x2
3 CMC:  ████████ 8      Worldweave x4, Teferi x1, Solve x1,
                         Displacer Kitten x1, Supreme Verdict x1
4 CMC:  █ 1             Thassa, Deep-Dwelling
10 CMC: █ 1             Omniscience (cheated via Sterling Grove tutor)
X CMC:  █ 1             Ornate Imitations (scales)

Lands: 24
```

24 one-and-two-drops means you always have plays early. The deck curves perfectly into Worldweave on turn 3 with Thopterist already generating value.

---

## How It Plays

### Turn 1: Land, pass
Hold up W or U if you drew a blink spell (habit — you won't need it yet).

### Turn 2: Emporium Thopterist or Fear of Change
- **Thopterist**: Starts conjuring Ornithopters next upkeep. If you have Worldweave in hand, this is the play — you want the passive engine online first
- **Fear of Change**: Immediate conjure on entry. Better if you have blink spells to chain value
- **Distinguished Conjurer**: If you have both a conjure creature and a blink spell for next turn

### Turn 3: Worldweave
NOW the engine is online. Every Ornithopter conjured by Thopterist triggers Worldweave for a bonus card. Every blink on Fear of Change generates multiple cards. You're pulling ahead every turn with zero mana investment.

### Turns 4-5: Thopter Army + Protection
- Cast your free Ornithopters — they're 2/2 fliers with Thopterist's buff
- Hold up Cloudshift to protect Thopterist or Fear of Change from removal
- Drop Thassa or Displacer Kitten for automatic blink value every turn
- Your hand should be overflowing with conjured cards

### Turns 6+: Close the Game
- **Path A — Thopter Beatdown**: 2-3 Ornithopters per turn, each a 2/2+ flier. They pile up fast. Swing in the air while holding up blink protection
- **Path B — Omniscience Finish**: Sterling Grove tutors Omniscience. Cast it (or cheat it with enough mana from ramping). Ornate Imitations for X = everything. Conjure 15+ random cards. Cast them all free. Game over
- **Path C — Grind**: Thopterist + Worldweave generates 2+ free cards per turn. No fair deck can keep up with that card advantage

### The Dream Sequence
```
Board: Emporium Thopterist + Worldweave + Omniscience

Upkeep: Thopterist conjures Ornithopter → Worldweave conjures random card
Main:   Cast Ornithopter (free) → 2/2 flier
        Cast Ornate Imitations, X=10 (free via Omniscience)
        → conjure 10 random cards
        → Worldweave triggers 10 times → 10 MORE random cards
        → Cast everything free via Omniscience
        → Swing with army of random creatures + Thopters
```

---

## Key Play Patterns

```
PASSIVE VALUE (every single turn, no mana):
  Your upkeep → Thopterist conjures Ornithopter
  → Worldweave conjures another card
  → Cast Ornithopter for 0 mana (2/2 flier)
  = 2 free cards + a creature, EVERY TURN

DEFENSIVE BLINK (most important reactive play):
  Opponent targets Thopterist/Fear of Change → Cloudshift in response
  = Creature saved + ETB re-triggers + you're up cards
  NEVER tap out if you have a creature worth protecting

OFFENSIVE CHAIN (when engine is rolling):
  Cast Opt → draw (Worldweave trigger) + Kitten blinks Fear of Change
  → Fear of Change conjures creature (Worldweave trigger)
  → Distinguished Conjurer draws (Worldweave trigger)
  = 1 mana, 4-5 cards generated

THASSA LOOP (automatic every end step):
  Thassa blinks Fear of Change → conjure + Conjurer draw + Worldweave
  = Free cards every turn, no mana spent, can't be interacted with easily
```

---

## Synergy Map

```
EMPORIUM THOPTERIST (the new core)
  │
  ├─→ Conjures Ornithopter each upkeep (FREE, AUTOMATIC)
  │     ├─→ Worldweave sees conjure → conjures another random card
  │     ├─→ Ornithopter costs 0 to cast → 2/2 flier with Thopterist buff
  │     └─→ Multiple Thopterists = multiple Ornithopters + stacking buffs
  │
  ├─→ Thopters get +2/+0 (ALL Thopters, including conjured Ornithopters)
  │     └─→ Ornithopter: 0/2 base → 2/2 with 1 Thopterist → 4/2 with 2
  │
  └─→ ITSELF is a blink target (re-entering doesn't re-conjure, but
       saves it from removal which is what matters)

WORLDWEAVE (the amplifier)
  │
  ├─→ Every conjure → another conjure (snowball effect)
  ├─→ Thopterist upkeep conjure → bonus card
  ├─→ Fear of Change blink conjure → bonus card
  ├─→ Ornate Imitations conjure X → X bonus cards (DOUBLES the payoff)
  └─→ Sterling Grove protects it + tutors Omniscience

BLINK PACKAGE (protection that generates value)
  │
  ├─→ Cloudshift / Essence Flux: save creatures from removal
  │     └─→ Fear of Change re-enters → conjure → Worldweave
  │     └─→ Distinguished Conjurer draws → Worldweave
  ├─→ Thassa: free blink every end step
  ├─→ Displacer Kitten: every noncreature spell = free blink
  └─→ Teferi: uncounterable spells + bounce utility

FINISHER PACKAGE
  │
  ├─→ Sterling Grove → sac to tutor Omniscience
  ├─→ Omniscience → cast everything free
  ├─→ Ornate Imitations X=15+ → conjure 15 creatures onto board (no Worldweave trigger)
  └─→ Solve the Equation → finds Ornate Imitations
```

---

## What Changed vs. Conjuration Game

| Old (Conjuration Game 60) | New (Thopterist Engine 60) |
|---|---|
| Blink-focused — needed creatures + blink spells in hand to generate value | **Passive engine** — Emporium Thopterist conjures every upkeep with NO mana |
| No board presence until blink chain started | **Thopter army** — free 2/2 fliers pile up while you build toward combo |
| 4x Emergent Haunting (backup conjure) | 2x Emergent Haunting (less needed — Thopterist is primary engine) |
| No aggressive plan | **Dual win condition** — Thopter beatdown OR Omniscience + Ornate |
| Oracle of the Alpha (fun but inconsistent) | Cut — Thopterist is more reliable and cheaper |
| Soulherder (grows but slow) | Cut — Thopterist provides enough passive value |
| Mystical Dispute (narrow counter) | Growth Spiral (ramp + draw, accelerates Worldweave) |
| Relied entirely on combo finish | Can win through combat damage alone with Thopter swarm |

---

## Matchups

| Matchup | Plan |
|---------|------|
| **Aggro** | Ornithopters block early. Cloudshift saves your Thopterist from burn. Thopter army stabilizes the board quickly. Supreme Verdict if desperate |
| **Control** | Teferi = uncounterable spells. Thopterist provides value they can't counter (upkeep trigger). Hold Dovin's Veto for their answer to Worldweave. Grind them out |
| **Midrange** | They play 1 card per turn, you generate 2-3 free. Thopter evasion goes over their ground creatures. Sterling Grove protects your engine |
| **Combo** | Race them. Your passive engine needs no setup beyond Thopterist + Worldweave. Dovin's Veto / Teferi to disrupt their key turn |

---

## Mulligan Guide

**Keep**: 2-3 lands (need U + one other) + Emporium Thopterist + any support
**Dream hand**: Island + Forest/Brokers + Emporium Thopterist + Worldweave + Cloudshift = engine online turn 3 with protection

**Also keep**:
- Thopterist + Fear of Change + lands = double engine
- Worldweave + Fear of Change + blink spell + lands = value from turn 2
- Sterling Grove + 2-3 lands = tutor whatever you need

**Mulligan**: No blue source, all expensive cards, no engine pieces (Thopterist/Fear of Change/Worldweave)

---

## Arena Import

```
4 Emporium Thopterist
4 Fear of Change
4 Distinguished Conjurer
2 Emergent Haunting
1 Thassa, Deep-Dwelling
1 Displacer Kitten
4 Worldweave
1 Omniscience
1 Sterling Grove
4 Cloudshift
2 Essence Flux
2 Opt
1 Dovin's Veto
1 Growth Spiral
1 Teferi, Time Raveler
1 Ornate Imitations
1 Solve the Equation
1 Supreme Verdict
4 Brokers Hideout
4 Fabled Passage
4 The World Tree
5 Island
4 Plains
2 Forest
1 Hidden Cataract
```

**Total: 60 cards** (36 spells + 24 lands)
**Wildcards needed**: None (Emporium Thopterist x4 owned per user, all other cards in collection)

---

## Upgrade Priorities (if you get wildcards)

1. **Shark Typhoon** (Rare) — Cycle for draw (Worldweave trigger) + flying Shark token. Great at every stage of the game
2. **2nd Omniscience** — You own 2. Running 1 currently for consistency, but 2nd copy means you don't auto-lose if the first gets countered
3. **Charming Prince** — Backup for Displacer Kitten if you want more creature-based blinks

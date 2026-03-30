# Maximum Conjure — Bant Chaos Engine (Historic Bo1)

**Format:** Historic | **Cards:** 61 | **Colors:** WUG
**Archetype:** Bant Conjure / Spellbook / Maximum Randomness
**Status:** Built from confirmed collection — zero wildcards needed

## Why This Deck

Nothing you cast is a card you put in the deck. Every single piece conjures, seeks, or generates random cards. You're playing a different deck every single game. This is the Thopterist Worldweave shell cranked to maximum chaos — every slot either conjures something random or enables more conjures.

## The Engine

```
PASSIVE CONJURE (every turn, no mana):
  Emporium Thopterist → conjures Ornithopter each upkeep
  → Worldweave sees conjure → conjures ANOTHER random card
  → Cast Ornithopter for 0 → 2/2 flier
  = 2 free random cards + a creature, EVERY TURN

SPELLBOOK CONJURES (ETB triggers):
  Spellbook Vendor → conjures from its spellbook on ETB
  Clever Conjurer → conjures random creatures
  Oracle of the Alpha → seeds Power Nine into library
  Fear of Change → exiles creature, conjures random one at MV+2
  Emergent Haunting → conjure creature on ETB

BLINK = MULTIPLY:
  Cloudshift / Essence Flux / Getaway Glamer on any conjure creature
  → Re-triggers ETB → more conjures → Worldweave amplifies each one
  Thassa → free blink every end step (automatic chaos generator)
  Displacer Kitten → every noncreature spell = free blink

AETHERFLUX FINISHER:
  All the free spells (Ornithopters + conjured stuff) gain life
  Aetherflux Reservoir: each spell gains increasing life
  → At 50+ life: pay 50 life, deal 50 damage. Laser beam finish.
```

## Decklist

### Conjure Creatures (18)

```
4 Emporium Thopterist        (1U)   — conjures Ornithopter each upkeep. Thopters get +2/+0
4 Fear of Change              (GU)   — ETB: exile creature, conjure random creature at MV+2
4 Distinguished Conjurer      (1W)   — draws card on creature ETB from exile. Blink payoff
3 Spellbook Vendor            (1W)   — ETB: conjure a card from its spellbook
2 Clever Conjurer             (2U)   — conjures random creatures
2 Emergent Haunting           (1U)   — conjure creature on ETB
1 Oracle of the Alpha         (2U)   — ETB: shuffles Power Nine into your library
```

### Blink Package (9)

```
4 Cloudshift                  (W)    — instant blink. Re-triggers all ETBs
2 Essence Flux                (U)    — instant blink in blue
2 Getaway Glamer              (W)    — instant blink, additional flexibility
1 Displacer Kitten            (3U)   — every noncreature spell = free blink
```

### Engine Pieces (6)

```
4 Worldweave                  (2G)   — every conjure/ETB → conjure another random card
1 Thassa, Deep-Dwelling       (3U)   — indestructible 6/5. Free blink every end step
1 Aetherflux Reservoir        (4)    — each spell = increasing life gain. Pay 50 life = 50 damage
```

### Spellbook Artifacts (1)

```
1 Tome of the Infinite        (2U)   — tap: conjure random spell from its curated spellbook
```

### Finisher (1)

```
1 Ornate Imitations           (XGU)  — conjure a random creature at each MV from 1 to X onto battlefield. Does NOT trigger Worldweave (conjured, not cast)
```

### Captive Weird (3)

```
3 Captive Weird               (U)    — 1-drop creature, cheap Worldweave trigger, transforms later
```

### Lands (23)

```
4 Brokers Hideout                    — Bant triland, fixes all three colors
4 The World Tree                     — fixes all colors at 6+ lands
4 Fabled Passage                     — fetch any basic
5 Island
3 Plains
2 Forest
1 Hidden Cataract                    — transforms into draw land late game
```

## How It Plays

### Turn 1: Captive Weird or pass
Cheap creature ready to be Worldweave fuel or Fear of Change fodder.

### Turn 2: Conjure creature
- **Emporium Thopterist**: Starts passive Ornithopter generation next upkeep
- **Fear of Change**: Exile your Captive Weird → conjure a random MV 3 creature
- **Spellbook Vendor**: Conjure from spellbook immediately
- **Distinguished Conjurer**: Sets up for blink value

### Turn 3: Worldweave
Now EVERY conjure generates an additional conjure. The chaos snowball begins.

### Turns 4-5: Blink chains + Thopter army
- Cast free Ornithopters (2/2 fliers with Thopterist buff)
- Blink Fear of Change → conjure bigger creature → Worldweave triggers
- Distinguished Conjurer draws off every blink
- Aetherflux Reservoir ticking up life with each spell cast
- Thassa or Displacer Kitten for automatic blinks every turn

### Turn 6+: Casino is open
- Oracle of the Alpha means you might draw Black Lotus or Mox
- Tome of the Infinite conjures random spells each activation
- Ornate Imitations for X=5+ floods the board with random creatures
- Conjured creatures do NOT trigger Worldweave (only cast spells do)
- Aetherflux Reservoir threatens the 50-damage laser at any point
- Your hand is overflowing with cards that didn't exist when the game started

### The Dream Sequence

```
Board: Thopterist + Worldweave + Thassa + Aetherflux Reservoir

Upkeep: Thopterist conjures Ornithopter → Worldweave conjures random card
Main:   Cast Ornithopter (free) → Aetherflux gains life
        Blink Fear of Change → conjure MV+2 creature
        → Worldweave conjures another card
        → Distinguished Conjurer draws
        → Aetherflux gains more life (3rd spell)
        Tome of the Infinite → conjure random spell → cast it
        → Aetherflux gains even more life (4th and 5th spells)
End:    Thassa blinks Fear of Change → another conjure → Worldweave

Life total: climbing toward 50 every turn
Board: filling with random creatures you've never seen before
Hand: full of conjured cards from other games' card pools
Opponent: confused
```

## The Randomness Scale

Every card in this deck, ranked by how random its output is:

| Card | Randomness Level |
|------|-----------------|
| Oracle of the Alpha | **MAXIMUM** — Power Nine shuffled in, you never know when you'll draw them |
| Tome of the Infinite | **MAXIMUM** — random spell from curated spellbook every activation |
| Ornate Imitations | **MAXIMUM** — conjures random creature at EVERY mana value 1 through X |
| Fear of Change | **HIGH** — conjures a random creature at specific MV |
| Emergent Haunting | **HIGH** — conjures random creature |
| Clever Conjurer | **HIGH** — conjures random creatures |
| Spellbook Vendor | **HIGH** — conjures from spellbook |
| Worldweave | **HIGH** — seeks (random from subset) a land each trigger |
| Captive Weird | **MEDIUM** — transforms into something |
| Emporium Thopterist | **LOW** — always conjures Ornithopter (predictable, but still conjure) |
| Blink spells | **INDIRECT** — multiplies all the above randomness |
| Aetherflux Reservoir | **DETERMINISTIC** — the one card that does exactly what it says |

## MTGA Export

```
4 Emporium Thopterist
4 Fear of Change
4 Distinguished Conjurer
3 Spellbook Vendor
2 Clever Conjurer
2 Emergent Haunting
1 Oracle of the Alpha
3 Captive Weird
1 Displacer Kitten
1 Thassa, Deep-Dwelling
4 Worldweave
1 Aetherflux Reservoir
1 Tome of the Infinite
1 Ornate Imitations
4 Cloudshift
2 Essence Flux
2 Getaway Glamer
4 Brokers Hideout
4 The World Tree
4 Fabled Passage
5 Island
3 Plains
2 Forest
1 Hidden Cataract
```

## Card Ownership

All 61 cards confirmed owned — zero wildcards needed.

## Mulligan Guide

**Keep**: 2-3 lands (at least U + one other) + any conjure creature + Worldweave or blink spell
**Dream hand**: Island + Plains + Brokers Hideout + Emporium Thopterist + Fear of Change + Worldweave + Cloudshift
**Mulligan**: No blue source, no conjure creatures, all lands, no engine pieces

## Potential Upgrades

- **2nd Aetherflux Reservoir** — more consistent laser threat
- **2nd Ornate Imitations** (Mythic WC) — more big conjure payoff turns
- **Omniscience** — cast everything free, including huge Ornate Imitations
- **Charming Prince** — another blink creature that also scries or gains life

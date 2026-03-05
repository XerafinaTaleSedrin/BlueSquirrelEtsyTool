# Selesnya Infinite Tokens — 80-Card Yorion Build

**Format**: Historic
**Companion**: Yorion, Sky Nomad (sideboard)
**Archetype**: Selesnya (G/W) Lifegain → Counters → Infinite Tokens → Thunderbond Army
**Strategy**: Gain life, put +1/+1 counters, generate tokens that all become copies of Thunderbond Vanguard (power/toughness = number of creatures you control). Go infinite. Swing with 500 copies of a 500/500.

---

## The Combos (How You Win)

### Combo 1: Infinite Tokens
**3 cards = infinite tokens + infinite life:**

```
Soul Warden (on field) + Scurry Oak (on field) + Heliod, Sun-Crowned (on field)

1. Any creature enters → Soul Warden gains you 1 life
2. You gain life → Heliod puts a +1/+1 counter on Scurry Oak
3. Scurry Oak gets a counter → creates a 1/1 Squirrel token
4. Squirrel enters → Soul Warden gains you 1 life
5. Go to step 2. Repeat forever.
```

**Conclave Mentor** makes this even better — each counter Heliod places becomes TWO counters, meaning Scurry Oak triggers twice per loop.

### Combo 2: Thunderbond Vanguard
**Every token becomes a copy of Thunderbond Vanguard.**

```
Thunderbond Vanguard: */*, power and toughness = number of creatures you control.
                      Each creature token enters as a copy of Thunderbond Vanguard.

With 10 creatures on board:
- Make a token → it's a 10/10 Thunderbond Vanguard
- Now you have 11 creatures → ALL Thunderbonds are 11/11
- Make another → 12/12. Another → 13/13.

With the infinite combo: each token is a Thunderbond copy.
After 250 tokens (Arena limit): everything is a 250/250.
```

### Combo 3: Yorion Reblink
**Yorion ETB: exile all other non-land permanents you own, return them.**

```
With Soul Warden + Scurry Oak + Conclave Mentor + Thunderbond on field:
- Cast Yorion → blinks everything
- Everything re-enters → Soul Warden triggers for EACH creature
- Each lifegain → Heliod/Conclave counter on Scurry Oak → tokens
- Tokens enter as Thunderbond copies → Soul Warden triggers again
- Chain reaction → massive board
```

---

## The Deck (80 cards)

### Companion
**Yorion, Sky Nomad** — in sideboard, always available to cast for 3WU

### Creatures (26)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Soul Warden | W | COMBO PIECE. Gain 1 life whenever any creature enters. Starts the infinite loop |
| 4x | Conclave Mentor | GW | Every +1/+1 counter placed becomes +1 MORE. Doubles the speed of counters. When it dies, distributes its counters to your team |
| 4x | Trelasarra, Moon Dancer | GW | Gets +1/+1 and scry 1 on every lifegain. Grows huge, filters draws to find combo pieces |
| 2x | Prosperous Innkeeper | 1G | Treasure on ETB (ramp!), gain 1 life on creature ETB (backup Soul Warden) |
| 4x | Scurry Oak | 2G | COMBO PIECE. Makes a 1/1 Squirrel whenever it gets a +1/+1 counter. Goes infinite with Soul Warden + Heliod |
| 2x | Heliod, Sun-Crowned | 2W | COMBO PIECE. Puts +1/+1 counter on a creature whenever you gain life. Completes the infinite loop |
| 1x | Rosie Cotton of South Lane | 2W | Whenever you create a token, put a +1/+1 counter on another creature. More counters = more Scurry Oak triggers |
| 1x | Mirkwood Bats | 3B | 2/3. Whenever you create a token, each opponent loses 1 life. Infinite tokens = opponent instantly dies. No combat step needed. Pay B with Swamp |
| 4x | Thunderbond Vanguard | 2W | THE FINISHER. All your tokens enter as copies of this. Power/toughness = number of creatures you control. 50 tokens = 50 copies of a 50/50 |

### Enchantments (14)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Ajani's Welcome | W | Soul Warden #5-8 as an enchantment. Harder to remove, survives board wipes |
| 2x | Authority of the Consuls | W | Opponent's creatures enter tapped AND you gain 1 life each time. Slows aggro, feeds your engine |
| 2x | Innkeeper's Talent | 1G | Level 1: +2/+2. Level 3: nontoken creature ETBs make a token copy. Copies your combo pieces! |
| 2x | Caretaker's Talent | 2W | Draw a card whenever one or more tokens enter. Card advantage engine. Don't draw yourself out with infinite tokens though — stop the loop first! |
| 2x | Felidar Retreat | 3W | Landfall: make a 2/2 Cat token (becomes Thunderbond copy!) OR put +1/+1 on all creatures (triggers Scurry Oak) |
| 1x | Anointed Procession | 3W | DOUBLE all tokens. Each Scurry Oak trigger makes 2 tokens. Each one enters as a Thunderbond Vanguard |
| 1x | Cathars' Crusade | 3WW | Every creature ETB gives ALL creatures +1/+1. With tokens entering = exponential growth. Triggers Scurry Oak again |

### Instants (4)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 3x | Path to Exile | W | Best removal in Historic. Exile any creature for 1 mana |
| 1x | Destroy Evil | 1W | Kills big creatures (4+ power) or destroys enchantments. Flexible answer |

### Sorceries (8)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Commune with Spirits | G | Look at top 5, find a creature or enchantment. Finds combo pieces for 1 mana |
| 4x | Cultivate | 2G | Get 2 lands (1 to field, 1 to hand). Ramp to cast Yorion + triggers Felidar Retreat landfall |

### Artifacts (2)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | The Great Henge | 7GG | With Thunderbond Vanguard at 5+ power, this costs 4-5 mana. Draws a card + puts +1/+1 counter on every creature ETB + gains 2 life. Every piece of this triggers something else |

### Lands (26)

| Qty | Card | Notes |
|-----|------|-------|
| 4x | Fabled Passage | Fetches any basic. Triggers landfall for Felidar Retreat |
| 4x | Blossoming Sands | G/W dual. Gains 1 life on ETB — triggers lifegain cards! |
| 2x | Temple of Plenty | G/W dual. Scry 1 helps find combo pieces |
| 1x | Swamp | For Mirkwood Bats' black cost. Yorion doesn't need blue — hybrid {W/U} means WW works fine |
| 8x | Forest | |
| 7x | Plains | |

### Sideboard

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Yorion, Sky Nomad | 3(W/U)(W/U) | COMPANION. Always in your opening hand. Blinks all non-land permanents on ETB for massive re-triggers |

---

## How It Plays

### Turn 1-2: Set Up
- Drop Soul Warden or Ajani's Welcome (lifegain trigger online)
- Conclave Mentor or Trelasarra ready to amplify counters/lifegain
- Commune with Spirits digs for missing combo pieces

### Turn 3: The Key Turn
- **Scurry Oak** OR **Thunderbond Vanguard** hits the field
- With Soul Warden + Scurry Oak: every creature that enters now gains life AND makes a token
- With Thunderbond: any future tokens become copies of it

### Turn 4: Combo or Value
- **Heliod completes the infinite**: Soul Warden + Scurry Oak + Heliod = infinite tokens
- All those tokens are Thunderbond copies = infinite creatures, each infinitely large
- **No Heliod?** Still generating massive value — every creature entering triggers lifegain → counters → tokens

### Turn 5: Yorion or Overwhelm
- **Cast Yorion** (always available as companion): blink everything, re-trigger all ETBs
- Or just attack with your army of 50/50 Thunderbond Vanguards

### Win Conditions
1. **Infinite combo + Thunderbond** — 250 copies of a 250/250. Attack. They're dead
2. **Cathars' Crusade snowball** — Even without the infinite, each token gives everything +1/+1
3. **Trelasarra beats** — Grows to 15/15+ from all the lifegain triggers
4. **Great Henge grind** — Draws cards, adds counters, gains life. Impossible to out-value
5. **Yorion reset** — Blink everything for a massive chain of re-triggers

---

## Synergy Web

```
         Soul Warden / Ajani's Welcome ◄──── ANY creature enters
                    │
               gain 1 life
                    │
         ┌──────────┼──────────┐
         ▼          ▼          ▼
    Heliod     Trelasarra   Conclave Mentor
  +1/+1 counter  grows     (extra counter)
         │
         ▼
    Scurry Oak ──────► creates token
                           │
                           ▼
                  Thunderbond Vanguard
                  (token enters as */*)
                           │
                    ┌──────┴──────┐
                    ▼             ▼
              Soul Warden    ALL Thunderbonds
              triggers again  get +1/+1 bigger
                    │
                    └──► INFINITE LOOP

   Multipliers:
   ├── Anointed Procession: DOUBLE all tokens
   ├── Cathars' Crusade: +1/+1 to ALL on each ETB → more Scurry Oak triggers
   ├── Rosie Cotton: +1/+1 counter per token → more Scurry Oak triggers
   ├── Caretaker's Talent: DRAW cards on token creation
   ├── Great Henge: +1/+1 counter + draw on each creature ETB
   └── Yorion: BLINK everything → re-trigger ALL ETBs
```

---

## Arena Import

```
4 Soul Warden
4 Conclave Mentor
4 Trelasarra, Moon Dancer
2 Prosperous Innkeeper
4 Scurry Oak
2 Heliod, Sun-Crowned
1 Rosie Cotton of South Lane
1 Mirkwood Bats
4 Thunderbond Vanguard
4 Ajani's Welcome
2 Authority of the Consuls
2 Innkeeper's Talent
2 Caretaker's Talent
2 Felidar Retreat
1 Anointed Procession
1 Cathars' Crusade
3 Path to Exile
1 Destroy Evil
4 Commune with Spirits
4 Cultivate
2 The Great Henge
4 Fabled Passage
4 Blossoming Sands
2 Temple of Plenty
1 Swamp
8 Forest
7 Plains

Sideboard
1 Yorion, Sky Nomad
```

---

## Key Changes from Previous Build

- **Added 4x Thunderbond Vanguard** — THE card. Turns every token into a massive creature. Power = number of creatures you control. With infinite tokens, they're all infinitely large
- **Added 4x Conclave Mentor** — Every counter effect places an extra counter. Accelerates the combo and distributes counters when it dies
- **Removed Divine Visitation** — Thunderbond is better. 4/4 flying angels < X/X where X = 250
- **Removed A-Iridescent Hornbeetle** — Thunderbond already turns tokens into real threats. Hornbeetle was redundant
- **Removed Shalai** — Needed the slots. Path to Exile handles problem creatures
- **Added 1x Swamp** — For Mirkwood Bats (Yorion doesn't need blue, hybrid W/U means Plains work)
- **Added 1x Mirkwood Bats** — Whenever you create a token, opponent loses 1 life. Infinite tokens = instant kill without attacking
- **Trimmed to exactly 80** — Clean Yorion companion build

## Upgrade Path

**With Uncommon Wildcards:**
- **Collected Company** (if available) — instant speed, puts 2 creatures from top 6 onto battlefield. Can assemble combo at instant speed on opponent's end step

**Sideboard Tech:**
- **Heroic Intervention** — protect the combo from board wipes
- **Shapers' Sanctuary** — draw a card whenever opponents target your creatures

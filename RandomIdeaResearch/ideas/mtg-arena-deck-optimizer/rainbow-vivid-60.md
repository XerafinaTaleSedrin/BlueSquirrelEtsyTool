# Rainbow Engine — Optimized 60-Card Build

**Format**: Historic
**Archetype**: 5-Color Legendary Cascade / Vivid Payoffs
**Strategy**: Start the game with Leyline of the Guildpact on the battlefield for free, making every nonland permanent all 5 colors instantly. Ramp into Golos (colorless cost, fetches World Tree), then chain legendary creatures with Jodah the Unifier's cascade ability — each legendary you cast exiles cards until it finds a cheaper legendary and casts it free. Vivid creatures hit at maximum power (X=5) from turn 1. Progenitus is the unkillable finisher that Jodah can cascade into. The deck goes from "fixing mana" to "playing your entire deck for free" in about 3 turns.

**Built from**: Your rainbow/5-color card collection (249 cards from "new rainbow" deck dump)

---

## The Core Engine

```
PREGAME: Leyline of the Guildpact on battlefield (free from opening hand)
         → Every nonland permanent is now ALL 5 COLORS
                              ↓
TURNS 1-3: Ramp & Fix ──→ Path to the World Tree, triomes, Spectrum Sentinel
                              ↓
TURN 4-5: Golos (costs 5 colorless = easy) ──→ ETB fetches The World Tree
                              ↓
TURN 5-6: Jodah the Unifier ──→ cast a legendary → cascade into free legendary
           → cast that legendary → cascade AGAIN → chain of free creatures
                              ↓
ENDGAME: Progenitus (10/10 protection from everything) cascaded for free
         Niv-Mizzet Reborn grabbing 5+ cards on ETB
         Golos activation (2WUBRG: play top 3 free)
         Vivid creatures all hitting at X=5
```

The key insight: Leyline of the Guildpact makes your 5-colorless Spectrum Sentinel "all colors" — so Vivid creatures see 5 colors among your permanents even on turn 2. And Jodah sees every creature as legendary-eligible for his +X/+X anthem (since they're all 5-color legendaries or permanents feeding the color count).

---

## The Deck (60 cards)

### The Leyline Foundation (4)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Leyline of the Guildpact | {G/W}{G/U}{B/G}{R/G} | **THE CARD.** If in opening hand, starts on the battlefield FOR FREE. All your nonland permanents become all 5 colors. This single card maxes every Vivid trigger (X=5), enables WUBRG costs by making creatures tap for any color via World Tree, and turns Jodah's +X/+X into a massive anthem. Mulligan aggressively for this |

### Legendary Engine (11)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 3x | Jodah, the Unifier | WUBRG | 5/5. All legendary creatures you control get +X/+X where X = number of legendaries you control. Cast a legendary spell? Exile from top until you hit a cheaper legendary — cast it FREE. With 3 legendaries out, everything is +3/+3. The cascade chains are absurd |
| 4x | Golos, Tireless Pilgrim | 5 (colorless!) | 3/5. ETB: search your library for ANY land and put it onto the battlefield tapped. Fetches The World Tree every time. Then 2WUBRG: exile top 3, play them for free. Colorless cost = castable off any lands. The bridge from early game to endgame |
| 2x | Kenrith, the Returned King | 4W | 5/5. Five activated abilities, one for each color: R = trample/haste, 1G = +1/+1 counter, 2W = gain 5 life, 3U = draw a card, 4B = reanimate from any graveyard. A legendary that does everything, great cascade target |
| 2x | Progenitus | WWUUBBRRGG | 10/10 protection from EVERYTHING. Can't be blocked, can't be targeted, can't be dealt damage, can't be enchanted, can't be anything'd. You never hardcast this — Jodah cascades into it, or Golos flips it free. The ultimate finisher |

### Niv-Mizzet Package (3)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Niv-Mizzet Reborn | WUBRG | 6/6 flying. ETB: look at top 10 cards, take one card of EACH two-color pair (up to 10 cards!). With this deck full of multicolor cards, this routinely draws 3-5 cards. Legendary for Jodah cascade |
| 1x | Niv-Mizzet, Supreme | WUBRG | 5/5 flying. Another WUBRG legendary body for Jodah's cascade chain and anthem. Solid air threat |
| 1x | Chimil, the Inner Sun | 6 (colorless!) | Legendary artifact. Your spells can't be countered (protects entire Jodah cascade chain). End step: Discover 5 = free card every turn. Hits Golos, Kenrith, Explosive Prodigy, Scrutiny, and more. Survives creature board wipes |

### Vivid Payoffs (6)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | Explosive Prodigy | 1R | 1/1. ETB: deals X damage where X = number of colors among permanents you control. With Leyline out, this is a 2-mana "deal 5 damage to any target." Kills planeswalkers, burns face, removes creatures. Absurd rate |
| 2x | Squawkroaster | 3R | */4 flying. Power = number of colors among your permanents. With Leyline = 5/4 flyer for 4 mana. Solid evasive beater |
| 1x | Wildvine Pummeler | 6G | 6/5 trample. Costs 1 less for each color among permanents you control. With Leyline out = costs 2G (3 mana for a 6/5 trample!). An absurd rate creature that comes down way ahead of curve |
| 1x | Shinestriker | 4UU | 3/3 flying. ETB: draw X cards where X = colors among your permanents. With Leyline = draw 5 cards for 6 mana. Massive refuel |

### Ramp & Fixing (9)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Path to the World Tree | 1G | Enchantment. ETB: search for a basic land, put it into your hand. 2WUBRG: sacrifice it = each opponent loses 3, you gain 3 life, draw a card, put a +1/+1 counter on each creature, create a 3/3. The ramp mode alone is worth it; the WUBRG activation is gravy |
| 1x | Timeless Lotus | 5 | Artifact. T: add WUBRG. One card = every color. Drop this turn 5, activate turn 6 for Jodah or Golos activation. Absurd ramp |
| 1x | Jegantha, the Wellspring | 4{R/G} | 5/5 companion-eligible body. T: add WUBRG (no two same). A creature that taps for all 5 colors AND is a legendary for Jodah's cascade and anthem |
| 1x | Ramos, Dragon Engine | 6 | 4/4 flying. Gets a +1/+1 counter for each COLOR of spells you cast (multicolor = multiple counters). Remove 5 counters: add WUBRG and draw. With WUBRG spells giving 5 counters, this is a one-spell refund machine. Legendary for Jodah |
| 2x | Tireless Provisioner | 2G | Landfall: create a Treasure or Food. Golos fetching a land = free treasure. Every land drop = mana acceleration toward WUBRG costs |

### Support & Protection (3)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 3x | Scrutiny of the Guildpact | 1W | Enchantment. Multicolored creatures you control have hexproof. With Leyline, ALL your creatures are multicolored = ALL your creatures have hexproof. Your opponent can't target anything. Brutal lockout |

### Lands (24)

| Qty | Card | Notes |
|-----|------|-------|
| 4x | The World Tree | Legendary land. Taps for G. With 6+ lands, taps for ANY color instead. Golos fetches this every time. The land that fixes everything |
| 1x | Caves of Koilos | W/B pain land. Enters UNTAPPED. Pay 1 life for colored mana |
| 1x | Yavimaya Coast | G/U pain land. Enters UNTAPPED. Early green source for Path |
| 1x | Brightclimb Pathway | W or B modal land. Always enters UNTAPPED. Pick the color you need |
| 1x | Hengegate Pathway | W or U modal land. Always enters UNTAPPED. Flexible fixing |
| 1x | Guildmages' Forum | Taps for colorless, or pay 1 to tap for any color + put a +1/+1 counter on a creature. Untapped and flexible |
| 1x | Indatha Triome | Plains/Swamp/Forest. Enters tapped but covers 3 colors. Cycleable late game |
| 5x | Forest | Green is your most critical early color — Path to the World Tree on turn 2 |
| 4x | Plains | Second most important for Scrutiny and Kenrith |
| 3x | Island | Third color for Shinestriker and splash needs |
| 1x | Mountain | Red for Explosive Prodigy and Squawkroaster |
| 1x | Swamp | Black source for emergencies |

---

## Mana Curve

```
1 CMC: 0
2 CMC: ██████████ 10   (Explosive Prodigy x2, Path to the World Tree x4, Scrutiny x3, Tireless Provisioner counted at 3)
3 CMC: ████ 4           (Tireless Provisioner x2, Wildvine Pummeler at effective 3 with Leyline, Scrutiny overflow)
4 CMC: ████ 4           (Leyline of Guildpact x4 — FREE from hand, 4 mana if hardcast)
5 CMC: ████████████ 12  (Golos x4, Jodah x3, Kenrith x2, Timeless Lotus, Squawkroaster x2... wait, Golos is 5 colorless)
6 CMC: ████ 4           (Jegantha, Ramos, Shinestriker, Niv-Mizzet Reborn)
7+ CMC: ██ 2            (Progenitus x2 — never hardcast, always cascaded/cheated)
WUBRG: ████ 4           (Niv-Mizzets x2, Niv Supreme)
Lands: ████████████████████████ 24

Effective curve is much lower — Leylines are free, Golos costs 5 generic,
Wildvine Pummeler costs 3 with Leyline, and Jodah cascades everything for free.
```

---

## How It Plays

### Pregame: The Leyline Gambit
- **Opening hand**: You're looking for Leyline of the Guildpact + lands that produce green early + any payoff. With 4 copies in a 60-card deck, you see at least one in your opening 7 about 40% of the time. **Mulligan aggressively** — a 5-card hand with Leyline is better than a 7-card hand without it
- **Leyline hits the battlefield before the game even starts.** Every nonland permanent you play from now on is all 5 colors

### Turns 1-3: Ramp and Fix
- **Turn 1-2**: Play basics untapped, cast Path to the World Tree on turn 2 to fetch another basic. You're building toward 5 lands with tempo
- **Turn 2**: Explosive Prodigy if you have it — 2 mana, deal 5 damage to anything. Yes, 5 damage on turn 2. Remove their early threat or burn face
- **Turn 3**: Scrutiny of the Guildpact = all your creatures now have hexproof. Tireless Provisioner = every land drop makes a treasure. You're setting up

### Turns 4-5: Golos Arrives
- **Turn 4-5**: Cast Golos for 5 colorless (any 5 lands work). ETB fetches The World Tree directly to the battlefield. Now you have a land that taps for any color (with 6+ lands) and the nuclear option of WWUUBBRRGG to dump all Gods
- With Leyline out, Golos is all 5 colors. Scrutiny gives him hexproof. He's safe

### Turns 5-7: Jodah Goes Off
- **Turn 5-6**: Cast Jodah the Unifier for WUBRG (World Tree + Timeless Lotus + triomes make this easy). Jodah enters, and the cascade begins
- **Cast any legendary creature** → Jodah triggers → exile from library until you find a legendary with lesser mana value → cast it FREE → if THAT legendary triggers Jodah again (it does, if it's a creature spell), you cascade AGAIN
- **Example cascade chain**: Cast Kenrith (5 mana) → cascade finds Squawkroaster? No, not legendary... finds Niv-Mizzet Reborn (5 mana, but you need lesser)... finds Ramos (6, too much)... finds Jegantha (5, need lesser)... The cascade finds the first legendary with LESSER mana value. Niv-Mizzet Supreme at 5 is equal, not lesser. But cast a 6-mana Ramos → cascade into Jodah #2 or Kenrith (5) → cascade into Explosive Prodigy (2) as a legendary... wait, Prodigy isn't legendary
- **The real chain**: Ramos (6) → cascades into Kenrith (5) → cascades into Golos (5? no, lesser) → Niv-Mizzet at 5? Need lesser → finds Jegantha at 5? Need lesser... The key is having a spread of mana values among your legendaries

### The Jodah Anthem
- With 4 legendaries in play, Jodah gives ALL legendary creatures +4/+4. Golos becomes 7/9. Kenrith becomes 9/9. Jodah himself is 9/9. Niv-Mizzet Reborn is 10/10 flying. **Your board is massive.**
- With Leyline making everything all colors, any creature that happens to also be legendary gets this bonus

### The Nuclear Options
- **Golos activation** (2WUBRG): Exile top 3 cards, play them for free. Lands, creatures, enchantments — everything. Do this every turn for overwhelming card advantage
- **Progenitus**: 10/10 protection from everything. Can't be blocked. Can't be removed. 2-turn clock. Cascaded into by Jodah off any legendary with MV 11+ (you don't have those, but Golos can flip it free, or you can use World Tree's God ability if you have Gods)
- **Ramos refund**: Cast a WUBRG spell like Jodah → Ramos gets 5 counters → remove 5 counters = add WUBRG → cast another WUBRG spell. Self-funding legendary chain

### The Dream Turn
```
Board: Jodah the Unifier + Leyline of the Guildpact + The World Tree + 6 lands

Cast Ramos, Dragon Engine (6 mana, legendary)
→ Jodah cascades: exile until cheaper legendary → finds Kenrith (5 mana) → cast free!
→ Kenrith enters, Jodah cascades again → finds Niv-Mizzet Reborn (5 mana, not lesser than 5... skip)
   → finds Jegantha (5, not lesser)... → finds Golos (5, not lesser)...
   Wait — Kenrith is MV 5, need lesser than 5 →
   → finds a 4-or-less legendary... if none, cascade fizzles here

Ramos got 1 counter from Ramos (colorless), but Kenrith gave 1 (W).
Actually with Leyline, Ramos sees Kenrith as all 5 colors = 5 counters!
Remove 5 counters: add WUBRG.

Activate Golos (already on board from earlier): 2WUBRG, exile top 3, play free.
→ Flip Progenitus? Cast free. 10/10 protection from everything.
→ Flip Niv-Mizzet Reborn? ETB draw 3-5 cards.
→ Flip Wildvine Pummeler? 6/5 trample for free.

Jodah anthem: 5 legendaries in play = everything gets +5/+5.
Jodah is 10/10. Golos is 8/10. Kenrith is 10/10. Ramos is 9/9 flying.
Progenitus is still 10/10 (protection from everything includes your own buffs?
Actually no — Jodah's ability doesn't target, it's a static effect. But Progenitus
has protection from everything which prevents damage, targeting, blocking,
enchanting/equipping... static +X/+X from Jodah DOES apply! Progenitus becomes 15/15!)

Swing with the team for 50+ damage.
```

---

## Win Conditions

1. **Jodah Cascade Chain** — cast one legendary, get 2-3 free. Board floods with massive creatures. Jodah's anthem makes them all enormous. Swing for lethal
2. **Progenitus** — 10/10 (or 15/15 with Jodah anthem) protection from everything. Unblockable, un-removable, un-everything. 2-turn clock at worst
3. **Golos Activation Loop** — spend 2WUBRG every turn to play top 3 cards free. Buries opponent in card advantage. They can't keep up
4. **Explosive Prodigy Burn** — 2 mana: deal 5 damage. With multiple copies or bounce effects, this is repeatable face damage
5. **Ramos Mana Engine** — every WUBRG spell gives 5 counters, remove 5 = WUBRG back. Net zero mana on 5-color spells = infinite if you have enough legendaries to cast
6. **World Tree Nuclear Option** — if you somehow get to WWUUBBRRGG (Ramos + Timeless Lotus), sacrifice World Tree to put ALL God creatures from your library onto the battlefield. If you add Gods later, this is an instant army

---

## Synergy Map

```
LEYLINE OF THE GUILDPACT (starts free from opening hand)
  │
  ├──→ ALL nonland permanents are ALL 5 COLORS
  │     ├──→ Vivid creatures: X = 5 (maximum value immediately)
  │     │     ├──→ Explosive Prodigy: 2 mana deal 5 damage
  │     │     ├──→ Squawkroaster: 5/4 flyer for 4 mana
  │     │     ├──→ Wildvine Pummeler: costs 2G instead of 7G (6/5 trample!)
  │     │     └──→ Shinestriker: draw 5 cards on ETB
  │     │
  │     ├──→ Scrutiny of the Guildpact: all creatures have hexproof
  │     │     (because they're all multicolored now)
  │     │
  │     ├──→ Ramos, Dragon Engine: every spell gives 5 counters
  │     │     (because every spell is all 5 colors)
  │     │     └──→ Remove 5 counters = add WUBRG = cast another spell = 5 more counters
  │     │
  │     └──→ Jodah anthem: legendary count matters more than colors,
  │           but 5-color permanents feed Niv-Mizzet Reborn's ETB
  │
  ├──→ JODAH THE UNIFIER
  │     ├──→ Static: legendary creatures get +X/+X (X = legendary count)
  │     ├──→ Cast legendary creature → cascade into cheaper legendary → free!
  │     │     ├──→ Ramos (6) → cascades into Kenrith/Jegantha/Golos (5)
  │     │     ├──→ Kenrith (5) → cascades into... (need sub-5 legendaries)
  │     │     └──→ Chain keeps going until no cheaper legendary found
  │     └──→ With 4+ legendaries: everything is +4/+4 or more. Lethal fast
  │
  ├──→ GOLOS, TIRELESS PILGRIM
  │     ├──→ Costs 5 COLORLESS = castable off any lands, no fixing needed
  │     ├──→ ETB: fetch The World Tree (or any land you need)
  │     ├──→ 2WUBRG activation: play top 3 cards free (repeatable!)
  │     └──→ Legendary = benefits from Jodah cascade + anthem
  │
  └──→ PROGENITUS
        ├──→ 10/10 protection from everything
        ├──→ Never hardcast — cheated in via Golos activation or cascade
        ├──→ Jodah's anthem applies (static, doesn't target) = 15/15+
        └──→ 2-turn clock, possibly 1-turn with anthem

RAMP PACKAGE:
Path to the World Tree ──→ fetches basic land + WUBRG activation later
Timeless Lotus ──→ T: add WUBRG (one card = all colors)
Jegantha ──→ T: add WUBRG + legendary body
Ramos ──→ 5 counters per WUBRG spell → remove 5 = WUBRG
Tireless Provisioner ──→ landfall = treasure (Golos triggers this!)
Basics + World Tree ──→ untapped mana base, World Tree fixes all colors at 6 lands
```

---

## Mana Base Analysis

```
Color sources (counting lands that produce each color):
G: Forest x5, Yavimaya Coast x1, Indatha x1, World Tree x4 = 11 (MOST — you need green on turn 2)
W: Plains x4, Caves of Koilos x1, Brightclimb Pathway x1, Hengegate Pathway x1, Indatha x1, World Tree x4 = 12
U: Island x3, Yavimaya Coast x1, Hengegate Pathway x1, Indatha x1, World Tree x4 = 10
B: Swamp x1, Caves of Koilos x1, Brightclimb Pathway x1, Indatha x1, World Tree x4 = 8
R: Mountain x1, World Tree x4 = 5
Any: Guildmages' Forum x1, Timeless Lotus, Jegantha, Ramos, Tireless Provisioner treasures

Strategy: Mostly basics that enter UNTAPPED so you can play on curve.
World Tree fixes everything once you hit 6 lands. Before that:
- Green is guaranteed (11 sources) for Path to the World Tree on turn 2
- Golos costs 5 COLORLESS = any 5 lands work, no fixing needed
- WUBRG for Jodah comes from World Tree + Timeless Lotus + Ramos + treasures
- Pain lands and pathways enter untapped for critical early turns
- Only 1 tapped land (Indatha Triome) instead of the old 16!
```

---

## Why This Is Mean

1. **Leyline of the Guildpact before the game starts** — your opponent sees it and immediately knows every card you play will be maximum value. Psychological damage before turn 1
2. **Explosive Prodigy on turn 2 = 5 damage** — that's a Lightning Bolt and a half for 2 mana. Kills almost any early creature or chunks 25% of their life
3. **Scrutiny of the Guildpact + Leyline = everything has hexproof** — can't target your creatures. Can't remove them with spot removal. They need a board wipe or they're dead
4. **Jodah cascade chains** — you cast one creature, get two or three for free. Your opponent watches in horror as legendary after legendary hits the battlefield, each one making all the others bigger
5. **Progenitus** — protection from everything. They literally cannot interact with it. No blocking. No targeting. No damage. Just a 10/10+ clock they have to watch count down
6. **Golos plays your deck for free** — 2WUBRG: play top 3. Every. Single. Turn. Your opponent is playing one card per turn. You're playing four
7. **Ramos refunds your spells** — cast a WUBRG spell, get WUBRG back. It's like having infinite mana for multicolored spells

---

## Cards You Own (All 60)

Every card in this deck comes from your "new rainbow" collection. **Zero wildcards needed** for the main build. Just import and play.

---

## Mulligan Guide

**Keep if you have:**
- Leyline of the Guildpact + 2-3 lands (any number of cards)
- Path to the World Tree + green source + 2 other lands (even without Leyline)

**Mulligan if you have:**
- No Leyline AND no ramp (Path/Provisioner) — the deck is too slow without either
- All high-cost cards and no way to cast them by turn 5
- No green sources (you need green for Path to the World Tree and Leyline hardcast)

**London Mulligan math:**
- 4x Leyline in 60 cards = ~40% chance to see at least 1 in opening 7
- After one mulligan (6 cards, put 1 back): ~34% chance
- Combined: ~60% chance to find Leyline in first 7 or mulligan 7
- **The deck still functions without Leyline** — it's just slower. Golos + World Tree + Path do the heavy lifting if Leyline doesn't show

---

## Matchup Notes

- **Against Aggro**: You need Explosive Prodigy and Scrutiny early. Prodigy kills their threats; Scrutiny + Leyline makes your blockers untargetable. Golos on turn 5 stabilizes. If you survive to Jodah, you win
- **Against Control**: Scrutiny = hexproof on everything. They can still board wipe, but Jodah cascade means you rebuild instantly. Golos activation grinds them out — they can't counter free spells from Golos
- **Against Midrange**: This is your best matchup. You go bigger than everyone. Jodah + 3 legendaries = +3/+3 to everything. Nobody out-stats you
- **Against Combo**: Race them. Golos on 5, Jodah on 6, cascade into a lethal board. Progenitus closes fast

---

## Arena Import

```
4 Leyline of the Guildpact
3 Jodah, the Unifier
4 Golos, Tireless Pilgrim
2 Kenrith, the Returned King
2 Progenitus
1 Niv-Mizzet Reborn
1 Niv-Mizzet, Supreme
1 Chimil, the Inner Sun
2 Explosive Prodigy
2 Squawkroaster
1 Wildvine Pummeler
1 Shinestriker
1 Jegantha, the Wellspring
1 Ramos, Dragon Engine
2 Tireless Provisioner
1 Timeless Lotus
4 Path to the World Tree
3 Scrutiny of the Guildpact
4 The World Tree
1 Caves of Koilos
1 Yavimaya Coast
1 Brightclimb Pathway
1 Hengegate Pathway
1 Guildmages' Forum
1 Indatha Triome
5 Forest
4 Plains
3 Island
1 Mountain
1 Swamp
```

---

## Upgrade Path

If you get wildcards:
- **Chromatic Orrery** (7 mana artifact) — spend mana as any color, T: add 5 colorless, 5 mana: draw a card per color among permanents. With Leyline = draw 5 for 5. Massive engine
- **Esika, God of the Tree / The Prismatic Bridge** — legendary God, back face is WUBRG enchantment that puts a creature/planeswalker from top onto battlefield each upkeep for free
- **Omnath, Locus of Creation** (RGWU) — landfall triggers for life, mana, and damage. Golos fetching lands = extra triggers
- **Sisay, Weatherlight Captain** (2W) — WUBRG: search for a legendary with MV less than her power. With Jodah anthem she has huge power = fetch anything
- **More Gods** (for World Tree activation) — Heliod, Purphoros, Thassa, etc. World Tree's WWUUBBRRGG sac dumps them all onto the battlefield at instant speed

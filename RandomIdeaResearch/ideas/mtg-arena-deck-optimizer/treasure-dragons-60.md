# Treasure Dragons — Optimized 60-Card Build

**Format**: Historic
**Archetype**: Red-based Dragon Treasure Ramp
**Strategy**: Generate treasures with early creatures, ramp into massive dragons ahead of curve. Goldspan Dragon makes treasures tap for double mana. Terror of the Peaks turns every dragon entering into a lightning bolt. Old Gnawbone turns combat damage into a mountain of treasure. Dragonspark Reactor counts every treasure entering and then explodes for 15+ damage. Revel in Riches: 10 treasures = you win.

**Built from**: Your dragon/treasure card collection (280 cards from "Strix Treasure Dragons")

---

## What Changed (Luxury Upgrade)

Three 1-of upgrades replacing the weakest cards, plus one extra cut to fix the deck at exactly 60 (the previous import block had 61 cards). Source of truth: the Arena Import block.

| IN | OUT | Why |
|----|-----|-----|
| 1x Fable of the Mirror-Breaker | 1x Darigaaz's Whelp | Fable makes a treasure (Chapter I), creates a 2/2 token that copies creatures (Chapter II), and transforms into a creature that copies any nonlegendary creature on attack. Was banned in Standard for being too good. Replaces the weakest creature in the deck |
| 1x Xorn | 1x Voltage Surge | Whenever you create a treasure, create an additional one. Doubles ALL treasure output from Goldspan, Gnawbone, Magda, Smothering Tithe — everything. Far more impact than a conditional 1-damage removal spell |
| 1x Haunted Ridge | 1x Swamp | R/B dual land that enters untapped if you control two or more other lands. Strictly better than a basic Swamp since it also taps for R. Fixes black for Deadly Dispute and Revel in Riches without costing you red access |
| (removed) | 1x Reckless Fireweaver | Previous import block had 61 cards. Cut to reach exactly 60. Fireweaver (1 damage per artifact ETB) is redundant with Dragonspark Reactor doing the same job better |

**Net effect**: More treasure generation (Xorn doubles output, Fable makes treasures + token value), better mana fixing (Haunted Ridge), stronger mid-game board (Fable's copy token is absurd with Terror of the Peaks or Goldspan Dragon).

---

## The Core Engine

This deck runs on a simple loop:

```
Make Treasures → Ramp into Dragons → Dragons make more Treasures → Ramp into BIGGER Dragons
                                                                          ↓
                                                           Terror of the Peaks: each one
                                                           deals damage equal to its power
                                                                          ↓
                                                           Dragonspark Reactor: counting
                                                           every treasure entering...
                                                           sac for 15+ damage to face
```

Splashes for Smothering Tithe (W), Revel in Riches (B), and Old Gnawbone (GG) are paid via treasure tokens — the deck is base red and fixes itself.

---

## The Deck (60 cards)

### Creatures (25)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Charming Scoundrel | 1R | 1/1 haste. ETB: make a Treasure OR rummage OR create a Wicked Role. Flexible early play |
| 2x | Magda, the Hoardmaster | 1R | Whenever you commit a crime, create a treasure. Sacrifice 3 treasures = 4/4 Scorpion Dragon with flying and haste. Treasure-to-dragon converter |
| 1x | Sarkhan, Soul Aflame | 1UR | Dragon spells cost 1 less. Whenever a dragon enters, Sarkhan becomes a COPY of it. Drop Terror of the Peaks? Now you have TWO Terrors |
| 1x | Captain Lannery Storm | 2R | 2/2 haste. Attacks = treasure. Sac a treasure = +1/+0. Early pressure that funds bigger plays |
| 1x | Professional Face-Breaker | 2R | 2/3 menace. Creatures deal combat damage = treasure. Sac a treasure = impulse draw. Card advantage AND ramp in one |
| 1x | Breeches, Eager Pillager | 2R | 3/3 first strike. Pirate attacks = treasure OR exile-draw OR remove a blocker. Triple threat |
| 2x | Gadrak, the Crown-Scourge | 2R | 5/4 flying for 3 mana! Can't attack without 4 artifacts (treasures count). End step: treasure for each creature that died. With removal and combat, this prints money |
| 2x | Galazeth Prismari | 2UR | 3/4 flying Elder Dragon. ETB: make a treasure. All your artifacts can tap for mana to cast instants/sorceries. Treasures become reusable mana rocks |
| 1x | Xorn | 2R | 3/2. Whenever you create one or more Treasure tokens, create an additional Treasure. Doubles output from Goldspan, Gnawbone, Magda, Smothering Tithe — everything |
| 1x | Jolene, Plundering Pugilist | 1RG | 4/2. Attack with power 4+ creatures = treasure. 1R sac a treasure = deal 1 damage. Works with every dragon you cast |
| 2x | Opportunistic Dragon | 2RR | 4/3 flying. ETB: steal an opponent's artifact or Human. Takes their stuff AND flies over for damage |
| 2x | Goldspan Dragon | 3RR | **THE CARD.** 4/4 flying haste. Attacks = treasure. Gets targeted = treasure. Treasures tap for TWO mana. This card is why the deck works |
| 2x | Atsushi, the Blazing Sky | 2RR | 4/4 flying trample. When it dies: 3 treasures OR exile 2 cards to play. They kill it? You get richer |
| 2x | Terror of the Peaks | 3RR | 5/4 flying. Every creature entering deals damage equal to its power to ANY target. Drop a 7/7 Gnawbone = Terror deals 7 to their face. Drop two dragons in a turn = game over |
| 2x | Bonehoard Dracosaur | 3RR | 5/5 flying first strike. Each upkeep: exile top 2 cards, play them this turn. Land = 3/1 Dinosaur token. Nonland = treasure. Card advantage that never stops |
| 1x | Old Gnawbone | 5GG | 7/7 flying. Whenever ANY creature you control deals combat damage, create that many treasures. 7 damage = 7 treasures. With multiple creatures attacking = 15+ treasures in one combat |
| 1x | Incinerator of the Guilty | 4RR | 6/6 flying trample. Deals combat damage = collect evidence X = deal X to ALL their creatures and planeswalkers. One-sided board wipe on a stick |

### Instants & Sorceries (8)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 3x | Dragon's Fire | 1R | Deal damage equal to a dragon's power you control or reveal. With a 5/5 on board = 5 damage for 2 mana. Best red removal in the deck |
| 1x | Deadly Dispute | 1B | Sacrifice an artifact (treasure), draw 2 cards, create a treasure. Net: draw 2 cards for free. Pay the B with a treasure |
| 2x | Prismari Command | 1UR | Choose 2: deal 2 damage + make a treasure, or draw/discard + make a treasure, or destroy an artifact. Incredibly flexible |
| 1x | Big Score | 3R | Draw 2 cards, create 2 treasures. Raw card advantage + ramp |
| 1x | An Offer You Can't Refuse | U | Counter ANY noncreature spell for 1 mana. Opponent gets 2 treasures — who cares, you're the treasure deck. Protects Goldspan, Smothering Tithe, and Revel in Riches from removal. Pay U with a treasure |

### Enchantments (4)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 1x | Fable of the Mirror-Breaker | 2R | Saga: Chapter I makes a 2/2 Goblin Shaman token. Chapter II: create a Treasure, then you may discard up to 2 cards and draw that many. Chapter III: transforms into Reflection of Kiki-Jiki, which creates token copies of your creatures. Banned in Standard for a reason |
| 1x | Dragon Mantle | R | Enchant a creature, draw a card. Gives firebreathing (R: +1/+0). Cantrip that turns any dragon into a mana sink finisher |
| 1x | Smothering Tithe | 3W | Every time opponent draws, they pay 2 or you get a treasure. They NEVER pay. You get 1-2 free treasures per turn forever. Pay the W from a treasure |
| 1x | Revel in Riches | 4B | Opponent's creatures die = you get treasure. Control 10+ treasures at upkeep = YOU WIN THE GAME. The ultimate treasure payoff. Pay the B from a treasure |

### Artifacts (2)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | Dragonspark Reactor | 1R | Gets a charge counter for EVERY artifact entering (including treasures). Sac it: deal damage equal to charge counters to a player + a creature. Goldspan makes 1 treasure per attack = 1 counter. Old Gnawbone dumps 7 = 7 counters. This routinely hits 15+ for a lethal explosion |

### Lands (24)

| Qty | Card | Notes |
|-----|------|-------|
| 19x | Mountain | Base red — you need red on turns 1-3 without fail |
| 1x | Haunted Ridge | R/B dual land. Enters untapped if you control 2+ other lands. Taps for R or B — fixes black without losing red access |
| 1x | Swamp | For Deadly Dispute or Revel in Riches if you don't have a treasure yet |
| 2x | Forest | For Jolene or a desperate Gnawbone hardcast |
| 1x | Tomb of the Spirit Dragon | Taps for colorless. Activate: gain 1 life per colorless creature. Emergency lifegain with artifact creatures/tokens |

---

## Mana Curve

```
1 CMC: ██ 2           (Dragon Mantle, Charming Scoundrel... effectively 2 mana)
2 CMC: ████████ 8     (Magda x2, Dragonspark Reactor x2, Dragon's Fire x3, Deadly Dispute)
3 CMC: ██████████ 10  (Sarkhan, Captain Lannery, Face-Breaker, Breeches, Gadrak x2, Xorn, Fable of the Mirror-Breaker, Prismari Command x2)
4 CMC: ██████████ 10  (Galazeth x2, Opportunistic Dragon x2, Atsushi x2, Big Score, Smothering Tithe, Jolene, Dragon Mantle counts as 1)
5 CMC: ██████████ 8   (Goldspan x2, Terror x2, Bonehoard x2, Revel in Riches, Incinerator)
7 CMC: █ 1            (Old Gnawbone)
Lands: ████████████████████████ 24
```

Top-heavy by design — treasures from turns 2-4 let you slam 5-drops on turn 3-4.

---

## How It Plays

### Turns 1-3: Build the Treasury
- **Turn 1**: Dragon Mantle on... nothing yet. Or hold it. Mountain, go.
- **Turn 2**: Magda, Charming Scoundrel (treasure mode), or Dragonspark Reactor. Start accumulating artifacts
- **Turn 3**: Captain Lannery attacks = treasure. Or Gadrak (5/4 body, will attack once you have 4 treasures). Or Face-Breaker for menace + combat treasures

### Turns 4-5: Dragons Arrive Early
- **Turn 4**: With 2-3 treasures, you have 6-7 mana available. Slam Goldspan Dragon (haste, attacks immediately = another treasure)
- **Turn 5**: Terror of the Peaks. Now every dragon entering deals damage. Play another creature = free damage
- Galazeth Prismari makes all your treasures tap for spell mana WITHOUT sacrificing them

### Turn 6+: The Avalanche
- **Old Gnawbone**: 7/7 flying, every point of combat damage = a treasure. Hit them for 7 = 7 treasures
- **Terror of the Peaks + Gnawbone entering**: Terror deals 7 to their face. Gnawbone then attacks for 7 more + 7 treasures
- **Dragonspark Reactor**: has been counting every treasure entering. 15+ counters? Sacrifice it: 15 damage to face
- **Revel in Riches**: you have 12 treasures. Upkeep. You win.
- **Magda**: Sacrifice 3 treasures = 4/4 flying haste Scorpion Dragon. Terror deals 4. Repeat.

### The Dream Turn
```
Board: Terror of the Peaks + Goldspan Dragon + Smothering Tithe + Dragonspark Reactor (10 counters)

Cast Old Gnawbone (pay 5GG with treasures, Goldspan doubles = only need 4 treasures)
→ Terror deals 7 to opponent (they're at 13)
→ Attack with Gnawbone + Goldspan
→ Gnawbone hits for 7 = 7 treasures (Reactor now at 17 counters)
→ Goldspan hits for 4 + makes a treasure (Reactor at 18)
→ Opponent at 2 life

Sacrifice Dragonspark Reactor: 18 damage. They're at -16. Very dead.
```

---

## Win Conditions

1. **Dragon beatdown** — 4/4 and 5/5 flyers stacked up. Classic and reliable
2. **Terror of the Peaks chain** — every dragon entering = free Lightning Bolt or better. Two dragons in one turn often = lethal
3. **Dragonspark Reactor explosion** — counts every treasure token entering. Sac for 15+ damage to face. The sneaky kill they don't see coming
4. **Revel in Riches** — 10 treasures at upkeep = you win. With this deck, 10 treasures happens naturally by turn 6-7
5. **Sarkhan copying Terror of the Peaks** — TWO Terrors on board = every creature entering deals DOUBLE its power. A 7/7 Gnawbone entering = 14 damage to face

---

## Synergy Map

```
TREASURE GENERATORS:
Charming Scoundrel ──→ 1 treasure on ETB
Magda ──→ treasure when you commit a crime (targeting with Dragon's Fire counts!)
Captain Lannery ──→ treasure on attack
Face-Breaker ──→ treasure on combat damage
Breeches ──→ treasure on Pirate attack
Gadrak ──→ treasure per dead creature at end step
Galazeth ──→ treasure on ETB
Goldspan ──→ treasure on attack + when targeted
Atsushi ──→ 3 treasures when it dies
Bonehoard Dracosaur ──→ treasure per nonland exiled each upkeep
Old Gnawbone ──→ treasures = combat damage dealt
Smothering Tithe ──→ treasure per opponent draw
Revel in Riches ──→ treasure per opponent creature death
Prismari Command ──→ treasure as a mode
Big Score ──→ 2 treasures
Deadly Dispute ──→ 1 treasure
Fable of the Mirror-Breaker ──→ 1 treasure (Chapter II) + rummage draw
                    ↓
TREASURE MULTIPLIER:
Xorn ──→ whenever you create a treasure, create an ADDITIONAL treasure
                    ↓
TREASURE PAYOFFS:
Goldspan ──→ treasures tap for DOUBLE mana
Galazeth ──→ artifacts tap for instant/sorcery mana (don't sac!)
Gadrak ──→ can attack with 4+ artifacts (treasures)
Magda ──→ sac 3 treasures = 4/4 flying haste dragon token
Face-Breaker ──→ sac treasure = impulse draw
Dragonspark Reactor ──→ charge counter per artifact entering → sac for MASSIVE damage
Revel in Riches ──→ 10 treasures = WIN THE GAME
Captain Lannery ──→ sac treasure = +1/+0
                    ↓
DRAGON PAYOFFS:
Terror of the Peaks ──→ creature ETB = deal power as damage
Sarkhan ──→ dragon enters = becomes a copy (TWO Terrors!)
Sarkhan ──→ dragon spells cost 1 less
Dragon's Fire ──→ removal scales with dragon power
Dragon Mantle ──→ firebreathing mana sink for lethal
```

---

## Color Splashing via Treasures

The deck is **base red** (19 Mountains) with tiny splashes paid by treasure tokens:

| Splash | Cards | When you need it | How you pay |
|--------|-------|-----------------|-------------|
| Blue | Sarkhan (1UR), Galazeth (2UR), Prismari Command (1UR) | Turn 3-4 | 1 treasure for U |
| Black | Deadly Dispute (1B), Revel in Riches (4B) | Turn 2+ (Dispute), Turn 5+ (Revel) | 1 treasure for B, or 2 Swamps |
| Green | Jolene (1RG), Old Gnawbone (5GG) | Turn 3+ (Jolene), Turn 5+ (Gnawbone via treasures) | 1-2 treasures for G, or 2 Forests |
| White | Smothering Tithe (3W) | Turn 4+ | 1 treasure for W |

With Goldspan Dragon doubling treasure mana, you often only need 2 treasures to cover a 4-mana splash card.

---

## Why This Is Mean

1. **Goldspan Dragon makes treasures tap for 2** — you're functionally playing with double mana while your opponent plays fair
2. **Terror of the Peaks punishes you for playing creatures AND for killing theirs** — they can't deal with your board without getting burned
3. **Smothering Tithe taxes their draws** — they pay 2 per draw or you get free mana. They never pay. You always profit
4. **Revel in Riches says "10 treasures = I win"** — and this deck hits 10 treasures routinely. They HAVE to destroy it or lose
5. **Dragonspark Reactor is a ticking time bomb** — they ignore it, it hits 20 counters and one-shots them. They destroy it? You still have 5 dragons
6. **Atsushi rewards them for killing it** — destroy my dragon? Thanks, here's 3 treasures. Now I'll cast something bigger
7. **Xorn doubles every treasure trigger** — Goldspan attacks? 2 treasures instead of 1. Gnawbone hits for 7? 14 treasures. Reactor goes nuclear twice as fast
8. **Fable of the Mirror-Breaker copies your best creature** — Reflection of Kiki-Jiki copying Terror of the Peaks or Goldspan Dragon is disgusting

---

## Cards You Own (All 60)

Every single card in this deck is confirmed owned (including 1x Fable of the Mirror-Breaker, 1x Xorn, 1x Haunted Ridge as luxury upgrades). **Zero wildcards needed.** Just import and play.

---

## Arena Import (Luxury Upgrade Build)

```
1 Charming Scoundrel
2 Magda, the Hoardmaster
1 Sarkhan, Soul Aflame
1 Captain Lannery Storm
1 Professional Face-Breaker
1 Breeches, Eager Pillager
1 Gadrak, the Crown-Scourge
1 Rapacious Dragon
2 Galazeth Prismari
1 Jolene, Plundering Pugilist
1 Opportunistic Dragon
1 Rapacious Dragon
1 Goldspan Dragon
1 Atsushi, the Blazing Sky
2 Terror of the Peaks
1 Bonehoard Dracosaur
1 Old Gnawbone
1 Incinerator of the Guilty
3 Dragon's Fire
1 Xorn
1 Deadly Dispute
2 Prismari Command
1 Big Score
1 An Offer You Can't Refuse
1 Fable of the Mirror-Breaker
1 Dragon Mantle
1 Smothering Tithe
1 Revel in Riches
2 Dragonspark Reactor
19 Mountain
1 Haunted Ridge
1 Gate of the Black Dragon
2 Forest
1 Tomb of the Spirit Dragon
```

---

## Upgrade Path

Already included (luxury upgrades):
- **Fable of the Mirror-Breaker** (1x) — INCLUDED. Makes treasure, makes a 2/2 that copies creatures. Banned in Standard for being too good
- **Xorn** (1x) — INCLUDED. Whenever you create a treasure, create an additional treasure. Doubles ALL your treasure output
- **Haunted Ridge** (1x) — INCLUDED. R/B dual land, enters untapped with 2+ other lands

If you get more wildcards:
- **Goldvein Hydra** (rare) — dies = treasures equal to its +1/+1 counters
- **Better mana base**: Stormcarved Coast, Rockfall Vale — more dual lands that enter untapped with the right conditions
- **Cruelty of Gix** — saga that searches for creatures and reanimates. Find Terror of the Peaks or Gnawbone from your deck
- **Additional copies of Fable/Xorn** — both are good enough to run 2-3x if you acquire more

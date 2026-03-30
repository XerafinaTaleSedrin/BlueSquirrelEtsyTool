# Orzhov Vito Drain — Historic BO1 (60 Cards)

**Format**: Historic BO1
**Archetype**: Orzhov (W/B) Lifegain → Drain
**Strategy**: Flood the board with cheap lifegain triggers (Soul Warden, Lunarch Veteran), convert every life gain into opponent life loss (Vito, Marauding Blight-Priest), and close with Sheoldred's passive drain or the Vito + Exquisite Blood infinite combo.

---

## The Combo

```
VITO + EXQUISITE BLOOD = INSTANT WIN

  Vito, Thorn of the Dusk Rose (2B, 1/3)
  → "Whenever you gain life, target opponent loses that much life"

  Exquisite Blood (4B, enchantment)
  → "Whenever an opponent loses life, you gain that much life"

  TOGETHER:
  → Any life gain → Vito drains opponent → Exquisite Blood gains you life
  → That life gain triggers Vito again → infinite loop → opponent dies

  TRIGGERS THAT START THE LOOP:
  → Soul Warden/Lunarch Veteran sees ANY creature ETB = gain 1 life = win
  → Scoured Barrens enters the battlefield = gain 1 life = win
  → Sheoldred on your draw step = gain 2 life = win
  → Deep-Cavern Bat attacks (lifelink) = win
  → Literally any life gain or opponent life loss = win

  You only need BOTH pieces on the field + any trigger.
  Unlike Heliod combo (3 cards), this is just 2 cards.
```

---

## The Drain Engine (without combo)

```
PASSIVE DRAIN:

  Soul Warden / Lunarch Veteran on battlefield (8 copies in deck)
  → ANY creature enters (yours OR opponent's) = you gain 1 life

  Vito / Marauding Blight-Priest on battlefield (6 copies in deck)
  → Every life gain = opponent loses life

  RESULT: Every creature that enters the battlefield drains your opponent.
  Your creatures: ETB gains you life → drains opponent
  Their creatures: ETB gains you life → drains opponent
  They can't play creatures without dying.

SHEOLDRED LAYER:
  Sheoldred, the Apocalypse (2BB, 4/5 deathtouch)
  → You draw a card = gain 2 life → triggers Vito/Blight-Priest drain
  → Opponent draws a card = they lose 2 life
  → With Vito: your draw = gain 2 → opponent loses 2 (from Vito) + normal draw damage
  → With Exquisite Blood: opponent's draw damage = you gain 2 = more drain

RIGHTEOUS VALKYRIE ANTHEM:
  Righteous Valkyrie (2W, 2/4 Angel Cleric)
  → Each Cleric/Angel ETB = gain life equal to its toughness
  → If you have 27+ life: all your creatures get +2/+2
  → Soul Warden/Lunarch Veteran feed you to 27 fast
  → Suddenly your 1/1s are 3/3s and your Sheoldred is a 6/7 deathtouch
```

---

## The Deck (60 cards)

### Lifegain Triggers (10)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 4x | Soul Warden | W | Gain 1 life whenever ANY creature enters the battlefield. Triggers Vito, Blight-Priest, Voice of the Blessed. Against creature decks, this is absurd — their own creatures drain them |
| 4x | Lunarch Veteran | W | Same as Soul Warden. 8 total copies means you almost always have one by turn 1-2. Disturb side is a 1/1 flier if it dies |
| 2x | Authority of the Consuls | W | Opponents' creatures enter tapped (can't attack immediately) + you gain 1 life each. Shuts down aggro AND triggers your drain engine |

### Drain Payoffs (4)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 3x | Marauding Blight-Priest | 2B | 3/2. Whenever you gain life, each opponent loses 1 life. With Soul Warden, every creature = drain 1. Multiple Blight-Priests stack — 2 on board = drain 2 per trigger |
| 2x | Vito, Thorn of the Dusk Rose | 2B | 1/3. Whenever you gain life, target opponent loses THAT MUCH life (scales with amount, unlike Blight-Priest's flat 1). Half of the infinite combo. Activated ability gives lifelink to all your creatures for 3BB |

### Value Creatures (9)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | Deep-Cavern Bat | 1B | 1/1 flying lifelink. ETB: look at opponent's hand, exile a noncreature/nonland card (returns when bat dies). Early disruption + lifelink triggers drain engine on attack |
| 3x | Righteous Valkyrie | 2W | 2/4 Angel Cleric. Whenever another Angel or Cleric ETB, gain life = its toughness. If at 27+ life, creatures get +2/+2. Most of your creatures are Clerics — this gains huge life AND provides an anthem |
| 4x | Sheoldred, the Apocalypse | 2BB | 4/5 deathtouch. You draw = gain 2 life. Opponent draws = they lose 2. The best card in the deck standalone. With Vito, your draw drains 4+ per turn. Completely warps the game around itself |

### Combo Piece (2)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | Exquisite Blood | 4B | Enchantment. Whenever an opponent loses life, you gain that much life. WITH VITO = INSTANT WIN. Even without Vito, turns Sheoldred's opponent-drain into lifegain, turns Blight-Priest drain into more lifegain, creates a snowball effect |

### Removal (6)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 3x | Cut Down | B | Instant. Destroy creature with power + toughness ≤ 5. Kills most early threats for 1 mana. Premium removal |
| 3x | Go for the Throat | 1B | Instant. Destroy non-artifact creature. Kills anything bigger that Cut Down misses. Clean 2-mana answer |

### Combo Protection (5)

| Qty | Card | Mana | Role |
|-----|------|------|------|
| 2x | Undying Malice | B | Instant. When target creature dies this turn, return it to the battlefield with a +1/+1 counter. Hold up 1 black mana when Vito is on the board — if they kill him, he comes right back and the combo still fires. Also saves Sheoldred from removal |
| 1x | Kaya's Ghostform | B | Enchantment — Aura. Enchant Vito preemptively. When he dies or gets exiled, he returns to the battlefield. No mana needed to activate — just having it attached protects him. Costs only 1 mana to set up |
| 2x | Alseid of Life's Bounty | W | 1/1 lifelink. Sacrifice + pay W: target creature gains protection from a color until end of turn. Protects Vito from targeted removal, AND it's a lifelink creature that triggers your drain engine while waiting. Sacrifice triggers Bastion of Remembrance if in play |

### Lands (24)

| Qty | Card | Notes |
|-----|------|-------|
| 3x | Concealed Courtyard | WB dual, untapped if you control ≤ 2 other lands. Best early dual |
| 1x | Brightclimb Pathway | Modal W or B. Always untapped |
| 1x | Caves of Koilos | WB, always untapped, 1 damage for colored mana |
| 1x | Hive of the Eye Tyrant | Enters untapped for B. Becomes a 3/3 menace attacker for 3B (exiles card from opponent's graveyard). Utility land |
| 4x | Scoured Barrens | WB dual, enters tapped, gain 1 life. The lifegain TRIGGERS VITO and Blight-Priest. With the combo out, this land entering = instant win |
| 4x | Fabled Passage | Fetches any basic untapped (after turn 3). Thins the deck |
| 6x | Swamp | Primary color |
| 4x | Plains | For white spells |

---

## Mana Curve

```
1 CMC:  █████████████████ 17 Soul Warden x4, Lunarch Veteran x4,
                              Cut Down x4, Authority of the Consuls x2,
                              Undying Malice x2, Kaya's Ghostform x1
2 CMC:  ████████ 8           Deep-Cavern Bat x2, Go for the Throat x3,
                              Alseid of Life's Bounty x2, Feed the Swarm x1
3 CMC:  ████████ 8           Marauding Blight-Priest x3,
                              Vito x2, Righteous Valkyrie x3
4 CMC:  ████ 4               Sheoldred, the Apocalypse x4
5 CMC:  ██ 2                 Exquisite Blood x2

Lands: 24     (wait, that's 39 spells — see note below)
```

> **Note**: 39 spells + 24 lands = 63. To hit 60, cut 3 cards.
> Recommended cuts: -1 Feed the Swarm, -1 Marauding Blight-Priest, -1 Cut Down.
> Final: 36 spells + 24 lands = 60.

```
FINAL MANA CURVE (60 cards):

1 CMC:  ████████████████ 16  Soul Warden x4, Lunarch Veteran x4,
                              Cut Down x3, Authority of the Consuls x2,
                              Undying Malice x2, Kaya's Ghostform x1
2 CMC:  ███████ 7            Deep-Cavern Bat x2, Go for the Throat x3,
                              Alseid of Life's Bounty x2
3 CMC:  ███████ 7            Marauding Blight-Priest x2,
                              Vito x2, Righteous Valkyrie x3
4 CMC:  ████ 4               Sheoldred, the Apocalypse x4
5 CMC:  ██ 2                 Exquisite Blood x2

Lands: 24
```

---

## How It Plays

### Turn 1: Lifegain Foundation
Soul Warden, Lunarch Veteran, or Authority of the Consuls. You want a lifegain trigger down ASAP. Cut Down if opponent plays a 1-drop threat.

### Turn 2: Disruption or Setup
Deep-Cavern Bat strips their best card. Alseid of Life's Bounty is a lifelink body that doubles as Vito insurance later. Or play a second lifegain creature. Go for the Throat if they play something scary.

### Turn 3: Drain Engine Online
Marauding Blight-Priest or Vito. NOW every lifegain trigger drains your opponent. With Soul Warden + Blight-Priest, every creature from either side = drain 1. Righteous Valkyrie also excellent here — gains life on your Cleric ETBs, working toward 27+ life anthem. If you have Vito, consider attaching Kaya's Ghostform to protect him.

### Turn 4: Sheoldred
Slam Sheoldred. You gain 2 on your draw → triggers Vito/Blight-Priest. Opponent loses 2 on their draw. The game clock accelerates dramatically. With the drain engine already running, opponent is losing 4-6 life per turn cycle just from triggers. Hold up Undying Malice if you have one — protect Sheoldred from removal.

### Turn 5: Combo or Overwhelm
If you have Exquisite Blood + Vito both in hand or on board, slam the missing piece. ANY trigger now = instant win. Even without the combo, your drain engine + Sheoldred is closing the game fast. At 27+ life, Righteous Valkyrie makes your team enormous. Use Alseid to sacrifice for protection if they try to remove Vito in response to Exquisite Blood resolving.

### The Kill Turn
With Vito + Exquisite Blood on the battlefield:
- Play ANY creature → Soul Warden triggers → gain 1 → Vito drains 1 → Exquisite Blood gains 1 → Vito drains 1 → infinite → opponent dies
- Your draw step → Sheoldred gains 2 → same infinite loop
- Even Scoured Barrens entering → gain 1 life → infinite

---

## Key Interactions

```
STACKING DRAINS:
  2x Marauding Blight-Priest on board + Soul Warden
  → Any creature ETB = gain 1 life = each Blight-Priest triggers
  → Opponent loses 2 life per creature entering

VITO vs BLIGHT-PRIEST:
  Vito: opponent loses THAT MUCH (scales with amount)
  Blight-Priest: opponent loses 1 (flat, regardless of amount)

  Sheoldred draw: gain 2
  → Vito: opponent loses 2
  → Blight-Priest: opponent loses 1
  Vito is better with big life gains. Blight-Priest is better
  with many small triggers. Both together = maximum drain.

RIGHTEOUS VALKYRIE LIFEGAIN:
  Valkyrie on board → play Soul Warden (Cleric, 1 toughness)
  → Valkyrie triggers: gain 1 life (toughness of entering Cleric)
  → Soul Warden triggers on itself: gain 1 life
  → 2 life gained = 2 drain triggers from Vito/Blight-Priest

SHEOLDRED + EXQUISITE BLOOD (no Vito needed):
  Sheoldred: opponent draws = loses 2
  Exquisite Blood: that loss = you gain 2
  That gain = still needs Vito to loop, BUT you gain 2 life per
  opponent draw step, which feeds Voice of the Blessed counters
  and gets you to Righteous Valkyrie's 27+ threshold faster

AUTHORITY OF THE CONSULS vs AGGRO:
  Their creatures enter tapped (can't attack immediately)
  + you gain 1 life each (triggers your drain engine)
  + completely neuters haste creatures
  Essentially: opponent's aggro strategy actively kills them

PROTECTING THE COMBO:
  Scenario: Vito on board, you cast Exquisite Blood. Opponent has removal.

  WITH UNDYING MALICE (B):
  → They cast removal on Vito in response to Exquisite Blood
  → You cast Undying Malice targeting Vito (1 black mana)
  → Vito dies, immediately returns with a +1/+1 counter (now 2/4)
  → Exquisite Blood resolves → combo online → any trigger = win

  WITH KAYA'S GHOSTFORM (already on Vito):
  → They cast removal on Vito
  → Ghostform triggers automatically — Vito returns to battlefield
  → No mana needed, no response required — it just works
  → Combo fires on next trigger

  WITH ALSEID OF LIFE'S BOUNTY:
  → They target Vito with a black removal spell (Go for the Throat, etc.)
  → Sacrifice Alseid + pay W: Vito gains protection from black
  → Removal fizzles, Vito survives
  → Bonus: Alseid dying triggers Soul Warden (creature left battlefield
    and another enters? No — but it triggers Bastion of Remembrance
    if in play: opponent loses 1 life → Exquisite Blood gains 1 →
    Vito drains 1 → infinite loop starts anyway!)
```

---

## Matchups

| Matchup | Plan |
|---------|------|
| **Aggro** | Authority of the Consuls shuts down their speed. Soul Warden/Lunarch Veteran gain life off THEIR creatures, keeping you alive while Blight-Priest/Vito drain them. Cut Down handles their threats. You stabilize and out-drain them |
| **Control** | Deep-Cavern Bat strips their sweeper or counter. Sheoldred is a must-answer threat that gains value immediately. Bastion of Remembrance punishes board wipes. If they let Vito + Exquisite Blood resolve, it's over |
| **Midrange** | Your drain engine makes their creatures work against them (Soul Warden triggers). Sheoldred dominates creature mirrors with deathtouch + life swing. Go for the Throat removes their bombs. Combo kills through stalled boards |
| **Combo** | Deep-Cavern Bat disrupts their hand. Your own combo (Vito + Exquisite Blood) is faster than most. Cut Down and Go for the Throat remove combo creatures. Race them — your passive drain is aggressive |

---

## Mulligan Guide

**Keep**: 1-2 lands + Soul Warden/Lunarch Veteran + any 3-drop drain payoff (Vito, Blight-Priest, or Valkyrie)

**Dream hand**: Plains + Swamp + Soul Warden + Lunarch Veteran + Marauding Blight-Priest + Sheoldred + Concealed Courtyard

**Mulligan**: No white source (can't cast your 1-drops), no creatures, all 4+ mana cards, 5+ lands

**Priority**: Turn 1 lifegain creature is the most important play. Every turn without one is wasted drain triggers.

---

## Arena Import

```
4 Soul Warden
4 Lunarch Veteran
2 Authority of the Consuls
2 Undying Malice
1 Kaya's Ghostform
2 Alseid of Life's Bounty
2 Deep-Cavern Bat
2 Marauding Blight-Priest
2 Vito, Thorn of the Dusk Rose
3 Righteous Valkyrie
4 Sheoldred, the Apocalypse
2 Exquisite Blood
3 Cut Down
3 Go for the Throat
3 Concealed Courtyard
1 Brightclimb Pathway
1 Caves of Koilos
1 Hive of the Eye Tyrant
4 Scoured Barrens
4 Fabled Passage
6 Swamp
4 Plains
```

**Total: 60 cards** (36 spells + 24 lands)
**Wildcards needed**: ZERO — all cards confirmed in your collection

---

## Why This Beats Your Selesnya Build

| | Selesnya Heliod | Orzhov Vito Drain |
|---|---|---|
| **Combo pieces** | 3 cards (Heliod + Scurry Oak + Soul Warden) | 2 cards (Vito + Exquisite Blood) |
| **Combo consistency** | Need all 3 specific cards on board | Need only 2 + any trigger (8+ triggers in deck) |
| **Without combo** | Lifegain is slow without payoff | Passive drain kills WITHOUT combo |
| **Removal weakness** | Kill any 1 of 3 pieces = combo dead | Kill Vito = Blight-Priest still drains. Kill both = Sheoldred still dominates |
| **Sheoldred factor** | Not in Selesnya colors | 4x Sheoldred — best card in Historic |
| **Defense** | Relies on creatures to block | Authority of the Consuls shuts down attacks |

---

## Upgrade Path

### Tier 1 — High Impact (craft these first)
| Card | Rarity | Qty | Why |
|------|--------|-----|-----|
| Thoughtseize | Rare | 3x | 1 mana hand disruption. Protects your combo turn, strips their answers. THE best black 1-drop in Historic |
| Godless Shrine | Rare | 4x | WB shock land. Untapped when needed. Massively improves mana consistency |

### Tier 2 — Strong Additions
| Card | Rarity | Qty | Why |
|------|--------|-----|-----|
| Fatal Push | Uncommon | 4x | Best 1-mana removal in Historic. Replaces Cut Down with strictly better card |
| Castle Locthwain | Rare | 2x | Untapped black land that draws cards late game. Free upgrade |
| Isolated Chapel | Rare | 4x | WB check land, usually untapped. Better mana base |

### Tier 3 — Power Upgrades
| Card | Rarity | Qty | Why |
|------|--------|-----|-----|
| Bloodletter of Aclazotz | Rare | you own 1 | 1BBB for a 2/4 flier that doubles all opponent life loss. Sheoldred drain becomes 4, Vito drain doubles. Win-more but devastating |
| Vein Ripper | Mythic | you own 2 | 3BBB 6/5 flying ward. Every creature death = drain 1 + gain 1. Could replace top-end slots |

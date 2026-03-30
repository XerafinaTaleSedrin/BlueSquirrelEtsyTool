# Mono-Black Sheoldred Combo (Historic Bo1)

**Format:** Historic | **Cards:** 60 | **Colors:** B
**Archetype:** Control/Combo — Instant Kill
**Status:** Built from confirmed collection (untapped.gg export 2026-03-14)

## The Combo

```
Vito, Thorn of the Dusk Rose + Exquisite Blood = INSTANT WIN

Vito:   "Whenever you gain life, target opponent loses that much life."
Blood:  "Whenever an opponent loses life, you gain that much life."

ANY trigger starts infinite loop:
  → You gain 1 life
  → Vito: opponent loses 1 life
  → Exquisite Blood: you gain 1 life
  → Vito: opponent loses 1 life
  → ∞ → opponent dies.

Sheoldred enables BOTH directions:
  → You draw a card: gain 2 life → triggers Vito → triggers Blood → ∞
  → Opponent draws a card: they lose 2 life → triggers Blood → triggers Vito → ∞

With Sheoldred + either combo piece in play, resolving the other piece
wins the game BEFORE your opponent gets another draw step.
```

## Why This Deck

1. **Sheoldred is the best creature in Historic** — 4/5 deathtouch that punishes every draw and rewards yours
2. **Two-card infinite combo** that each piece is strong independently
3. **Mono-black = perfect mana** — never lose to color screw
4. **Every piece is strong alone:**
   - Sheoldred alone: 4+ life swing per turn cycle
   - Vito alone: turns all lifegain into damage (Sheoldred's +2 becomes +4 total)
   - Exquisite Blood alone: every removal spell heals you
5. **12 premium removal spells** keep you alive until combo assembled

## Decklist

### Creatures (8)

```
4 Sheoldred, the Apocalypse  (2BB)  — best creature in Historic, enables combo from either direction
4 Vito, Thorn of the Dusk Rose (1BB) — COMBO PIECE A: lifegain → opponent life loss
```

### Enchantments (8)

```
4 Exquisite Blood             (3BB)  — COMBO PIECE B: opponent life loss → your lifegain
4 Scavenger's Talent           (B)   — level 1: surveil 2 to find combo pieces
```

### Removal (12)

```
4 Cut Down                     (B)   — kills most early creatures
4 Infernal Grasp               (1B)  — kills anything, 2 life is irrelevant with lifegain
3 Go for the Throat             (1B)  — kills non-artifact creatures
1 Hero's Downfall              (1BB) — kills creatures AND planeswalkers
```

### Card Advantage / Tutors (7)

```
2 Sign in Blood                (BB)  — draw 2 cards (also triggers Sheoldred lifegain)
2 Beseech the Mirror           (1BBB)— TUTOR: finds whichever combo piece you're missing
2 Feed the Swarm               (1B)  — kills creatures OR enchantments (critical vs Rest in Peace)
1 Read the Bones               (2B)  — scry 2 + draw 2, deep dig for combo
```

### Lands (25)

```
1 Hive of the Eye Tyrant              — creature land, exiles from graveyard
1 Takenuma, Abandoned Mire            — channel: return creature from graveyard
1 Crawling Barrens                     — creature land for late game
22 Swamp
```

## How It Plays

### Phase 1: Survive (Turns 1-3)
Deploy Scavenger's Talent for surveil. Use Cut Down, Infernal Grasp, Go for the Throat to kill everything your opponent plays. You have 12 removal spells — use them aggressively. Your life total doesn't matter because the combo will win regardless.

### Phase 2: Establish (Turns 3-4)
- **Turn 3:** Vito, Thorn of the Dusk Rose. A 1/4 body blocks well. Now all lifegain = damage.
- **Turn 4:** Sheoldred, the Apocalypse. 4/5 deathtouch blocks everything. Now you gain 2 per draw, they lose 2 per draw. With Vito: you gain 2 → they lose 2 (Vito) → that's 4 life swing per YOUR draw step alone.

### Phase 3: Kill (Turn 5+)
- **Turn 5:** Exquisite Blood. If Vito is in play, the instant you gain ANY life or deal ANY damage, the infinite loop starts. With Sheoldred, this happens on your next draw step automatically.
- **Alternative:** Beseech the Mirror on turn 4 to find whichever piece you're missing.

### The Kill Sequence
```
Board: Sheoldred + Vito + Exquisite Blood

Your draw step:
  → Sheoldred: you gain 2 life
  → Vito: opponent loses 2 life
  → Exquisite Blood: you gain 2 life
  → Vito: opponent loses 2 life
  → Exquisite Blood: you gain 2 life
  → ∞ → opponent at 0 → you win

OR opponent's draw step:
  → Sheoldred: opponent loses 2 life
  → Exquisite Blood: you gain 2 life
  → Vito: opponent loses 2 life
  → Exquisite Blood: you gain 2 life
  → ∞ → opponent at 0 → you win
```

You don't even need to attack. You just need to pass to a draw step.

## Card Ownership

| Card | Owned | Needed | Status |
|------|-------|--------|--------|
| Sheoldred, the Apocalypse | 4 | 4 | OWNED |
| Vito, Thorn of the Dusk Rose | 4 | 4 | OWNED |
| Exquisite Blood | 4 | 4 | OWNED |
| Scavenger's Talent | 4 | 4 | OWNED |
| Cut Down | 4 | 4 | OWNED |
| Infernal Grasp | 4 | 4 | OWNED |
| Go for the Throat | 3 | 3 | OWNED |
| Hero's Downfall | 4 | 1 | OWNED |
| Sign in Blood | 3 | 2 | OWNED |
| Beseech the Mirror | 2 | 2 | OWNED |
| Feed the Swarm | 4 | 2 | OWNED |
| Read the Bones | 2 | 1 | OWNED |
| Hive of the Eye Tyrant | 1 | 1 | OWNED |
| Takenuma, Abandoned Mire | 1 | 1 | OWNED |
| Crawling Barrens | 4 | 1 | OWNED |

**Wildcards needed: 0** — Entire deck is buildable right now.

## Matchup Notes

### vs Aggro (Mono-Red, White Weenie)
- Lean on removal hard. 12 kill spells = they can't keep a board.
- Sheoldred's 4/5 deathtouch body walls everything.
- Even without combo, Sheoldred + Exquisite Blood = gain life off every removal spell you cast.
- You can combo as early as turn 5 to close before they recover.

### vs Control (Azorius, Dimir)
- Deploy threats one at a time to play around counterspells.
- Vito on 3 is the best lead — 3 mana is under Absorb range on the play, and they may not respect it.
- Sheoldred demands immediate removal or it takes over.
- Beseech the Mirror at instant speed? No, sorcery. But it finds whatever you need.
- Feed the Swarm can kill their enchantment-based hate.

### vs Midrange (Rakdos, Jund)
- Removal mirrors favor whoever has the better topend — that's you (infinite combo).
- Their Thoughtseize hurts, but you have redundancy (4x of each combo piece).
- Sheoldred mirror: whoever resolves theirs first usually wins.

### vs Graveyard Decks
- Hive of the Eye Tyrant exiles their graveyard while attacking.
- You don't rely on your graveyard at all.

## Mulligan Guide

**Snap keep:** Land + removal + either combo piece (Vito or Exquisite Blood)
**Great:** 3-4 lands + Scavenger's Talent + removal + Sheoldred or Vito
**Good:** Lands + multiple removal (control the board, draw into combo)
**Keepable:** Beseech the Mirror + 4 lands (tutor for whatever you need)
**Mulligan:** No black mana, no removal, 6+ lands, triple Exquisite Blood with no way to survive

**Key principle:** You don't need the full combo in your opener. You need to survive. The combo assembles naturally with 4x of each piece + 2 tutors + Scavenger's Talent filtering.

## MTGA Export

```
4 Sheoldred, the Apocalypse
4 Vito, Thorn of the Dusk Rose
4 Exquisite Blood
4 Scavenger's Talent
4 Cut Down
4 Infernal Grasp
3 Go for the Throat
1 Hero's Downfall
2 Sign in Blood
2 Beseech the Mirror
2 Feed the Swarm
1 Read the Bones
1 Hive of the Eye Tyrant
1 Takenuma, Abandoned Mire
1 Crawling Barrens
22 Swamp
```

## Potential Upgrades (require wildcards)

- **4x Fatal Push** (B, Uncommon) — replace Go for the Throat, better vs artifacts
- **4x Thoughtseize** (B, Rare) — proactive disruption, see their hand, strip answers
- **4x Castle Locthwain** (Rare land) — draw cards off your lands in late game
- **3x Graveyard Trespasser** (1BB, Rare) — excellent 3-drop, gains life, exiles graveyard
- **Liliana of the Veil** (1BB, Mythic) — grinds out midrange/control
- **Sorin, Imperious Bloodlord** (1BB, Rare) — can cheat Sheoldred into play turn 3

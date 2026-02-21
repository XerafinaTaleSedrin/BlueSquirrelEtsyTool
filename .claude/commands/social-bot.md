# Social Media Bot — Manual Generation

Generate weekly social media posts and/or monthly blog content for Marika Olson Consulting, running locally via Claude Code instead of API tokens.

**Argument**: $ARGUMENTS — one of: `weekly`, `blog`, or `both` (default: `weekly`)

**Repo**: `/c/Users/marik/MyProjects/marika-social-bot`

This replaces the removed cron jobs. Run on Sundays for Monday posting.

## Step 0: Sync with Remote

Pull the latest from remote before doing anything:

```bash
cd /c/Users/marik/MyProjects/marika-social-bot && git fetch origin && git pull
```

If there are local uncommitted changes, stash them first with `git stash`, pull, then `git stash pop`.

## Weekly Social Posts (5 posts, Mon–Fri)

### Step 1: Load Configuration

Read all config files:
- `config/brand.json` — company name, colors, website
- `config/pillars.json` — voice prompt, 3 content pillars, post formats, service angles
- `config/calendar.json` — weekly slots (Mon–Fri with platform assignments), pillar rotation
- `config/hashtags.json` — hashtag sets and platform rules
- `config/templates.json` — 28 content angle templates
- `config/memory.json` — generation count, topics covered, templates used, pillar index
- `config/blog.json` — check for this month's blog theme for content alignment

### Step 2: Check for Seed Content

Check if `seed/launch_calendar.json` exists and has unused weeks (compare `seed_weeks_used` in memory to available weeks). If seed weeks remain, use pre-authored content instead of generating. If seeds are exhausted, proceed with generation.

### Step 3: Determine Weekly Slots

Using `calendar.json`, build 5 post slots:

| Day | Platform | Time |
|-----|----------|------|
| Monday | Instagram | 10:00 AM PT |
| Tuesday | Instagram | 10:00 AM PT |
| Wednesday | LinkedIn | 4:30 PM PT |
| Thursday | Instagram | 10:00 AM PT |
| Friday | LinkedIn | 4:30 PM PT |

For each slot, assign a pillar from the rotation using `pillar_index` from memory, and randomly select a format from that pillar's allowed formats.

### Step 4: Generate Each Post

For each of the 5 slots, **you** generate the content in Marika's voice following:
- The `voice_prompt` from `pillars.json`
- The assigned pillar's tone, description, and CTA style
- The selected format's structure (quote_card, carousel, personal_reflection, or announcement_cta)
- A content angle template from `templates.json` (avoid recently used ones from `memory.json`)
- Platform rules: Instagram = 150-300 word caption + 8-12 hashtags; LinkedIn = 300-600 words + 3-5 hashtags
- Monthly blog theme alignment if available (reference blog topic from complementary angle)
- Avoid topics already in `memory.json` `topics_covered`

**Format-specific output:**

**quote_card**: `quote_text` (1-2 punchy sentences), `caption`, `hashtags`, `topic_summary`

**carousel**: `slides` (4-6 slides with hook/content/CTA), `caption`, `hashtags`, `topic_summary`

**personal_reflection**: `key_line` (one strong line for image), `caption` (200-400 words), `hashtags`, `topic_summary`

**announcement_cta**: `headline`, `body_text`, `cta_text`, `caption`, `hashtags`, `topic_summary`

Save the full set to `output/posts.json` as a JSON array.

### Step 5: Render Graphics & Preview

Run the graphics renderer and preview builder:

```bash
cd /c/Users/marik/MyProjects/marika-social-bot && python -c "
import sys; sys.path.insert(0, 'scripts')
from create_graphics import render_all
from build_preview import build_preview
render_all('output/posts.json')
build_preview()
"
```

Report which images were generated.

### Step 6: Update Memory

Update `config/memory.json`:
- Increment `generation_count`
- Set `last_generated` to now
- Append to `posts_generated` with week number, date, source ("local"), post count
- If seed content was used, increment `seed_weeks_used`
- Otherwise, advance `pillar_index` by 2 (mod 5)
- Append used template IDs to `templates_used` (keep last 15)
- Append topic summaries to `topics_covered` (keep last 50)

### Step 7: Commit and Push

```bash
cd /c/Users/marik/MyProjects/marika-social-bot && git add config/memory.json output/ && git commit -m "Weekly social generation #N (YYYY-MM-DD) — local" && git push
```

---

## Monthly Blog Post

Only run this if `$ARGUMENTS` is `blog` or `both`. Check `config/blog.json` calendar for the current month's entry. Skip if this month has already been completed (check `blog_months_completed` in memory).

### Step 1: Load Blog Config

Read `config/blog.json` for:
- The 6-part blog structure (Hook, Pattern, Evidence, Honest Part, When to Get Help, CTA)
- SEO requirements (800-1500 words, keyword placement, meta description)
- This month's calendar entry (title, keywords, type)

### Step 2: Check for Seed Blog

If the calendar entry has `seed: true`, look for a pre-written draft in `seed/blog_drafts/`. Use it if found.

### Step 3: Write the Blog Post

Write the full blog post **in Marika's voice** following:
- The `voice_prompt` from `blog.json`
- The 6-part structure with target word counts for each section
- SEO requirements: target keyword in title, first paragraph, and at least one H2
- Include a 150-160 character meta description
- Focus on the service type specified (operations, web_design, or integration)

Save to `output/blog/SLUG.md` as clean markdown.

### Step 4: Generate 4 Derivative Social Posts

Create derivative social content from the blog:

1. **Tuesday Instagram** — Quote card teaser. Pull a key insight and create a visual quote + short caption pointing to the blog.
2. **Wednesday LinkedIn** — 300-500 word excerpt that stands alone as a valuable insight, with link to full post.
3. **Thursday Instagram** — 3-5 slide carousel distilling the blog's key points into scannable slides.
4. **Friday LinkedIn** — 300-400 word discussion post with an audience question, inspired by the blog topic.

Save to `output/blog/blog_social_posts.json`.

### Step 5: Render Graphics & Preview

```bash
cd /c/Users/marik/MyProjects/marika-social-bot && python -c "
import sys; sys.path.insert(0, 'scripts')
from create_graphics import render_all
from build_preview import build_blog_preview
render_all('output/blog/blog_social_posts.json')
build_blog_preview()
"
```

### Step 6: Update Memory

Update `config/memory.json`:
- Increment `blog_posts_generated`
- Add current month to `blog_months_completed`

### Step 7: Commit and Push

```bash
cd /c/Users/marik/MyProjects/marika-social-bot && git add config/memory.json output/ && git commit -m "Monthly blog generation (YYYY-MM) — local" && git push
```

---

## Summary

After completing, report:
- Which mode was run (weekly/blog/both)
- For weekly: list all 5 posts with day, platform, pillar, format, and topic summary
- For blog: post title and derivative post summaries
- Whether graphics rendered and preview built
- Whether the push succeeded
- Remind the user to review `output/preview.html` before posting

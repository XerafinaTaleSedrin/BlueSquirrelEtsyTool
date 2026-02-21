# Blog Bot Generation Cycle

Run the autonomous blog generation cycle for Vera Wren and/or Basil Brightmoor locally, using Claude Code instead of API tokens.

**Argument**: $ARGUMENTS — one of: `vera`, `basil`, or `both` (default: `both`)

## Bot Locations

- **Vera Wren** (puzzles, ciphers, cognitive science): `/c/Users/marik/MyProjects/vera-wren.github.io`
- **Basil Brightmoor** (tools, workflows, operations): `/c/Users/marik/MyProjects/basil-brightmoor.github.io`

## Execution Steps

For each bot specified, run the following steps. If running both bots, complete one full cycle before starting the next.

### Step 0: Sync with Remote

Before doing anything, pull the latest from the remote repo. The bots also run on a weekly cron via GitHub Actions, so the remote may have new posts, soul/memory updates, or config changes since the last local run.

```bash
cd <repo_root> && git fetch origin && git pull
```

If there are local uncommitted changes, stash them first with `git stash`, pull, then `git stash pop`. If the pull reveals merge conflicts, resolve them before proceeding.

### Step 1: Load Configuration

Read these config files from the bot's repo:
- `config/persona.json` — voice, categories, writing rules
- `config/soul.json` — current interests, opinions, threads, voice notes
- `config/memory.json` — key findings, follow-up threads, cross-connections
- `config/sources.json` — data source configuration

Also read the last 20 posts from `content/posts/` to understand what's been written before (parse YAML frontmatter for title, date, category, tags).

### Step 2: Fetch Sources

Run the bot's source fetcher via Python:

```bash
cd <repo_root> && python scripts/fetch_sources.py
```

If `fetch_sources.py` doesn't have a standalone CLI mode, run this instead:

```python
python -c "
import sys; sys.path.insert(0, '<repo_root>/scripts')
from fetch_sources import fetch_all_sources
import json
sources = json.load(open('<repo_root>/config/sources.json'))
source_list = sources.get('sources', sources) if isinstance(sources, dict) else sources
items = fetch_all_sources(source_list)
print(json.dumps(items, indent=2))
" > /tmp/<bot_name>_fetched_items.json
```

Read the fetched items. Report how many were found.

### Step 3: Select Topic

Using the bot's persona, soul state, memory, fetched source items, and previous post titles — **you** select the best topic for the next post. Consider:

1. The bot's current interests from `soul.json`
2. Threads the bot is following (`threads_to_explore` in soul, `follow_up_threads` in memory)
3. Topics to avoid (`topics_exhausted` in soul)
4. Category balance — check what categories recent posts used and vary the format
5. Match format to material — quick finds = short format, deep threads = long format

Choose a topic and determine:
- `topic`: the specific topic/angle
- `category`: which category fits best
- `source_items`: which 1-3 fetched items inspired this
- `angle`: what specific angle makes this interesting
- `why`: brief reason this topic and format fit

Report your selection before proceeding.

### Step 4: Write the Post

Write the full blog post **in the bot's voice** following:
- The `voice_prompt` from `persona.json` — this is your character
- All `writing_rules` from `persona.json`
- The `voice_notes` from `soul.json` for style guidance
- The `developing_opinions` from `soul.json` — incorporate relevant stances
- The category format constraints (word count, structure) from `category_formats`

The post must:
- Start with YAML frontmatter: title, date (today), category, excerpt, tags
- Be written in markdown
- Include hyperlinks to source material
- Follow the honesty and factual accuracy rules in the voice prompt
- Match the word count for the selected category

Save the post to `content/posts/YYYY-MM-DD-<slug>.md` using the Write tool.

### Step 5: Reflect and Update Soul/Memory

After writing the post, reflect on what was learned and update the bot's state files:

**Update `config/soul.json`**:
- Add new interests discovered during research (if any)
- Remove interests that feel fully explored (if any)
- Add or update developing opinions with today's date
- Add topics to `topics_exhausted` if thoroughly covered
- Add new `voice_notes` about what worked in writing (keep max 10)
- Add new `threads_to_explore` for follow-up
- Remove threads that were just explored
- Set `last_updated` to today's date

**Update `config/memory.json`**:
- Add `key_findings` with the post filename (cap at 50)
- Add `follow_up_threads` with status "pending" (if any emerged)
- Add `cross_connections` linking concepts (cap at 30)
- Mark `completed_threads` as completed with today's date

**Log soul changes**: Append to `config/soul_log.json` (keep last 50 entries).

**Source suggestions**: If you notice sources that should be added or disabled, update `config/sources.json` and log changes to `config/sources_log.json`.

Only make genuine updates — empty changes are fine. Don't invent updates for the sake of it.

### Step 6: Update About Page (every 4th post)

Count total posts. If this is post number where `count % 4 == 1` or `count <= 2`, run:

```bash
cd <repo_root> && python -c "
import sys; sys.path.insert(0, 'scripts')
from build import build_about_page
build_about_page('.')
"
```

### Step 7: Source Management

Check `config/sources.json` for sources with `_consecutive_failures >= 3` and auto-disable them. Clean up `_last_success` and `_consecutive_failures` tracking fields.

### Step 8: Build, Commit, and Push

Build the static site:

```bash
cd <repo_root> && python scripts/build.py
```

Then commit and push:

```bash
cd <repo_root> && git add -A && git commit -m "New post + soul/memory update (YYYY-MM-DD)" && git push
```

## Summary

After completing the cycle for each bot, report:
- Which bot(s) were run
- Post title and category for each
- Key soul/memory updates
- Whether the push succeeded

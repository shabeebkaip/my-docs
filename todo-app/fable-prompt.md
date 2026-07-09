# Prompt: Todo App + Reminders (for Claude Fable 5)

Use this as a standalone prompt to hand off or continue this setup elsewhere.

## Context

I keep a simple file-based todo system instead of Microsoft To Do or Todoist (connector wouldn't connect). It lives in this folder:

`Shab.co/my-docs/todo-app/`

Two files:
- `todos.md` — single source of truth. Checklist format with two sections, `## Open` and `## Completed`, using `- [ ]` and `- [x]` markdown checkboxes.
- `index.html` — a read-only, styled snapshot view of `todos.md` (warm/neutral color palette, rounded card layout, open items as unchecked boxes, completed items struck through). Regenerated from `todos.md` any time it changes — same CSS/structure, just refresh the two `<ul>` lists.

## What I need you to do

1. Read `todos.md`, understand current open/completed items.
2. When I tell you to add a todo, append `- [ ] <task>` under `## Open`.
3. When I tell you something is done, move that line to `## Completed`, changing `- [ ]` to `- [x]`.
4. After any change to `todos.md`, regenerate `index.html` to match (same look, updated content).
5. Keep confirmations brief — 1-3 sentences, no headers or bullet lists in chat replies.

## Reminder schedule (recreate if this is a new environment)

Three recurring reminders, each following the read → ask → update file → regenerate HTML → confirm flow above:

- **9:00 AM** — ask what I want to get done today; append new items to `## Open`.
- **1:00 PM** — show current open items; ask what's done or needs reprioritizing; update accordingly.
- **6:00 PM** — evening wrap-up; ask what got finished and what should roll over to tomorrow.

If setting these up fresh, use a scheduling tool with cron `0 9 * * *`, `0 13 * * *`, and `0 18 * * *` (local time), each pointing at this same `todos.md` / `index.html` pair.

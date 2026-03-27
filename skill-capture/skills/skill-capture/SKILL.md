---
name: skill-capture
description: Convert a conversation or workflow into a versioned, reusable skill. Detects reusable patterns in chat, scaffolds skill directories, writes SKILL.md with proper frontmatter, and maintains a capture log. Use when the user says "turn this into a skill", "save this workflow", "make this reusable", or invokes /skill-capture.
---

# Skill Capture

Convert any conversation or workflow into a durable, reusable skill.

## Trigger

- Manual: `/skill-capture` or "turn this into a skill" or "save this workflow"
- Automatic: When a request implies reusable behavior (e.g., "remember this workflow", "document this process")

## What This Does

Most people don't know how to go from "I just did something useful" to "I have a reusable workflow." This skill automates that transition:

1. **Detects** the reusable pattern in your conversation
2. **Extracts** the core workflow steps
3. **Scaffolds** a proper skill directory
4. **Writes** a SKILL.md with frontmatter and instructions
5. **Logs** the capture for traceability

## Workflow

### Step 1: Identify the Pattern

Analyze the conversation or workflow to extract:

- **Name:** What is this skill called? (lowercase, hyphens, verb-led)
- **Trigger:** What does the user say to invoke it?
- **Inputs:** What information does this skill need?
- **Steps:** What is the fixed process?
- **Outputs:** What does it produce?
- **Edge cases:** What can go wrong? How to handle it?

### Step 2: Validate Uniqueness

Check if a skill with this name already exists:

```bash
ls skills/<slug>/SKILL.md 2>/dev/null
```

- **Exists:** Update in place (preserve intent, fix issues)
- **Missing:** Scaffold new skill

### Step 3: Scaffold the Skill

Create the directory structure:

```
skills/<slug>/
├── SKILL.md          # Core instructions (required)
├── scripts/          # (optional) Executable code
├── references/       # (optional) Documentation for context
└── assets/           # (optional) Templates, images
```

### Step 4: Write SKILL.md

Write the skill file with proper structure:

```markdown
---
name: <slug>
description: <What it does + when to trigger it>
---

# <Skill Name>

<One paragraph explaining what this skill does and why it exists.>

## Trigger

- Manual: `/<slug>` or "<natural language trigger>"
- Automatic: <when it should fire on its own>

## Inputs

- Required:
  - <input 1>
  - <input 2>
- Optional:
  - <input 3>

## Workflow

### Step 1: <Step Name>
<What to do>

### Step 2: <Step Name>
<What to do>

[... continue for all steps]

## Output Format

<What the skill produces>

## Error Handling

<What can go wrong and how to recover>

## Quality Standards

<What "done" looks like>
```

### SKILL.md Writing Rules

1. **Frontmatter is the trigger mechanism** — The `description` field is how Codex decides when to use the skill. Make it comprehensive. Include both what it does AND when to use it.

2. **Body is for instructions only** — The body only loads after the skill triggers. Don't put "when to use" information in the body — it won't help.

3. **Use imperative form** — "Run this", "Check that", "Write the file". Not "You should run this" or "This skill runs this".

4. **Keep it under 500 lines** — If it's getting long, move details to `references/` files. Context window is shared with everything else.

5. **Include concrete examples** — Prefer short, real examples over verbose explanations.

6. **Set appropriate freedom** — Match specificity to fragility:
   - **High freedom** (text instructions): When multiple approaches work
   - **Medium freedom** (scripts with parameters): When a preferred pattern exists
   - **Low freedom** (specific scripts): When operations are error-prone

### Step 5: Log the Capture

Append to the capture log:

```markdown
## <slug> — YYYY-MM-DD

- **Trigger:** <what the user said>
- **Source:** <conversation or file>
- **Files created:**
  - `skills/<slug>/SKILL.md`
- **Invocation example:** `/<slug> <example args>`
```

### Step 6: Report

Return to the user:
- All file paths created/updated
- One invocation example
- Any decisions made (e.g., "merged with existing skill" or "created new")

## Drift Guardrails

- **One skill per command alias** — Don't create duplicate versions unless explicitly requested
- **Always persist to files** — Never keep the workflow only in chat
- **Report failures immediately** — If any write fails, report the exact path and stop
- **Don't over-engineer** — A 20-line SKILL.md is better than a 200-line one that tries to cover every edge case

## Naming Conventions

- Lowercase letters, digits, and hyphens only
- Verb-led: `daily-briefing`, `scrape-transcript`, `audit-writing`
- Under 64 characters
- Namespace by tool when it helps: `gh-issues`, `notion-query`

## Related Skills

- `skill-auditor` — Review skills for quality

---
name: skill-auditor
description: Review existing skills for quality, completeness, and spec compliance. Checks frontmatter, context efficiency, progressive disclosure, and adherence to the skill spec. Use when the user says "audit this skill", "review my skill", "improve this skill", or wants quality feedback on a SKILL.md.
---

# Skill Auditor

Review skills for quality, completeness, and spec compliance.

## Trigger

- Manual: "audit this skill", "review my skill", "improve this skill"
- Post-capture: Run after `skill-capture` to validate the new skill

## What This Checks

### 1. Frontmatter Quality

| Check | Pass Criteria |
|-------|--------------|
| `name` exists | Present, lowercase, hyphens, under 64 chars |
| `description` exists | Present, describes what + when to trigger |
| Description triggers | Would Codex correctly identify when to use this? |
| No extra frontmatter | Only `name` and `description` fields |

### 2. Body Quality

| Check | Pass Criteria |
|-------|--------------|
| Imperative form | "Run this" not "You should run this" |
| Under 500 lines | Body is concise |
| No "when to use" in body | That belongs in description, not body |
| Concrete examples | Has at least one real example |
| Progressive disclosure | Large details moved to references/ |

### 3. Directory Structure

| Check | Pass Criteria |
|-------|--------------|
| SKILL.md exists | Required file present |
| No extra docs | No README.md, CHANGELOG.md, etc. in skill dir |
| Scripts tested | Scripts have been run and produce correct output |
| References referenced | Any references/ files are linked from SKILL.md |
| Assets appropriate | Assets are output files, not docs |

### 4. Context Efficiency

| Check | Pass Criteria |
|-------|--------------|
| No redundancy | Information lives in one place, not duplicated |
| Right level of specificity | Matches task fragility (high/medium/low freedom) |
| Lean body | Only essential info in SKILL.md body |
| Searchable references | Large reference files have table of contents |

### 5. Workflow Completeness

| Check | Pass Criteria |
|-------|--------------|
| Trigger defined | Clear trigger phrases listed |
| Inputs specified | Required vs optional inputs documented |
| Steps are deterministic | Each step has clear start/end criteria |
| Output format defined | User knows exactly what they'll get |
| Error handling | Known failure modes documented |
| Quality standards | "Done" criteria defined |

## Workflow

### Step 1: Read the Skill

Load `skills/<slug>/SKILL.md` and scan the skill directory.

### Step 2: Run Checks

Evaluate against all 5 categories above.

### Step 3: Score and Report

Output format:

```
## SKILL AUDIT: <slug>

### Score: X/10

### Passes
- ✓ [Check name]

### Issues
- ✗ [Check name]: [What's wrong + how to fix]

### Suggestions
- [Improvement idea 1]
- [Improvement idea 2]

### Quick Fixes
[Specific edits to make right now]
```

### Step 4: Apply Fixes (Optional)

If the user approves, apply the suggested fixes:
- Rewrite frontmatter
- Restructure body
- Move content to references/
- Add missing sections

## Quality Standards

1. **Honest** — Don't inflate scores or skip issues
2. **Specific** — Quote exact text that needs changing
3. **Actionable** — Every issue has a concrete fix
4. **Prioritized** — Most impactful fixes first

## Related Skills

- `skill-capture` — Create new skills (upstream)

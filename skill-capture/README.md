# Skill Capture

The tool that builds tools. Turn workflows into reusable skills.

## What's Inside

**2 skills + 1 scaffold script.**

### Skill Capture
Detects reusable patterns in your conversations and converts them into proper skill directories. Extracts the workflow, writes SKILL.md with frontmatter, and maintains a versioned capture log. Most people don't know how to go from "I just did something useful" to "I have a reusable workflow." This automates that transition.

### Skill Auditor
Reviews existing skills for quality. Checks frontmatter completeness, context efficiency, progressive disclosure, workflow completeness, and adherence to the skill spec. Outputs a score with specific, actionable fixes.

### skill-init.sh
Standalone bash script to scaffold a new skill directory with a SKILL.md template. `bash skill-init.sh my-skill --description "Does X"`.

## Quick Start

### Create a new skill
```
bash scripts/skill-init.sh my-skill --description "Does X when triggered by Y"
```

### Capture from conversation
Just say "turn this into a skill" after completing a workflow. The capture skill will:
1. Identify the reusable pattern
2. Scaffold the directory
3. Write the SKILL.md
4. Log the capture

### Audit an existing skill
Say "audit this skill" and point to any SKILL.md file.

## The Problem This Solves

Every Codex power user eventually discovers the same thing: they keep rewriting the same prompts, the same workflows, the same scripts. The solution is skills — but creating them is a manual, error-prone process that most people skip.

This plugin makes skill creation automatic:
- **After any useful conversation** → "Turn this into a skill"
- **Before sharing a workflow** → "Audit this skill"
- **When starting from scratch** → `bash scripts/skill-init.sh <name>`

## Skill Quality Checklist

When the auditor reviews your skills, it checks:

| Category | What It Checks |
|----------|---------------|
| Frontmatter | name, description, trigger accuracy |
| Body | imperative form, under 500 lines, concrete examples |
| Structure | no extra docs, references linked, assets appropriate |
| Efficiency | no redundancy, right specificity, lean body |
| Workflow | triggers, inputs, steps, outputs, errors, quality bar |

## Origin

Built from a production skill-capture workflow that has created 30+ skills. The auditor checks come from the official Codex skill-creator spec. The scaffold script produces spec-compliant skill directories out of the box.

## License

MIT

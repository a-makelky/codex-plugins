#!/usr/bin/env bash
# skill-init.sh — Scaffold a new skill directory with SKILL.md template
# Usage: bash skill-init.sh <skill-name> [--description "One line description"]
set -euo pipefail

SKILL_NAME="${1:-}"
DESCRIPTION="${2:-TODO: Add description}"

if [[ -z "$SKILL_NAME" ]]; then
  echo "Usage: bash skill-init.sh <skill-name> [--description 'description']"
  echo "Example: bash skill-init.sh daily-briefing --description 'Daily intelligence briefing with schedule, weather, and markets'"
  exit 1
fi

# Validate name: lowercase, hyphens, digits only
if ! echo "$SKILL_NAME" | grep -qE '^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$'; then
  echo "ERROR: Skill name must be lowercase letters, digits, and hyphens only."
  echo "Got: $SKILL_NAME"
  exit 1
fi

if [[ "${2:-}" == "--description" ]]; then
  DESCRIPTION="${3:-TODO: Add description}"
fi

SKILL_DIR="./skills/${SKILL_NAME}"

if [[ -d "$SKILL_DIR" ]]; then
  echo "Skill directory already exists: $SKILL_DIR"
  exit 1
fi

mkdir -p "$SKILL_DIR"

cat > "$SKILL_DIR/SKILL.md" <<EOF
---
name: ${SKILL_NAME}
description: ${DESCRIPTION}
---

# $(echo "$SKILL_NAME" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')

TODO: Add one paragraph explaining what this skill does and why it exists.

## Trigger

- Manual: \`/${SKILL_NAME}\` or "<natural language trigger>"
- Automatic: <when it should fire on its own>

## Inputs

- Required:
  - <input 1>
- Optional:
  - <input 2>

## Workflow

### Step 1: <Step Name>

TODO: Describe the first step.

### Step 2: <Step Name>

TODO: Describe the second step.

## Output Format

TODO: Define what this skill produces.

## Error Handling

TODO: Document known failure modes and recovery steps.

## Quality Standards

1. TODO: Define what "done" looks like
EOF

echo "Scaffolded: ${SKILL_DIR}/SKILL.md"
echo "Next: Edit SKILL.md with your workflow, then run skill-auditor to validate."

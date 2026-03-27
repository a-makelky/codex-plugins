# Content Flywheel

Raw notes in, publish-ready posts out. A complete content production system.

## What's Inside

**6 skills, 1 pipeline.**

### Content Intake
Scans your notes, transcripts, and research for post-worthy ideas. Extracts key insights and creates Hopper files with 2-3 content angles each.

### Content Writer
Drafts content in your authentic voice using a voice guide. Handles raw notes, transcripts, rough drafts, or topic outlines. Outputs platform-formatted drafts.

### AI Writing Audit
Catches 16+ categories of AI writing patterns: clichés, inflated phrases, weasel words, false balance, empty modifiers, marketing fluff, and more. Outputs flagged issues with corrections.

### LinkedIn Hook Writer
Generates 10 pattern-breaking hooks using 5 techniques: contradiction, specific numbers, direct accusation, stolen thought, and absurd reframe. Character-counted for LinkedIn.

### Content Flywheel (Orchestrator)
Ties it all together. Scans the Hopper, runs the full pipeline (draft → audit → hooks), packages everything into a single publish-ready file, and moves it to the Forge.

### Garrison Queue
Manages your posting queue. Move content from Forge to ready-to-post, track what's been published, and archive completed posts.

## The Pipeline

```
Hopper (raw input) → Intake → Writer → Audit → Hooks → Forge (review) → Garrison (queue) → Archives (posted)
```

Each skill works standalone. The pipeline is where they compound.

## Quick Start

1. Create a `voice-guide.md` from the template in `references/`
2. Drop raw notes into the `hopper/` directory
3. Run `/content-flywheel` to process
4. Review the output in `forge/`
5. Move to queue with "move [topic] to queue"
6. Post, then "mark [topic] posted" to archive

## Directory Structure

```
content-flywheel/
├── hopper/            # Drop raw notes here
├── hopper/processed/  # Consumed inputs
├── forge/             # Drafted + audited + hooked
├── garrison/          # Ready to post
└── archives/          # Posted content
```

## Origin

Built from a production content pipeline that runs daily. The audit categories come from analyzing 100+ AI-generated drafts. The hook techniques come from Ruben Hassid's framework. The voice-guide approach comes from 6 months of iterating on authentic writing with AI.

## License

MIT

# Oracle PPTX Agent Skill

Create Oracle-compliant PowerPoint presentations following FY26 brand guidelines (v8.5).

## Quick Info

- **Version**: 1.0.0
- **Oracle Template Version**: FY26 v8.5 (January 2026)
- **Default Theme**: Dark (OCI/Database branding)
- **Skill Size**: ~32MB (includes all fonts, icons, templates)

## What's Included

- ✅ Complete Oracle brand guidelines
- ✅ Dark and Light theme templates (51 + 55 slides)
- ✅ Oracle Sans Tab fonts
- ✅ 1,060+ Oracle icons (dark/light themes)
- ✅ Python scripts for template manipulation
- ✅ OOXML validation utilities
- ✅ Pre-generated template inventories
- ✅ Example workflows

## Usage

Read `SKILL.md` for complete documentation.

**Quick Start**:
1. Select theme (Dark/Light)
2. Plan content and map to layouts
3. Use `scripts/rearrange.py` to build presentation
4. Use `scripts/inventory.py` to extract placeholders
5. Create replacement JSON with content
6. Use `scripts/replace.py` to populate slides
7. Validate Oracle brand compliance

## Directory Structure

```
skills/oracle-pptx/
├── SKILL.md              # Complete skill documentation (READ THIS FIRST)
├── README.md             # This file
├── scripts/              # Python utilities
├── ooxml/                # OOXML manipulation
├── resources/            # All resources (self-contained)
│   ├── fonts/            # Oracle Sans Tab fonts
│   ├── icons/            # Oracle icons (dark/light)
│   ├── templates/        # PPTX templates + inventories
│   └── guidelines.md     # Oracle brand guidelines
└── examples/             # Example workflows
```

## Self-Contained Design

This skill is **completely self-contained**:
- ❌ No external dependencies
- ❌ No references to files outside skill directory
- ✅ All resources bundled
- ✅ Portable (copy/move without breaking)
- ✅ Version controlled

## Resource Provenance

All resources copied from reference sources:
- Scripts: `reference/skills/pptx/`
- Fonts: `reference/resources/fonts/`
- Icons: `reference/resources/icons/`
- Templates: `reference/resources/templates/`
- Guidelines: `reference/guidelines/`

## Requirements

- Python 3.x
- PowerPoint desktop app (for editing/presenting)
- Oracle Sans Tab fonts installed (included in `resources/fonts/`)

## Support

For Oracle brand questions, contact Oracle Brand Team.

For skill usage, refer to `SKILL.md`.

---
name: oracle-pptx
description: "Create Oracle-compliant PowerPoint presentations following Oracle brand guidelines. Supports Dark (default) and Light themes with OCI/Database branding. Use when creating Oracle presentations, slides, or decks that must follow Oracle design standards."
---

# Oracle PPTX Creation

## Overview

Create professional PowerPoint presentations that strictly follow Oracle's FY26 brand guidelines. All resources self-contained—no external dependencies.

**Current version**: Oracle FY26 templates (v8.5, January 2026)

**When to use**: Creating Oracle-branded presentations, slides, or decks for events, meetings, or documentation.

**Templates**:
- **Dark theme** (default): Large live events, formal presentations (51 layouts)
- **Light theme**: Virtual events, documentation, internal meetings (55 layouts)

## ⚠️ BEFORE YOU START - READ THESE FIRST

**CRITICAL - Read these guidelines BEFORE creating presentations:**

1. **`resources/guidelines.md`** - Complete Oracle design standards, color palettes, typography
2. **`resources/brand-compliance.md`** - Oracle brand requirements, compliance rules

These documents contain essential Oracle brand requirements that MUST be followed. Skipping them will result in non-compliant presentations.

---

## Quick Start

### Step 1: Plan Your Presentation

Examine template inventory to identify available layouts:

```bash
# View all layouts with descriptions
cat resources/templates/dark-inventory.json | jq 'to_entries | map({slide: .key, title: .value["shape-0"].paragraphs[0].text})'
```

**Key layout types** (find actual slide numbers in inventory):
- Cover slides
- Speaker introduction slides
- Section dividers (title-only)
- Title + Body (bullet lists)
- 2-column layouts
- 3-column layouts
- Bold statement/impact slides
- Statistics/timeline slides
- Thank you/closing

### Step 2: Create Slide Structure

Use `rearrange.py` to build your presentation with selected slide numbers:

```bash
python scripts/rearrange.py \
  resources/templates/dark-template.pptx \
  working.pptx \
  0,16,12,16,17,30,12,16,18,39
```

Example sequence breakdown:
- 0: Cover
- 16: Title + Body (bullets)
- 12: Divider
- 17: 2-column
- 30: Bold statement
- 39: Thank you

### Step 3: Generate Content Inventory

Extract placeholder structure from your working presentation:

```bash
python scripts/inventory.py working.pptx inventory.json
```

Review `inventory.json` to understand:
- Shape IDs for each slide
- Placeholder dimensions (width, height)
- Default text/formatting
- Placeholder types (TITLE, BODY, etc.)

### Step 4: Create Content JSON

Build replacement JSON matching the inventory structure:

```json
{
  "slide-0": {
    "shape-0": {
      "paragraphs": [{"text": "Presentation Title", "bold": true}]
    },
    "shape-1": {
      "paragraphs": [{"text": "Subtitle goes here"}]
    }
  },
  "slide-1": {
    "shape-0": {
      "paragraphs": [{"text": "Section Title", "bold": true}]
    },
    "shape-2": {
      "paragraphs": [
        {"text": "First key point", "bullet": true, "level": 0},
        {"text": "Second key point", "bullet": true, "level": 0},
        {"text": "Third key point", "bullet": true, "level": 0}
      ]
    }
  }
}
```

**CRITICAL - Avoid common errors:**
- ❌ Do NOT populate footer shapes - footers are automatic
- ❌ Do NOT use timeline/statistics layouts without actual data
- ❌ Do NOT use emoji icons - use professional icons from library

### Step 5: Apply Content

Replace placeholder text with your content:

```bash
python scripts/replace.py working.pptx content.json final.pptx
```

**Auto-fix feature**: The script automatically adjusts font sizes and spacing if content overflows placeholders. Write full, detailed content—formatting is optimized automatically.

---

## Critical Rules

**⚠️ REMINDER:** Have you read `resources/guidelines.md` and `resources/brand-compliance.md`? These are REQUIRED reading.

### Footer Handling (MOST COMMON ERROR)

**Footers are AUTOMATIC - never add manually:**

**Year Token:** Template footers contain `{YEAR}` tokens that are automatically replaced with the current year (following Claude agent skills best practices for time-sensitive content).

✅ **CORRECT** - Leave footer shapes empty:
```json
{
  "slide-N": {
    "shape-0": {"paragraphs": [{"text": "Title"}]},
    "shape-1": {"paragraphs": [{"text": "Content"}]}
    // Footer shapes NOT included - template handles automatically with current year
  }
}
```

❌ **WRONG** - Manual footer causes duplicates/issues:
```json
{
  "slide-N": {
    "shape-0": {"paragraphs": [{"text": "Title"}]},
    "shape-X": {"paragraphs": [{"text": "Copyright © 2026..."}]}  // ❌ HARDCODED YEAR
  }
}
```

**Why footers fail:**
1. Footer shape ID included in replacement JSON → duplicate/floating footer
2. Using wrong slide layouts → footer doesn't render
3. Manual text added → conflicts with template default

**Fix**: Remove ALL footer shape entries from replacement JSON. Template copyright footers appear automatically.

### Layout Selection

**Match content to appropriate layouts** (check inventory for slide numbers):

**AVOID these patterns:**
- ❌ All bullet lists (boring, unprofessional)
- ❌ Same layout repeated 5+ times
- ❌ Speaker slides in middle of content
- ❌ Timeline/statistics slides without data
- ❌ Empty placeholders

**PREFER varied layouts:**
- ✅ Mix: bullets, 2-column, 3-column, bold statements
- ✅ Section dividers every 4-6 content slides
- ✅ Image/visual slides for impact
- ✅ Statistics slides ONLY with actual numbers

### Icon Usage (NEW REQUIREMENT)

**Use professional icons from library - NEVER emoji:**

✅ **CORRECT** - Reference library icons:
```
"Cloud Migration" → Reference OCI Migration icon (see ICON-LIBRARY.md)
"Data Analytics" → Reference Analytics icon (Business category)
"Customer Experience" → Reference CX icon (Customer category)
```

❌ **WRONG** - Emoji icons unprofessional:
```
"💰 Finance" → Use Analytics icon instead
"📊 Dashboard" → Use Data-Engineering icon instead
"🎯 Goals" → Use Target/Arrow icon instead
```

**Icon library**: 1,078 professional SVG icons organized by category
**See**: `resources/icons/ICON-LIBRARY.md` for complete catalog with search

### Content Quality

**For professional presentations:**
- 3-5 bullets per slide (not more)
- 8-12 words per bullet
- Vary sentence structure
- Use action verbs
- Avoid jargon overload

**Multi-column layouts:**
- 2-3 items per column
- Parallel structure across columns
- Headers + supporting points
- Max 35 characters per bullet in narrow columns

## Advanced Features

### Layout Reference Files

**Detailed layout guidance** → See `resources/templates/layout-mapping.md`
**Common patterns** → See examples in `examples/` directory

### Scripts Reference

**Core scripts** (all include `--help`):

```bash
python scripts/rearrange.py --help   # Build slide structure
python scripts/inventory.py --help   # Extract placeholders
python scripts/replace.py --help     # Apply content
```

### Template Inventories

**Pre-generated inventories available:**
- `resources/templates/dark-inventory.json` (51 slides)
- `resources/templates/light-inventory.json` (55 slides)

Use these to understand layout structure without generating new inventories.

## Validation Checklist

Before finalizing presentations:

**Brand compliance:**
- [ ] Oracle Sans Tab fonts used
- [ ] Footer shows: "Copyright © 2026, Oracle and/or its affiliates"
- [ ] Colors from Oracle palette only
- [ ] No emoji - professional icons only

**Content quality:**
- [ ] Varied layouts (not all bullets)
- [ ] No text overflow or cutoff
- [ ] All placeholders filled (no empties)
- [ ] 3-5 bullets max per slide

**Technical:**
- [ ] No speaker slides in content sections
- [ ] Section dividers at topic transitions
- [ ] Statistics slides have actual data
- [ ] Footers automatic (not manual)

## Troubleshooting

### Common Issues

**Footer not showing:**
- Check you're using content layouts (not dividers/special slides)
- Verify footer shapes NOT in replacement JSON
- Confirm using official dark/light template

**Timeline slide appears empty:**
- Timeline layout requires specific data structure
- Use standard bullet or bold statement layouts instead
- Check `layout-mapping.md` for timeline usage

**Text overflow errors:**
- Auto-fix adjusts fonts automatically (9pt minimum)
- If persistent, content genuinely too long for placeholder
- Split into multiple slides or use wider layout

**Wrong layout selected:**
- Check `dark-inventory.json` for actual slide numbers
- Layout numbers change between template versions
- Don't hardcode slide numbers—examine inventory first

## Resources

**⚠️ MUST READ BEFORE GENERATING:**
- **`resources/guidelines.md`** - Complete Oracle design standards (REQUIRED)
- **`resources/brand-compliance.md`** - Oracle brand requirements (REQUIRED)

**Reference Materials:**
- **`resources/icons/ICON-LIBRARY.md`** - 540 professional icons with filenames
- **`resources/icons/icon-index.json`** - Machine-readable icon index for scripts
- **`resources/templates/layout-mapping.md`** - Layout descriptions and best practices

**Examples**: `examples/` directory - Step-by-step workflow tutorials

## File Structure

```
skills/oracle-pptx/
├── SKILL.md                        # This file
├── scripts/                        # Python utilities
│   ├── inventory.py                # Extract placeholders
│   ├── rearrange.py                # Build slide structure
│   ├── replace.py                  # Apply content (with auto-fix)
│   └── thumbnail.py                # Generate previews
├── resources/
│   ├── fonts/OracleSans/          # Oracle Sans Tab fonts (37 files)
│   ├── icons/                      # 1,078 SVG icons
│   │   ├── ICON-LIBRARY.md        # ← Icon catalog with categories
│   │   ├── dark-theme/            # Icons for dark presentations
│   │   └── light-theme/           # Icons for light presentations
│   ├── templates/
│   │   ├── dark-template.pptx     # 51 layouts
│   │   ├── light-template.pptx    # 55 layouts
│   │   ├── dark-inventory.json    # Pre-generated inventory
│   │   ├── light-inventory.json   # Pre-generated inventory
│   │   └── layout-mapping.md      # Layout descriptions
│   ├── guidelines.md              # Oracle brand standards (REQUIRED)
│   └── brand-compliance.md        # Oracle compliance (REQUIRED)
```

## Dependencies

**Python packages** (pre-installed in Claude Code environment):
- `python-pptx` - PPTX manipulation
- `pillow` - Image processing
- `six` - Python 2/3 compatibility

**Install if needed:**
```bash
pip install python-pptx pillow six
```

## Version Information

- **Template version**: Oracle FY26 v8.5 (January 2026)
- **Skill version**: 1.1.0 (with auto-fix, icon library, optimized guidance)
- **Last updated**: January 2026

---

**Questions?** 
- **Oracle brand**: Read `resources/guidelines.md` and `resources/brand-compliance.md` (REQUIRED)
- **Layout selection**: See `resources/templates/layout-mapping.md`
- **Icons**: See `resources/icons/ICON-LIBRARY.md` for complete index
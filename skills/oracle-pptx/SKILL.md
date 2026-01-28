---
name: oracle-pptx
description: "Create Oracle-compliant PowerPoint presentations following Oracle brand guidelines. Supports Dark (default) and Light themes with OCI/Database branding. Use when creating Oracle presentations, slides, or decks that must follow Oracle design standards."
---

# Oracle PPTX Creation

## Overview

This skill enables creation of Oracle-compliant PowerPoint presentations that strictly follow Oracle's current brand guidelines. All resources are self-contained within this skill directory—no external dependencies required.

**Current template version**: Based on latest Oracle FY26 templates (v8.5, January 2026). This version includes updated footers, Pine 140 color, new abstract backgrounds, and left middle title layouts.

**When to use this skill**:
- Creating Oracle-branded presentations or slides
- Making Oracle-compliant decks for events, meetings, or documentation
- Any mention of "Oracle presentation", "Oracle PowerPoint", "Oracle slides", or "Oracle deck"

**Templates available**:
- **Dark theme** (default): For large live events, formal presentations (51 slides)
- **Light theme**: For all other uses, virtual events, documentation (55 slides)

**Default branding**: OCI/Database themed slides (primary Oracle template option)

## Quick Start

### Basic Workflow

1. **Select theme**: Dark (default) or Light
2. **Plan content**: Outline presentation structure
3. **Select layouts**: Map content to appropriate template slides
4. **Rearrange slides**: Use `scripts/rearrange.py` to build presentation
5. **Generate inventory**: Use `scripts/inventory.py` to extract text placeholders
6. **Create content**: Generate replacement JSON with Oracle-formatted content
7. **Populate slides**: Use `scripts/replace.py` to insert content
8. **Validate**: Verify Oracle brand compliance

### File Paths (All Relative to Skill Directory)

```
skills/oracle-pptx/
├── SKILL.md                         # This file
├── scripts/                         # Python utilities
│   ├── inventory.py                 # Extract text placeholders
│   ├── rearrange.py                 # Duplicate and reorder slides
│   ├── replace.py                   # Populate content
│   └── thumbnail.py                 # Generate visual thumbnails
├── ooxml/                          # OOXML manipulation
│   ├── scripts/                    # pack.py, unpack.py, validate.py
│   └── schemas/                    # XML validation schemas
├── resources/                      # Self-contained resources
│   ├── fonts/OracleSans/          # Oracle Sans Tab fonts
│   ├── icons/                     # Oracle icons
│   │   ├── dark-theme/           # ~530 SVG icons
│   │   └── light-theme/          # ~530 SVG icons
│   ├── templates/                # Templates and inventories
│   │   ├── dark-template.pptx
│   │   ├── light-template.pptx
│   │   ├── dark-inventory.json
│   │   └── light-inventory.json
│   └── guidelines.md             # Oracle brand guidelines
└── examples/                     # Example workflows
```

## Oracle Brand Guidelines

### Theme Selection

**Dark Theme (Default)**:
- Primary use: Large live events, formal presentations
- Speaker slides: NO headshots (speakers shown live on stage)
- Background: Slate 170 (#2A2F2F)

**Light Theme**:
- All uses outside large live events
- Speaker slides: WITH headshots for virtual events
- Background: Neutral 10 (#FBF9F8)
- **Special note**: Hyperlinks must be manually changed to Sky 120 (yellow) on light slides

### Themed vs. Standard Content Slides

**Themed Slides** (Customizable for events/branding):
- Cover/title slides
- Section dividers
- Speaker slides (1-6 speakers)
- Quote slides
- Impact statements
- Thank you/closing slides

**Standard Content Slides** (Minimal branding, content-focused):
- Title + body layouts
- 2-column, 3-column layouts
- Title + 3 points
- Bold statements
- Story slides with photos/stats
- Abstract backgrounds

### Fonts

**Required**: Oracle Sans Tab family
- Oracle Sans Tab Regular
- Oracle Sans Tab Bold

**Installation**:
- Fonts included in `resources/fonts/OracleSans/`
- User must install fonts locally on their machine
- **Critical**: Edit and present in PowerPoint desktop app, NOT web/SharePoint browser

### Colors

**Theme Colors**:
- Brand 170: #F0CC72 (yellow/gold)
- Teal 70: #89B2B0
- Pine 70: #86B596
- Sky 140: #04536F
- Rose 140: #6C3F49
- Oracle Red: #C74634

**Custom Colors**: Predefined by numbered swatches (1-49)
- Pine 140 (added in v8.3)
- OCI/Database themed colors

**Hyperlinks**:
- Dark slides: Brand 170 (Custom color 2)
- Light slides: Sky 120 (Custom color 27) - **must be manually set**

**Do NOT use**:
- PowerPoint-generated tints
- Standard colors outside Oracle palette

### Footer Format

**Standard format** (mandatory on all slides):
```
Copyright © [YEAR], Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted
```

Replace `[YEAR]` with the current year.

**Configurable confidentiality levels**:
- Internal (default)
- Restricted
- Highly Restricted

**Year**: Update to current year

### Accessibility Requirements

- **High contrast**: Text and backgrounds must meet Oracle contrast standards
- **Alt text**: Provide guidance for images (slide notes or placeholders)
- **Reading order**: Maintain logical content flow

## Template Structure

### Dark Template (51 slides, 0-indexed: 0-50)

**Key layouts** (refer to `resources/templates/dark-inventory.json` for complete list):
- Slide 0: Master brand/OCI/Database cover
- Slides 1-6: Speaker slides (1, 2, 3, 4, 6 speakers, profile)
- Slides 7-12: Section dividers, thank you, impact
- Slides 13-50: Content layouts (title+body, 2/3-column, quotes, stories, etc.)

### Light Template (55 slides, 0-indexed: 0-54)

**Key layouts** (refer to `resources/templates/light-inventory.json` for complete list):
- Slide 0: Master brand/OCI/Database cover
- Slides 1-6: Speaker slides (1, 2, 3, 4, 6 speakers, profile)
- Slides 7-14: Section dividers, thank you, impact
- Slides 15-54: Content layouts (title+body, 2/3-column, quotes, stories, etc.)

**Note**: Slides are 0-indexed. First slide = 0, last slide = count-1.

## Detailed Workflow

### Step 1: Select Theme and Plan Content

1. **Confirm theme** with user:
   - Dark (default for large events)
   - Light (for other uses)

2. **Analyze content requirements**:
   - How many slides?
   - Content types: title, sections, bullet points, images, quotes, speakers, statistics
   - Determine appropriate layouts for each content piece

3. **Create presentation outline** with template mapping:
   ```markdown
   # Presentation Outline
   
   ## Slide 1: Cover
   - Template: slide-0 (OCI/Database cover)
   - Content: Presentation title, subtitle, presenter info, date
   
   ## Slide 2: Agenda
   - Template: slide-12 (Title + single body - RECOMMENDED)
   - Content: 3 bullet points (max for this layout)
   
   ## Slide 3: Key Message
   - Template: slide-18 (Bold statement)
   - Content: Impact statement with visual
   
   ...
   ```

### Step 2: Rearrange Template Slides

Use `scripts/rearrange.py` to create a working presentation with slides in the correct order:

```bash
# Example: Create 5-slide presentation from Dark template
python scripts/rearrange.py resources/templates/dark-template.pptx working.pptx 0,12,12,18,11

# Slide indices:
# 0 = Cover
# 12 = Title+single body (used twice) - RECOMMENDED for bullet lists
# 18 = Bold statement
# 11 = Thank you

# AVOID: slide 13 (multi-box layout leaves empty placeholders)
```

**Important**: 
- Slide indices are 0-based
- Same index can appear multiple times (duplicates that slide)
- Order matters—appears in final presentation in the order specified

### Step 3: Generate Text Inventory

Extract all text placeholders from the working presentation:

```bash
python scripts/inventory.py working.pptx text-inventory.json
```

**Inventory structure**:
```json
{
  "slide-0": {
    "shape-0": {
      "placeholder_type": "TITLE",
      "left": 1.5,
      "top": 2.0,
      "width": 7.5,
      "height": 1.2,
      "paragraphs": [
        {
          "text": "Presentation title text",
          "bold": true,
          "font_size": 28.0,
          "alignment": "CENTER"
        }
      ]
    }
  }
}
```

**Key features**:
- Slides named "slide-0", "slide-1", etc.
- Shapes ordered by visual position (top-to-bottom, left-to-right)
- Placeholder types: TITLE, CENTER_TITLE, SUBTITLE, BODY, OBJECT, or null
- Default font sizes extracted from layout placeholders
- Only non-default properties included

### Step 4: Create Replacement Content

Generate JSON with Oracle-formatted content:

```json
{
  "slide-0": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "Oracle Cloud Infrastructure",
          "bold": true,
          "alignment": "CENTER",
          "font_size": 32.0
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "Subhead goes here on one line",
          "alignment": "CENTER"
        }
      ]
    }
  },
  "slide-1": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "Introduction",
          "bold": true
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "First key point",
          "bullet": true,
          "level": 0
        },
        {
          "text": "Second key point",
          "bullet": true,
          "level": 0
        },
        {
          "text": "Third key point",
          "bullet": true,
          "level": 0
        }
      ]
    }
  }
}
```

**Critical formatting rules**:
- **Headers/titles**: Use `"bold": true`
- **Bullets**: Use `"bullet": true, "level": 0` (do NOT include bullet symbols •, -, * in text)
- **Alignment**: Include `"alignment": "CENTER"` or `"alignment": "RIGHT"` (LEFT is default, omit it)
- **Colors**: Use `"color": "FF0000"` (RGB) or `"theme_color": "DARK_1"`
- **Font**: Specify `"font_name": "Oracle Sans Tab"`, `"font_size": 14.0` when different from default
- **Auto-clearing**: Shapes not listed in replacement JSON are automatically cleared

**Validation tip**: The `replace.py` script validates that all shapes in replacement JSON exist in the inventory. If you reference non-existent shapes, you'll get clear error messages showing available shapes.

### Step 5: Apply Replacements

```bash
python scripts/replace.py working.pptx replacement-text.json output.pptx
```

The script will:
- Extract inventory of ALL text shapes
- Validate shapes in replacement JSON exist
- Clear text from ALL shapes in inventory
- Apply new text only to shapes with "paragraphs" defined
- Preserve formatting (bullets, alignment, colors, fonts)
- Save updated presentation

### Step 6: Visual Validation

Generate thumbnail grids to inspect layout:

```bash
python scripts/thumbnail.py output.pptx thumbnails --cols 4
```

**Check for**:
- Text cutoff (text cut off by headers, shapes, or slide edges)
- Text overlap (text overlapping other text or shapes)
- Positioning issues (content too close to boundaries)
- Contrast problems (insufficient text/background contrast)

**If issues found**: Adjust HTML margins/spacing/colors and regenerate presentation.

## Layout Selection Guide

### Matching Content to Layouts

**Use template inventories** (`resources/templates/dark-inventory.json` or `light-inventory.json`) to find appropriate layouts.

**Decision tree**:

1. **Cover/Title slide**: Use slide 0 (OCI/Database themed cover)

2. **Speaker slides**:
   - 1 speaker: slide 1
   - 2 speakers: slide 3
   - 3 speakers: slide 4
   - 4 speakers: slide 5
   - 6 speakers: slide 6
   - Profile (experience/expertise/location): slide 2

3. **Section dividers**: Slides 7-8 (dark/light variations)

4. **Content slides**:
   - Single topic with bullets: slide 12 (Title + single body placeholder - RECOMMENDED)
   - **AVOID slide 13**: Multi-box layout (leaves empty placeholders)
   - Two distinct items/concepts: slide 24 (proper 2-column layout)
   - Key message/impact: slide 18 (Bold statement)
   - Quote with attribution: Quote layout slides
   - Story with image: Story slides with photo layouts
   - Statistics/data: Stats layouts

5. **Closing**: Slide 11 (Thank you)

**Critical matching rules**:
- **Use slide 12 for bullet lists**: Single large body placeholder (7.0" x 0.8"), fits ~3 bullets
- **AVOID slide 13**: Multi-box layout with 5 small boxes - leaves empty placeholders
- **Use slide 24 for 2-column**: Proper 2-column layout with 2 body placeholders (5.4" x 1.4" each)
- **Match placeholder count to content**: Fill ALL placeholders - no empties
- **Limit bullets per slide**: Max 3-4 bullets per placeholder to avoid overflow
- **Break into multiple slides**: If you have too much content, use multiple slide-12 layouts

## Icons

**Access icons** from `resources/icons/`:
- **Dark theme presentations**: Use `resources/icons/dark-theme/*.svg` (~530 icons)
- **Light theme presentations**: Use `resources/icons/light-theme/*.svg` (~530 icons)

**Icon categories**: Technology, Vehicles & Transport, and more (organized by filename)

**Usage**: Reference icons by filename when creating presentations. Icons are SVG format for scalability.

## Validation and Troubleshooting

**For complete validation checklist and troubleshooting guide**: See [resources/brand-compliance.md](resources/brand-compliance.md)

**Quick checks**:
- Oracle Sans Tab fonts used
- Footer format correct with current year
- Colors from Oracle palette only
- No text cutoff or overlap

## Advanced Features

**OOXML Editing**: For direct XML manipulation, unpack/edit/validate/repack:
```bash
python ooxml/scripts/unpack.py presentation.pptx output_dir/
# Edit XML files (ppt/slides/slide{N}.xml, ppt/theme/theme1.xml)
python ooxml/scripts/validate.py output_dir/ --original presentation.pptx
python ooxml/scripts/pack.py output_dir/ final.pptx
```

**PDF Export**: See [resources/brand-compliance.md](resources/brand-compliance.md) for detailed export instructions

**Oracle Brand Team**: Contact for template compatibility, custom templates, icon library (VPN), photography guidance (VPN)

## Template Information

- **Dark template**: 51 slides (297 text elements, 0-indexed: 0-50)
- **Light template**: 55 slides (328 text elements, 0-indexed: 0-54)
- **Template base**: Oracle FY26 templates with OCI/Database branding
- **Key features**: Pine 140 color, abstract backgrounds, left middle title layouts, high-contrast accessibility

<details>
<summary>Template Version History</summary>

**Current (v8.5, January 2026)**:
- Updated footers to current year
- Added Pine 140 color
- New abstract background layouts
- Left middle title layouts

**Previous versions**: Contact Oracle Brand Team for historical template information.
</details>

## Examples

See `examples/` directory for:
- `basic-presentation/`: Simple 5-slide presentation workflow
- `multi-speaker/`: Presentation with multiple speakers
- `sample-outputs/`: Generated presentation examples with thumbnails

---

**Self-Contained Design**: This skill contains all necessary resources (scripts, fonts, icons, templates, guidelines) with no external dependencies. The skill directory can be copied or moved without breaking functionality.

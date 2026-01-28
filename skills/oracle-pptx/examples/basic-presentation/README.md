# Basic Oracle Presentation Example

This example demonstrates creating a simple 5-slide Oracle presentation using the Dark theme.

## Presentation Outline

1. **Cover**: Oracle Cloud Infrastructure - Main title
2. **Agenda**: Overview of presentation topics
3. **Key Benefits**: 3-column layout with benefits
4. **Customer Success**: Bold statement with impact
5. **Thank You**: Closing slide

## Step-by-Step Workflow

### Step 1: Plan Presentation Structure

**Content requirements**:
- Cover slide with title, subtitle, presenter
- Agenda with 3 bullet points
- Key benefits in 3 columns
- Customer success statement
- Thank you slide

**Template mapping** (Dark theme, 0-indexed):
```
0  → Cover (slide 0)
13 → Agenda: Title + Body (slide 13)
23 → Key Benefits: 3-Column (slide 23)
18 → Customer Success: Bold Statement (slide 18)
11 → Thank You (slide 11)
```

### Step 2: Rearrange Template Slides

```bash
cd skills/oracle-pptx
python scripts/rearrange.py \
    resources/templates/dark-template.pptx \
    examples/basic-presentation/working.pptx \
    0,13,23,18,11
```

**Result**: `working.pptx` with 5 slides in the correct order

### Step 3: Generate Text Inventory

```bash
python scripts/inventory.py \
    examples/basic-presentation/working.pptx \
    examples/basic-presentation/inventory.json
```

**Result**: `inventory.json` with all text placeholders extracted

### Step 4: Create Replacement Content

Create `replacement.json` with Oracle-formatted content:

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
          "text": "Building the Future of Cloud Computing",
          "alignment": "CENTER"
        }
      ]
    },
    "shape-2": {
      "paragraphs": [
        {
          "text": "Jane Smith"
        }
      ]
    },
    "shape-3": {
      "paragraphs": [
        {
          "text": "Cloud Solutions Architect"
        }
      ]
    },
    "shape-4": {
      "paragraphs": [
        {
          "text": "Oracle Cloud Infrastructure"
        }
      ]
    },
    "shape-5": {
      "paragraphs": [
        {
          "text": "January 28, [CURRENT_YEAR]"
        }
      ]
    }
  },
  "slide-1": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "Agenda",
          "bold": true
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "Overview of Oracle Cloud Infrastructure",
          "bullet": true,
          "level": 0
        },
        {
          "text": "Key benefits and differentiators",
          "bullet": true,
          "level": 0
        },
        {
          "text": "Customer success stories",
          "bullet": true,
          "level": 0
        }
      ]
    }
  },
  "slide-2": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "Key Benefits",
          "bold": true
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "Performance",
          "bold": true
        },
        {
          "text": "Industry-leading compute, storage, and network performance for mission-critical workloads"
        }
      ]
    },
    "shape-2": {
      "paragraphs": [
        {
          "text": "Security",
          "bold": true
        },
        {
          "text": "Built-in security at every layer with zero trust architecture and automated threat detection"
        }
      ]
    },
    "shape-3": {
      "paragraphs": [
        {
          "text": "Cost Efficiency",
          "bold": true
        },
        {
          "text": "Up to 50% lower costs compared to other cloud providers with transparent pricing"
        }
      ]
    }
  },
  "slide-3": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "10,000+ customers",
          "bold": true,
          "font_size": 48.0
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "have migrated to Oracle Cloud Infrastructure, achieving an average of 40% cost savings and 3x performance improvement"
        }
      ]
    }
  },
  "slide-4": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "Thank You",
          "bold": true,
          "alignment": "CENTER",
          "font_size": 44.0
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "Questions?",
          "alignment": "CENTER"
        }
      ]
    }
  }
}
```

### Step 5: Apply Replacements

```bash
python scripts/replace.py \
    examples/basic-presentation/working.pptx \
    examples/basic-presentation/replacement.json \
    examples/basic-presentation/output.pptx
```

**Result**: `output.pptx` with all content populated

### Step 6: Visual Validation

```bash
python scripts/thumbnail.py \
    examples/basic-presentation/output.pptx \
    examples/basic-presentation/thumbnails \
    --cols 5
```

**Result**: `thumbnails.jpg` with visual grid of all slides

### Step 7: Validate Oracle Compliance

**Checklist**:
- ✅ Oracle Sans Tab fonts used
- ✅ Oracle color palette (Brand 170, theme colors)
- ✅ Footer format: `Copyright © 2026, Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted`
- ✅ Dark theme background (Slate 170 #2A2F2F)
- ✅ High contrast text
- ✅ Proper layout selection

## Key Learnings

### Layout Selection
- Used slide 23 (3-column) for exactly 3 benefits
- Each column has header + description
- Content matched to placeholder structure

### Formatting
- Headers: `"bold": true`
- Bullets: `"bullet": true, "level": 0` (no bullet symbols in text)
- Cover text: `"alignment": "CENTER"`
- Large numbers: `"font_size": 48.0` for impact

### Oracle Brand
- Default confidentiality: "Internal/Restricted/Highly Restricted"
- Year: Use current year in footer
- Theme: Dark (default for formal presentations)

## Files in This Example

- `README.md` - This file
- `outline.md` - Detailed presentation outline
- `working.pptx` - After rearrange step
- `inventory.json` - Extracted text inventory
- `replacement.json` - Content with Oracle formatting
- `output.pptx` - Final presentation
- `thumbnails.jpg` - Visual validation grid

## Adaptation Guide

To adapt this example for your content:

1. **Change template mapping**: Select appropriate slides from Dark/Light template
2. **Update replacement.json**: Replace content while preserving formatting properties
3. **Verify shape names**: Run `inventory.py` on your working file to get correct shape names
4. **Adjust confidentiality**: Change footer level if needed (Internal/Restricted/Highly Restricted)
5. **Select theme**: Use `light-template.pptx` for non-event presentations

## Common Mistakes to Avoid

❌ **Don't use 1-based indexing**: Slides start at 0, not 1
❌ **Don't include bullet symbols**: Use `"bullet": true` instead of "• First point"
❌ **Don't skip inventory step**: Always generate fresh inventory after rearranging
❌ **Don't reference non-existent shapes**: Verify shape names in inventory before creating replacement JSON

✅ **Do match content to layouts**: 3-column layout for 3 items
✅ **Do preserve Oracle formatting**: Bold headers, proper alignment
✅ **Do validate visually**: Generate thumbnails to catch layout issues
✅ **Do use relative paths**: All paths relative to skill directory

## Next Steps

After creating your presentation:
1. Open in PowerPoint desktop app (not web)
2. Verify fonts display correctly (Oracle Sans Tab)
3. Check footer year and confidentiality level
4. Export to PDF for external sharing (preserves fonts)

For more complex examples, see:
- `../multi-speaker/` - Presentation with speaker slides
- `../sample-outputs/` - Various presentation types

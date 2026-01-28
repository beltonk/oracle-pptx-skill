# Oracle PPTX Examples

This directory contains example workflows demonstrating how to create Oracle-compliant presentations.

## Available Examples

### basic-presentation/
Simple 5-slide presentation using Dark theme with OCI/Database branding.

**Demonstrates**:
- Theme selection (Dark)
- Layout mapping (cover, agenda, 3-column, bold statement, thank you)
- Content formatting (bold headers, bullets, alignment)
- Complete workflow from outline to final presentation

**Files**:
- `README.md` - Step-by-step workflow guide
- Example outline and replacement JSON
- Generated outputs

### multi-speaker/
Presentation featuring multiple speakers with headshots (virtual event format).

**Demonstrates**:
- Speaker slide layouts (2-6 speakers)
- Speaker profile slides
- Mixing speaker slides with content slides
- Virtual event formatting

### sample-outputs/
Collection of generated presentations showing various layout types and themes.

**Includes**:
- Dark theme examples
- Light theme examples
- Various layout combinations
- Visual thumbnail grids

## Quick Reference

### Basic Workflow
1. Select theme (Dark/Light)
2. Plan content structure
3. Map content to template slides
4. Rearrange: `python scripts/rearrange.py template.pptx working.pptx 0,13,23,18,11`
5. Inventory: `python scripts/inventory.py working.pptx inventory.json`
6. Create replacement JSON with content
7. Replace: `python scripts/replace.py working.pptx replacement.json output.pptx`
8. Validate: `python scripts/thumbnail.py output.pptx thumbnails --cols 4`

### Common Template Mappings

**5-Slide Basic** (Dark):
```
0,13,13,18,11
Cover → Title+Body → Title+Body → Bold Statement → Thank You
```

**7-Slide Multi-Speaker** (Dark):
```
0,4,7,13,19,9,11
Cover → 3 Speakers → Section → Title+Body → 2-Column → Impact → Thank You
```

**Customer Story** (Light):
```
0,15,28,38,14,13
Cover → Title+Body → Image+Text → Statistics → Quote → Thank You
```

## File Naming Conventions

- `*-template.pptx` - Oracle templates (Dark/Light)
- `working.pptx` - After rearrange step
- `inventory.json` - Extracted text inventory
- `replacement.json` - Content with formatting
- `output.pptx` - Final presentation
- `thumbnails.jpg` - Visual validation grid

## Tips for Creating Examples

### Layout Selection
- **Match placeholder count to content**: Don't force 2 items into 3-column layout
- **Count items first**: Know how many distinct concepts before selecting layout
- **Use appropriate slides**: Refer to `resources/templates/layout-mapping.md`

### Content Formatting
- **Headers**: `"bold": true`
- **Bullets**: `"bullet": true, "level": 0` (NO bullet symbols • in text)
- **Alignment**: `"alignment": "CENTER"` or `"RIGHT"` (LEFT is default, omit)
- **Colors**: Use Oracle palette only
- **Fonts**: Oracle Sans Tab (Bold for headers, Regular for body)

### Oracle Brand Compliance
- Footer: `Copyright © [YEAR], Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted` (use current year)
- Theme: Dark (events) or Light (other uses)
- Colors: Brand 170, Teal 70, Pine 70, Sky 140, Rose 140, Oracle Red
- Hyperlinks: Brand 170 (dark) or Sky 120 (light, manual change)

## Visual Validation

Always generate thumbnails to check:
- ✅ No text cutoff
- ✅ No text overlap
- ✅ Proper spacing
- ✅ Correct alignment
- ✅ High contrast

```bash
python scripts/thumbnail.py output.pptx thumbnails --cols 4
```

## Common Issues

### Issue: Shapes not found
**Fix**: Generate fresh inventory after rearranging slides

### Issue: Text overflow
**Fix**: Reduce content, decrease font size, or use larger layout

### Issue: Wrong colors
**Fix**: Use only Oracle palette colors (see `resources/guidelines.md`)

### Issue: Fonts substituted
**Fix**: Install Oracle Sans Tab fonts, edit in desktop PowerPoint

## Next Steps

1. Study examples to understand workflow
2. Adapt for your content
3. Refer to `../SKILL.md` for complete documentation
4. Check `resources/templates/layout-mapping.md` for layout guide

## Contributing Examples

When adding new examples:
1. Create descriptive directory name
2. Include README.md with step-by-step workflow
3. Provide all intermediate files (outline, inventory, replacement, output)
4. Generate thumbnail grid for visual reference
5. Document key learnings and common mistakes
6. Test workflow end-to-end before committing

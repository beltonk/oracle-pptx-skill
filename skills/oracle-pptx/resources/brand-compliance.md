# Oracle Brand Compliance Guide

## Validation Checklist

Before finalizing Oracle presentations, verify:

### Brand Compliance
- ✅ Oracle Sans Tab fonts used (Bold for headers, Regular for body)
- ✅ Colors from Oracle palette only (no PowerPoint tints or standard colors)
- ✅ Footer format correct with current year and confidentiality level
- ✅ Layouts from Oracle templates (not custom layouts)
- ✅ Theme-appropriate icons (dark vs. light)

### Accessibility
- ✅ High contrast text and backgrounds
- ✅ Alt text guidance for images
- ✅ Logical reading order
- ✅ Font sizes meet minimums

### Visual Quality
- ✅ No text cutoff or overlap
- ✅ Proper spacing and alignment
- ✅ Consistent formatting across slides
- ✅ Appropriate layout selection for content

### Technical
- ✅ Presentation opens in PowerPoint desktop app
- ✅ Fonts display correctly (not substituted)
- ✅ No validation errors from `ooxml/scripts/validate.py`

## Troubleshooting

### Issue: Fonts not displaying correctly
**Solution**: 
- User must install Oracle Sans Tab fonts from `resources/fonts/OracleSans/`
- Must edit/present in PowerPoint desktop app (not web/SharePoint)
- For external sharing, export to PDF to preserve fonts

### Issue: Replace script shows "Shape not found" error
**Solution**:
- Generate fresh inventory: `python scripts/inventory.py working.pptx fresh-inventory.json`
- Verify shape names in inventory match your replacement JSON
- Check slide numbers are correct (0-indexed)

### Issue: Text overflow in shapes
**Solution**:
- Reduce text length or font size
- Select larger placeholder layout
- Split content across multiple slides

### Issue: Colors don't match Oracle brand
**Solution**:
- Use only colors specified in guidelines (see Colors section in SKILL.md)
- Reference `resources/guidelines.md` for complete color specifications
- Use theme colors or custom color swatches 1-49

### Issue: Hyperlinks wrong color on light slides
**Solution**:
- Hyperlinks on light slides must be manually changed to Sky 120 (Custom color 27)
- PowerPoint only supports one default hyperlink color, so light slides require manual adjustment

## Export for External Sharing

When sharing Oracle presentations externally, save as PDF to preserve fonts:

### PC/Windows Export
```
File > Export > Create PDF/XPS document > Create PDF/XPS
> Check "Minimum size (publishing online)" > Publish
```

### Mac Export (2-step for size reduction)
```
Step 1: File > Export > File format: PDF > Export
Step 2: Open newly created PDF > File > Reduce file size
```

**Why PDF?**: Ensures Oracle Sans Tab fonts display correctly for recipients who don't have fonts installed.

## Contact Oracle Brand Team

For questions beyond this skill:
- Template compatibility questions
- Custom template building
- Updated Oracle icon library (requires VPN)
- Oracle photography guidance (requires VPN)

**Note**: Core resources (templates, fonts, icons, guidelines) are already included in this skill.

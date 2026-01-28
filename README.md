# Oracle PPTX Agent Skill

**AI agent skill for creating Oracle-compliant PowerPoint presentations**

This project provides a comprehensive agent skill that enables AI assistants (Claude, ChatGPT, etc.) to create professional PowerPoint presentations that strictly follow Oracle's brand guidelines, templates, and accessibility requirements.

## What's Included

### Oracle PPTX Skill (`skills/oracle-pptx/`)

A self-contained agent skill with everything needed to create Oracle-branded presentations:

- **Templates**: Dark (51 slides) and Light (55 slides) Oracle FY26 templates
- **Brand Guidelines**: Complete Oracle PowerPoint design standards
- **Fonts**: Oracle Sans Tab font family (37 font files)
- **Icons**: 1,078 SVG icons for dark and light themes
- **Scripts**: Python utilities for PPTX manipulation
- **Documentation**: Comprehensive guides and examples
- **Examples**: Step-by-step workflow tutorials

**Size**: 32MB | **Files**: 1,179 | **Self-contained**: No external dependencies

## Quick Start

### For AI Agents (Claude.ai, Cursor, etc.)

1. **Locate the skill**:
   ```bash
   cd skills/oracle-pptx/
   ```

2. **Read the main documentation**:
   ```bash
   cat SKILL.md
   ```

3. **Follow the workflow** described in SKILL.md to create presentations

### For Developers/Users

#### Prerequisites

- Python 3.x
- PowerPoint (desktop app for editing/presenting)
- Git (for cloning/managing the repository)

#### Installation

1. **Clone the repository** (when available):
   ```bash
   git clone <repository-url>
   cd oracle-pptx-skill
   ```

2. **Install Python dependencies**:
   ```bash
   pip3 install "markitdown[pptx]" defusedxml python-pptx
   ```

3. **Install Oracle fonts** (required for editing):
   - Navigate to `skills/oracle-pptx/resources/fonts/OracleSans/`
   - Install all .otf font files on your system
   - Fonts include: Oracle Sans Tab (Regular, Italic, Bold, Bold Italic, etc.)

4. **Verify installation**:
   ```bash
   python3 skills/oracle-pptx/scripts/inventory.py --help
   ```

## Usage

### Creating a Basic Oracle Presentation

```bash
cd skills/oracle-pptx

# 1. Plan your presentation structure
# - Cover slide
# - Content slides (bullet points, 2-column, etc.)
# - Thank you/closing slide

# 2. Rearrange template slides (Dark theme, slides 0, 13, 11)
python3 scripts/rearrange.py \
  resources/templates/dark-template.pptx \
  "0,13,11" \
  output.pptx

# 3. Generate inventory of text placeholders
python3 scripts/inventory.py output.pptx inventory.json

# 4. Create replacement JSON with your content
# See examples/basic-presentation/README.md for structure

# 5. Populate slides with content
python3 scripts/replace.py \
  output.pptx \
  replacement.json \
  final-presentation.pptx

# 6. Validate OOXML structure
python3 ooxml/scripts/validate.py final-presentation.pptx

# 7. Open and review in PowerPoint
open final-presentation.pptx
```

### Using with AI Assistants

#### Claude.ai

1. Upload the skill:
   - Zip the `skills/oracle-pptx/` directory
   - Go to Settings > Features > Custom Skills
   - Upload the zip file

2. Start a conversation:
   ```
   Create an Oracle presentation about cloud migration with 5 slides
   ```

#### Claude Code / Cursor

1. Copy the skill to your project:
   ```bash
   cp -r skills/oracle-pptx ~/.cursor/skills/
   # or
   cp -r skills/oracle-pptx .cursor/skills/
   ```

2. The agent will automatically use the skill when you request Oracle presentations

## Templates

### Dark Theme (Default)
- **Use for**: Large live events, formal presentations
- **Slides**: 51 (indexed 0-50)
- **Key layouts**: 
  - Cover (slide 0)
  - Speaker profiles (slides 1-6)
  - Section dividers (slides 7-8)
  - Content slides (slides 13-50)

### Light Theme
- **Use for**: Virtual events, documentation, internal use
- **Slides**: 55 (indexed 0-54)
- **Key layouts**: Similar to Dark theme with 4 additional slides

See `skills/oracle-pptx/resources/templates/layout-mapping.md` for complete layout reference.

## Brand Compliance

All presentations must follow Oracle's brand guidelines:

### Required Elements
- ✅ **Footer**: `Copyright © [YEAR], Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted`
- ✅ **Fonts**: Oracle Sans Tab only (Bold for headers, Regular for body)
- ✅ **Colors**: Oracle palette only (Brand 170, Teal 70, Pine 70, Sky 140, Rose 140, Oracle Red)
- ✅ **Layouts**: From Oracle templates (no custom layouts)
- ✅ **Accessibility**: High contrast, alt text, logical reading order

### Validation Checklist

See `skills/oracle-pptx/resources/brand-compliance.md` for:
- Complete validation checklist
- Troubleshooting common issues
- Export instructions for external sharing
- Contact info for Oracle Brand Team

## Documentation

### Core Documentation
- **`skills/oracle-pptx/SKILL.md`**: Main agent skill documentation (460 lines)
- **`skills/oracle-pptx/README.md`**: Quick reference for the skill
- **`skills/oracle-pptx/resources/guidelines.md`**: Oracle brand guidelines (181 lines)
- **`skills/oracle-pptx/resources/brand-compliance.md`**: Validation and troubleshooting

### Reference Guides
- **`skills/oracle-pptx/resources/templates/layout-mapping.md`**: Layout selection guide
- **`skills/oracle-pptx/examples/README.md`**: Example workflows overview
- **`skills/oracle-pptx/examples/basic-presentation/README.md`**: Step-by-step tutorial

## Architecture

### Project Structure

```
oracle-pptx-skill/
├── README.md                          # This file
├── AGENTS.md                          # Agent skills system configuration
├── skills/                            # Agent skills
│   └── oracle-pptx/                  # Oracle PPTX skill (self-contained)
│       ├── SKILL.md                  # Main skill documentation
│       ├── README.md                 # Quick reference
│       ├── scripts/                  # Python utilities
│       │   ├── inventory.py          # Extract text placeholders
│       │   ├── rearrange.py          # Duplicate/reorder slides
│       │   ├── replace.py            # Populate content
│       │   └── thumbnail.py          # Generate visual thumbnails
│       ├── ooxml/                    # OOXML manipulation
│       │   ├── scripts/              # pack, unpack, validate
│       │   └── schemas/              # XML validation schemas
│       ├── resources/                # Self-contained resources
│       │   ├── templates/            # Dark + Light templates
│       │   ├── fonts/OracleSans/    # Font files (37 files)
│       │   ├── icons/                # 1,078 SVG icons
│       │   ├── guidelines.md         # Brand guidelines
│       │   └── brand-compliance.md   # Validation guide
│       └── examples/                 # Example workflows
├── reference/                         # Reference materials (development)
│   ├── guidelines/                   # Oracle brand guidelines
│   ├── resources/                    # Source resources
│   └── skills/pptx/                  # Base PPTX skill reference
└── openspec/                         # Spec-driven development
    ├── specs/                        # Approved specifications
    └── changes/archive/              # Historical changes
```

### Self-Contained Design

The `skills/oracle-pptx/` directory is **fully self-contained**:
- ✅ All scripts bundled (no external references)
- ✅ All resources copied (fonts, icons, templates)
- ✅ All guidelines included (no Oracle VPN required)
- ✅ Portable: Copy/move without breaking references

**Why**: Eliminates external dependencies, ensures portability, and guarantees all agents have identical resources.

## Technical Details

### Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `inventory.py` | Extract text placeholders from slides | Read-only analysis |
| `rearrange.py` | Duplicate and reorder slides from template | Creates new PPTX |
| `replace.py` | Populate placeholders with content | Modifies PPTX |
| `thumbnail.py` | Generate visual thumbnail grids | Requires LibreOffice |
| `ooxml/scripts/unpack.py` | Extract PPTX to XML files | Advanced editing |
| `ooxml/scripts/pack.py` | Repackage XML files to PPTX | Advanced editing |
| `ooxml/scripts/validate.py` | Verify OOXML structure | Quality assurance |

### Dependencies

**Required**:
- `markitdown[pptx]`: Text extraction from PowerPoint
- `defusedxml`: Secure XML parsing
- `python-pptx`: PowerPoint file manipulation

**Optional**:
- LibreOffice (`soffice`): For thumbnail generation

Install with:
```bash
pip3 install "markitdown[pptx]" defusedxml python-pptx
```

### Compatibility

- **Python**: 3.7+
- **PowerPoint**: Desktop app (Windows/Mac) for editing/presenting
- **Platforms**: macOS, Windows, Linux (for script execution)
- **Agent Platforms**: Claude.ai, Claude API, Claude Code, Cursor, Anthropic Agent SDK

**Note**: PowerPoint web/SharePoint do not support Oracle Sans Tab fonts. Use desktop app or export to PDF for external sharing.

## Examples

### Example 1: 5-Slide Product Launch (Dark Theme)

See `skills/oracle-pptx/examples/basic-presentation/README.md` for:
- Complete step-by-step workflow
- JSON structure examples
- Brand compliance checklist
- Common mistakes to avoid

### Example 2: Multi-Speaker Presentation

See `skills/oracle-pptx/examples/README.md` for common patterns:
- Cover slide + speaker profiles
- Section dividers
- Content variations (bullet points, 2-column, 3-column)
- Closing/thank you slides

## Troubleshooting

### Fonts not displaying correctly
**Solution**: Install Oracle Sans Tab fonts from `skills/oracle-pptx/resources/fonts/OracleSans/` and use PowerPoint desktop app (not web).

### "Shape not found" error
**Solution**: Generate fresh inventory with `scripts/inventory.py` and verify shape names match your replacement JSON.

### Colors don't match Oracle brand
**Solution**: Use only colors specified in `resources/guidelines.md`. Reference custom color swatches 1-49.

### Text overflow in shapes
**Solution**: Reduce text length, decrease font size, or select a larger placeholder layout.

**For complete troubleshooting**: See `skills/oracle-pptx/resources/brand-compliance.md`

## OpenSpec Development

This project uses OpenSpec for spec-driven development:

```bash
# List specifications
openspec list --specs

# View specification
openspec show oracle-pptx-creation --type spec

# List historical changes
openspec list --archived
```

**Current specs**:
- `oracle-pptx-creation`: Requirements for Oracle PPTX creation skill (12 requirements)

## Contributing

### Adding New Features

1. Create an OpenSpec proposal:
   ```bash
   openspec create <change-id>
   ```

2. Document requirements, design, and tasks

3. Implement following the tasks

4. Archive when complete:
   ```bash
   openspec archive <change-id> --yes
   ```

### Code Style

- Follow existing patterns in `skills/oracle-pptx/scripts/`
- Concise Python code, minimal verbosity
- Clear variable names
- Include error handling

## Resources

### Oracle Brand Resources (Included)
- ✅ FY26 Dark and Light templates (v8.5)
- ✅ Oracle Sans Tab fonts (37 font files)
- ✅ Oracle icons for presentations (1,078 SVG files)
- ✅ Brand guidelines (extracted markdown)

### Oracle Brand Resources (VPN Required)
- Oracle icon library (extended)
- Oracle photography guidelines
- Custom template building guidance

**Contact Oracle Brand Team** for resources requiring VPN access.

## License

Oracle templates, fonts, icons, and guidelines are proprietary to Oracle Corporation. This skill is for internal Oracle use or authorized partners only.

## Version Information

- **Skill Version**: 1.0.0
- **Template Base**: Oracle FY26 v8.5 (January 2026)
- **Compliance**: Claude Agent Skills specifications and best practices
- **Status**: Production-ready

## Support

### For Agent Skill Issues
- Review `skills/oracle-pptx/SKILL.md` for usage guidance
- Check `skills/oracle-pptx/resources/brand-compliance.md` for troubleshooting
- Verify Python dependencies are installed

### For Oracle Brand Questions
- Contact Oracle Brand Team
- Reference `skills/oracle-pptx/resources/guidelines.md`

### For Technical Issues
- Validate PPTX structure: `python3 ooxml/scripts/validate.py <file.pptx>`
- Check Python version: `python3 --version` (3.7+ required)
- Verify fonts installed: Check system font library for "Oracle Sans Tab"

---

**Ready to create Oracle-compliant presentations with AI?**

Start with the examples in `skills/oracle-pptx/examples/` or read the main documentation in `skills/oracle-pptx/SKILL.md`.

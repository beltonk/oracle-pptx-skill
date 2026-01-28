# Oracle PPTX Agent Skill

**AI agent skill for creating Oracle-compliant PowerPoint presentations**

Universal agent skill that enables AI assistants (Claude, ChatGPT, Cursor, etc.) to create professional PowerPoint presentations that strictly follow Oracle's brand guidelines, templates, and accessibility requirements.

[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Skills Format](https://img.shields.io/badge/format-Claude%20Agent%20Skills-blue.svg)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills)
[![Compatible](https://img.shields.io/badge/compatible-openskills-green.svg)](https://github.com/numman-ali/openskills)

**Size**: 32MB | **Files**: 1,179 | **Self-contained**: No external dependencies

---

## 🚀 Installation

### Recommended: Install with openskills

[openskills](https://github.com/numman-ali/openskills) is the universal skills loader for AI coding agents. It works with Claude Code, Cursor, Windsurf, Aider, and any agent that can read `AGENTS.md`.

**One command to install globally for all agents**:

```bash
npx openskills install beltonk/oracle-pptx-skill --global --universal
```

**What this does**:
- ✅ Installs to `~/.agent/skills/` (works with all AI agents)
- ✅ Updates your `AGENTS.md` automatically
- ✅ Enables progressive disclosure (loads skill only when needed)
- ✅ No manual copying or configuration required

**Use the skill**:

Once installed, AI agents automatically discover and use the skill when you request Oracle presentations:

```
Create an Oracle presentation about cloud migration with 5 slides using the Dark theme
```

**Verify installation**:

```bash
npx openskills list
# Should show: oracle-pptx

npx openskills read oracle-pptx
# Should display the skill documentation
```

**Update the skill**:

```bash
npx openskills update oracle-pptx
```

---

### Alternative: Manual Installation Methods

<details>
<summary><b>Claude.ai - Upload as custom skill</b></summary>

1. **Clone and package**:
   ```bash
   git clone https://github.com/beltonk/oracle-pptx-skill.git
   cd oracle-pptx-skill/skills
   zip -r oracle-pptx.zip oracle-pptx/
   ```

2. **Upload to Claude.ai**:
   - Go to Settings > Features > Custom Skills
   - Click "Upload Skill"
   - Select `oracle-pptx.zip`
   - Wait for upload to complete

3. **Use the skill**:
   ```
   Create an Oracle presentation about cloud migration with 5 slides
   ```
</details>

<details>
<summary><b>Claude Code / Cursor - Manual copy</b></summary>

```bash
# Clone the repository
git clone https://github.com/beltonk/oracle-pptx-skill.git

# For Cursor (global)
cp -r oracle-pptx-skill/skills/oracle-pptx ~/.cursor/skills/

# For Cursor (project-specific)
cp -r oracle-pptx-skill/skills/oracle-pptx .cursor/skills/

# For Claude Code (global)
cp -r oracle-pptx-skill/skills/oracle-pptx ~/.claude/skills/

# For Claude Code (project-specific)
cp -r oracle-pptx-skill/skills/oracle-pptx .claude/skills/
```

The AI agent will automatically discover and use the skill when you request Oracle presentations.
</details>

<details>
<summary><b>Claude API - Upload via API</b></summary>

```bash
# Clone and navigate to the repository
git clone https://github.com/beltonk/oracle-pptx-skill.git
cd oracle-pptx-skill/skills/oracle-pptx

# Create a tarball
tar -czf oracle-pptx.tar.gz .

# Upload using curl (replace YOUR_API_KEY)
curl -X POST https://api.anthropic.com/v1/skills \
  -H "x-api-key: YOUR_API_KEY" \
  -H "anthropic-version: 2024-10-22" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "file=@oracle-pptx.tar.gz" \
  -F "name=oracle-pptx"

# Or use the Skills API client (Python example)
python3 <<EOF
from anthropic import Anthropic

client = Anthropic(api_key="YOUR_API_KEY")

with open("oracle-pptx.tar.gz", "rb") as f:
    skill = client.skills.create(
        file=f,
        name="oracle-pptx"
    )

print(f"Skill uploaded: {skill.id}")
EOF
```
</details>

---

### Prerequisites for Local Script Usage

If you want to run the Python scripts directly (optional):

```bash
# Install Python dependencies
pip3 install "markitdown[pptx]" defusedxml python-pptx

# Install Oracle fonts (required for PowerPoint editing)
# Navigate to: skills/oracle-pptx/resources/fonts/OracleSans/
# Then install all .otf files on your system:
# - macOS: Double-click each .otf file and click "Install Font"
# - Windows: Right-click each .otf file and select "Install"
# - Linux: Copy to ~/.fonts/ and run fc-cache -f -v
```

---

## 📦 What's Included

The `skills/oracle-pptx/` directory is a **self-contained agent skill** with everything needed:

- **Templates**: Dark (51 slides) and Light (55 slides) Oracle FY26 templates with pre-generated inventories
- **Brand Guidelines**: Complete Oracle PowerPoint design standards (181 lines)
- **Fonts**: Oracle Sans Tab font family (37 .otf files)
- **Icons**: 1,078 SVG icons optimized for dark and light themes
- **Scripts**: Python utilities for PPTX manipulation (inventory, rearrange, replace, thumbnail)
- **OOXML Tools**: XML manipulation utilities (unpack, pack, validate)
- **Documentation**: Comprehensive guides, examples, and troubleshooting
- **Examples**: Step-by-step workflow tutorials

**Self-contained design**:
- ✅ All scripts bundled (no external references)
- ✅ All resources copied (fonts, icons, templates)
- ✅ All guidelines included (no Oracle VPN required)
- ✅ Portable: Copy/move without breaking references

---

## 🎯 Quick Start

### Using with AI Agents

Once installed via openskills (or any alternative method), simply ask:

```
Create an Oracle presentation with the following structure:
- Cover slide: "Cloud Migration Strategy"
- Content slide: Benefits of cloud adoption (3 bullet points)
- Content slide: Migration timeline
- Thank you slide

Use the Dark theme.
```

The AI agent will:
1. Read the skill documentation
2. Select appropriate template slides
3. Follow Oracle brand guidelines
4. Create the presentation using the scripts
5. Validate brand compliance

### Creating a Presentation Manually (Scripts)

```bash
cd skills/oracle-pptx

# 1. Rearrange template slides (Dark theme: cover, content, closing)
python3 scripts/rearrange.py \
  resources/templates/dark-template.pptx \
  "0,13,11" \
  output.pptx

# 2. Generate inventory of text placeholders
python3 scripts/inventory.py output.pptx inventory.json

# 3. Create replacement JSON with your content
# See examples/basic-presentation/README.md for JSON structure

# 4. Populate slides with content
python3 scripts/replace.py \
  output.pptx \
  replacement.json \
  final-presentation.pptx

# 5. Validate OOXML structure
python3 ooxml/scripts/validate.py final-presentation.pptx

# 6. Open and review in PowerPoint
open final-presentation.pptx  # macOS
# or: start final-presentation.pptx  # Windows
```

---

## 🎨 Templates

### Dark Theme (Default)
- **Use for**: Large live events, formal presentations, executive briefings
- **Slides**: 51 (indexed 0-50)
- **Key layouts**: 
  - Cover with OCI/Database branding (slide 0)
  - Speaker profiles (1-6 speakers, slides 1-6)
  - Section dividers (slides 7-8)
  - Impact statements (slides 9-10)
  - Content slides (13-50): bullet points, 2-column, 3-column, images, etc.
  - Thank you/closing (slide 11)

### Light Theme
- **Use for**: Virtual events, documentation, internal meetings, workshops
- **Slides**: 55 (indexed 0-54)
- **Key layouts**: Similar to Dark theme with 4 additional layouts

**Complete layout reference**: See `skills/oracle-pptx/resources/templates/layout-mapping.md`

---

## ✅ Brand Compliance

All presentations must follow Oracle's brand guidelines:

### Required Elements
- ✅ **Footer**: `Copyright © [YEAR], Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted`
- ✅ **Fonts**: Oracle Sans Tab only (Bold for headers, Regular for body)
- ✅ **Colors**: Oracle palette only (Brand 170, Teal 70, Pine 70, Sky 140, Rose 140, Oracle Red, Pine 140)
- ✅ **Layouts**: From Oracle templates (no custom layouts)
- ✅ **Icons**: From Oracle icon library (1,078 included)
- ✅ **Accessibility**: High contrast, alt text guidance, logical reading order

### Validation Checklist

Before finalizing presentations:
- Oracle Sans Tab fonts used throughout
- Footer format correct with current year
- Colors from Oracle palette only (no PowerPoint tints)
- No text cutoff or overlap
- Layouts from templates (not custom)
- Theme-appropriate icons (dark vs. light)

**Complete checklist**: See `skills/oracle-pptx/resources/brand-compliance.md`

---

## 📚 Documentation

### Core Documentation
- **`skills/oracle-pptx/SKILL.md`** (460 lines): Main agent skill documentation with complete workflows
- **`skills/oracle-pptx/README.md`** (81 lines): Quick reference for the skill
- **`skills/oracle-pptx/resources/guidelines.md`** (181 lines): Oracle brand guidelines extracted from official docs
- **`skills/oracle-pptx/resources/brand-compliance.md`**: Validation checklist, troubleshooting, export guide

### Reference Guides
- **`skills/oracle-pptx/resources/templates/layout-mapping.md`** (183 lines): Complete layout selection guide with decision trees
- **`skills/oracle-pptx/examples/README.md`** (143 lines): Example workflows overview
- **`skills/oracle-pptx/examples/basic-presentation/README.md`** (315 lines): Step-by-step tutorial for 5-slide presentation

---

## 🛠️ Technical Details

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

**Required** (for script usage):
- Python 3.7+
- `markitdown[pptx]`: Text extraction from PowerPoint
- `defusedxml`: Secure XML parsing
- `python-pptx`: PowerPoint file manipulation

**Optional**:
- LibreOffice (`soffice`): For thumbnail generation

**Install with**:
```bash
pip3 install "markitdown[pptx]" defusedxml python-pptx
```

### Compatibility

| Platform | Support | Notes |
|----------|---------|-------|
| **AI Agents** | ✅ Claude Code, Cursor, Windsurf, Aider, any agent with AGENTS.md | Via openskills or manual install |
| **Claude.ai** | ✅ Custom Skills upload | Zip and upload via Settings |
| **Claude API** | ✅ Skills API (`/v1/skills`) | Upload via API endpoint |
| **Python** | ✅ 3.7+ | For script execution |
| **PowerPoint** | ✅ Desktop app (Windows/Mac) | Required for editing/presenting |
| **PowerPoint Web** | ⚠️ Limited | Fonts not supported, view-only |
| **Linux** | ✅ Scripts work | Use LibreOffice Impress (partial compatibility) |

---

## 💡 Examples

### Example 1: 5-Slide Product Launch (Dark Theme)

See `skills/oracle-pptx/examples/basic-presentation/README.md` for:
- Complete step-by-step workflow
- JSON structure examples
- Brand compliance checklist
- Common mistakes to avoid
- Expected output samples

### Example 2: Multi-Speaker Presentation

See `skills/oracle-pptx/examples/README.md` for common patterns:
- Cover slide + speaker profiles (1-6 speakers)
- Section dividers for topic breaks
- Content variations (bullet points, 2-column, 3-column, images)
- Impact statements and quotes
- Closing/thank you slides

---

## 🔧 Troubleshooting

### "ModuleNotFoundError" when running scripts
**Solution**: Install Python dependencies:
```bash
pip3 install "markitdown[pptx]" defusedxml python-pptx
```

### Fonts not displaying correctly in PowerPoint
**Solution**: 
- Install Oracle Sans Tab fonts from `skills/oracle-pptx/resources/fonts/OracleSans/`
- Restart PowerPoint after installation
- Use PowerPoint desktop app (not web version)
- For external sharing, export to PDF to preserve fonts

### "Shape not found" error when running replace.py
**Solution**: 
- Generate fresh inventory: `python3 scripts/inventory.py working.pptx fresh-inventory.json`
- Verify shape names in inventory match your replacement JSON
- Check slide numbers are correct (0-indexed)

### Colors don't match Oracle brand
**Solution**: 
- Use only colors specified in `resources/guidelines.md`
- Reference theme colors or custom color swatches 1-49
- Avoid PowerPoint's standard colors or tints

### Text overflow in shapes
**Solution**: 
- Reduce text length or font size
- Select a larger placeholder layout
- Split content across multiple slides

### openskills command not found
**Solution**: 
- Run with `npx`: `npx openskills list`
- Or install globally: `npm install -g openskills`

**For complete troubleshooting**: See `skills/oracle-pptx/resources/brand-compliance.md`

---

## 🏗️ Architecture

### Project Structure

```
oracle-pptx-skill/
├── README.md                          # This file
├── AGENTS.md                          # Agent skills system configuration
├── .gitignore                         # Git ignore rules
├── skills/                            # Agent skills
│   └── oracle-pptx/                  # Oracle PPTX skill (self-contained)
│       ├── SKILL.md                  # Main skill documentation (460 lines)
│       ├── README.md                 # Quick reference (81 lines)
│       ├── scripts/                  # Python utilities
│       │   ├── inventory.py          # Extract text placeholders
│       │   ├── rearrange.py          # Duplicate/reorder slides
│       │   ├── replace.py            # Populate content
│       │   └── thumbnail.py          # Generate visual thumbnails
│       ├── ooxml/                    # OOXML manipulation
│       │   ├── scripts/              # pack, unpack, validate
│       │   └── schemas/              # XML validation schemas
│       ├── resources/                # Self-contained resources
│       │   ├── templates/            # Dark + Light templates + inventories
│       │   ├── fonts/OracleSans/    # Font files (37 .otf files)
│       │   ├── icons/                # 1,078 SVG icons (dark + light)
│       │   ├── guidelines.md         # Brand guidelines (181 lines)
│       │   └── brand-compliance.md   # Validation guide
│       └── examples/                 # Example workflows
│           ├── README.md             # Examples overview
│           └── basic-presentation/   # 5-slide tutorial
└── openspec/                         # Spec-driven development
    ├── specs/                        # Approved specifications
    │   └── oracle-pptx-creation/     # 12 requirements
    └── changes/archive/              # Historical changes
```

**Note**: `/reference` directory excluded from repository (development materials only)

---

## 🤝 Contributing

### Adding New Features

This project uses [OpenSpec](https://github.com/fissionai/openspec) for spec-driven development:

1. **Create a proposal**:
   ```bash
   openspec create <change-id>
   ```

2. **Document** requirements, design, and tasks in `openspec/changes/<id>/`

3. **Implement** following the tasks

4. **Archive** when complete:
   ```bash
   openspec archive <change-id> --yes
   ```

### Code Style

- Follow existing patterns in `skills/oracle-pptx/scripts/`
- Concise Python code with minimal verbosity
- Clear, descriptive variable names
- Include error handling and validation
- Add docstrings for functions

### Submitting Changes

1. Fork the repository
2. Create a feature branch
3. Make your changes following the code style
4. Test thoroughly with Oracle templates
5. Submit a pull request with clear description

---

## 📖 Resources

### Oracle Brand Resources (Included in this Skill)
- ✅ FY26 Dark and Light templates (v8.5)
- ✅ Oracle Sans Tab fonts (37 font files)
- ✅ Oracle icons for presentations (1,078 SVG files)
- ✅ Brand guidelines (extracted from official docs)
- ✅ Pre-generated template inventories

### Oracle Brand Resources (VPN Required)
- Oracle icon library (extended collection)
- Oracle photography guidelines
- Custom template building guidance

**Contact Oracle Brand Team** for resources requiring VPN access or custom template requests.

---

## 📄 License

Oracle templates, fonts, icons, and guidelines are proprietary to Oracle Corporation. This skill is for internal Oracle use or authorized partners only.

See [LICENSE](LICENSE) for complete terms.

---

## 📌 Version Information

- **Skill Version**: 1.0.0
- **Template Base**: Oracle FY26 v8.5 (January 2026)
- **SKILL.md Format**: Claude Agent Skills specification compliant
- **Compliance**: 100% with Claude Agent Skills best practices
- **openskills Compatible**: ✅ Yes (standard SKILL.md format)
- **Status**: Production-ready

---

## 💬 Support

### For Agent Skill Issues
- Review `skills/oracle-pptx/SKILL.md` for complete usage guidance
- Check `skills/oracle-pptx/resources/brand-compliance.md` for troubleshooting
- Verify Python dependencies are installed: `pip3 list | grep -E "markitdown|defusedxml|python-pptx"`
- Report issues: [GitHub Issues](https://github.com/beltonk/oracle-pptx-skill/issues)

### For Oracle Brand Questions
- Contact Oracle Brand Team for official guidance
- Reference `skills/oracle-pptx/resources/guidelines.md` for documented standards
- VPN required for extended icon library and custom template requests

### For Technical Issues
- Validate PPTX structure: `python3 ooxml/scripts/validate.py <file.pptx>`
- Check Python version: `python3 --version` (3.7+ required)
- Verify fonts installed: Check system font library for "Oracle Sans Tab"
- Check openskills: `npx openskills list` should show `oracle-pptx`

---

## 🌟 Related Projects

- [openskills](https://github.com/numman-ali/openskills) - Universal skills loader for AI coding agents
- [Anthropic Skills](https://github.com/anthropics/skills) - Official Anthropic agent skills
- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills) - Official documentation

---

**Ready to create Oracle-compliant presentations with AI?**

```bash
# Install with one command
npx openskills install beltonk/oracle-pptx-skill --global --universal

# Then ask your AI agent
"Create an Oracle presentation about cloud migration with 5 slides"
```

Start with the examples in `skills/oracle-pptx/examples/` or read the main documentation in `skills/oracle-pptx/SKILL.md`.

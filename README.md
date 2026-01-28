# Oracle PPTX Agent Skill

**AI agent skill for creating Oracle-compliant PowerPoint presentations**

Universal agent skill that enables AI assistants to create professional PowerPoint presentations following Oracle's brand guidelines, templates, and accessibility requirements.

[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Skills Format](https://img.shields.io/badge/format-Claude%20Agent%20Skills-blue.svg)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills)
[![Compatible](https://img.shields.io/badge/compatible-openskills-green.svg)](https://github.com/numman-ali/openskills)

**Self-contained**: 32MB | 1,179 files | No external dependencies

---

## 🚀 Installation

Install the skill globally with [openskills](https://github.com/numman-ali/openskills):

```bash
# Install the skill
npx openskills install beltonk/oracle-pptx-skill --global --universal

# Sync to update AGENTS.md
npx openskills sync
```

**That's it!** The skill is now available to all your AI agents (Claude Code, Cursor, Windsurf, Aider, etc.).

**Verify installation**:

```bash
npx openskills list
# Should show: oracle-pptx
```

**Update the skill**:

```bash
npx openskills update oracle-pptx
npx openskills sync
```

---

## 🎯 How to Use

Once installed, simply ask your AI agent to create Oracle presentations:

```
Create an Oracle presentation with the following structure:
- Cover slide: "Cloud Migration Strategy"
- Content slide: Benefits of cloud adoption (3 bullet points)
- Content slide: Migration timeline
- Thank you slide

Use the Dark theme and follow Oracle brand guidelines.
```

The AI agent will:
1. Load the oracle-pptx skill automatically
2. Select appropriate template slides
3. Follow Oracle brand guidelines
4. Create a compliant presentation

---

## 📦 What's Included

This skill provides everything needed to create Oracle-branded presentations:

### Templates
- **Dark theme** (51 slides): For large live events, formal presentations
- **Light theme** (55 slides): For virtual events, documentation, internal use

### Resources
- **Brand guidelines**: Complete Oracle PowerPoint design standards
- **Fonts**: Oracle Sans Tab font family (37 font files)
- **Icons**: 1,078 SVG icons optimized for dark and light themes
- **Scripts**: Python utilities for PPTX manipulation
- **Examples**: Step-by-step workflow tutorials

### Documentation
- **SKILL.md** (460 lines): Complete agent skill documentation with workflows
- **Layout mapping**: Guide for selecting appropriate slide layouts
- **Brand compliance**: Validation checklist and troubleshooting
- **Examples**: 5-slide tutorial and multi-speaker patterns

---

## 🎨 Templates

### Dark Theme (Default)
**Use for**: Large live events, formal presentations, executive briefings

**Key layouts**:
- Cover with OCI/Database branding
- Speaker profiles (1-6 speakers)
- Section dividers
- Impact statements
- Content slides: bullet points, 2-column, 3-column, images
- Thank you/closing

### Light Theme
**Use for**: Virtual events, documentation, internal meetings, workshops

**Key layouts**: Similar to Dark theme with additional layouts

**Complete reference**: See `skills/oracle-pptx/resources/templates/layout-mapping.md`

---

## ✅ Oracle Brand Compliance

All presentations created with this skill follow Oracle's brand standards:

### Required Elements
- ✅ **Footer**: `Copyright © [YEAR], Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted`
- ✅ **Fonts**: Oracle Sans Tab only (Bold for headers, Regular for body)
- ✅ **Colors**: Oracle palette (Brand 170, Teal 70, Pine 70, Sky 140, Rose 140, Oracle Red, Pine 140)
- ✅ **Layouts**: From Oracle templates (no custom layouts)
- ✅ **Icons**: From Oracle icon library (1,078 included)
- ✅ **Accessibility**: High contrast, alt text, logical reading order

### Validation
The skill includes:
- Complete validation checklist
- Common issue troubleshooting
- Export guidance for external sharing
- Oracle Brand Team contact information

**Details**: See `skills/oracle-pptx/resources/brand-compliance.md`

---

## 💡 Examples

### Example 1: Simple 5-Slide Presentation

```
Create a 5-slide Oracle presentation about our Q1 results:
- Cover: "Q1 2026 Results"
- Content: Key highlights (3 bullet points)
- Content: Revenue growth chart placeholder
- Content: Next quarter goals
- Closing: Thank you with contact info

Use Dark theme.
```

### Example 2: Multi-Speaker Event

```
Create an Oracle presentation for a 3-speaker panel:
- Cover: "AI Innovation Summit"
- Speaker profiles for: Sarah Chen (AI Lead), Mike Rodriguez (Cloud Architect), Lisa Park (Product Manager)
- Section divider: "The Future of AI"
- Content: 5 key trends
- Thank you slide

Use Light theme.
```

**Detailed tutorials**: See `skills/oracle-pptx/examples/`

---

## 📚 Documentation

All documentation is included in the skill package:

- **`skills/oracle-pptx/SKILL.md`**: Main agent skill documentation (460 lines)
- **`skills/oracle-pptx/resources/guidelines.md`**: Oracle brand guidelines (181 lines)
- **`skills/oracle-pptx/resources/brand-compliance.md`**: Validation and troubleshooting
- **`skills/oracle-pptx/resources/templates/layout-mapping.md`**: Layout selection guide (183 lines)
- **`skills/oracle-pptx/examples/`**: Step-by-step tutorials

AI agents access these automatically when needed through progressive disclosure.

---

## 🔧 For PowerPoint Editing

If you need to edit presentations in PowerPoint (optional):

1. **Install Oracle fonts**: Available in `skills/oracle-pptx/resources/fonts/OracleSans/`
   - macOS: Double-click each .otf file and click "Install Font"
   - Windows: Right-click each .otf file and select "Install"
   - Linux: Copy to `~/.fonts/` and run `fc-cache -f -v`

2. **Use PowerPoint desktop app**: Web version doesn't support Oracle fonts

3. **For external sharing**: Export to PDF to preserve fonts

---

## 🛠️ Troubleshooting

### Skill not loading
```bash
npx openskills list        # Verify oracle-pptx is installed
npx openskills sync        # Update AGENTS.md
```

### AI agent not using the skill
Make sure your request mentions "Oracle presentation" or "Oracle slides" to trigger the skill.

### Font issues in PowerPoint
Install Oracle Sans Tab fonts from `skills/oracle-pptx/resources/fonts/OracleSans/` and use PowerPoint desktop app.

### For more help
- Check `skills/oracle-pptx/resources/brand-compliance.md` for complete troubleshooting
- Report issues: [GitHub Issues](https://github.com/beltonk/oracle-pptx-skill/issues)

---

## 🏗️ What is OpenSpec?

This project uses [OpenSpec](https://github.com/fissionai/openspec) for spec-driven development. OpenSpec manages:

- **Specifications**: Requirements for the oracle-pptx-creation capability (12 requirements)
- **Change tracking**: Historical record of how the skill was built
- **Validation**: Ensures changes meet requirements before implementation

```bash
# View specifications
openspec list --specs

# View change history
ls openspec/changes/archive/
```

**For contributors**: See the Contributing section below.

---

## 🤝 Contributing

### Adding Features

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

### Submitting Changes

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Oracle templates
5. Submit a pull request

---

## 📖 Resources

### Included in This Skill
- ✅ Oracle FY26 templates (Dark and Light, v8.5)
- ✅ Oracle Sans Tab fonts (37 font files)
- ✅ Oracle icons (1,078 SVG files)
- ✅ Brand guidelines
- ✅ Pre-generated template inventories

### Requires Oracle VPN
- Extended icon library
- Photography guidelines
- Custom template building

**Contact Oracle Brand Team** for VPN-required resources.

---

## 📄 License

Oracle templates, fonts, icons, and guidelines are proprietary to Oracle Corporation. This skill is for internal Oracle use or authorized partners only.

---

## 📌 Version

- **Version**: 1.0.0
- **Template Base**: Oracle FY26 v8.5
- **Format**: Claude Agent Skills specification compliant
- **openskills**: ✅ Compatible
- **Status**: Production-ready

---

## 💬 Support

### Issues with the Skill
- Review documentation: `skills/oracle-pptx/SKILL.md`
- Check troubleshooting: `skills/oracle-pptx/resources/brand-compliance.md`
- Report bugs: [GitHub Issues](https://github.com/beltonk/oracle-pptx-skill/issues)

### Oracle Brand Questions
- Contact Oracle Brand Team
- Reference: `skills/oracle-pptx/resources/guidelines.md`

### openskills Issues
- See [openskills documentation](https://github.com/numman-ali/openskills)
- Verify: `npx openskills list` shows `oracle-pptx`

---

## 🌟 Related

- [openskills](https://github.com/numman-ali/openskills) - Universal skills loader for AI agents
- [Anthropic Skills](https://github.com/anthropics/skills) - Official Anthropic agent skills
- [Claude Agent Skills Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills) - Official specification

---

**Ready to create Oracle presentations?**

```bash
# Install in 2 commands
npx openskills install beltonk/oracle-pptx-skill --global --universal
npx openskills sync

# Then ask your AI agent
"Create an Oracle presentation about cloud security with 5 slides"
```

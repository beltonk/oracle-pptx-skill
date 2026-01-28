# Installation Guide

Quick guide for installing and using the Oracle PPTX agent skill across different platforms.

## For Users with openskills

If you have `openskills` installed:

### Clone and install

```bash
# Clone the repository
git clone https://github.com/beltonk/oracle-pptx-skill.git
cd oracle-pptx-skill

# The skill is already in the correct location: skills/oracle-pptx/
# Use with openskills:
openskills read oracle-pptx
```

The skill will be automatically discovered when you need to create Oracle presentations.

## For Claude.ai Users

### Upload as a custom skill

1. **Download the skill**:
   ```bash
   git clone https://github.com/beltonk/oracle-pptx-skill.git
   cd oracle-pptx-skill
   ```

2. **Create a zip file**:
   ```bash
   cd skills
   zip -r oracle-pptx.zip oracle-pptx/
   ```

3. **Upload to Claude.ai**:
   - Go to Settings > Features > Custom Skills
   - Click "Upload Skill"
   - Select `oracle-pptx.zip`
   - Wait for upload to complete

4. **Use the skill**:
   ```
   Create an Oracle presentation about cloud migration with 5 slides
   ```

## For Claude Code / Cursor Users

### Copy to your skills directory

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

## For Claude API Users

### Upload via API

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

## Install Python Dependencies

Required for running the scripts locally:

```bash
pip3 install "markitdown[pptx]" defusedxml python-pptx
```

## Install Oracle Fonts

Required for editing presentations in PowerPoint:

1. Navigate to the fonts directory:
   ```bash
   cd oracle-pptx-skill/skills/oracle-pptx/resources/fonts/OracleSans/
   ```

2. **macOS**: Double-click each `.otf` file and click "Install Font"

3. **Windows**: Right-click each `.otf` file and select "Install" or "Install for all users"

4. **Linux**: 
   ```bash
   mkdir -p ~/.fonts
   cp *.otf ~/.fonts/
   fc-cache -f -v
   ```

## Verify Installation

### For openskills

```bash
openskills read oracle-pptx
# Should display the skill documentation
```

### For script usage

```bash
cd oracle-pptx-skill/skills/oracle-pptx
python3 scripts/inventory.py --help
# Should display help text
```

### For font installation

Open PowerPoint and check if "Oracle Sans Tab" appears in the font list.

## Quick Start

Once installed, try creating a simple presentation:

```bash
cd oracle-pptx-skill/skills/oracle-pptx

# 1. Rearrange template slides (cover, content, closing)
python3 scripts/rearrange.py \
  resources/templates/dark-template.pptx \
  "0,13,11" \
  output.pptx

# 2. Generate inventory
python3 scripts/inventory.py output.pptx inventory.json

# 3. Review inventory.json and create replacement.json with your content

# 4. Populate slides
python3 scripts/replace.py output.pptx replacement.json final.pptx

# 5. Open in PowerPoint
open final.pptx  # macOS
# or: start final.pptx  # Windows
```

## Troubleshooting

### "ModuleNotFoundError" when running scripts
**Solution**: Install Python dependencies:
```bash
pip3 install "markitdown[pptx]" defusedxml python-pptx
```

### Fonts not appearing in PowerPoint
**Solution**: 
- Install fonts from `skills/oracle-pptx/resources/fonts/OracleSans/`
- Restart PowerPoint after installation
- Use PowerPoint desktop app (not web version)

### "Permission denied" when running scripts
**Solution**: Make scripts executable:
```bash
chmod +x skills/oracle-pptx/scripts/*.py
```

### openskills command not found
**Solution**: Install openskills or use the skill directly by reading `skills/oracle-pptx/SKILL.md`

## Platform-Specific Notes

### macOS
- Fonts install to `/Library/Fonts/` or `~/Library/Fonts/`
- Use `open` command to launch PowerPoint
- May need to approve font installation in Security & Privacy settings

### Windows
- Fonts install to `C:\Windows\Fonts\`
- Use PowerPoint desktop app, not Office Online
- Right-click scripts and "Run with Python" if double-clicking doesn't work

### Linux
- PowerPoint not available; use LibreOffice Impress (partial compatibility)
- For full Oracle brand compliance, export to PDF after creating on Windows/Mac
- Scripts work normally with Python 3.7+

## Getting Help

- **Documentation**: See `skills/oracle-pptx/SKILL.md` for complete guidance
- **Examples**: Check `skills/oracle-pptx/examples/` for step-by-step tutorials
- **Troubleshooting**: See `skills/oracle-pptx/resources/brand-compliance.md`
- **Issues**: Report at https://github.com/beltonk/oracle-pptx-skill/issues

## Next Steps

1. Read the main documentation: `skills/oracle-pptx/SKILL.md`
2. Try the basic example: `skills/oracle-pptx/examples/basic-presentation/README.md`
3. Review Oracle brand guidelines: `skills/oracle-pptx/resources/guidelines.md`
4. Create your first Oracle presentation!

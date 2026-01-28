# Project Context

## Purpose

This project provides AI agent skills for creating Oracle-compliant PowerPoint presentations. The goal is to enable rapid creation of professional, brand-compliant Oracle presentations that strictly follow Oracle's FY26 design guidelines, templates, and accessibility requirements.

## Tech Stack

- **Python 3.x**: For OOXML manipulation, template processing, and validation
- **PowerPoint/OOXML**: Office Open XML format for presentation files
- **Markdown**: For skill documentation and content extraction
- **OpenSpec**: Spec-driven development and change management

### Dependencies
- `markitdown[pptx]`: Text extraction from PowerPoint files
- `defusedxml`: Secure XML parsing
- `python-pptx`: PowerPoint file manipulation
- Python scripts from existing `pptx` skill:
  - `ooxml/scripts/unpack.py`, `pack.py`, `validate.py`
  - `scripts/rearrange.py`, `inventory.py`, `replace.py`, `thumbnail.py`

## Project Conventions

### Code Style
- Concise Python code with minimal verbosity
- Avoid redundant print statements
- Clear, descriptive variable names without over-verbosity
- Follow existing code patterns from `reference/skills/pptx/`

### Architecture Patterns
- **Skill-based architecture**: Capabilities delivered as agent skills (markdown documentation)
- **Template-based workflow**: Use Oracle's official templates as base, rearrange slides, populate content
- **Separation of concerns**: 
  - Core PPTX manipulation → existing `pptx` skill
  - Oracle-specific guidance → new `oracle-pptx` skill
- **Reference-based approach**: Skills reference templates and guidelines files, extract on-demand

### File Organization
```
./
├── openspec/                      # Spec-driven development artifacts
│   ├── changes/                   # Proposed changes
│   │   └── add-oracle-pptx-skill/ # Current proposal
│   └── specs/                     # Approved specifications (after archiving)
├── skills/                        # Agent skills (future)
│   └── oracle-pptx/              # Oracle PPTX skill (to be created)
├── reference/                     # Reference materials
│   ├── guidelines/               # Oracle brand guidelines
│   │   ├── Oracle Powerpoint Guidelines.md  # Extracted guidelines
│   │   └── Oracle Powerpoint Guidelines.pptx # Source document
│   ├── resources/                # Oracle resources
│   │   ├── templates/           # PowerPoint templates
│   │   │   ├── Oracle Powerpoint Template (Dark).pptx
│   │   │   └── Oracle Powerpoint Template (Light).pptx
│   │   ├── fonts/               # Oracle Sans Tab fonts
│   │   │   └── OracleSans/
│   │   └── icons/               # Oracle icons (SVG)
│   │       ├── dark-theme/
│   │       └── light-theme/
│   └── skills/
│       └── pptx/                 # Existing PPTX skill (reference)
└── AGENTS.md                     # Agent instructions and skill catalog
```

### Testing Strategy
- **Template validation**: Validate all template manipulations against OOXML schemas
- **Visual validation**: Generate thumbnail grids to verify layout correctness
- **Brand compliance**: Check fonts, colors, footers, and accessibility
- **End-to-end testing**: Test complete workflows for Dark and Light themes

### Git Workflow
- This is not currently a git repository
- Changes are managed through OpenSpec workflow:
  1. Create proposal in `openspec/changes/`
  2. Implement according to tasks.md
  3. Archive to `openspec/changes/archive/` after deployment

## Domain Context

### Oracle Brand Guidelines (FY26)
- **Current version**: 8.5 (January 2026)
- **Template types**: Dark theme (default for large events) and Light theme (other uses)
- **Fonts**: Oracle Sans Tab family (downloadable with VPN)
- **Accessibility**: Higher contrast, alt text, reading order requirements
- **Slide categories**:
  - **Themed slides**: Cover, section, speakers, thank you, impact (event-customizable)
  - **Standard content**: Title+body, multi-column, quotes, stories (content-focused)

### Oracle Template Structure
- **Dark template**: 51 slides (0-50 indexed)
- **Light template**: 55 slides (0-54 indexed)
- **Themed covers**: OCI/Database style (primary template option)
- **Speaker layouts**: 1, 2, 3, 4, or 6 speakers (with/without headshots)
- **Footer format**: `Copyright © 2026, Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted`

### Key Constraints
- Must use PowerPoint desktop app (not web/SharePoint) for editing
- Oracle Sans Tab fonts must be installed locally
- VPN required for Oracle icon library and brand resources
- Templates are versioned; skill targets FY26 v8.5
- Slides are 0-indexed in all template operations

## Important Constraints

### Technical Constraints
- Python 3.14+ required for latest dependencies
- LibreOffice (`soffice`) required for thumbnail generation (optional feature)
- Poppler (`pdftoppm`) required for PDF-to-image conversion (optional feature)
- Template files must be preserved as-is (no modifications to reference files)

### Brand Constraints
- All presentations must follow Oracle FY26 guidelines strictly
- No deviation from approved colors, fonts, or layouts
- Footer format is mandatory on all slides
- Accessibility compliance is non-negotiable
- Template compatibility must be maintained with other Oracle presentations

### User Workflow Constraints
- Users must have Oracle Sans Tab fonts installed
- Users must edit/present in desktop PowerPoint app
- For external sharing, must export to PDF to preserve fonts
- VPN access required for Oracle brand resources

## External Dependencies

### Oracle Resources (VPN Required)
- Oracle icon library: [VPN link not provided in guidelines]
- Oracle photography library and style guide: [VPN link not provided in guidelines]
- Oracle Brand team: Contact for template compatibility and custom template building

### Reference Files (Local)
**Guidelines**:
- `reference/guidelines/Oracle Powerpoint Guidelines.md`: Extracted design standards (ready to use)
- `reference/guidelines/Oracle Powerpoint Guidelines.pptx`: Source document (FY26 v8.5)

**Templates**:
- `reference/resources/templates/Oracle Powerpoint Template (Dark).pptx`: Dark theme (51 slides)
- `reference/resources/templates/Oracle Powerpoint Template (Light).pptx`: Light theme (55 slides)

**Resources**:
- `reference/resources/fonts/OracleSans/`: Oracle Sans Tab font family
- `reference/resources/icons/dark-theme/`: Icons for dark presentations (~530 SVG files)
- `reference/resources/icons/light-theme/`: Icons for light presentations (~530 SVG files)

### Skills
- Existing `pptx` skill at `reference/skills/pptx/`: Core PowerPoint manipulation capabilities
- This skill provides: HTML-to-PPTX conversion, OOXML editing, template workflows, validation

## Success Criteria

An implementation is successful when:
1. AI agents can create Oracle-compliant presentations by reading the skill
2. All Oracle brand requirements are accurately represented in skill documentation
3. Both Dark and Light theme workflows are fully supported
4. Template inventories and layout mappings are accurate and complete
5. Validation steps ensure brand compliance before finalization
6. Integration with existing `pptx` skill works seamlessly
7. Examples demonstrate end-to-end workflows clearly

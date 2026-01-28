# Design: Oracle PPTX Agent Skill

## Context

Oracle has established comprehensive brand guidelines for PowerPoint presentations in FY26 (version 8.5+). These guidelines include:

- **Themed slides**: Cover, section, speaker, thank you, impact statement - customizable for specific events/branding
- **Standard content slides**: Main content with minimal branding, content-focused
- **Accessibility updates**: Higher contrast, alt text requirements, reading order specifications
- **Template compatibility**: Standardized format types across all Oracle templates
- **Two theme options**: Dark theme (primary/default for large live events) and Light theme (for all other uses)

The skill must bridge the gap between general PowerPoint creation capabilities (existing `pptx` skill) and Oracle-specific requirements.

## Goals / Non-Goals

### Goals
- Provide step-by-step workflows for creating Oracle-compliant presentations
- Codify Oracle's design standards (colors, fonts, layouts, spacing) for AI agent reference
- Support both Dark and Light theme creation with Dark as the default
- Enable template-based presentation creation using Oracle's official templates
- Ensure accessibility compliance is built into the workflow
- Provide clear guidance on themed vs. standard content slides
- Include validation steps to verify Oracle brand compliance

### Non-Goals
- Modifying or extending the core `pptx` skill (reuse existing capabilities)
- Creating new template files (use existing Oracle templates)
- Building a UI or interactive tool (this is an AI agent skill)
- Supporting non-Oracle branding (skill is Oracle-specific)
- Backwards compatibility with pre-FY26 templates

## Decisions

### Decision 1: Skill Structure - Template-Based Workflow
**Choice**: Use the existing `pptx` skill's template-based workflow (rearrange.py, inventory.py, replace.py)

**Rationale**: 
- Oracle templates have well-defined slide layouts that map to the template workflow
- Reuses proven tooling from the existing `pptx` skill
- Separates concerns: core PPTX manipulation (existing skill) vs. Oracle-specific guidance (new skill)

**Alternatives considered**:
- HTML-to-PPTX workflow: Not suitable because Oracle templates have specific layouts that must be preserved
- Direct XML editing: Too low-level and error-prone for brand guideline compliance

### Decision 2: Theme Selection - Dark as Default
**Choice**: Dark theme is the default, with Light theme as an option

**Rationale**:
- Oracle guidelines specify Dark theme for "large live events" (primary use case)
- Light theme for "all uses outside large live events"
- Default should align with the most formal/official presentation context

### Decision 3: Guidelines Integration - Copy Extracted Markdown
**Choice**: Copy pre-extracted guidelines from `reference/guidelines/Oracle Powerpoint Guidelines.md` into skill

**Rationale**:
- Guidelines already extracted to markdown format from official PowerPoint document
- Makes guidelines immediately accessible to AI agents within skill directory
- Provides searchable, structured guidance in skill's `resources/guidelines.md`
- Enables the agent to make informed decisions about layout selection, color usage, etc.
- Maintains single source of truth in reference/ while providing local copy in skill

**Alternatives considered**:
- Referencing external files: Would break self-contained design
- Re-extracting guidelines: Unnecessary duplication of work since markdown already exists
- Minimal guidance: Would result in non-compliant presentations

### Decision 4: Template Inventory - Pre-Generated Reference
**Choice**: Include pre-generated template inventories for common slide types, defaulting to OCI/Database themed slides

**Rationale**:
- Speeds up presentation creation by providing known-good layout mappings
- Documents which slide layouts exist and their purposes
- Enables pattern matching (e.g., "2-column content" → slide 34 in Dark template)
- OCI/Database theme chosen as primary template option

## Key Oracle Brand Requirements

### Colors
- **Theme colors**: Defined in Oracle's theme files (extracted from templates)
- **Custom colors**: 
  - Pine 140 (added in v8.3)
  - OCI/Database themed colors (primary option)
- **Accessibility**: High contrast requirements
- **Links**: Blue default (manually change to yellow on Light slides)

### Fonts
- **Oracle Sans Tab family**: Required (download if not installed)
- **Edit in desktop app**: Must use PowerPoint desktop app, not web/SharePoint
- **Font validation**: Skill should remind users to verify fonts are installed

### Layouts
- **Themed slides**: Cover (OCI/Database style preferred), Section dividers, Speaker slides (1-6 speakers), Thank you, Impact statement
- **Content slides**: Title + body, 2-column, 3-column, Title + 3 points, Bold statement, Quote, Story slides, Abstract backgrounds
- **Special layouts**: Customer story slides with call-to-action fields, Statistics layouts, Photo + text combinations

### Footer Requirements
- Standard format: `Copyright © 2026, Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted`
- Updated from 2025 to 2026 in v8.5
- Footer guidance example on slide 11

### Accessibility
- Higher contrast (compared to previous versions)
- Alt text for images
- Reading order defined
- Specific guidance in guidelines document

### Slide Numbering
- Slides are 0-indexed in template manipulation
- Must account for this in all template mappings

## Technical Architecture

```
skills/oracle-pptx/
├── SKILL.md                    # Main skill documentation
├── scripts/                    # Python scripts for template manipulation
│   ├── inventory.py            # Extract text shapes from presentations
│   ├── rearrange.py           # Duplicate and reorder slides
│   ├── replace.py             # Populate templates with content
│   └── thumbnail.py           # Generate visual thumbnail grids
├── ooxml/                     # OOXML manipulation utilities
│   ├── scripts/               # Core OOXML scripts
│   │   ├── pack.py           # Repack OOXML files
│   │   ├── unpack.py         # Unpack OOXML files
│   │   ├── validate.py       # Validate OOXML structure
│   │   └── validation/       # Validation modules
│   └── schemas/              # OOXML XML schemas for validation
├── resources/                 # Self-contained resources (copied from reference/)
│   ├── fonts/                # Oracle Sans Tab font family
│   │   └── OracleSans/       # Font files
│   ├── icons/                # Oracle icons
│   │   ├── dark-theme/       # Icons for dark theme (SVG)
│   │   └── light-theme/      # Icons for light theme (SVG)
│   ├── templates/            # Oracle templates
│   │   ├── dark-template.pptx
│   │   ├── light-template.pptx
│   │   ├── dark-inventory.json
│   │   └── light-inventory.json
│   └── guidelines.md         # Extracted Oracle guidelines
└── examples/                  # Example workflows and outputs
    ├── basic-presentation/    # Simple 5-slide example
    ├── multi-speaker/        # Multiple speakers example
    └── sample-outputs/       # Generated presentation examples
```

### Self-Contained Design
All resources required for the skill are contained within the skill directory:
- **No external dependencies**: All scripts, schemas, fonts, icons, and templates are copied into the skill
- **Portable**: The entire skill can be moved or shared without breaking references
- **Version controlled**: Resources are versioned with the skill, not referenced externally

### Skill Activation
Skill should be triggered when users request:
- "Create an Oracle presentation"
- "Make Oracle-compliant slides"
- "Use Oracle template" (with dark/light specification)
- "Oracle branded deck"
- Any mention of Oracle + PowerPoint/PPTX/presentation

### Dependencies
- **Pattern reference**: Existing `pptx` skill provides the structural pattern to follow
- **Resource sources**: All resources copied from `reference/` during implementation:
  - Python scripts from `reference/skills/pptx/scripts/`
  - OOXML utilities from `reference/skills/pptx/ooxml/`
  - Fonts from `reference/resources/fonts/OracleSans/`
  - Icons from `reference/resources/icons/dark-theme/` and `reference/resources/icons/light-theme/`
  - Templates from `reference/resources/templates/Oracle Powerpoint Template (Dark).pptx` and `Oracle Powerpoint Template (Light).pptx`
  - Guidelines from `reference/guidelines/Oracle Powerpoint Guidelines.md` (extracted) and `.pptx` (source)
- **Runtime dependencies**: Only standard Python libraries (defusedxml, python-pptx, markitdown)

### Workflow Integration

1. **Theme Selection**: Agent asks user to confirm theme (Dark default, or Light)
2. **Template Analysis**: Read pre-generated inventory from `resources/templates/`
3. **Content Planning**: User provides content, agent maps to appropriate slide layouts
4. **Layout Selection**: Agent selects layouts based on Oracle guidelines and content structure
5. **Template Rearrangement**: Use `scripts/rearrange.py` to duplicate and reorder slides
6. **Content Replacement**: Use `scripts/replace.py` to populate slides with user content
7. **Validation**: Verify Oracle brand compliance (fonts, colors, footers, accessibility)
8. **Output**: Generate final PPTX file

All script references are relative to the skill directory (`skills/oracle-pptx/`), ensuring portability.

## Risks / Trade-offs

### Risk: Template Version Drift
- **Issue**: Oracle templates are versioned (currently v8.5), future versions may have different layouts
- **Mitigation**: 
  - Document template version in skill (FY26 v8.5)
  - Include version detection in workflow
  - Recommend checking Oracle Brand team for latest templates
  - Design skill to be easily updatable when new templates released

### Risk: Font Availability
- **Issue**: Oracle Sans Tab fonts must be downloaded separately
- **Mitigation**:
  - Include clear instructions in skill to verify fonts installed
  - Provide download link (VPN required)
  - Warn that presentations must be edited in desktop app, not web

### Risk: Complex Layout Mappings
- **Issue**: Dark template (51 slides) and Light template (55 slides) have many layout options
- **Mitigation**:
  - Pre-generate and document common layout patterns
  - Include visual thumbnails in `examples/` directory
  - Create decision tree for layout selection based on content type
  - Store pre-generated inventories in `resources/templates/`

### Trade-off: Skill Size vs. Completeness
- **Choice**: Self-contained comprehensive skill with all resources embedded
- **Rationale**: 
  - Oracle brand compliance is critical; partial guidance would lead to non-compliant presentations
  - Self-contained design eliminates external dependencies and version conflicts
  - Makes skill portable and easier to maintain
- **Impact**: Larger skill directory (~5-10MB with fonts/icons), but ensures:
  - No broken references to external files
  - Consistent behavior across environments
  - Complete offline capability

## Migration Plan

No migration required - this is a new capability. Existing `pptx` skill users are unaffected.

## Open Questions

1. **Template inventory generation**: Should we pre-generate and include full inventories for both templates?
   - **Recommendation**: Yes, pre-generate complete inventories and store in `resources/templates/` for fast access
   
2. **Custom color extraction**: Should we extract exact RGB values from Oracle templates for programmatic use?
   - **ANSWERED**: Use extracted guidelines from `reference/guidelines/Oracle Powerpoint Guidelines.md` as base, enhance with RGB values in skill's `resources/guidelines.md`

3. **Layout thumbnails**: Should we include visual thumbnail grids in the skill?
   - **Recommendation**: Yes, generate during skill creation and include in `examples/` directory

4. **Cover slide selection**: Should we support multiple themed cover options?
   - **Recommendation**: Default to OCI/Database themed cover slides as the primary option

5. **Footer customization**: Can users modify the confidentiality level (Internal/Restricted/Highly Restricted)?
   - **Recommendation**: Yes, make this a configurable parameter with Internal as default

6. **Resource management**: How to handle resource updates (fonts, icons, templates, guidelines)?
   - **ANSWERED**: Copy all resources during implementation into skill directory from organized reference locations:
     - Templates: `reference/resources/templates/`
     - Fonts: `reference/resources/fonts/`
     - Icons: `reference/resources/icons/`
     - Guidelines: `reference/guidelines/` (markdown already extracted)
   - Updates require re-copying from reference sources

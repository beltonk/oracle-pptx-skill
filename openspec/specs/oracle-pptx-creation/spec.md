# oracle-pptx-creation Specification

## Purpose
TBD - created by archiving change add-oracle-pptx-skill. Update Purpose after archive.
## Requirements
### Requirement: Oracle Brand Compliance
The system SHALL enable creation of PowerPoint presentations that comply with Oracle FY26 brand guidelines including colors, fonts, layouts, and accessibility requirements.

#### Scenario: Create Oracle-branded presentation with correct theme colors
- **WHEN** an AI agent creates an Oracle presentation
- **THEN** the presentation SHALL use Oracle-approved theme colors from the template
- **AND** custom colors SHALL match Oracle's defined palette (including Pine 140)
- **AND** link colors SHALL be blue (or yellow on Light slides)

#### Scenario: Apply Oracle fonts correctly
- **WHEN** an AI agent creates an Oracle presentation
- **THEN** the presentation SHALL use Oracle Sans Tab font family
- **AND** the agent SHALL verify fonts are available or instruct user to download
- **AND** the agent SHALL remind user to edit in PowerPoint desktop app (not web)

#### Scenario: Include proper Oracle footer
- **WHEN** an AI agent creates an Oracle presentation
- **THEN** each slide SHALL include the standard footer format: "Copyright © 2026, Oracle and/or its affiliates | Confidential: Internal/Restricted/Highly Restricted"
- **AND** the confidentiality level SHALL be configurable (Internal/Restricted/Highly Restricted)
- **AND** the year SHALL match the current year

#### Scenario: Meet accessibility requirements
- **WHEN** an AI agent creates an Oracle presentation
- **THEN** the presentation SHALL use high-contrast colors for text and backgrounds
- **AND** images SHALL have placeholder guidance for alt text
- **AND** slide reading order SHALL follow Oracle's accessibility guidelines

### Requirement: Theme Selection
The system SHALL support both Dark theme and Light theme presentations with Dark theme as the default.

#### Scenario: Default to Dark theme
- **WHEN** a user requests an Oracle presentation without specifying theme
- **THEN** the system SHALL use the Dark theme template by default
- **AND** the system SHALL use Oracle's Dark template file as the base

#### Scenario: Allow Light theme selection
- **WHEN** a user explicitly requests Light theme
- **THEN** the system SHALL use the Light theme template
- **AND** the system SHALL apply Light-theme-specific formatting (e.g., yellow links)
- **AND** the system SHALL use Oracle's Light template file as the base

#### Scenario: Explain theme usage guidelines
- **WHEN** the system creates an Oracle presentation
- **THEN** the system SHALL inform user that Dark theme is for "large live events"
- **AND** Light theme is for "all uses outside large live events"
- **AND** speaker slides for live events should omit headshots

### Requirement: Template-Based Workflow
The system SHALL use Oracle's official FY26 PowerPoint templates (version 8.5+) and preserve their layouts, formatting, and design elements.

#### Scenario: Select appropriate slide layouts
- **WHEN** a user provides presentation content
- **THEN** the system SHALL analyze content structure and select appropriate Oracle slide layouts
- **AND** the system SHALL choose from: cover slides, section dividers, speaker slides (1-6 speakers), content slides (1/2/3-column), bold statements, quotes, story slides, and thank you slides
- **AND** the system SHALL distinguish between themed slides (customizable for events) and standard content slides (minimal branding)

#### Scenario: Use template rearrangement workflow
- **WHEN** creating an Oracle presentation
- **THEN** the system SHALL use `skills/oracle-pptx/scripts/rearrange.py` to duplicate and reorder template slides
- **AND** the system SHALL map content requirements to specific slide indices from the template
- **AND** the system SHALL use 0-based indexing for all slide references
- **AND** the system SHALL load templates from `skills/oracle-pptx/resources/templates/`

#### Scenario: Preserve template formatting
- **WHEN** populating Oracle template slides with content
- **THEN** the system SHALL use `skills/oracle-pptx/scripts/replace.py` to update text while preserving formatting
- **AND** the system SHALL use `skills/oracle-pptx/scripts/inventory.py` to extract text shapes
- **AND** the system SHALL maintain Oracle's paragraph properties (bullets, alignment, font sizes)
- **AND** the system SHALL preserve shape sizes and positions from the template

### Requirement: Layout Inventory and Mapping
The system SHALL maintain accurate inventories of available layouts in both Dark and Light templates for efficient layout selection.

#### Scenario: Provide layout inventory for Dark theme
- **WHEN** creating a Dark theme presentation
- **THEN** the system SHALL load the Dark template inventory from `skills/oracle-pptx/resources/templates/dark-inventory.json`
- **AND** the system SHALL reference layout mappings from `skills/oracle-pptx/resources/templates/layout-mapping.md`
- **AND** the system SHALL provide descriptions of each available layout (51 slides, 0-indexed 0-50)
- **AND** the system SHALL map common content patterns to appropriate slide indices

#### Scenario: Provide layout inventory for Light theme
- **WHEN** creating a Light theme presentation
- **THEN** the system SHALL load the Light template inventory from `skills/oracle-pptx/resources/templates/light-inventory.json`
- **AND** the system SHALL reference layout mappings from `skills/oracle-pptx/resources/templates/layout-mapping.md`
- **AND** the system SHALL provide descriptions of each available layout (55 slides, 0-indexed 0-54)
- **AND** the system SHALL map common content patterns to appropriate slide indices

#### Scenario: Use OCI/Database themed cover slides
- **WHEN** a user needs a cover slide
- **THEN** the system SHALL use OCI/Database themed cover slides as the default option
- **AND** the system SHALL apply the appropriate OCI/Database branding and styling

### Requirement: Content Planning and Population
The system SHALL help users plan presentation content and map it to appropriate Oracle slide layouts.

#### Scenario: Analyze content and suggest layouts
- **WHEN** a user describes presentation content
- **THEN** the system SHALL identify content types (title, sections, bullet points, images, quotes, statistics, stories)
- **AND** the system SHALL suggest appropriate Oracle layouts for each content piece
- **AND** the system SHALL warn if content structure doesn't match selected layout (e.g., 2 items in a 3-column layout)

#### Scenario: Generate replacement JSON with Oracle formatting
- **WHEN** populating Oracle template slides
- **THEN** the system SHALL create replacement JSON with proper paragraph properties
- **AND** the system SHALL include formatting: bold for headers, bullets for lists, alignment for centered text, theme colors or RGB colors
- **AND** the system SHALL exclude bullet symbols from text (•, -, *) when `"bullet": true`

#### Scenario: Clear unused template placeholders
- **WHEN** applying content to Oracle templates
- **THEN** the system SHALL automatically clear text from shapes not specified in replacement JSON
- **AND** the system SHALL only populate shapes that have content in the replacement JSON
- **AND** the system SHALL preserve template shapes that are meant to remain empty

### Requirement: Themed vs. Standard Content Slides
The system SHALL distinguish between themed slides (event-customizable) and standard content slides (content-focused).

#### Scenario: Identify themed slides
- **WHEN** creating an Oracle presentation
- **THEN** the system SHALL recognize themed slides as: cover, section dividers, speaker slides, thank you, and impact statement
- **AND** the system SHALL inform user these slides are "meant to be updated for specific events or branding moments"

#### Scenario: Identify standard content slides
- **WHEN** creating an Oracle presentation
- **THEN** the system SHALL recognize standard content slides as: title + body, multi-column layouts, quotes, stories, statistics
- **AND** the system SHALL inform user these slides have "minimal branding, allowing the content to be the focus"

### Requirement: Speaker Slide Customization
The system SHALL support speaker slides with 1-6 speakers and optional headshots based on event type.

#### Scenario: Create speaker slide for large live events
- **WHEN** creating a speaker slide for a large live event
- **THEN** the system SHALL use speaker slide layouts without headshot placeholders
- **AND** the system SHALL include speaker name and title fields

#### Scenario: Create speaker slide for virtual events
- **WHEN** creating a speaker slide for virtual events or non-live uses
- **THEN** the system SHALL use speaker slide layouts with headshot placeholders
- **AND** the system SHALL include speaker name, title, and photo placeholders
- **AND** the system SHALL support layouts for 1, 2, 3, 4, or 6 speakers

#### Scenario: Include speaker profile information
- **WHEN** creating detailed speaker slides
- **THEN** the system SHALL support speaker profile layouts with: experience, expertise, and location fields
- **AND** the system SHALL include icon placeholders for location, building, and document icons

### Requirement: Validation and Quality Assurance
The system SHALL validate Oracle presentations for brand compliance before finalizing.

#### Scenario: Validate Oracle brand requirements
- **WHEN** completing an Oracle presentation
- **THEN** the system SHALL verify: Oracle fonts are used, footer format is correct, colors match Oracle palette, layouts are from Oracle templates
- **AND** the system SHALL check for accessibility compliance (contrast, alt text guidance)
- **AND** the system SHALL warn user of any non-compliant elements

#### Scenario: Visual validation with thumbnails
- **WHEN** validating Oracle presentation layout
- **THEN** the system SHALL offer to generate thumbnail grids using `skills/oracle-pptx/scripts/thumbnail.py`
- **AND** the system SHALL inspect thumbnails for: text cutoff, text overlap, positioning issues, contrast problems
- **AND** the system SHALL recommend corrections if issues are found
- **AND** the system SHALL reference example thumbnails in `skills/oracle-pptx/examples/`

#### Scenario: Provide troubleshooting guidance
- **WHEN** validation identifies issues
- **THEN** the system SHALL provide specific guidance on how to fix issues
- **AND** the system SHALL reference relevant sections of Oracle guidelines
- **AND** the system SHALL suggest consulting Oracle Brand team for complex questions

### Requirement: Template Version Compatibility
The system SHALL document and track Oracle template versions to ensure compatibility.

#### Scenario: Document template version
- **WHEN** using Oracle templates
- **THEN** the system SHALL document that it uses Oracle FY26 templates version 8.5
- **AND** the system SHALL note key features of this version: updated 2026 footers, Pine 140 color, new abstract background layouts, Left middle title layouts

#### Scenario: Detect template version mismatches
- **WHEN** a user provides a different Oracle template version
- **THEN** the system SHALL warn that slide indices and layouts may differ
- **AND** the system SHALL recommend using the documented template version
- **AND** the system SHALL suggest checking with Oracle Brand team for latest templates

### Requirement: Self-Contained Skill Structure
The system SHALL be fully self-contained with all required scripts, resources, and dependencies within the skill directory.

#### Scenario: Use self-contained scripts
- **WHEN** creating or editing Oracle presentations
- **THEN** the system SHALL use scripts from within the skill directory: `skills/oracle-pptx/scripts/inventory.py`, `skills/oracle-pptx/scripts/rearrange.py`, `skills/oracle-pptx/scripts/replace.py`, `skills/oracle-pptx/scripts/thumbnail.py`
- **AND** the system SHALL use OOXML utilities from `skills/oracle-pptx/ooxml/scripts/`
- **AND** all script paths SHALL be relative to the skill directory

#### Scenario: Use self-contained resources
- **WHEN** accessing fonts, icons, or templates
- **THEN** the system SHALL reference resources from `skills/oracle-pptx/resources/`
- **AND** fonts SHALL be loaded from `resources/fonts/OracleSans/`
- **AND** icons SHALL be loaded from `resources/icons/dark-theme/` or `resources/icons/light-theme/`
- **AND** templates SHALL be loaded from `resources/templates/`
- **AND** no external file dependencies SHALL be required

#### Scenario: Portable skill deployment
- **WHEN** the skill directory is copied or moved
- **THEN** all functionality SHALL remain intact without path updates
- **AND** all resources SHALL be accessible from the new location
- **AND** the skill SHALL work in any environment with Python installed

### Requirement: Resource References and Access
The system SHALL provide access to all Oracle brand resources through the self-contained skill structure.

#### Scenario: Access Oracle template files
- **WHEN** creating Oracle presentations
- **THEN** the system SHALL use the Dark template from `skills/oracle-pptx/resources/templates/dark-template.pptx`
- **AND** the system SHALL use the Light template from `skills/oracle-pptx/resources/templates/light-template.pptx`
- **AND** the system SHALL reference pre-generated inventories from `resources/templates/dark-inventory.json` and `resources/templates/light-inventory.json`

#### Scenario: Access Oracle fonts
- **WHEN** verifying or documenting font usage
- **THEN** the system SHALL reference Oracle Sans Tab fonts from `skills/oracle-pptx/resources/fonts/OracleSans/`
- **AND** the system SHALL provide installation instructions for these fonts
- **AND** the system SHALL note fonts are included in the skill for reference

#### Scenario: Access Oracle icons
- **WHEN** users need icons for presentations
- **THEN** the system SHALL reference icons from `skills/oracle-pptx/resources/icons/dark-theme/` for dark presentations
- **AND** the system SHALL reference icons from `skills/oracle-pptx/resources/icons/light-theme/` for light presentations
- **AND** the system SHALL provide guidance on icon selection based on content

#### Scenario: Access Oracle guidelines
- **WHEN** creating Oracle presentations
- **THEN** the system SHALL reference guidelines from `skills/oracle-pptx/resources/guidelines.md` (copied from `reference/guidelines/Oracle Powerpoint Guidelines.md`)
- **AND** the system SHALL note that guidelines are extracted from official Oracle FY26 v8.5 PowerPoint Guidelines
- **AND** the system SHALL provide design standards, color specifications, font requirements, layout guidance, footer formats, and accessibility requirements

#### Scenario: Provide Oracle brand resource links
- **WHEN** user needs additional Oracle brand information not in the skill
- **THEN** the system SHALL note that Oracle icon library and photography guidance require VPN access
- **AND** the system SHALL recommend contacting Oracle Brand team for template compatibility questions
- **AND** the system SHALL note that core resources (templates, fonts, icons, guidelines) are already included in the skill

### Requirement: PDF Export Guidance
The system SHALL provide guidance for exporting Oracle presentations as PDFs for external sharing.

#### Scenario: Export for external sharing
- **WHEN** user needs to share Oracle presentation externally
- **THEN** the system SHALL recommend saving as PDF to preserve fonts
- **AND** the system SHALL provide PC export instructions: File > export > create PDF/XPS > minimum size
- **AND** the system SHALL provide Mac export instructions: File > export > PDF, then File > reduce file size
- **AND** the system SHALL note this ensures Oracle fonts display correctly for recipients


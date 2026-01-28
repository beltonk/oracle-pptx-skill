# Change: Add Oracle PPTX Agent Skill

## Why

Users need an easy way to create Oracle-compliant PowerPoint presentations that strictly follow Oracle's FY26 brand guidelines, design standards, and template requirements. Currently, there's no systematic way to ensure presentations adhere to Oracle's specific requirements for layouts, colors, fonts, spacing, headers, footers, and theme usage.

## What Changes

- Create a new agent skill at `./skills/oracle-pptx/` that provides comprehensive guidance for creating Oracle-compliant presentations
- Extract and codify Oracle PowerPoint guidelines from the official Oracle PowerPoint Guidelines document
- Support both Dark theme (default) and Light theme templates based on Oracle's official FY26 templates
- Default to OCI/Database themed slides as the primary template option
- Provide systematic workflows for:
  - Creating new Oracle-branded presentations with proper theme selection
  - Applying Oracle's design standards (colors, fonts, layouts, spacing)
  - Using Oracle-specific slide layouts (cover, section, speakers, content, thank you, etc.)
  - Ensuring accessibility compliance (contrast, alt text, reading order)
  - Managing themed slides vs. standard content slides
  - Proper footer formatting and copyright compliance
- Reference and extend the existing `pptx` skill for core PowerPoint manipulation capabilities
- Include template inventories and layout mappings for both Dark and Light themes
- Provide validation guidance to ensure Oracle brand compliance

## Impact

- **Affected specs**: Creates new `oracle-pptx-creation` capability
- **Affected code**: 
  - New skill directory: `./skills/oracle-pptx/`
  - New skill file: `./skills/oracle-pptx/SKILL.md`
  - Reference files: 
    - Guidelines: `reference/guidelines/Oracle Powerpoint Guidelines.md` (extracted), `reference/guidelines/Oracle Powerpoint Guidelines.pptx` (source)
    - Templates: `reference/resources/templates/Oracle Powerpoint Template (Dark).pptx`, `reference/resources/templates/Oracle Powerpoint Template (Light).pptx`
    - Resources: `reference/resources/fonts/`, `reference/resources/icons/`
  - Dependencies: Leverages existing `reference/skills/pptx/` skill tooling
- **User benefit**: Enables rapid creation of Oracle-compliant presentations with confidence that all brand guidelines are followed
- **Compatibility**: Works alongside existing `pptx` skill, extending it for Oracle-specific use cases

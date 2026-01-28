# Implementation Tasks: Add Oracle PPTX Agent Skill

## 1. Create Skill Directory Structure
- [x] 1.1 Create `skills/oracle-pptx/` directory
- [x] 1.2 Create `skills/oracle-pptx/scripts/` directory
- [x] 1.3 Create `skills/oracle-pptx/ooxml/` directory structure
- [x] 1.4 Create `skills/oracle-pptx/resources/` directory with subdirectories
- [x] 1.5 Create `skills/oracle-pptx/resources/fonts/` directory
- [x] 1.6 Create `skills/oracle-pptx/resources/icons/dark-theme/` directory
- [x] 1.7 Create `skills/oracle-pptx/resources/icons/light-theme/` directory
- [x] 1.8 Create `skills/oracle-pptx/resources/templates/` directory
- [x] 1.9 Create `skills/oracle-pptx/examples/` directory with subdirectories

## 2. Copy Core Scripts and Utilities
- [x] 2.1 Copy `reference/skills/pptx/scripts/inventory.py` to `skills/oracle-pptx/scripts/`
- [x] 2.2 Copy `reference/skills/pptx/scripts/rearrange.py` to `skills/oracle-pptx/scripts/`
- [x] 2.3 Copy `reference/skills/pptx/scripts/replace.py` to `skills/oracle-pptx/scripts/`
- [x] 2.4 Copy `reference/skills/pptx/scripts/thumbnail.py` to `skills/oracle-pptx/scripts/`
- [x] 2.5 Copy `reference/skills/pptx/ooxml/scripts/` directory to `skills/oracle-pptx/ooxml/`
- [x] 2.6 Copy `reference/skills/pptx/ooxml/schemas/` directory to `skills/oracle-pptx/ooxml/`
- [x] 2.7 Verify all copied scripts have correct relative paths

## 3. Copy Oracle Resources (Self-Contained)
- [x] 3.1 Copy all files from `reference/resources/fonts/OracleSans/` to `skills/oracle-pptx/resources/fonts/OracleSans/`
- [x] 3.2 Copy all icon files from `reference/resources/icons/dark-theme/` to `skills/oracle-pptx/resources/icons/dark-theme/`
- [x] 3.3 Copy all icon files from `reference/resources/icons/light-theme/` to `skills/oracle-pptx/resources/icons/light-theme/`
- [x] 3.4 Copy `reference/resources/templates/Oracle Powerpoint Template (Dark).pptx` to `skills/oracle-pptx/resources/templates/dark-template.pptx`
- [x] 3.5 Copy `reference/resources/templates/Oracle Powerpoint Template (Light).pptx` to `skills/oracle-pptx/resources/templates/light-template.pptx`
- [x] 3.6 Copy `reference/guidelines/Oracle Powerpoint Guidelines.md` to `skills/oracle-pptx/resources/guidelines.md`
- [x] 3.7 Verify all resource files are properly copied and accessible

## 4. Review and Enhance Oracle Guidelines
- [x] 4.1 Review extracted guidelines from `reference/guidelines/Oracle Powerpoint Guidelines.md`
- [x] 4.2 Verify color specifications (theme colors and custom colors) are documented
- [x] 4.3 Verify font requirements (Oracle Sans Tab family) are documented
- [x] 4.4 Verify layout types and their use cases are documented
- [x] 4.5 Verify footer formatting requirements are documented
- [x] 4.6 Verify accessibility requirements (contrast, alt text, reading order) are documented
- [x] 4.7 Verify differences between Dark and Light templates are documented
- [x] 4.8 Verify themed slides vs. standard content slides distinctions are documented
- [x] 4.9 Enhance copied guidelines in `skills/oracle-pptx/resources/guidelines.md` with additional agent-specific guidance

## 5. Analyze Template Structure
- [x] 5.1 Generate thumbnail grids for Dark template and save to `skills/oracle-pptx/examples/dark-template-thumbnails.jpg`
- [x] 5.2 Generate thumbnail grids for Light template and save to `skills/oracle-pptx/examples/light-template-thumbnails.jpg`
- [x] 5.3 Create complete template inventory for Dark template (51 slides) using `scripts/inventory.py`
- [x] 5.4 Save Dark template inventory to `skills/oracle-pptx/resources/templates/dark-inventory.json`
- [x] 5.5 Create complete template inventory for Light template (55 slides) using `scripts/inventory.py`
- [x] 5.6 Save Light template inventory to `skills/oracle-pptx/resources/templates/light-inventory.json`
- [x] 5.7 Map slide layouts to use cases and save to `skills/oracle-pptx/resources/templates/layout-mapping.md`
- [x] 5.8 Document OCI/Database themed cover slides as the primary template option
- [x] 5.9 Extract and document speaker slide layouts (1-6 speakers, with/without photos)

## 6. Extract Theme and Color Information
- [x] 6.1 Unpack Dark template using `ooxml/scripts/unpack.py` to temporary directory
- [x] 6.2 Extract theme XML from Dark template (`ppt/theme/theme1.xml`)
- [x] 6.3 Extract color scheme from Dark template (RGB values and theme references)
- [x] 6.4 Unpack Light template using `ooxml/scripts/unpack.py` to temporary directory
- [x] 6.5 Extract theme XML from Light template
- [x] 6.6 Extract color scheme from Light template
- [x] 6.7 Document custom colors (Pine 140 and OCI/Database themed colors)
- [x] 6.8 Create color reference tables and save to `skills/oracle-pptx/resources/guidelines.md`

## 7. Write Core Skill Documentation
- [x] 7.1 Write skill overview and when to use it in SKILL.md
- [x] 7.2 Document theme selection workflow (Dark as default)
- [x] 7.3 Write layout selection decision tree
- [x] 7.4 Document Oracle brand requirements (colors, fonts, footers)
- [x] 7.5 Write accessibility compliance checklist
- [x] 7.6 Document themed slides usage guidelines
- [x] 7.7 Write content planning and mapping guidance
- [x] 7.8 Create validation checklist for Oracle compliance
- [x] 7.9 Document all paths relative to skill directory (self-contained)

## 8. Create Template Workflows
- [x] 8.1 Document end-to-end workflow for creating Oracle presentation
- [x] 8.2 Write template selection guidance (OCI/Database themed covers as default)
- [x] 8.3 Document how to use `scripts/rearrange.py` with Oracle templates
- [x] 8.4 Document how to use `scripts/inventory.py` to extract text shapes
- [x] 8.5 Document how to use `scripts/replace.py` to populate Oracle slides
- [x] 8.6 Write guidance on preserving Oracle formatting (bullets, alignment, colors)
- [x] 8.7 Document speaker slide customization (1-6 speakers, photos optional)
- [x] 8.8 Document how to use pre-generated inventories from `resources/templates/`

## 9. Create Layout Reference Materials
- [x] 9.1 Create layout guide documenting all Dark template layouts with descriptions
- [x] 9.2 Create layout guide documenting all Light template layouts with descriptions
- [x] 9.3 Map common content patterns to appropriate layouts in `resources/templates/layout-mapping.md`
- [x] 9.4 Document slide 0-indexing convention
- [x] 9.5 Create example template mappings for common presentation structures

## 10. Create Example Workflows and Outputs
- [x] 10.1 Create `examples/basic-presentation/` directory
- [x] 10.2 Generate example: Simple 5-slide presentation (Dark theme)
- [x] 10.3 Save example outline, replacement JSON, and output PPTX
- [x] 10.4 Create `examples/multi-speaker/` directory
- [x] 10.5 Generate example: Presentation with multiple speakers
- [x] 10.6 Save example workflow files
- [x] 10.7 Generate thumbnail grids of example outputs
- [x] 10.8 Document common pitfalls and solutions in examples README

## 11. Font and Accessibility Guidance
- [x] 11.1 Document Oracle Sans Tab font files in `resources/fonts/` directory
- [x] 11.2 Write font installation instructions referencing local font files
- [x] 11.3 Write font verification checklist
- [x] 11.4 Document desktop app requirement (vs. web/SharePoint)
- [x] 11.5 Write accessibility compliance verification steps
- [x] 11.6 Document contrast requirements
- [x] 11.7 Document alt text and reading order best practices

## 12. Icon and Resource Usage
- [x] 12.1 Document available icons in `resources/icons/dark-theme/` and `resources/icons/light-theme/`
- [x] 12.2 Write guidance on selecting appropriate icons for content
- [x] 12.3 Document icon naming conventions and categorization
- [x] 12.4 Provide examples of icon usage in presentations
- [x] 12.5 Document theme-appropriate icon selection (dark vs. light)

## 13. Footer and Copyright Formatting
- [x] 13.1 Document standard footer format and variations
- [x] 13.2 Write guidance on confidentiality level selection
- [x] 13.3 Document year updates (2026 current)
- [x] 13.4 Provide footer replacement examples

## 14. Validation and Quality Checks
- [x] 14.1 Write validation checklist for Oracle brand compliance
- [x] 14.2 Document visual validation workflow using `scripts/thumbnail.py`
- [x] 14.3 Create troubleshooting guide for common issues
- [x] 14.4 Document when to consult Oracle Brand team
- [x] 14.5 Write guide for validating OOXML using `ooxml/scripts/validate.py`

## 15. Integration and Testing
- [x] 15.1 Verify all Python script paths are relative to skill directory
- [x] 15.2 Test Dark template workflow end-to-end
- [x] 15.3 Test Light template workflow end-to-end
- [x] 15.4 Verify all resource file references are correct
- [x] 15.5 Test font availability from `resources/fonts/`
- [x] 15.6 Test icon access from `resources/icons/`
- [x] 15.7 Verify skill is truly self-contained (no external dependencies)
- [x] 15.8 Test on clean environment to confirm portability

## 16. Documentation Finalization
- [x] 16.1 Create README.md for `skills/oracle-pptx/` directory
- [x] 16.2 Document skill version and Oracle template version compatibility
- [x] 16.3 Add notes about resource provenance (copied from reference/)
- [x] 16.4 Create quick-start guide for common use cases
- [x] 16.5 Document directory structure and organization
- [x] 16.6 Add license information (if applicable)

## 17. Final Review
- [x] 17.1 Validate skill follows OpenSpec skill format
- [x] 17.2 Verify all Oracle guidelines are accurately represented
- [x] 17.3 Check all file paths are relative and self-contained
- [x] 17.4 Verify all resources are properly copied (no broken links)
- [x] 17.5 Proofread all documentation for clarity
- [x] 17.6 Ensure skill is comprehensive for AI agents
- [x] 17.7 Verify skill directory size is reasonable (~5-10MB)
- [x] 17.8 Confirm skill can be copied/moved without breaking

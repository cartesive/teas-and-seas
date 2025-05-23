# Jurisdiction Extensions Guide

## Overview

The Teas & Seas framework supports jurisdiction-specific variations of clauses through an extension system. This allows legal clauses to be adapted to local laws and regulations while maintaining a consistent base structure.

## Naming Convention

### Base Clauses
- Base clauses use simple identifiers (e.g., `A6`, `P5`, `L3`)
- These represent the standard, generic version of a clause

### Jurisdiction Extensions
- Extensions add jurisdiction codes after the base identifier
- Format: `[BaseID]-[CountryCode]-[RegionCode]`
- Examples:
  - `A6-CA-AB` - Age clause for Alberta, Canada
  - `A6-CA-BC` - Age clause for British Columbia, Canada
  - `P5-EU` - Privacy clause for European Union
  - `L3-US-CA` - Liability clause for California, USA

## Important Usage Notes

1. **When referencing clauses generally**, use the base identifier:
   - "Our terms include clause A6" ✓
   - "We comply with P5 requirements" ✓

2. **When referencing specific jurisdictions**, include the full extension:
   - "In British Columbia, we use A6-CA-BC" ✓
   - "California users are subject to L3-US-CA" ✓

3. **For users in a specific jurisdiction**, the base identifier suffices:
   - If you're in Canada and know your province, just refer to "A6"
   - The appropriate jurisdiction-specific version will apply

## Directory Structure

Jurisdiction extensions are organized within each clause category:

```
core/
├── age-requirements/
│   ├── AGE0.md
│   ├── A6.md
│   └── extensions/
│       ├── A6-CA-AB.md
│       ├── A6-CA-BC.md
│       └── A6-CA-ON.md
├── privacy/
│   ├── P0.md
│   └── extensions/
│       └── P0-EU.md
```

## Creating New Extensions

When local laws require variations:

1. Create an `extensions/` folder in the relevant clause category
2. Name the file using the convention: `[BaseID]-[Jurisdiction].md`
3. Include:
   - Modified clause text
   - Jurisdiction-specific notes
   - References to relevant local laws
   - Explanation of differences from base clause

## Common Jurisdiction Codes

### Countries
- `CA` - Canada
- `US` - United States
- `UK` - United Kingdom
- `EU` - European Union
- `AU` - Australia

### Canadian Provinces
- `AB` - Alberta
- `BC` - British Columbia
- `ON` - Ontario
- `QC` - Quebec
- (etc.)

### US States
- `CA` - California
- `NY` - New York
- `TX` - Texas
- (etc.)
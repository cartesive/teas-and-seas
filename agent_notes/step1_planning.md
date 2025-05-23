# Step 1: Restructure Repository Architecture

## Current Structure Analysis
- texts/ - Contains the T&C files
- assets/ - Contains logo files
- Root level files: README.md, LICENSE, TODO.txt

## Proposed New Structure
```
teas-and-seas/
├── core/                    # Core T&C clauses
│   ├── privacy/            # P0-P9
│   ├── warranty/           # W0-W9
│   ├── termination/        # T0-T9
│   ├── severability/       # S0-S9
│   ├── liability/          # L0-L9
│   ├── payment/            # PAY0-PAY9
│   ├── user-content/       # UC0-UC9
│   ├── intellectual-property/ # IP0-IP9
│   ├── disputes/           # D0-D9
│   └── general/            # G0-G9
├── jurisdictions/          # Jurisdiction-specific additions
│   ├── US/
│   ├── EU/
│   ├── CA/
│   └── UK/
├── examples/               # Complete T&C examples
│   ├── saas/
│   ├── ecommerce/
│   └── mobile-app/
├── tools/                  # Scripts and generators
│   ├── builder/
│   ├── validator/
│   └── badge-generator/
├── assets/                 # Images, logos, badges
├── agent_notes/           # Development notes
└── docs/                  # Documentation
    ├── CONTRIBUTING.md
    ├── LEGAL_COMMONS.md
    └── guides/
```

## Versioning System
- Each clause file will have a version header
- Format: `# [CODE] v[MAJOR].[MINOR].[PATCH]`
- Example: `# P2 v1.0.0`
- Changelog at bottom of each file

## Naming Conventions
- Section codes: Single letter or short acronym (P, W, T, PAY, IP)
- Files: `[CODE][LEVEL].md` (e.g., P2.md, W0.md)
- Metadata file per section: `[CODE]_meta.json` with descriptions
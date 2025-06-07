# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Teas and Seas is a Legal Commons project that standardizes Terms & Conditions clauses using a 0-9 level system. Each clause type (Privacy, Liability, etc.) has 10 levels ranging from most user-friendly (0) to most business-protective (9).

## Architecture & Structure

### Core Clause System
- **Location**: `/core/` directory
- **Organization**: Each clause type has its own subdirectory (e.g., `/core/privacy/`, `/core/liability/`)
- **Naming Convention**: Files follow pattern `[PREFIX][LEVEL].md` (e.g., `P0.md`, `L5.md`)
- **Clause Types**:
  - Privacy (P)
  - Liability (L)
  - Warranty (W)
  - Termination (T)
  - Acceptable Use (AU)
  - User Content (UC)
  - Payment (PAY)
  - Intellectual Property (IP)
  - Disputes (D)
  - Cookies (C)
  - Age Requirements (AGE/A)
  - General
  - Severability (S)

### Clause File Template
Each clause file must include:
1. Emoji/icon summary
2. Plain English explanation
3. Legal text
4. Examples of when to use

### Extension System
- **Location**: `/core/[clause-type]/extensions/`
- **Purpose**: Jurisdiction-specific variations (e.g., `/core/age-requirements/extensions/A6-CA-ON.md` for Ontario)

## Development Guidelines

### Adding New Clauses
- Maintain balance between levels (0-9)
- Use plain language in explanations
- Include practical examples
- Follow existing file format exactly

### Tone and Neutrality Requirements
- **CRITICAL**: Maintain strict neutrality when describing clause levels
- Never characterize businesses as "predatory," "exploitative," or using "traps"
- Recognize that stricter terms often reflect legitimate business needs:
  - Higher risk exposure or regulatory requirements
  - International compliance obligations
  - Fraud prevention and security needs
  - High operational costs or investment protection
- Present the natural tension between user freedoms and business controls as a balance, not a negative
- Use neutral, factual language that explains both user impact AND business rationale
- Avoid inflammatory terms like "aggressive," "unfair," or "hostile"
- Examples should reference legitimate business contexts, not assume malicious intent

### Current Priorities (from TODO.txt)
- Complete intermediate levels (1-4, 6-8) for existing clause types
- Age requirement extensions for various jurisdictions
- Build clause builder tool
- Create badge generator
- Develop validation tools

### Contributing
- See `/docs/CONTRIBUTING.md` for detailed guidelines
- Emphasis on clarity over complexity
- Community-driven approach
- Legal accuracy with accessibility

## Important Notes
- This is primarily a content/documentation project, not a software application
- No build, test, or lint commands currently exist
- Project is in early beta stage
- MIT licensed for open collaboration
# Teas & Seas Repository Structure

## Directory Layout

### `/core/`
Contains the standardized T&C clauses organized by type. Each type has levels 0-9.

- **privacy/** - Privacy policies (P0-P9)
- **warranty/** - Warranty disclaimers (W0-W9)
- **termination/** - Termination clauses (T0-T9)
- **severability/** - Severability provisions (S0-S9)
- **liability/** - Liability limitations (L0-L9)
- **payment/** - Payment terms (PAY0-PAY9)
- **user-content/** - User-generated content policies (UC0-UC9)
- **intellectual-property/** - IP ownership and licensing (IP0-IP9)
- **disputes/** - Dispute resolution (D0-D9)
- **general/** - General provisions (G0-G9)

### `/jurisdictions/`
Jurisdiction-specific modifications and additions to core clauses.

### `/examples/`
Complete T&C documents showing how to combine clauses for different use cases.

### `/tools/`
Utilities for working with T&S clauses:
- **builder/** - Generate complete T&C documents
- **validator/** - Check clause compatibility
- **badge-generator/** - Create visual badges for your T&C levels

### `/docs/`
Project documentation and guides.

## File Naming Convention

- Core clauses: `[CODE][LEVEL].md` (e.g., `P2.md`, `W0.md`)
- Metadata: `[CODE]_meta.json` per section
- Versions tracked in file headers
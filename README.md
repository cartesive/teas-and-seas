![](assets/logo.png)

# Teas and Seas (Beta)

A set of Terms and Conditions (T's and C's) that are easy to use, and fair for your customers.

## What is it, and why?

**Terms and Conditions are a pain, and nobody reads them anyway.**

It takes too long to read terms and conditions, and they are not well understood. This collection of universal, pre-written T's&C's are designed to be easy to assemble and easy to consume.

Developers know their software licenses by shorthand acronyms, like MIT, GPL, BSD, etc. These are generally well understood because they are consistent across projects and their intent is known even without re-reading the text.

This project aims to do the same for Terms and Conditions.

The project will be a success if a large set of people come to know that, say, "P2" level privacy refers to a site, service or software that collects data incidentally -- and may use cookies -- but does not try to identify you individually or combine data for re-use or sale to third parties.

## The Level System

Every clause type uses a 0-9 scale:
- **Level 0**: Maximum user freedom, no restrictions, most protective of users
- **Levels 1-3**: Light touch, user-friendly
- **Levels 4-6**: Balanced approach, industry standard
- **Levels 7-9**: Business-protective, more restrictive

For example:
- **P0**: We don't collect any data whatsoever
- **P5**: We collect data needed for the service, use analytics, but don't sell personal data
- **P9**: We collect everything and share with partners extensively

## How to use

1. **Pick your levels**: Choose what level (0-9) you want for each clause type
2. **Combine clauses**: Use individual clauses like [P2](core/privacy/P2.md) + [L5](core/liability/L5.md) + [W0](core/warranty/W0.md)
3. **Display clearly**: Show your T&C levels prominently (e.g., "P2•L5•W0•T1")

Each clause includes:
- 📌 **Summary** - One-line description
- 👤 **What This Means For You** - Plain English explanation
- 📜 **Legal Text** - Formal language for legal validity
- 🔍 **Examples** - Real-world use cases

## Available Clause Types

| Code | Type | Description | Example |
|------|------|-------------|---------|
| **P** | [Privacy](core/privacy/) | Data collection & sharing | [P0](core/privacy/P0.md), [P5](core/privacy/P5.md) |
| **L** | [Liability](core/liability/) | Limitation of damages | [L0](core/liability/L0.md), [L5](core/liability/L5.md) |
| **W** | [Warranty](core/warranty/) | Product guarantees | [W0](core/warranty/W0-Warrantee.md) |
| **T** | [Termination](core/termination/) | Account/service ending | [T0](core/termination/T0-Termintation.md) |
| **S** | [Severability](core/severability/) | Invalid clause handling | [S0](core/severability/S0-Severability.md) |
| **AGE** | [Age Requirements](core/age-requirements/) | Age restrictions | [AGE0](core/age-requirements/AGE0.md) |

More types coming soon: Payment (PAY), User Content (UC), Intellectual Property (IP), Disputes (D), and [many others](STRUCTURE.md).

## The Vision

Imagine a world where:
- You see "P2•L5•W0" on a website and instantly know what you're agreeing to
- Small businesses can have proper legal terms without expensive lawyers
- Users actually understand what they're signing up for
- Terms compete on fairness, not obscurity

## Contributing

This is a community project - a "Legal Commons" for the benefit of all. We need:
- 📝 More clause drafts at different levels
- ⚖️ Legal review from lawyers who believe in clarity
- 🌍 Jurisdiction-specific adaptations
- 💡 Feedback on what works and what doesn't

See our [contribution guidelines](docs/CONTRIBUTING.md) for detailed information on how to help.

## The Legal Commons Movement

Teas & Seas is part of a larger movement to make legal terms accessible to everyone. Just as Open Source transformed software development, we believe Legal Commons can transform how legal documents are created and understood.

Learn more about [the Legal Commons philosophy](docs/LEGAL_COMMONS.md) and why lawyers, developers, and users should care about standardized, clear legal terms.

## Quick Start Example

A typical SaaS startup might use:
- **P2** - Aggregate data collection, no selling
- **L5** - Liability limited to 12 months of fees
- **W1** - Basic functionality warranty
- **T1** - Either party can terminate with 30 days notice

Result: `P2•L5•W1•T1` - A balanced, fair set of terms that users can understand at a glance.
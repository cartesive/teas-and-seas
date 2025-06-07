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

### ✅ Complete (All levels 0-9 available)

| Code | Type | Description | Example |
|------|------|-------------|---------|
| **P** | [Privacy](core/privacy/) | Data collection & sharing | [P0](core/privacy/P0.md), [P5](core/privacy/P5.md), [P9](core/privacy/P9.md) |
| **L** | [Liability](core/liability/) | Limitation of damages | [L0](core/liability/L0.md), [L5](core/liability/L5.md), [L9](core/liability/L9.md) |
| **W** | [Warranty](core/warranty/) | Product guarantees | [W0](core/warranty/W0.md), [W5](core/warranty/W5.md), [W9](core/warranty/W9.md) |
| **T** | [Termination](core/termination/) | Account/service ending | [T0](core/termination/T0.md), [T5](core/termination/T5.md), [T9](core/termination/T9.md) |
| **PAY** | [Payment](core/payment/) | Billing, refunds, pricing | [PAY0](core/payment/PAY0.md), [PAY5](core/payment/PAY5.md), [PAY9](core/payment/PAY9.md) |
| **UC** | [User Content](core/user-content/) | Content ownership & rights | [UC0](core/user-content/UC0.md), [UC5](core/user-content/UC5.md), [UC9](core/user-content/UC9.md) |
| **AU** | [Acceptable Use](core/acceptable-use/) | Usage restrictions | [AU0](core/acceptable-use/AU0.md), [AU5](core/acceptable-use/AU5.md), [AU9](core/acceptable-use/AU9.md) |
| **D** | [Disputes](core/disputes/) | Conflict resolution | [D0](core/disputes/D0.md), [D5](core/disputes/D5.md), [D9](core/disputes/D9.md) |
| **C** | [Cookies](core/cookies/) | Cookie & tracking policies | [C0](core/cookies/C0.md), [C5](core/cookies/C5.md), [C9](core/cookies/C9.md) |
| **IP** | [Intellectual Property](core/intellectual-property/) | IP ownership & licensing | [IP0](core/intellectual-property/IP0.md), [IP5](core/intellectual-property/IP5.md), [IP9](core/intellectual-property/IP9.md) |

### 🚧 In Progress

| Code | Type | Description | Status |
|------|------|-------------|--------|
| **S** | [Severability](core/severability/) | Invalid clause handling | Level 0 only |
| **AGE** | [Age Requirements](core/age-requirements/) | Age restrictions | Levels 0, 6 only |
| **General** | [General](core/general/) | Misc. terms | Being restructured |

More types coming soon. See our [complete structure plan](STRUCTURE.md).

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

## Detailed Example: Building Your T&C

Let's say you're launching a photo sharing app. Here's how you'd build your Terms & Conditions:

### Step 1: Identify Your Business Model
You're a freemium photo sharing service with optional paid features. You want to be user-friendly but need some protections.

### Step 2: Choose Your Levels

**Privacy (P)** - You need analytics but respect user privacy:
- ❌ P0 (no data collection) - Can't improve the service
- ❌ P1 (minimal data) - Need more for features
- ✅ **P2** - Perfect! Analytics without individual tracking
- ❌ P5+ - Too invasive for your values

**Liability (L)** - Standard protections without being extreme:
- ❌ L0-L2 - Too much liability exposure
- ✅ **L4** - Reasonable limits, fair to both sides
- ❌ L7+ - Too aggressive, might scare users

**Warranty (W)** - You're confident but realistic:
- ❌ W0 - Can't guarantee perfection
- ✅ **W2** - Good warranty with reasonable limits
- ❌ W5+ - Too many disclaimers

**Payment (PAY)** - Fair billing for premium users:
- ✅ **PAY2** - Clear pricing, pro-rated refunds
- ❌ PAY5+ - Too restrictive on refunds

**User Content (UC)** - Users own their photos:
- ✅ **UC1** - Users keep ownership, you get service license
- ❌ UC5+ - You don't need broad content rights

**Termination (T)** - Easy come, easy go:
- ✅ **T2** - Users can leave anytime, you need cause
- ❌ T5+ - Too restrictive on user freedom

**Acceptable Use (AU)** - Prevent abuse, allow creativity:
- ✅ **AU3** - Clear rules without micromanaging
- ❌ AU0 - Need some content guidelines
- ❌ AU7+ - Too restrictive for creative platform

### Step 3: Your T&C Badge
**`P2•L4•W2•PAY2•UC1•T2•AU3`**

### Step 4: What This Means for Users
When users see your badge, they instantly know:
- 📊 Their data is used for analytics but not sold
- ⚖️ Liability is limited but fair
- ✅ The service comes with real guarantees
- 💳 Billing is transparent with refunds
- 📸 They own their photos completely
- 🚪 They can leave anytime easily
- 📝 Clear, reasonable usage rules

### Compare with Competitors
- **Big Social Network**: `P8•L9•W8•PAY7•UC6•T8•AU8` (Very restrictive)
- **Open Source Alternative**: `P0•L0•W9•PAY0•UC0•T0•AU1` (Maximum freedom)
- **Your Balanced Approach**: `P2•L4•W2•PAY2•UC1•T2•AU3` (Fair middle ground)

Users can now make informed choices at a glance!
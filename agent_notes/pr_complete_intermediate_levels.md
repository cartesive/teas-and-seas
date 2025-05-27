# Pull Request: Complete intermediate clause levels for core sections

## Branch Name
`complete-intermediate-clause-levels`

## PR Title
Complete intermediate clause levels for core sections

## PR Description

### Summary
- Completed intermediate levels (1-4, 6-8) for three core clause types
- Removed duplicate/incorrect files from termination and warranty sections
- Brings total completed sections to 4 (Privacy already complete)

### Changes Made

#### 1. Acceptable Use (AU) - Added 7 new levels
- AU1: Minimal restrictions - only illegal content and severe harm
- AU2: Light restrictions - illegal content, direct harm, severe disruption
- AU3: Moderate restrictions - standard online behavior rules
- AU4: Clear restrictions - includes content standards
- AU6: Strict rules with broad categories
- AU7: Very strict with vague standards
- AU8: Extreme restrictions, arbitrary enforcement

#### 2. Cookies (C) - Added 7 new levels
- C1: Essential cookies only, auto-expire quickly
- C2: Essential plus preferences, no tracking
- C3: Functional plus anonymous analytics
- C4: Standard cookies with consent banner
- C6: Extensive cookies, implied consent
- C7: Aggressive tracking, cookie walls
- C8: Pervasive tracking, deceptive practices

#### 3. Disputes (D) - Added 7 new levels
- D1: Friendly resolution, full rights preserved
- D2: Negotiation first, user choice of venue
- D3: Structured escalation, arbitration optional
- D4: Arbitration preferred with opt-out
- D6: Mandatory arbitration, company-favorable
- D7: Restrictive arbitration, loser pays
- D8: Extreme restrictions, foreign arbitration

#### 4. Cleanup
- Removed `T0-Termintation.md` (duplicate of T0.md)
- Removed `W0-Warrantee.md` (duplicate of W0.md)

### Test Plan
- [x] All new clause files follow the established template format
- [x] Language progression from 0-9 is logical and consistent
- [x] Each level provides clear differentiation from adjacent levels
- [x] Summary, user explanation, legal text, and examples are included
- [x] Version history added to all new files

### Next Steps
This PR advances the project significantly toward completing Step 2 of the implementation plan. After this merge, the following sections still need intermediate levels:
- Intellectual Property (IP)
- Payment (PAY)
- Termination (T)
- User Content (UC)
- Warranty (W)
- Liability (L) - needs only L7 and L8

### Files Changed
- 21 new clause files added
- 2 duplicate files removed
- Total: 23 files changed, 441 insertions(+), 6 deletions(-)

---

To create the PR:
1. Push the branch: `git push -u origin complete-intermediate-clause-levels`
2. Go to https://github.com/cartesive/teas-and-seas
3. Click "Compare & pull request" for the new branch
4. Copy the above description into the PR
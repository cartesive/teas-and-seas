# Adding Extensions to Terms and Conditions

Extensions allow you to customize clauses for specific jurisdictions while maintaining the core clause structure. This guide explains how to add extensions, with specific examples from Canadian age requirement variations.

## When to Use Extensions

Extensions are needed when:
- Local laws require different terms than the base clause
- Regional regulations impose specific requirements
- Cultural or business practices vary by jurisdiction
- Age restrictions differ based on local laws (e.g., drinking age, age of majority)

## Extension Structure

### Directory Organization
Extensions are placed in an `extensions/` subdirectory under the relevant clause category:
```
core/
├── age-requirements/
│   ├── A6.md                    # Base clause
│   └── extensions/
│       ├── A6-CA-AB.md          # Alberta, Canada
│       ├── A6-CA-BC.md          # British Columbia, Canada
│       └── A6-CA-ON.md          # Ontario, Canada
```

### Naming Convention
Extension files follow this pattern: `{CLAUSE}-{COUNTRY}-{REGION}.md`
- `{CLAUSE}`: The base clause identifier (e.g., A6)
- `{COUNTRY}`: ISO country code (e.g., CA for Canada)
- `{REGION}`: Region/province/state code (e.g., BC for British Columbia)

## Creating an Extension

### 1. File Structure Template
```markdown
# {CLAUSE}-{COUNTRY}-{REGION} - {Title} ({Full Jurisdiction Name})

## Clause Text

[Modified clause text specific to this jurisdiction]

## Jurisdiction-Specific Notes

[Explain why this variation exists and key differences]
- Key legal requirement 1
- Key legal requirement 2
- Reference to local laws/regulations

[Additional context about the jurisdiction's requirements]
```

### 2. Content Guidelines
- Keep the same structure as the base clause
- Only modify what's legally necessary
- Clearly explain why the variation exists
- Reference specific laws or regulations when applicable
- Maintain consistency with the base clause's intent

## Example: Canadian Age Requirement Variations

### Understanding Canadian Jurisdiction Differences

Canada's provinces have different age requirements based on:
1. **Age of Majority**: When a person becomes a legal adult
2. **Legal Drinking Age**: Minimum age to purchase/consume alcohol
3. **Provincial Regulations**: Each province sets its own rules

### British Columbia Specific Requirements

British Columbia requires age 19 for alcohol-related services because:
- **Legal Drinking Age**: 19 years (higher than some provinces)
- **Age of Majority**: 19 years (matches drinking age)
- **Consistency**: Both legal adult status and alcohol access align at 19

Example extension (A6-CA-BC.md):
```markdown
# A6-CA-BC - Must Be Over 19 (British Columbia, Canada)

## Clause Text

Users must be at least nineteen (19) years of age to access or use the Service. By accessing or using the Service, you represent and warrant that you are at least nineteen (19) years old.

## Jurisdiction-Specific Notes

In British Columbia, Canada:
- Legal drinking age: 19 years
- Age of majority: 19 years

This variation adjusts the age requirement to comply with British Columbia's provincial regulations, particularly for services involving alcohol.
```

### Why Jurisdictions Differ

#### Alberta vs. British Columbia
- **Alberta**: 18 years (both drinking age and age of majority)
- **British Columbia**: 19 years (both drinking age and age of majority)
- **Impact**: Services must adapt age requirements based on operating province

#### Key Considerations
1. **Service Type**: Alcohol-related services must follow drinking age laws
2. **User Location**: Consider where users access the service
3. **Business Registration**: Province of incorporation may affect requirements
4. **Multi-Provincial Operations**: May need to apply highest age requirement

## Best Practices

1. **Research First**: Verify current laws before creating extensions
2. **Document Sources**: Include references to specific regulations
3. **Keep It Simple**: Only add what's legally necessary
4. **Maintain Consistency**: Follow the base clause structure
5. **Update Regularly**: Laws change; review extensions periodically

## Adding Your Extension

1. Create the extension file in the appropriate `extensions/` directory
2. Follow the naming convention exactly
3. Use the template structure
4. Document why the variation exists
5. Test with the validator tool (when available)
6. Submit via pull request with clear description

## Common Extension Types

- **Age Requirements**: Varying age of majority/drinking age
- **Privacy Laws**: GDPR (EU), PIPEDA (Canada), CCPA (California)
- **Consumer Protection**: Cooling-off periods, warranty requirements
- **Language Requirements**: Quebec French language laws
- **Dispute Resolution**: Arbitration restrictions in some jurisdictions

## Questions?

When creating extensions, consider:
- Is this variation legally required or just recommended?
- Does it conflict with the base clause's intent?
- Will it affect other clauses in the terms?
- Is the explanation clear for non-lawyers?

For complex jurisdictional requirements, consider consulting with local legal counsel.
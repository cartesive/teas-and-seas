# Tests

This directory contains tests for the Terms & Conditions builder functionality.

## Running Tests

### Browser Tests

Open `test-builder.html` in your browser to run the test suite. The tests will:

- Verify all clause data loads correctly
- Test document generation functionality
- Validate markdown parsing
- Check integration between components

### Live Site Tests

To test against the live GitHub Pages site, open `test-live-site.html` which fetches the actual deployed code and tests it.

## Test Structure

- **Clause Data Tests**: Verify that all required clause types exist and have proper structure
- **Document Generation Tests**: Test the core `fetchClause` functionality 
- **Integration Tests**: End-to-end testing of document creation and markdown rendering

## Adding Tests

To add new tests, use the `TestRunner` class:

```javascript
const runner = new TestRunner();

runner.test('Test name', async () => {
    // Test code here
    assert(condition, 'error message');
    assertEquals(actual, expected, 'error message');
    assertContains(haystack, needle, 'error message');
});

const results = await runner.run();
```

## Continuous Testing

These tests should be run:
- Before any deployment
- After adding new clauses
- When modifying the builder logic
- After updating dependencies (like marked.js)
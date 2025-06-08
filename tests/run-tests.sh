#!/bin/bash

# T&C Builder Test Runner
echo "🧪 Running Terms & Conditions Builder Tests"
echo "=========================================="

# Check if we're in the right directory
if [ ! -f "test-builder.html" ]; then
    echo "❌ Error: Please run this script from the /tests directory"
    exit 1
fi

echo ""
echo "📂 Available Tests:"
echo "  1. test-builder.html    - Unit tests for builder components"
echo "  2. test-live-site.html  - Integration tests against live GitHub Pages"
echo ""

# Function to open tests in browser
open_test() {
    local test_file="$1"
    local description="$2"
    
    echo "🌐 Opening $description..."
    
    # Try different ways to open browser depending on OS
    if command -v xdg-open > /dev/null; then
        xdg-open "$test_file"
    elif command -v open > /dev/null; then
        open "$test_file"
    elif command -v start > /dev/null; then
        start "$test_file"
    else
        echo "ℹ️  Please open $test_file in your browser"
    fi
}

# Run tests based on argument
case "${1:-all}" in
    "unit")
        open_test "test-builder.html" "unit tests"
        ;;
    "live")
        open_test "test-live-site.html" "live site tests"
        ;;
    "all"|"")
        echo "🚀 Running all tests..."
        open_test "test-builder.html" "unit tests"
        sleep 2
        open_test "test-live-site.html" "live site tests"
        ;;
    "help"|"-h"|"--help")
        echo "Usage: $0 [unit|live|all|help]"
        echo ""
        echo "Options:"
        echo "  unit  - Run only unit tests"
        echo "  live  - Run only live site tests"  
        echo "  all   - Run all tests (default)"
        echo "  help  - Show this help message"
        ;;
    *)
        echo "❌ Unknown option: $1"
        echo "Run '$0 help' for usage information"
        exit 1
        ;;
esac

echo ""
echo "✅ Test runner complete"
echo "📊 Check browser windows for test results"
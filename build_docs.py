#!/usr/bin/env python3
"""
Build script to compile all T&C clause files into JSON format
for the interactive T&C builder.
"""

import os
import json
from pathlib import Path

def build_clause_data():
    """Build JSON data structure from all clause markdown files."""
    
    # Clause type mapping (folder name -> prefix)
    clause_mapping = {
        'privacy': 'P',
        'liability': 'L', 
        'warranty': 'W',
        'termination': 'T',
        'acceptable-use': 'AU',
        'user-content': 'UC',
        'payment': 'PAY',
        'intellectual-property': 'IP',
        'disputes': 'D',
        'cookies': 'C',
        'age-requirements': 'AGE',
        'severability': 'S'
    }
    
    core_dir = Path('core')
    data = {}
    
    for clause_type, prefix in clause_mapping.items():
        clause_dir = core_dir / clause_type
        if not clause_dir.exists():
            print(f"Warning: {clause_dir} does not exist")
            continue
            
        data[clause_type] = {}
        
        # Read levels 0-9
        for level in range(10):
            file_path = clause_dir / f"{prefix}{level}.md"
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                    data[clause_type][str(level)] = content
                    print(f"✅ Loaded {clause_type} level {level}")
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")
            else:
                print(f"⚠️  Missing: {file_path}")
    
    return data

def update_html_with_data(data):
    """Update index.html with embedded JSON data."""
    
    html_path = Path('docs/index.html')
    if not html_path.exists():
        print(f"❌ {html_path} does not exist")
        return
    
    # Read current HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create JavaScript data declaration
    js_data = f"        const CLAUSE_DATA = {json.dumps(data, indent=12)};"
    
    # Find and replace the fetchClause function and related code
    start_marker = "        let documentCache = {};"
    end_marker = "        function updateBadge() {"
    
    start_idx = html_content.find(start_marker)
    end_idx = html_content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("❌ Could not find markers in HTML file")
        return
    
    # Replace the entire fetchClause section with embedded data
    new_js_section = f"""        let documentCache = {{}};
        let currentDocument = '';

{js_data}

        async function fetchClause(clauseType, level) {{
            const key = `${{clauseType}}-${{level}}`;
            if (documentCache[key]) {{
                return documentCache[key];
            }}

            try {{
                if (CLAUSE_DATA[clauseType] && CLAUSE_DATA[clauseType][level]) {{
                    const content = CLAUSE_DATA[clauseType][level];
                    console.log(`✅ Loaded ${{clauseType}} level ${{level}} from embedded data`);
                    documentCache[key] = content;
                    return content;
                }} else {{
                    throw new Error(`No data found for ${{clauseType}} level ${{level}}`);
                }}
            }} catch (error) {{
                console.error(`Error loading ${{clauseType}} level ${{level}}:`, error);
                return `[Error: Could not load ${{clauseType.replace('-', ' ')}} clause level ${{level}}]`;
            }}
        }}

        """
    
    # Reconstruct HTML
    new_html = (
        html_content[:start_idx] + 
        new_js_section + 
        html_content[end_idx:]
    )
    
    # Write updated HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"✅ Updated {html_path} with embedded clause data")

def main():
    """Main build process."""
    print("🔨 Building T&C clause data...")
    
    # Build the data structure
    data = build_clause_data()
    
    # Count total clauses
    total_clauses = sum(len(levels) for levels in data.values())
    print(f"\n📊 Loaded {total_clauses} total clauses across {len(data)} clause types")
    
    # Update HTML file
    update_html_with_data(data)
    
    print("\n🎉 Build complete! The T&C builder now has all clause data embedded.")

if __name__ == "__main__":
    main()
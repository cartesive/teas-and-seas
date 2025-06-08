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
        'severability': 'S',
        'general': 'G'
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

def write_data_json(data):
    """Write clause data to docs/data.json file."""
    
    json_path = Path('docs/data.json')
    
    # Write the data as pretty-printed JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Written clause data to {json_path}")

def main():
    """Main build process."""
    print("🔨 Building T&C clause data...")
    
    # Build the data structure
    data = build_clause_data()
    
    # Count total clauses
    total_clauses = sum(len(levels) for levels in data.values())
    print(f"\n📊 Loaded {total_clauses} total clauses across {len(data)} clause types")
    
    # Write data to JSON file
    write_data_json(data)
    
    print("\n🎉 Build complete! Clause data written to docs/data.json")

if __name__ == "__main__":
    main()
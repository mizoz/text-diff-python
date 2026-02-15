#!/usr/bin/env python3
"""Simple text diff tool."""

import sys
from pathlib import Path


def diff_lines(a: list, b: list) -> list:
    """Compare two lists of lines."""
    result = []
    max_len = max(len(a), len(b))
    
    for i in range(max_len):
        line_a = a[i] if i < len(a) else None
        line_b = b[i] if i < len(b) else None
        
        if line_a == line_b:
            result.append(f"  {line_a or ''}")
        elif line_a is None:
            result.append(f"+ {line_b}")
        elif line_b is None:
            result.append(f"- {line_a}")
        else:
            result.append(f"- {line_a}")
            result.append(f"+ {line_b}")
    
    return result


def main():
    if len(sys.argv) < 3:
        print("Usage: text_diff.py <file1> <file2>")
        sys.exit(1)
    
    file1 = Path(sys.argv[1])
    file2 = Path(sys.argv[2])
    
    if not file1.exists():
        print(f"Error: {file1} not found")
        sys.exit(1)
    
    if not file2.exists():
        print(f"Error: {file2} not found")
        sys.exit(1)
    
    lines1 = file1.read_text().splitlines()
    lines2 = file2.read_text().splitlines()
    
    diff = diff_lines(lines1, lines2)
    
    for line in diff:
        print(line)
    
    print(f"\n({len(lines1)} vs {len(lines2)} lines)")


if __name__ == "__main__":
    main()

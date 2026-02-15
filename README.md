# Text Diff Python

A Python library and CLI tool to compare and show differences between text files.

## Features

- Side-by-side diff view
- Unified diff format
- Word-level diff highlighting
- Ignore whitespace option
- Color output in terminal
- Compare directories
- Python API for integration

## Installation

```bash
pip install text-diff-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/text-diff-python.git
cd text-diff-python
pip install -e .
```

## Usage

### Command Line

```bash
# Compare two files
text-diff file1.txt file2.txt

# Unified diff format
text-diff --unified file1.txt file2.txt

# Word-level diff
text-diff --word-diff file1.txt file2.txt

# Ignore whitespace
text-diff --ignore-whitespace file1.txt file2.txt

# Compare directories
text-diff ./dir1 ./dir2
```

### Python API

```python
from text_diff import TextDiff

diff = TextDiff()

# Compare two strings
result = diff.compare("Hello World", "Hello Universe")
print(result)

# Compare files
result = diff.compare_files("file1.txt", "file2.txt")
print(result)
```

## Options

- `-u, --unified` - Show unified diff format
- `-w, --word-diff` - Show word-level differences
- `-i, --ignore-whitespace` - Ignore whitespace changes
- `-c, --color` - Enable colored output

## License

MIT License

## Author

mizoz

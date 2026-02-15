# Text Diff Python

[![PyPI Version](https://img.shields.io/pypi/v/text-diff-python?style=flat-square)](https://pypi.org/project/text-diff-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/text-diff-python?style=flat-square)](https://pypi.org/project/text-diff-python/)
[![License](https://img.shields.io/pypi/l/text-diff-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/text-diff-python?style=flat-square)](https://pypi.org/project/text-diff-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/text-diff-python?style=flat-square)](https://github.com/mizoz/text-diff-python)

> A Python CLI tool for comparing and showing differences between text files.

## Features

- Compare two text files
- Side-by-side diff view
- Unified diff format
- Word-level diff
- Ignore whitespace option
- Python API for integration

## Installation

### From PyPI

```bash
pip install text-diff-python
```

### From Source

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
text-diff --words file1.txt file2.txt
```

### Python API

```python
from text_diff import TextDiffer

differ = TextDiffer()

# Compare texts
diff = differ.compare("Hello World", "Hello Universe")
print(diff)
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-u, --unified` | Unified diff format |
| `-w, --words` | Word-level diff |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!

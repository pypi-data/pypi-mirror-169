# Description

Basic tools to read, format, filter and display hex values

# Installation

`pip install hexlib`

# Usage

- The class `HexTwin` is the hexadecimal representation of a file
- The class `Hexdump` format and prints:
  1. `HexTwin` instances
  2. Lists of hex values
     -  ["AA", "BB", "CC", "DD", "EE", "00"]


# Example

```python
from hexlib.HexTwin import HexTwin
from hexlib.Hexdump import Hexdump

# 1.) HexTwin instance
twin = HexTwin("path/to/file/test.txt")
dump = Hexdump()

# Activates filtering for zero rows
dump.filter(filterZeroRows=True) 
twin.printTwin(t)

# Activates filtering for non-ascii rows (Includes zero rows)
dump.filter(filterNonAsciiRows=True) 
twin.printTwin(t)

# 2.) List of hex values
a = ["AA", "BB", "CC", "DD", "EE"]
b = Hexdump()
b.printHexValues(a)

```

# License

MIT
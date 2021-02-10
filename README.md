# DRF Generator

The DRF generator defines a syntax for expressing many [DRF](https://cdcvs.fnal.gov/redmine/projects/drf/wiki) strings in a single string.

The syntax is inspired by Unix (bash) glob syntax, but not an exact match as glob is meant to file paths.

## Features

### List

Curly brackets surrounding comma separated values define a list of strings to be included with each generated DRF string.

For example:

```bash
python drf_generator.py "{I,R}:VT001"
```

Generates:

```text
I:VT001
R:VT001
```

### Range

Curly brackets surrounding two values separated by a double dot (`..`) define a range of integers to be included with each generated DRF string.

For example:

```bash
python drf_generator.py "I:VT{000..002}"
```

Generates:

```text
I:VT000
I:VT001
I:VT002
```

## TODOs

- Allow square bracket lists
- Define a special, non-glob, range step

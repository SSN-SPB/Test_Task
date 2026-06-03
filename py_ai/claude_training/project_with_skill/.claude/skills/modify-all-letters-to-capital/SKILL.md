---
name: modify-all-letters-to-capital
description: Converts all alphabetic characters in the provided text to uppercase while preserving punctuation, whitespace, and numbers. Use when the user asks to capitalize text, wants UPPERCASE formatting, or requests text normalization to uppercase.
---

# Modify All Letters to Capital

Convert all alphabetic characters in the provided text to uppercase while preserving punctuation, whitespace, and numbers.

## When to Use

- User asks to capitalize text.
- User asks for UPPERCASE formatting.
- User requests text normalization to uppercase.

## Input

Any text string.

## Output

The same text with all letters converted to uppercase. Punctuation, whitespace, and numbers are left unchanged.

## How to Apply

Take the input text and uppercase every alphabetic character. Return only the transformed text, with no extra commentary.

## Examples

Input:
```
hello world 123
```

Output:
```
HELLO WORLD 123
```

Input:
```
Claude CLI is awesome!
```

Output:
```
CLAUDE CLI IS AWESOME!
```

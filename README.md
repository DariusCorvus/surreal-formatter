# SurrealQL Formatter

This repository has the purpose to become a beautiful SurrealQL Formatter, shaped like a beautiful surql ⏣, always consistent like π.

## Why?

I never got satisfied by formatters for SQL, and never thought about writing my own to meet my wishes.
- SurrealDB blowed a new wind into my direction and inspired me to give the community something back, for the gift of this stunning database.
- I don't like it to think about formatting, i want to save my file and see the magic of a formatter coming to live.
- Also the results for `INFO FOR TABLE <table>` are strings without formatting, to give my eyes a chill, a good formatter is needed.

## Installation

> **Warning**
> Never install from a source you don't trust.

```bash
git clone https://www.github.com/DariusCorvus/surreal-formatter.git
cd surreal-formatter
pip install .
```

## Usage

To use the formatter, you can pipe the content you want to beautify into the programm `surreal-formatter` or pass the file name as an argument.

To get a overview over the programm, just run:
```bash
$ surreal-formatter --help
```
```
Usage: surreal-formatter [OPTIONS] [INPUT] [OUTPUT]

Options:
  --tabsize INTEGER
  --help             Show this message and exit.
```

The default in and output of `surreal-formatter` are `stdin` and `stdout` to give us the pipe functionality
```bash
$ echo 'SELECT * FROM user;' | 
surreal-formatter --tabsize 2
```
```sql
SELECT
     *
  FROM user
;
```
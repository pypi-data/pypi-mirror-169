# ovtable

[![build](https://github.com/piperliu/ovtable/workflows/build/badge.svg)](https://github.com/piperliu/ovtable/actions?query=workflow%3Abuild)  [![coverage](https://img.shields.io/codecov/c/github/piperliu/ovtable)](https://codecov.io/gh/piperliu/ovtable)  [![pypi](https://img.shields.io/pypi/v/ovtable.svg)](https://pypi.org/project/ovtable/)  [![support-version](https://img.shields.io/pypi/pyversions/ovtable)](https://img.shields.io/pypi/pyversions/ovtable)  [![license](https://img.shields.io/github/license/piperliu/ovtable)](https://github.com/piperliu/ovtable/blob/main/LICENSE)  [![commit](https://img.shields.io/github/last-commit/piperliu/ovtable)](https://github.com/piperliu/ovtable/commits/main)

💻 based on curses, ovtable is a table displayed in the terminal with Python API

## Installation

Install via pip:

```
python -m pip install -U prettytable
```

Or install from source:

```bash
git clone git@github.com:PiperLiu/ovtable.git
cd ovtable
make refresh
```

Get the best experience with **Monospaced Fonts!** e.g. Let's get [Fira Code](https://github.com/tonsky/FiraCode)!

## Tutorial on how to use ovtable

```
>>> import ovtable

>>> ot = ovtable.OvTable(60, 30, True)
>>> # 60 is width, 30 is height
>>> # True means you want to use __str__
>>> # False means you want to render it (use ot.render())

>>> ot.add_row(1)
>>> ot[0, 0] = "Hello, OvTable"
>>> print(ot)
┌──────────────────────────────────────────────────────────┐
│                      Hello, OvTable                      │
└──────────────────────────────────────────────────────────┘

>>> ot.add_row(2)
>>> ot[1, 0] = [("I'm red", "r"), (" ok, I'm blue", "b")]
>>> ot[1, 1] = "I am in row 2, col 2"
>>> print(ot)
┌──────────────────────────────────────────────────────────┐
│                      Hello, OvTable                      │
├────────────────────────────┬─────────────────────────────┤
│    I'm red ok, I'm blue    │    I am in row 2, col 2     │
└────────────────────────────┴─────────────────────────────┘
```

With `ot[x, y] = value` or `ot[x, y] = [(s1, color1), (s2, color2), ...]`, we can render some interesting things! See [./examples/](./examples/).

```python examples/walker.py``` as below:

![](./assets/images/walker.gif)

## Why not PrettyTable?

Why created ovtable when we already have [PrettyTable](https://github.com/jazzband/prettytable)?

Well, mainly two reasons:
- First, PrettyTable does not support different number of rows per line.
- Second, our APIs is more suitable for rendering tables dynamically.

## Contribution

We welcome all forms of contributions (including but not limited to issues and pull requests).

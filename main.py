#!/usr/bin/env python3
"""make.fun bounty entry: The Best Meal You Ever Had.

The best meal you ever had, in one line. No restaurant name,
no recipe — just the taste, and the person across the table.
"""

MEAL = "The best meal I ever had was instant noodles at 2 a.m., eaten standing up, with the person I loved laughing at how happy I was — and the noodles were, honestly, perfect."


def meal():
    """Return the best meal you ever had, in one line."""
    return MEAL


def main():
    print(meal())


if __name__ == "__main__":
    main()

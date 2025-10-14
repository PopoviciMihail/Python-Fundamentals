from typing import List

def findWord(rules: List[str]) -> str:
    """
    Găsește cuvântul complet din regulile de precedență.

    Args:
        rules (List[str]): Reguli de forma "A>B", unde A precede pe B.

    Returns:
        str: Cuvântul complet format.
    """

    next_letter = {}
    prev_letter = {}

    for rule in rules:
        a, b = rule.split(">")
        next_letter[a] = b
        prev_letter[b] = a

    start = ""
    for letter in next_letter:
        if letter not in prev_letter:
            start = letter
            break

    word = start
    while start in next_letter:
        start = next_letter[start]
        word += start

    return word

if __name__ == "__main__":
    print(findWord(["P>E", "E>R", "R>U"]))                       # PERU
    print(findWord(["I>N", "A>I", "P>A", "S>P"]))                # SPAIN
    print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))  # HUNGARY
    print(findWord(["I>F", "W>I", "S>W", "F>T"]))                # SWIFT
    print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))  # PORTUGAL
    print(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]))  # SWITZERLAND

from typing import List

def doubles(s: str) -> int:
    """
    Returneaza lungimea celei mai lungi secvente consecutive de duble.

    Args:
        s (str): Sirul de aruncari de zaruri, in format "X-Y,X-Y,...".

    Returns:
        int: Lungimea maxima a unei secvente de duble consecutive.
    """
    rolls: List[str] = s.split(",")
    max_streak = 0
    current_streak = 0

    for roll in rolls:
        x, y = roll.split("-")
        if x == y:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak

if __name__ == "__main__":
    print(doubles("6-3"))  # should return 0
    print(doubles("1-2,2-2"))  # should return 1
    print(doubles("1-1,5-5,2-3,3-5,2-4"))  # should return 2
    print(doubles("3-5,5-3,4-3,6-5"))  # should return 0
    print(doubles("4-4,6-6,3-4,6-6"))  # should return 2
    print(doubles("6-4,2-2,3-3,6-6,3-4,6-6,5-5"))  # should return 3
    print(doubles("3-3,3-3,4-4,6-4,6-6,2-2,1-1,6-6"))  # should return 4
    print(doubles("1-2,3-3,2-2,4-5,3-4,5-5,4-4,5-5,6-5,4-4,1-1"))  # should return 3
    print(doubles("1-1,2-2,6-6,6-6,3-3"))  # should return 5
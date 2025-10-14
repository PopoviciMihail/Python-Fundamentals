from typing import Dict

def char_frequency(sentence: str) -> Dict[str, int]:
    """
    Calculeaza frecventa fiecarui caracter dintr-un text.

    Args:
        sentence (str): Textul analizat.

    Returns:
        Dict[str, int]: Dictionar cu caracterele si numărul de aparitii.
    """
    freq: Dict[str, int] = {}
    for char in sentence:
        freq[char] = freq.get(char, 0) + 1
    return freq



if __name__ == "__main__":
    sentence = "This is a common interview question"
    result = char_frequency(sentence)
    print(result)

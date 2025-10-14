from typing import Dict

def char_frequency(sentence: str) -> Dict[str, int]:
    """
    Calculează frecvența fiecărui caracter dintr-un text.

    Args:
        sentence (str): Textul analizat.

    Returns:
        Dict[str, int]: Dicționar cu caracterele și numărul de apariții.
    """
    freq: Dict[str, int] = {}
    for char in sentence:
        freq[char] = freq.get(char, 0) + 1
    return freq



if __name__ == "__main__":
    sentence = "This is a common interview question"
    result = char_frequency(sentence)
    print(result)

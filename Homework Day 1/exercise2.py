from typing import List, Any

def split_into_chunks(payload: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Imparte o lista in subliste (chunks) de dimensiune fixa.

    Args:
        payload (List[Any]): Lista de valori care trebuie impartita.
        chunk_size (int): Dimensiunea fiecarui chunk (subliste).

    Returns:
        List[List[Any]]: O lista de subliste, fiecare avand maximum `chunk_size` elemente.
        
    """
    return [payload[i:i + chunk_size] for i in range(0, len(payload), chunk_size)]


if __name__ == "__main__":
    payload = [1, 7, 2, 3, 4, 5, 7]
    chunk_size = 3
    result = split_into_chunks(payload, chunk_size)
    print(result)

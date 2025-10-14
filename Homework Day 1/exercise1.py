def fizzbuzz(n: int) -> None:
    """
    Afișează rezultatul FizzBuzz pentru un numar dat.

    Reguli:
        - Daca numarul este divizibil cu 3 si 5 -> afiseaza "FizzBuzz"
        - Daca este divizibil doar cu 3 -> afiseaza "Fizz"
        - Daca este divizibil doar cu 5 -> afiseaza "Buzz"
        - Altfel -> afiseaza numarul insusi

    Args:
        n (int): Numarul pentru care se aplica regulile FizzBuzz.

    Returns:
        None
    """
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


def fizzbuzz_100() -> None:
    """
    Ruleaza exercitiul FizzBuzz pentru primele 100 de numere (1–100)
    si afiseaza rezultatele pe linii separate.

    Args:
        None

    Returns:
        None
    """
    for i in range(1, 101):
        fizzbuzz(i)


fizzbuzz_100()

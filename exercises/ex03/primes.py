"""EX03 - prime functions."""

__author__: str = 730387431


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(-4))
    print(is_prime(1))
    print(is_prime(0))
    print(is_prime(11))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))
    # ex. print(is_prime(5)), print(list_primes(10, 20))

def is_prime(x: int) -> bool:
    """Determines if number is prime."""
    div: int = 2
    if x <= 1:
        return False
    while div < x:
        if x % div == 0:
            return False
        div += 1
    return True


def list_primes(x: int, y: int) -> list[int]:
    """Makes a list of all primes between 2 numbers."""
    # For every number between two numbers if the number is prime add the number to the list
    primes: list[int] = []
    while x < y:
        if is_prime(x):
            primes.append(x)
            x += 1
        else:
            x += 1
    return primes
    

if __name__ == "__main__":
    main()
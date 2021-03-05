"""EX03 - palindromify function."""

__author__: str = 730387431


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    palindromify("red", True)
    palindromify("live on time ", False)
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))


def palindromify(x: str, y: bool) -> str:
    """A function that creates palindromes."""
    if y: 
        i: int = 0
        even_palindrome: str = x
        while i < len(x):
            even_palindrome += x[len(x) - (1 + i)]
            i += 1
        return even_palindrome
    else:
        odd_palindrome: str = x
        i: int = 0
        while i < len(x) - 1:
            odd_palindrome += x[len(x) - (2 + i)]
            i += 1
        return odd_palindrome


if __name__ == "__main__":
    main()
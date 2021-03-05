"""EX03 - avoid_fifth function."""

__author__: str = 730387431


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(phrase: str) -> str:
    """A function that eliminates e"""
    without_e: str = ""
    for letter in phrase:
        if letter != "e" and letter != "E":
            without_e += letter
    return without_e


if __name__ == "__main__":
    main()
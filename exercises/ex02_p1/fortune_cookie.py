"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730387431"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune() -> str:
    cookie_number: int = randint(1, 4)
    if cookie_number < 2:
        return "Fortune Cookie Message 1"
    else:
        if cookie_number < 3:
            return "Fortune Cookie Message 2"
        else:
            if cookie_number < 4:
                return "Fortune Cookie Message 3"
            else:
                return "Fortune Cookie Message 4"

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()

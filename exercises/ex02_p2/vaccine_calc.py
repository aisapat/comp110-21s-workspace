"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730387431"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    num_days: int = int(days_to_target(population, doses, doses_per_day, target))
    # TODO 4: Call future_date and store result in a variable.
    yay: str = str(future_date(num_days))
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(num_days) + " days, which falls on " + str(yay) + ".")


def days_to_target(a: int, b: int, c: int, d: int) -> int:
    """calculates number of days until target is reached"""
    num_vac: int = int(round((d / 100) * (a * 2)))
    ppl_left: int = int(num_vac - b)
    days: int = int(ppl_left / c)
    return(days)


# TODO 3: Define future_date function
def future_date(x: int) -> str:
    """calcutes the date that target is reached"""
    days_till: timedelta = timedelta(x)
    today: datetime = datetime.today()
    best_day: datetime = today + days_till
    return best_day.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()

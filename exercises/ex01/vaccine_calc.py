"""A vaccination calculator."""

__author__ = "730387431"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...


population: int = int(input("Population: "))
administered: int = int(input("Doses administered: "))
per_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))


num_vac: int = round(float(target / 100.0) * (population * 2))
ppl_left: int = num_vac - administered

days: int = int(ppl_left / per_day)
num_days: timedelta = timedelta(days)

today: datetime = datetime.today()

best_day: datetime = today + num_days

print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + best_day.strftime("%B %d, %Y") + ".")
#!/usr/bin/env python3

import sys

print("here")

sys.exit()

now=int(input("Please enter a time in 24-hour format: "))
hoursahead=int(input("Please enter some number of hours in the future: "))

then24=(now+hoursahead%24)%24
then12=then24%12
daysahead=hoursahead//24

print("The new time in 24-hour format is", then24, "In 12-hour format is", then12, "with", daysahead, "days elapsed")


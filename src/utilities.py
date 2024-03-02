# this file holds all required functions

import calendar


def provide_calendar(year: int):
    y = 2024
    for m in range(1, 13):
        print(calendar.month(y, m))
    return True


if __name__ == '__main__':
    provide_calendar(2024)

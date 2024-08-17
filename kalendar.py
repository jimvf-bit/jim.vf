import os

os.system("clear")
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _is_leap(year):
    """year -> 1 if leap year, else 0."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_in_month(year, month):
    """year, month -> number of days in that month in that year."""
    assert 1 <= month <= 12, "Month should be between 1 and 12."
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]


def ok():
    a = (_days_in_month(y, o))
    count = 1
    for i in range(1, a + 1):
        print(i, end=" ")
        if i == count * 7:
            print()
            count += 1


y = int(input("Enter year: "))
o = int(input("Enter month: "))

print(f"\n\t{y}-yil {o}-oy")
ok()

# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# print(calendar.month(yil,oy))

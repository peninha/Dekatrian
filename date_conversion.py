# -*- coding: utf-8 -*-
"""
Some functions to convert between Dekatrian and Gregorian calender.
@author: Pena
11\10\2017
dekatrian.com
"""


def Dek2week(dekDay, dekMonth, dekYear):
    """
    Returns the Gregorian week day from a Dekatrian date.
    1 = Sunday; 2 = Monday; 3 = Tuesday ... 7 = Saturday.
    """
    weekDay = ((WeekdayOnFirstAuroran(dekYear)
                + DekatrianWeek(dekDay, dekMonth) - 2) % 7) + 1
    if dekMonth == 0:
        weekDay = ((weekDay - 3 + dekDay) % 7) + 1
    return weekDay


def DekatrianWeek(dekDay, dekMonth):
    """
    Returns the Dekatrian week day from a Dekatrian date.
    Here we can see the elegance of Dekatrian, since it's not necessary to
    inform the year. Actually, barely it's necessary to inform the month,
    as it's only needed to check if that is an Achronian day.
    0 = Achronian; 1 = first week day; 2 = second week day ... 7 = seventh.
    """
    if dekMonth == 0:
        return 0
    else:
        dekWeekDay = ((dekDay-1) % 7) + 1
        return dekWeekDay


def WeekdayOnFirstAuroran(dekYear):
    """
    Returns the Gregorian week day for the 1 Auroran of a given year
    """
    weekDay = ((1 + 5*((dekYear) % 4) + 4*((dekYear) % 100)
                + 6*((dekYear) % 400)) % 7) + 1
    return weekDay


def CheckLeapYear(dekYear):
    if (dekYear % 4 == 0) and (dekYear % 100 != 0 or dekYear % 400 == 0):
        return 1
    else:
        return 0


def YearDayOnDekaDate(dekDay, dekMonth, dekYear):
    """
    Returns the day of the year of a Dekatrian date.
    Achronian is the day 1.
    Sinchronian is day 2 when it exists.
    """
    if dekMonth == 0:
        return dekDay
    else:
        return (CheckLeapYear(dekYear)) + 1 + (dekMonth-1)*28 + dekDay


def YearDayOnGregDate(day, month, year):
    """
    Returns the day of the year of a Gregorian date.
    Jan 1 is the day 1.
    Dez 31 is the day 365 or 366, whether it's a leap year or not
    """
    Jan = 31
    Fev = 28 + CheckLeapYear(year)
    Mar = 31
    Apr = 30
    Mai = 31
    Jun = 30
    Jul = 31
    Ago = 31
    Set = 30
    Out = 31
    Nov = 30
    Dez = 31
    Meses = (Jan, Fev, Mar, Apr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez)
    i = 0
    days = 0
    while i < (month-1):
        days += Meses[i]
        i += 1
    return days + day


def Dek2Greg(dekDay, dekMonth, dekYear):
    """
    Returns a Dekatrian date from a Gregorian date.
    """
    YearDay = YearDayOnDekaDate(dekDay, dekMonth, dekYear)
    Jan = 31
    Fev = 28 + CheckLeapYear(dekYear)
    Mar = 31
    Apr = 30
    Mai = 31
    Jun = 30
    Jul = 31
    Ago = 31
    Set = 30
    Out = 31
    Nov = 30
    Dez = 31
    Meses = (Jan, Fev, Mar, Apr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez)
    for mes, dias in enumerate(Meses, start=1):
        if YearDay > dias:
            YearDay -= dias
        else:
            break
    return (YearDay, mes, dekYear)


def Greg2Dek(day, month, year):
    """
    Returns a Gregorian date from a Dekatrian date
    """
    YearDay = YearDayOnGregDate(day, month, year)
    LeapYear = CheckLeapYear(year)
    #print(YearDay)
    if YearDay > (1 + LeapYear):
        YearDay -= 1 + LeapYear
        #print(YearDay)
        dekMonth = int((YearDay-1) / 28) + 1
        dekDay = (YearDay-1) % 28 + 1
    else:
        dekMonth = 0
        dekDay = day
    return (dekDay, dekMonth, year)


if __name__ == "__main__":
    # Exemples #
    print("Dekatrian 28\\13\\2015 falls on Greg week day: "
          + str(Dek2week(28, 13, 2015)))
    print("Dekatrian 1\\0\\2016 falls on Greg week day: "
          + str(Dek2week(1, 0, 2016)))
    print("Dekatrian 2\\0\\2016 falls on Greg week day: "
          + str(Dek2week(2, 0, 2016)))
    print("Dekatrian 1\\1\\2016 falls on Greg week day: "
          + str(Dek2week(1, 1, 2016)))
    print("Achronian corresponds to Dekatrian week day: "
          + str(DekatrianWeek(1, 0)))
    print("Dekatrian 1\\1\\2016 happens on Gregorian week day: "
          + str(WeekdayOnFirstAuroran(2016)))
    print("Dekatrian 3\\1\\2017 is the year day: "
          + str(YearDayOnDekaDate(3, 1, 2017)))
    print("Dekatrian 10\\10\\2017 corresponds to Gregorian "
          + str(Dek2Greg(10, 10, 2017)))
    print("Gregorian 29/12/2016 is the year day: "
          + str(YearDayOnGregDate(29, 12, 2016)))
    print("Gregorian 3/1/2016 corresponds to Dekatrian: "
          + str(Greg2Dek(3, 1, 2016)))

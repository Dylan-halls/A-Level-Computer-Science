"""
Week 3.

Code for week 3 homework.
"""

import datetime
from calendar import monthrange


def water_temp():
    try:
        water_temp = int(input("water temperature: "))
    except ValueError:
        print("temp is a number")
        start()
    if water_temp <= 0:
        print("Water Frozen")
    elif water_temp >= 100:
        print("Water Boiling")
    else:
        print("Water Neither Boiling Or Frozen")


def work_for_pay():
    try:
        hours_worked = int(input("hours worked: "))
        hourly_pay = int(input("pay for an hours work: "))
    except ValueError:
        print("i need a number")
        start()()
    if (hours_worked <= 0) or (hours_worked >= 60):
        print("Error: wrong amount of time")
        work_for_pay()
    if hours_worked > 40:
        print("Your Pay Would Be: %d" % (hours_worked*(hourly_pay*1.5)))
    else:
        print("Your Pay Would Be: %d" % (hours_worked*hourly_pay))


def exam_mark():
    def _print(data):
        print(data)
        exit()

    def _pass():
        pass
    try:
        marks = int(input("marks: "))
    except ValueError:
        print("i need a number")
        start()
    _print("Grade A") if marks >= 81 else _pass()
    _print("Grade B") if marks >= 71 else _pass()
    _print("Grade C") if marks >= 61 else _pass()
    _print("Grade D") if marks >= 51 else _pass()
    _print("Grade E") if marks >= 41 else _pass()
    _print("Grade U") if marks <= 40 else _pass()


def month2day():
    try:
        month_num = int(input("month_num: "))
    except ValueError:
        print("i need a number")
        start()
    print(monthrange(datetime.datetime.now().year, month_num)[1])


def date2date():
    try:
        day = int(input("day: "))
        month = int(input("month: "))
        year = int(input("year: "))
    except ValueError:
        print("i need a number")
        start()
    try:
        print(datetime.date(int(str(20)+str(year)), month, day).strftime('%c'))
    except ValueError:
        print("Wrong date for date")
        start()

def start():
    todo = {
            "3.1": "water_temp()",
            "3.2": "work_for_pay()",
            "3.3": "exam_mark()",
            "3.4": "month2day()",
            "3.5": "date2date()"
           }

    print("Programs:\n")
    [print(i) for i in todo]
    choice = input("Choice: ")
    try:
        eval(todo[choice])
    except KeyError:
        print("Invalid Choice...")
        start()


start()

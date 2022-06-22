"""
Author: Ahmad Abu Hattab
Date: 06/20/2022
Athan tracker.
"""

import threading
import time
import tkinter as tk
from win10toast import ToastNotifier
from datetime import datetime
from datetime import date
from datetime import timedelta
import time
from tkinter import *
from random import randint
import sys
sys.setrecursionlimit(2000)


#def time_comp(time_ringer):
#def time_compp():

# Day 1 would be this:
# Jun 04 Sat	03:50 am	05:39 am	01:22 pm	05:22 pm	08:58 pm	10:08 pm
# Just mental notes




# Read the data from the prayer times text
def read_txt(file_name): # 04/25/2022
    """Read from text file and return the data.

    Args:
        file_name (str): The name of the text file.

    Returns:
        ([[str]]): The data from the text."""

    with open(file_name, 'r', encoding='utf-8') as f:
        data = []
        # read text line by line
        for line in f.readlines():
            parsed_line = line.strip('').split()
            data.append(parsed_line)

        return data


prayer_timings = read_txt('prayertimes.txt')
prayer_timings24 = read_txt('prayertimes24.txt')
# print(date.today())
def date_returner_sorted():
    """Take data from array and bubble sort it

    Args:
        today (str): The time.
        split_day (list): All the timings for prayers (future).
        prayer_timings (str): all the prayer timings in document

    Returns:
        split_day (list): All the timings for prayers, but sorted using bubble sort method"""

    today = date.today()
    today = str(today)
    split_day = []
    datecurrent = today[8] + today[9]

    for i in prayer_timings:
        i[1] = int(i[1])
        split_day.append(i[1])


    for i in range(len(split_day)):
        for j in range(0, len(split_day) - 1):
            if split_day[j] > split_day[j+1]:
                split_day[j], split_day[j+1] = split_day[j+1], split_day[j]
    # OUTPUT
    return (split_day)


def date_returner():
    """Take data from file and return the index for the date

    Args:
        today (str): The time.
        split_day (list): All the timings for prayers (future).
        datecurrent (str): index of today's date
        prayer_timings (str): all the prayer timings in document

    Returns:
        split_day (list): All the timings for prayers, but sorted using bubble sort method"""
    today = date.today()
    today = str(today)
    split_day = []
    datecurrent = today[8] + today[9]

    for i in prayer_timings:
        split_day.append(i[1])

    if datecurrent in split_day:
        datecurrent = int(datecurrent)
        return (datecurrent)
    else:
        return "error"

def date_returner_fajr():
    today = date_returner()
    today = today + 1
    return today


def date_returner_bin():
    target = date_returner()
    split_day = date_returner_sorted()

    low = 0
    high = len(split_day) - 1
    while low <= high:
        mid = (high + low) // 2
        if split_day[mid] == target:
            # Output
            return mid

        if split_day[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    # Output
    return -1



# All the prayer functions that return a time
def fajr(timings):
    split_day = []
    for i in prayer_timings:
        split_day.append(i[3])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def sunrise(timings):
    split_day = []
    for i in prayer_timings:
        split_day.append(i[5])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def duhr(timings):
    split_day = []
    for i in prayer_timings:
        split_day.append(i[7])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def asr(timings):
    split_day = []
    for i in prayer_timings:
        split_day.append(i[9])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def magrib(timings):
    split_day = []
    for i in prayer_timings:
        split_day.append(i[11])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def isha(timings):
    split_day = []
    for i in prayer_timings:
        split_day.append(i[13])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
# ------------------------------------------------------------ 12 hour format vs 24 hour format
def fajr24(timings):
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[3])
    realfajrtime = split_day[date_returner()]
    return(realfajrtime)

def fajr24_nextday():
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[3])
    realfajrtime = split_day[date_returner_fajr()]
    return(realfajrtime)

def sunrise24(timings):
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[4])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def duhr24(timings):
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[5])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def asr24(timings):
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[6])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def magrib24(timings):
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[7])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)
def isha24(timings):
    split_day = []
    for i in prayer_timings24:
        split_day.append(i[8])

    realfajrtime = split_day[date_returner()]
    return(realfajrtime)


# TESTER FOR ABOVE ^^^^^^^^^^^^
# print(fajr24(prayer_timings24))
# print(sunrise24(prayer_timings24))
# print(duhr24(prayer_timings24))
# print(asr24(prayer_timings24))
# print(magrib24(prayer_timings24))
# print(isha24(prayer_timings24))



def comp_time_for_gui():
    time = datetime.now()
    twelvehourtime = time.strftime('%I:%M:%S %p')
    return twelvehourtime

# Converts all the timings into readable int's
def fajr_time_converter(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")

    for i in fajr(prayer_timings):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_fajr.append(i)
    return new_fajr
def sunrise_time_converter(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_sunrise = []
    #prayer_timings = prayer_timings.remove(":")

    for i in sunrise(prayer_timings):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_sunrise.append(i)
    return new_sunrise
def duhr_time_converter(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_duhr = []
    #prayer_timings = prayer_timings.remove(":")

    for i in duhr(prayer_timings):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_duhr.append(i)
    return new_duhr
def asr_time_converter(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_asr = []
    #prayer_timings = prayer_timings.remove(":")

    for i in asr(prayer_timings):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_asr.append(i)
    return new_asr
def magrib_time_converter(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_magrib = []
    #prayer_timings = prayer_timings.remove(":")

    for i in magrib(prayer_timings):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_magrib.append(i)
    return new_magrib
def isha_time_converter(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_isha = []
    #prayer_timings = prayer_timings.remove(":")

    for i in isha(prayer_timings):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_isha.append(i)
    if new_isha[-2] == "P":
        isPM = True
    else:
        isPM = False
    new_isha = new_isha[0:4]
    return new_isha
def comp_time_converter(time_rings):
    time = datetime.now()
    twelvehourtime = time.strftime('%I:%M:%S %p')
    twelvehourtime = str(twelvehourtime)
    #print(time)
    new_time = []
    new_time_mine = []
    isPM = None
    for i in twelvehourtime:
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_time.append(i)
    if new_time[-2] == "P":
        isPM = True
    else:
        isPM = False
    new_time = new_time[0:6]

        #new_time_mine = new_time_mine.append(new_time[0], new_time[1], new_time[2])
    return new_time

# -----------TESTER-------------------DOWN
# print(fajr_time_converter(prayer_timings))
# print(sunrise_time_converter(prayer_timings))
# print(duhr_time_converter(prayer_timings))
# print(asr_time_converter(prayer_timings))
# print(magrib_time_converter(prayer_timings))
# print(isha_time_converter(prayer_timings))
# print(comp_time_converter(prayer_timings))
# -----------TESTER-------------------UP





#---------------------RETURNS IF PM OR AM-----------------DOWN
def fajr_time_converter_am(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")
    isPM = None
    for i in prayer_timings:
        if i[4] == 'pm':
            isPM = True
        else:
            isPM = False

        return isPM
def sunrise_time_converter_am(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")
    isPM = None
    for i in prayer_timings:
        if i[6] == 'pm':
            isPM = True
        else:
            isPM = False

        return isPM
def duhr_time_converter_pm(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")
    isPM = None
    for i in prayer_timings:
        if i[8] == 'pm':
            isPM = True
        else:
            isPM = False

        return isPM
def asr_time_converter_pm(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")
    isPM = None
    for i in prayer_timings:
        if i[10] == 'pm':
            isPM = True
        else:
            isPM = False

        return isPM
def magrib_time_converter_pm(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")
    isPM = None
    for i in prayer_timings:
        if i[12] == 'pm':
            isPM = True
        else:
            isPM = False

        return isPM
def isha_time_converter_pm(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")
    isPM = None
    for i in prayer_timings:
        if i[14] == 'pm':
            isPM = True
        else:
            isPM = False

        return isPM

#def comp_time_converter_am_pm(time_rings):
    # prayer_timings = read_txt('prayertimes.txt')
    # new_fajr = []
    # #prayer_timings = prayer_timings.remove(":")
    # isPM = None
    # for i in prayer_timings:
    #     if i[4] == 'pm':
    #         isPM = True
    #     else:
    #         isPM = False
    #
    #     return isPM

# def update():
#    lab['text'] = randint(0,1000)
#    root.after(1000, update) # run itself again after 1000 ms

# -----------TESTER-------------------DOWN
# print(fajr_time_converter_sec(prayer_timings))
# print(sunrise_time_converter_sec(prayer_timings))
# print(duhr_time_converter_sec(prayer_timings))
# print(asr_time_converter_sec(prayer_timings))
# print(magrib_time_converter_sec(prayer_timings))
# print(isha_time_converter_sec(prayer_timings))
# print(comp_time_converter_sec(prayer_timings))
# -----------TESTER-------------------UP


# def comp_time(ring):
#     time = datetime.now()
#     max_tot = []
#     for i in time[0]:
#         i = int(i)*36000
#         max_tot.append(i)
#     for i in time[1]:
#         i = int(i) * 3600
#         max_tot.append(i)
#     for i in time[2]:
#         i = int(i) * 600
#         max_tot.append(i)
#     for i in time[3]:
#         i = int(i) * 60
#         max_tot.append(i)
#     max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
#     return(max_tot)
# print(comp_time(prayer_timings))

# def time_comp(time_ringer):
#     pass # empty function that doesnt work
def comp_time_converter_pmam(time_rings):
    """Take prayer time and convert to seconds

    Args:
        today (str): The time.
        thetimeholderstor (list): empty list.
        time (str): fajr prayer timings
        prayer_timings: All the prayer timings

    Returns:
        max_tot (list): prayer time converted to seconds"""
    time = datetime.now()
    twelvehourtime = time.strftime('%I:%M %p')
    twelvehourtime = str(twelvehourtime)
    #print(time)
    new_time = []
    new_time_mine = []
    isPM = None
    for i in twelvehourtime:
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_time.append(i)
    if new_time[-2] == "P":
        isPM = True
    else:
        isPM = False
    new_time = new_time[0:4]

        #new_time_mine = new_time_mine.append(new_time[0], new_time[1], new_time[2])
    return isPM
# ---------------------RETURNS IF PM OR AM-----------------UP
#---------------------TESTER-----------------DOWN
# print(fajr_time_converter_am(prayer_timings))
# print(sunrise_time_converter_am(prayer_timings))
# print(duhr_time_converter_pm(prayer_timings))
# print(asr_time_converter_pm(prayer_timings))
# print(magrib_time_converter_pm(prayer_timings))
# print(isha_time_converter_pm(prayer_timings))
# print(comp_time_converter_pmam(prayer_timings))
#---------------------TESTER-----------------UP






# 1 minute = 60 seconds
# 10 minute = 600 seconds
# 1 hour = 3600 seconds
# 10 hours = 36000 seconds

# THIS CONVERTS ALL OF THE TIME INTO SECONDS SO IT CAN BE USED IN THE CLASS
def fajr_time_converter_sec(time_rings):
    """Take prayer time and convert to seconds

    Args:
        today (str): The time.
        thetimeholderstor (list): empty list.
        time (str): fajr prayer timings
        prayer_timings: All the prayer timings

    Returns:
        max_tot (list): prayer time converted to seconds"""
    prayer_timings = read_txt('prayertimes.txt')
    time = fajr_time_converter(prayer_timings)

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    if fajr_time_converter_am(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot
def sunrise_time_converter_sec(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    time = sunrise_time_converter(prayer_timings)
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    if sunrise_time_converter_am(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot
def duhr_time_converter_sec(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    time = duhr_time_converter(prayer_timings)
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    if duhr_time_converter_pm(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot
def asr_time_converter_sec(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    time = asr_time_converter(prayer_timings)
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    if asr_time_converter_pm(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot
def magrib_time_converter_sec(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    time = magrib_time_converter(prayer_timings)
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    if magrib_time_converter_pm(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot
def isha_time_converter_sec(time_rings):
    prayer_timings = read_txt('prayertimes.txt')
    time = isha_time_converter(prayer_timings)
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    if isha_time_converter_pm(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot
def comp_time_converter_sec(time_rings):
    time = comp_time_converter(prayer_timings)
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    for i in time[4]:
        i = int(i)
        max_tot.append(i)
    for i in time[5]:
        i = int(i)
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3] + max_tot[4] + max_tot[5]
    if comp_time_converter_pmam(prayer_timings) == True:
        max_tot = max_tot + 43200
        return (max_tot)
    else:
        return max_tot

# -----------TESTER-------------------DOWN
# print(fajr_time_converter_sec(prayer_timings))
# print(sunrise_time_converter_sec(prayer_timings))
# print(duhr_time_converter_sec(prayer_timings))
# print(asr_time_converter_sec(prayer_timings))
# print(magrib_time_converter_sec(prayer_timings))
# print(isha_time_converter_sec(prayer_timings))
# print(comp_time_converter_sec(prayer_timings))
# -----------TESTER-------------------UP



# def comp_time(ring):
#     time = datetime.now()
#     max_tot = []
#     for i in time[0]:
#         i = int(i)*36000
#         max_tot.append(i)
#     for i in time[1]:
#         i = int(i) * 3600
#         max_tot.append(i)
#     for i in time[2]:
#         i = int(i) * 600
#         max_tot.append(i)
#     for i in time[3]:
#         i = int(i) * 60
#         max_tot.append(i)
#     max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
#     return(max_tot)
# print(comp_time(prayer_timings))



#--------------TEST------------DOWN
# print(fajr_time_converter_sec(prayer_timings))
# print(sunrise_time_converter_sec(prayer_timings))
# print(duhr_time_converter_sec(prayer_timings))
# print(asr_time_converter_sec(prayer_timings))
# print(magrib_time_converter_sec(prayer_timings))
# print(isha_time_converter_sec(prayer_timings))
# print(comp_time_converter_sec(prayer_timings))
#--------------TEST------------UP




def comp_timerfinderwiner24_for():
    """Take data from file and return the date but in 24 hour format

    Args:
        today (str): The time.
        thetimeholderstor (list): empty list.
        time (str): current time in 24 hour format

    Returns:
        thetimeholderstor (list): 24 hour format"""
    time = datetime.now()
    time = str(time)
    thetimeholderstor = []
    for i in time[11:13]:
        thetimeholderstor.append(i)
    for i in time[14:16]:
        thetimeholderstor.append(i)
    for i in time[17:19]:
        thetimeholderstor.append(i)
    return thetimeholderstor

#-----------------------------------------
def fajr_time_converter_24hour():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")

    for i in fajr24(prayer_timings24):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_fajr.append(i)
    return new_fajr
def sunrise_time_converter_24hour():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_sunrise = []
    #prayer_timings = prayer_timings.remove(":")

    for i in sunrise24(prayer_timings24):
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_sunrise.append(i)
    return new_sunrise
def duhr_time_converter_24hour():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_sunrise = []
    # prayer_timings = prayer_timings.remove(":")

    for i in duhr24(prayer_timings24):
        if ":" in i:
            i = i.replace(":", '')
        else:
            new_sunrise.append(i)
    return new_sunrise
def asr_time_converter_24hour():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_sunrise = []
    # prayer_timings = prayer_timings.remove(":")

    for i in asr24(prayer_timings24):
        if ":" in i:
            i = i.replace(":", '')
        else:
            new_sunrise.append(i)
    return new_sunrise
def magrib_time_converter_24hour():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_sunrise = []
    # prayer_timings = prayer_timings.remove(":")

    for i in magrib24(prayer_timings24):
        if ":" in i:
            i = i.replace(":", '')
        else:
            new_sunrise.append(i)
    return new_sunrise
def isha_time_converter_24hour():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_sunrise = []
    # prayer_timings = prayer_timings.remove(":")

    for i in isha24(prayer_timings24):
        if ":" in i:
            i = i.replace(":", '')
        else:
            new_sunrise.append(i)
    return new_sunrise
def comp_time_converter_24hour():
    time = datetime.now()
    time = str(time)
    thetimeholderstor = []
    for i in time[11:13]:
        thetimeholderstor.append(i)
    for i in time[14:16]:
        thetimeholderstor.append(i)
    for i in time[17:19]:
        thetimeholderstor.append(i)
    return thetimeholderstor
# TESTER FOR ABOVE ^^^^^^^
# print(fajr_time_converter_24hour())
# print(sunrise_time_converter_24hour())
# print(duhr_time_converter_24hour())
# print(asr_time_converter_24hour())
# print(magrib_time_converter_24hour())
# print(isha_time_converter_24hour())
# print(comp_time_converter_24hour())
def fajr_time_converter_24hour_nextday():
    prayer_timings24 = read_txt('prayertimes24.txt')
    new_fajr = []
    #prayer_timings = prayer_timings.remove(":")

    for i in fajr24_nextday():
        if ":" in i:
            i = i.replace(":",'')
        else:
            new_fajr.append(i)
    return new_fajr


# THIS CONVERTS ALL OF THE TIME INTO SECONDS SO IT CAN BE USED IN THE CLASS
def fajr_time_converter_sec24():
    prayer_timings = read_txt('prayertimes.txt')
    time = fajr_time_converter_24hour()

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
def sunrise_time_converter_sec24():
    prayer_timings = read_txt('prayertimes.txt')
    time = sunrise_time_converter_24hour()

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
def duhr_time_converter_sec24():
    prayer_timings = read_txt('prayertimes.txt')
    time = duhr_time_converter_24hour()

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
def asr_time_converter_sec24():
    prayer_timings = read_txt('prayertimes.txt')
    time = asr_time_converter_24hour()

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
def magrib_time_converter_sec24():
    prayer_timings = read_txt('prayertimes.txt')
    time = magrib_time_converter_24hour()

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
def isha_time_converter_sec24():
    prayer_timings = read_txt('prayertimes.txt')
    time = isha_time_converter_24hour()

    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
def comp_time_converter_sec24():
    time = comp_time_converter_24hour()
    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    for i in time[4]:
        i = int(i) * 10
        max_tot.append(i)
    for i in time[5]:
        i = int(i)
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3] + max_tot[4] + max_tot[5]
    return max_tot
def fajr_time_converter_sec24_nextday():
    prayer_timings = read_txt('prayertimes.txt')
    time = fajr_time_converter_24hour_nextday()


    max_tot = []
    for i in time[0]:
        i = int(i)*36000
        max_tot.append(i)
    for i in time[1]:
        i = int(i) * 3600
        max_tot.append(i)
    for i in time[2]:
        i = int(i) * 600
        max_tot.append(i)
    for i in time[3]:
        i = int(i) * 60
        max_tot.append(i)
    max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
    return (max_tot)
# print(fajr_time_converter_sec24())
# print(fajr_time_converter_sec24_nextday())

# TESTER FOR ABOVE ^^^^^^^^
# print(fajr_time_converter_sec24())
# print(sunrise_time_converter_sec24())
# print(duhr_time_converter_sec24())
# print(asr_time_converter_sec24())
# print(magrib_time_converter_sec24())
# print(isha_time_converter_sec24())
# print(comp_time_converter_sec24())

#print(datetime.date)


# -----------TESTER-------------------DOWN
# print(fajr_time_converter_sec(prayer_timings))
# print(sunrise_time_converter_sec(prayer_timings))
# print(duhr_time_converter_sec(prayer_timings))
# print(asr_time_converter_sec(prayer_timings))
# print(magrib_time_converter_sec(prayer_timings))
# print(isha_time_converter_sec(prayer_timings))
# print(comp_time_converter_sec(prayer_timings))
# -----------TESTER-------------------UP


# def comp_time(ring):
#     time = datetime.now()
#     max_tot = []
#     for i in time[0]:
#         i = int(i)*36000
#         max_tot.append(i)
#     for i in time[1]:
#         i = int(i) * 3600
#         max_tot.append(i)
#     for i in time[2]:
#         i = int(i) * 600
#         max_tot.append(i)
#     for i in time[3]:
#         i = int(i) * 60
#         max_tot.append(i)
#     max_tot = max_tot[0] + max_tot[1] + max_tot[2] + max_tot[3]
#     return(max_tot)
# print(comp_time(prayer_timings))

def time_comp(time_ringer):
    """Compare times and give back a seconds to countdown

    Args:
        computer_time (int): Computer's time.
        fajr_time (int): Fajr time in seconds.
        sunrise_time (int): Sunrise time in seconds.
        duhr_time (int): Duhr time in seconds.
        asr_time (int): Asr time in seconds.
        magrib_time (int): Magrib time in seconds.
        isha_time (int): Isha time in seconds.
        fighting_time (list): The prayers to be subtracted and give a time for countdown
        time_left (int): 0 for now until changed.

    Returns:
        time_left (int): Time left for the next prayer.
        """




    computer_time = int(comp_time_converter_sec24())
    fajr_time = int(fajr_time_converter_sec24())
    sunrise_time = int(sunrise_time_converter_sec24())
    duhr_time = int(duhr_time_converter_sec24())
    asr_time = int(asr_time_converter_sec24())
    magrib_time = int(magrib_time_converter_sec24())
    isha_time = int(isha_time_converter_sec24())
    fighting_time = []
    time_left = 0

    if computer_time > fajr_time:
        if computer_time > sunrise_time:
            if computer_time > duhr_time:
                if computer_time > asr_time:
                    if computer_time > magrib_time:
                        if computer_time > isha_time: # if 10pm is passed 9pm then subtract 3am small from 10pm big
                            #print("Isha Passed")
                            fighting_time.append(86400 - isha_time + fajr_time)
                            fighting_time.append(0)
                            print(fighting_time)
                        else:
                            #print("Magrib Passed")
                            fighting_time.append(isha_time)
                            fighting_time.append(computer_time)
                    else:
                        #print("Asr Passed")
                        fighting_time.append(magrib_time)
                        fighting_time.append(computer_time)
                else:
                    #print("Duhr Passed")
                    fighting_time.append(asr_time)
                    fighting_time.append(computer_time)
            else:
                #print("Sunrise Passed")
                fighting_time.append(duhr_time)
                fighting_time.append(computer_time)
        else:
            #print("Fajr Passed")
            fighting_time.append(sunrise_time)
            fighting_time.append(computer_time)
    else:
        #print("Isha Passed")
        fighting_time.append(fajr_time)
        fighting_time.append(computer_time)
        print(fighting_time)

    time_left = fighting_time[0] - fighting_time[1] # One Liner Ice
    #print(fighting_time)
    #print(time_left)
    return(time_left)
# print(time_comp(prayer_timings24))
def time_compp():
    """Compare times and give back a the current prayer
    Depending on which prayer has passed, the code will return a string for the prayer.

    Args:
        computer_time (int): Computer's time.
        fajr_time (int): Fajr time in seconds.
        sunrise_time (int): Sunrise time in seconds.
        duhr_time (int): Duhr time in seconds.
        asr_time (int): Asr time in seconds.
        magrib_time (int): Magrib time in seconds.
        isha_time (int): Isha time in seconds.

    Returns:
        "Fajr" (str): Fajr prayer time.
        "Sunrise" (str): Sunrise prayer time.
        "Duhr" (str): Duhr prayer time.
        "Asr" (str): Asr prayer time.
        "Magrib" (str): Magrib prayer time.
        "Isha" (str): Isha prayer time.
        """




    computer_time = int(comp_time_converter_sec24())
    fajr_time = int(fajr_time_converter_sec24())
    sunrise_time = int(sunrise_time_converter_sec24())
    duhr_time = int(duhr_time_converter_sec24())
    asr_time = int(asr_time_converter_sec24())
    magrib_time = int(magrib_time_converter_sec24())
    isha_time = int(isha_time_converter_sec24())
    fighting_time = []
    time_left = 0

    if computer_time > fajr_time:
        if computer_time > sunrise_time:
            if computer_time > duhr_time:
                if computer_time > asr_time:
                    if computer_time > magrib_time:
                        if computer_time > isha_time: # if 10pm is passed 9pm then subtract 3am small from 10pm big
                            #print("Isha Passed")
                            return "Fajr"
                        else:
                            #print("Magrib Passed")
                            return "Isha"
                    else:
                        #print("Asr Passed")
                        return "Magrib"
                else:
                    #print("Duhr Passed")
                    return "Asr"
            else:
                #print("Sunrise Passed")
                return "Duhr"
        else:
            #print("Fajr Passed")
            return "Sunrise"
    else:
        #print("Isha Passed")
        return "Fajr"

# print(time_compp())

def time_left_for_gui():
    time = time_comp(prayer_timings)

    ttime = str(timedelta(seconds=time))
    return ttime
# print(time_left_for_gui())
#-----------------------------------------


def compare_time():
    if comp_time_converter_pmam(prayer_timings) == True: # We want to eliminate all the non-pm's here, but HOW!??!
        pass

class CountdownTimer:

    def __init__(self):
        prayer_timings = read_txt('prayertimes.txt')
        self.root = tk.Tk()
        self.root.geometry("460x460")
        self.root.title("Prayer Times")

        # self.time_entry = tk.Entry(self.root, font=("Helvetica", 20))
        # self.time_entry.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        # self.stop_button = tk.Button(self.root, font=("Helvetica", 30), text="Start", command=self.start_thread)
        # self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.root, font=("Helvetica", 32, 'underline'), fg="green", text=f"{time_compp()} in: {time_left_for_gui()}")
        self.time_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.date_label = tk.Label(self.root, font=("Helvetica", 14, 'bold italic'), fg="red", text=f"{date.today()}")
        self.date_label.grid(row=9, column=0, columnspan=1, padx=5, pady=5)

        self.timer_label = tk.Label(self.root, font=("Helvetica", 16, 'bold italic'), fg="red", text=f"Clock: {comp_time_for_gui()}")
        self.timer_label.grid(row=9, column=1, columnspan=1, padx=5, pady=5)

        #-------------------------------PRAYERS-----------------------------------DOWN
        self.fajr_label = tk.Label(self.root, font=("Helvetica", 24, 'bold italic'), text=f"Fajr:")
        self.fajr_label.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.fajrr_label = tk.Label(self.root, font=("Helvetica", 22), text=f"{fajr(prayer_timings)} am")
        self.fajrr_label.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

        self.sunrise_label = tk.Label(self.root, font=("Helvetica", 24, 'bold italic'), text=f"Sunrise:")
        self.sunrise_label.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.sunrisee_label = tk.Label(self.root, font=("Helvetica", 22), text=f"{sunrise(prayer_timings)} am")
        self.sunrisee_label.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

        self.duhr_label = tk.Label(self.root, font=("Helvetica", 24, 'bold italic'), text=f"Duhr:")
        self.duhr_label.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.duhrr_label = tk.Label(self.root, font=("Helvetica", 22), text=f"{duhr(prayer_timings)} pm")
        self.duhrr_label.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

        self.asr_label = tk.Label(self.root, font=("Helvetica", 24, 'bold italic'), text=f"Asr:")
        self.asr_label.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.asrr_label = tk.Label(self.root, font=("Helvetica", 22), text=f"{asr(prayer_timings)} pm")
        self.asrr_label.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

        self.magrib_label = tk.Label(self.root, font=("Helvetica", 24, 'bold italic'), text=f"Magrib:")
        self.magrib_label.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
        self.magribb_label = tk.Label(self.root, font=("Helvetica", 22), text=f"{magrib(prayer_timings)} pm")
        self.magribb_label.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

        self.isha_label = tk.Label(self.root, font=("Helvetica", 24, 'bold italic'), text=f"Isha:")
        self.isha_label.grid(row=6, column=0, columnspan=1, padx=5, pady=5)
        self.ishaa_label = tk.Label(self.root, font=("Helvetica", 22), text=f"{isha(prayer_timings)} pm")
        self.ishaa_label.grid(row=6, column=1, columnspan=1, padx=5, pady=5)
        #-------------------------------PRAYERS-----------------------------------UP
        def updatetimer():
            self.time_label.config(text=f"{time_compp()} in: {time_left_for_gui()}")
            self.time_label.after(1000, updatetimer)
        def updatedate():
            self.timer_label.config(font=("Helvetica", 16, 'bold italic'), fg="red", text=f"Clock: {comp_time_for_gui()}")
            self.timer_label.after(1000, updatedate)
        def updatefajr():
            self.fajrr_label.config(font=("Helvetica", 22), text=f"{fajr(prayer_timings)} am")
            self.fajrr_label.after(1000, updatefajr)
        def updatesun():
            self.sunrisee_label.config(font=("Helvetica", 22), text=f"{sunrise(prayer_timings)} am")
            self.sunrisee_label.after(1000, updatesun)
        def updateduhr():
            self.duhrr_label.config(font=("Helvetica", 22), text=f"{duhr(prayer_timings)} pm")
            self.duhrr_label.after(1000, updateduhr)
        def updateasr():
            self.asrr_label.config(font=("Helvetica", 22), text=f"{asr(prayer_timings)} pm")
            self.asrr_label.after(1000, updateasr)
        def updatemagrib():
            self.magribb_label.config(font=("Helvetica", 22), text=f"{magrib(prayer_timings)} pm")
            self.magribb_label.after(1000, updatemagrib)
        def updateisha():
            self.ishaa_label.config(font=("Helvetica", 22), text=f"{isha(prayer_timings)} pm")
            self.ishaa_label.after(1000, updateisha)
        def updatedatee():
            self.date_label.config(font=("Helvetica", 14, 'bold italic'), fg="red", text=f"{date.today()}")
            self.date_label.after(1000, updatedatee)
        #---------------------------------------------------PRAYER TIMER UPDATE ^^^^
        self.time_label.after(1000, updatetimer())
        self.timer_label.after(1000, updatedate())
        self.fajrr_label.after(1000, updatefajr())
        self.sunrisee_label.after(1000, updatesun())
        self.duhrr_label.after(1000, updateduhr())
        self.asrr_label.after(1000, updateasr())
        self.magribb_label.after(1000, updatemagrib())
        self.ishaa_label.after(1000, updateisha())
        self.date_label.after(1000, updatedatee())
        #-----------------------------DATE BELOW







        #self.timer_label.after
        #
        # updatetimer()
        #
        self.stop_loop = False
        self.root.mainloop()




    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("Invalid")
            return

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"Time left: {hours:02d}:{minutes:02d}:{seconds:02d}")
            # self.root.update()
            time.sleep(1)

        if not self.stop_loop:
            toast = ToastNotifier()
            toast.show_toast("Masjid", "It's salah time!", duration=10)

    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="Text: 00:00:00")


def main():
    prayer_timings = read_txt('prayertimes.txt')

    CountdownTimer()

if __name__ == '__main__':
    main()

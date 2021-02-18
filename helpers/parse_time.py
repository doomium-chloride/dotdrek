import re
import numpy as np

def hms_to_minutes(hour, minute, second):
    return hour * 60 + minute + second / 60

def minutes_to_hms(minutes):
    hour = int(minutes // 60)
    minutes -= hour * 60
    minute = int(np.floor(minutes))
    second = int(np.floor(minutes - minute))
    return "{0}:{1}:{2}".format(hour, minute, second)

def time_str_to_minutes(time_str):
    #[hour, min, sec]
    hms = time_str.split(":")
    if len(hms) != 3 or not hms[0].isnumeric():
        return float('-inf')
    hour = int(hms[0])
    minute = int(hms[1])
    second = int(hms[2])

    return hms_to_minutes(hour, minute, second)

def numerify_string(string):
    return re.sub("[^0-9]", "", string)

def parse_numeric_time(time):
    if(time < 10):
        # assume hours
        return hms_to_minutes(time, 0, 0)
    else:
        # assume minutes
        return hms_to_minutes(0, time, 0)

def parse_hms_string(string):
    total_minutes = 0
    had_h = False
    had_m = False
    # lower case
    if 'h' in string:
        str_arr = string.split('h')
        if len(str_arr) > 0:
            had_h = True
            try:
                hour = float(numerify_string(str_arr[0]))
                total_minutes += hms_to_minutes(hour, 0, 0)
            except ValueError:
                pass
        string = ''.join(str_arr[1:])
    if 'm' in string or had_h:
        str_arr = string.split('m')
        if len(str_arr) > 0:
            if 'm' in string:
                had_m = True
            try:
                minute = float(numerify_string(str_arr[0]))
                total_minutes += hms_to_minutes(0, minute, 0)
            except ValueError:
                pass
        string = ''.join(str_arr[1:])
    if had_m:
        str_arr = string.split('m')
        if len(str_arr) > 0:
            try:
                sec = float(numerify_string(str_arr[0]))
                total_minutes += hms_to_minutes(0, 0, sec)
            except ValueError:
                pass
    return total_minutes

def parse_colon_string(string, colon = ":"):
    str_arr = string.split(colon)
    if len(str_arr) <= 0:
        return 0
    if len(str_arr) == 1:
        return hms_to_minutes(float(str_arr[0]), 0, 0)
    if len(str_arr) == 2:
        return hms_to_minutes(float(str_arr[0]), float(str_arr[1]), 0)
    return hms_to_minutes(float(str_arr[0]), float(str_arr[1]), float(str_arr[2]))
    

def parse_string_time(string):
    string = string.lower()
    if ":" in string:
        return parse_colon_string(string)
    elif ";" in string:
        return parse_colon_string(string, ";")
    else:
        return parse_hms_string(string)
    

def parse_time(string):
    string = re.sub(" ", "", string)
    if string.isnumeric():
        time = float(string)
        return parse_numeric_time(time)
    else:
        return parse_string_time(string)
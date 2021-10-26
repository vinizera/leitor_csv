def dayCheck(year, month, day):
    from datetime import datetime
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday']
    correct_date = None
    try:
        new_date = datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
        return False
    after_feb = 1
    if month > 2:
        after_feb = 0
    aux = year - 1700 - after_feb
    day_of_Week = 5
    day_of_Week += (aux + after_feb) * 365
    day_of_Week += aux // 4 - aux // 100 + (aux + 100) // 400
    day_of_Week += offset[month - 1] + (day - 1)
    day_of_Week %= 7
    return week[day_of_Week]


def logCheck(id, initial_date, final_date, key_set):
    valid_key = None
    initial_date_code = initial_date.replace("-", "")
    final_date_code = final_date.replace("-", "")
    if initial_date_code != final_date_code:
        valid_key = False
        return valid_key
    while len(initial_date_code) == 8 and str(initial_date_code).isnumeric() and str(id).isnumeric():

        date_array = initial_date.split("-")
        year = int(date_array[0])
        month = int(date_array[1])
        day = int(date_array[2])
        date_check = dayCheck(year, month, day)
        if not date_check:
            valid_key = False
            return valid_key

        key = str(id) + str(initial_date_code)
        if key in key_set:
            valid_key = False
            return valid_key
        else:
            key_set.add(key)
            valid_key = True
            return valid_key
    else:
        return valid_key


def checkTime(time):
    if len(time) == 8:
        if str(time.replace(":", "")).isnumeric():
            time_form = time.split(":")
            if len(time_form) != 3:
                return False
            time_check = list()
            if 20 >= int(time_form[0]) >= 8:
                time_check.append(str(time_form[0]))
            else:
                return False
            if 59 >= int(time_form[1]) >= 0:
                time_check.append(str(time_form[1]))
            else:
                return False
            if 59 >= int(time_form[2]) >= 0:
                time_check.append(str(time_form[2]))
            else:
                return False
            return time_check
        else:
            return False
    else:
        return False

def checkTimeDif(initial_time, final_time):
    initial_time_array = checkTime(initial_time)
    final_time_array = checkTime(final_time)
    if initial_time_array[0] > final_time_array[0]:
        return False
    elif (initial_time_array[0] == final_time_array[0]) and (initial_time_array[1] > final_time_array[1]):
        return False
    elif (initial_time_array[0] == final_time_array[0]) \
            and (initial_time_array[1] == final_time_array[1]) \
            and (initial_time_array[2] >= final_time_array[2]):
        return False
    else:
        return True

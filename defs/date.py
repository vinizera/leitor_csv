from datetime import date


def getDateName():
    date_name = str(date.today()).replace("-", "")
    return date_name

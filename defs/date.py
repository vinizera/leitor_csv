def getDateNum():
    from datetime import date
    date_name = str(date.today()).replace("-", "")
    return date_name

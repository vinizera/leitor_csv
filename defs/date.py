def getDateNum():
    """
    :return: Data atual numericamente formatada (sem quaisquer sinais)
    """
    from datetime import date
    date_name = str(date.today()).replace("-", "")
    return date_name

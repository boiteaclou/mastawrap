import datetime


def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S.f")
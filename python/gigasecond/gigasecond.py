import datetime

GIGA = 10 ** 9
DELTA_GIGASECOND = datetime.timedelta(seconds=GIGA)

def add_gigasecond(birth_date):
    '''Given a datetime.date return the date + 1 gigasecond'''
    return birth_date + DELTA_GIGASECOND
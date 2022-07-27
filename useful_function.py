#String to Int convertor
def str_to_int(s):
    if type(s) == int:
        return s
    elif s.isnumeric() == True:
        return int(s)
    n = ''
    for i in s:
        if i.isnumeric() == True:
            n += i
    return int(n)

#Age to date convertor
from datetime import date
def get_year(yearDate):
    today = date.today()
    return today.year - yearDate

#Remove empty space
def remove_space(w):
    if type(w) != str:
        return w
    return w.strip()



__author__ = 'nikhil'

from time import strftime

while True:
    a = input('Enter : ')
    if int(a) == 1:
        checker = True
    else:
        checker = False

    if checker:
        print(strftime("%Y-%m-%d")+'.log')
    else:
        print('false h')
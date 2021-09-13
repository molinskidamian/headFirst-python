from datetime import datetime
from random import randint
from time import sleep

odds = [
    1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
    21, 23, 25, 27, 29, 31, 33, 35, 37,
    39, 41, 43, 45, 47, 49, 51, 53, 55,
    57, 59 ]

rightNowMinutes = datetime.today().minute
seconds = datetime.today().second

print('Aktulanie jest minuta: ' + str(rightNowMinutes))
print("Aktualnie upłyneło sekund: " + str(seconds))



index = 0
total = 5

while index < total:
    sekNum = randint(0, 59)
    print('Losowa liczba z zakresu 0 - 59: ' + str(sekNum))
    print('Wstrzymanie funkcji na ' + str(sekNum) + ' sekund')
    sleep(sekNum)
    if rightNowMinutes in odds:
        print('Minuta ' + str(rightNowMinutes) + ' NIE! jest parzysta')
    else:
        print('Minuta ' + str(rightNowMinutes) + ' jest parzysta')

if rightNowMinutes in odds:
    print('Aktualna minuta nie jest parzysta')
else:
    print('Aktualna minuta jest parzyzta')
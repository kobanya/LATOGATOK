'''
NB- 2023 03 20
LATOGATÓK
'''

from random import *

nap = int(input("Hány nap látogatóit generálja a program: "))

for i in range(1, nap+1):
    latogatok = randrange(80)
    print(f"{i}. nap: {latogatok} fő")
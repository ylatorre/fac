
from qtido import *

import sys

def principale():

    print("Bienvenu dans", sys.argv[0])
    print("------------------------------")

    qui = sys.argv[1]
    print("Bonjour", qui)

    if len(sys.argv) > 2:
        n = int(sys.argv[2])
        for i in range(n):
            print(i+1, "cool")

principale()


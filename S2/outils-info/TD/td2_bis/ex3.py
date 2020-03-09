import random
x = random.randrange(18)
i = 0
while i == 0:
    y = int(input("alors ?"))
    if x > y:
        print('plus')
    else:
        if x < y:
            print('moins')
        else:
            if x == y:
                print('bravo')
                i = 1
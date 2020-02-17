i = 0
n = 0
while i == 0:
    n = n + 1
    j = n % 3
    k = n % 5
    if j == 0 and k == 0:
        print("PoumTchak",n)
        
    else:
        if j == 0 and k != 0:
            print("Poum",n)
        else:
            if j != 0 and k == 0:
                print('Tchak',n)
        
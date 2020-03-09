a = int(input('a :'))
b = int(input('b :'))
c = int(input('c :'))

if a < b and a < c:
    print(b + c)
    print('a est le plus petit')
else: 
    if b < c and b < a:
        print(c + a)
        print('b est le plus petit')
    else:
        if c < b and c < a:
            print(b + a)
            print('c est le plus petit')
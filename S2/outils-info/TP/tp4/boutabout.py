def bout_a_bout(ch1, ch2):
    print("L1 :", len(ch1))
    print("L2 :", len(ch2))
    l = len(ch1) + len(ch2)
    print("Total :", l)
    return ch1 + ch2
    print("Jamais")
a = "Toto"
b = bout_a_bout(a,"Titi")
c = bout_a_bout(a, b)
print()




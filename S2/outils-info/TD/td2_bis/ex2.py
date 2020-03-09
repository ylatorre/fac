impot = int(input("Envoie t'as money :"))

if impot < 8000:
    print('rien a payer')
else:
    if impot >= 8000 and impot < 25000:
        x = float(impot * (10/100))
        print('payer 10%',x)
    else:
        if impot >= 25000:
            x = float(impot * (20/100))
            print("merci pour ton oseille mec",x,"balles mec c'est trop bien")


n = int(input("Saisir un nombre entier : "))

if n < 2:
    print("Ce nombre n'est pas premier")
else:
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False

    if premier:
        print("Ce nombre est premier")
    else:
        print("Ce nombre n'est pas premier")

print("Les nombres premiers de 1 à 100 :")

for n in range(2, 101):
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False
    if premier:
        print(n)
    """
var n,i:entier
ecrire("saisir un entier)
lire n
si n < 2 alors
    ecrire("Ce nombre n'est pas premier")
sinon 
    premier = vrai
    pour i de 2 jusqua n faire 
        si n % i == 0 alors
            premier = faux

    si premier alors
        ecrire("Ce nombre est premier")
    sinon
        ecrire("Ce nombre n'est pas premier")

ecrire("Les nombres premiers de 1 à 100 :")

pour n de 2 jusqua 101 faire 
    premier = vrai
    pour i de 2 jusqua n faire
        si n % i == 0 alors
            premier = faux
    si premier alors
        ecrire(n)"""
while True:
    n = input("Saisir une valeur : ")
    if n.isdigit():
        n = int(n)
        break
S = 0
for i in range(1,10):
    while True:
        a = input("Saisir une valeur : ")
        if a.isdigit():
            a = int(a)
            break
    if a == n :
        S += 1
print("La première valeur apparait", S, "fois")
"""
Var n,a,S,i:entier
Début
Lire n
S = 0
pour i allant de 1 à 10 faire
    Lire a
    si a == n alors
        S += 1
Finpour
Ecrire"La première valeur apparait", S, "fois"
Fin
"""
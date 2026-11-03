n = int(input("Saisir le nombre d'etudiants : "))

somme = 0

for i in range(1, n + 1):
    note = float(input("Donner une note : "))
    somme = somme + note

moyenne = somme / n

print("La moyenne est :", moyenne)
"""
var moyenne, i, somme:reel
var n : entier
ecrire(Saisir le nombre d'etudiants) 
lire n
somme=0
pour i de 1 jusqua n+1 faire
   ecrire(Donner une note )
   lire note
   somme=somme+note
moyenne=somme/n
ecrire("La moyenne est :", moyenne)

phrase = input("Saisir une phrase : ")
S = 0
for i in range(len(phrase)):
    if phrase[0] == phrase[i]:
        S += 1
print(f"La lettre {phrase[0]} apparait {S} fois" )
"""
Var phrase : chaine de caractère
Var i,S : Entier
S = 0
pour i allant de 0 à longueur(phrase)-1 faire
    si phrase[0] == phrase[i] alors
        S += 1
Ecrire"La lettre ",phrase[0] ,"apparait",S ,"fois"
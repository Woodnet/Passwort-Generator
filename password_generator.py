#
#	Author: Pulsar
#	YouTube: https://www.youtube.com/channel/UCVo0vjlE50dn2LFynrGe9yA
# GitHub: https://www.github.com/Woodnet
# Twitter: https://twitter.com/7Pulsar
#	Python-Version: Python 3.8.2
#	Recommended OS: Windows 10
#	--> Please write a comment on GitHub-issues.
#

import os,random,sys
from time import sleep
import pyperclip as pc 

def passwort_generieren(länge):
    len_klein_buchstaben = len(library['buchstaben'])
    len_groß_buchstaben = len_klein_buchstaben
    len_zahlen = len(library['zahlen'])
    len_zeichen = len(library['zeichen'])
    len_zahlen -= 1
    len_groß_buchstaben -= 1
    len_klein_buchstaben -= 1
    len_zeichen -= 1
    PASSWORT = []
    for i in range(länge):
        zahl_klein_buchstabe = random.randint(0,len_klein_buchstaben)
        zahl_zahlen = random.randint(0,len_zahlen)
        zahl_zeichen = random.randint(0,len_zeichen)
        zahl_groß_buchstabe = random.randint(0,len_groß_buchstaben)

        buchstabe_k = library['buchstaben'][zahl_klein_buchstabe]
        buchstabe_g = library['buchstaben'][zahl_groß_buchstabe].upper()
        zahl = str(library['zahlen'][zahl_zahlen])
        zeichen = library['zeichen'][zahl_zeichen]

        string = buchstabe_k + buchstabe_g + zahl + zeichen

        PASSWORT.append(string)
    passwort = "".join(PASSWORT)
    return passwort

library = {
    'buchstaben': [
        "a","b","c","d","e","f","g","h","i",
        "j","k","l","m","n","o","p","q","r",
        "s","t","u","v","w","x","y","z",
    ],
    'zahlen': [1,2,3,4,5,6,7,8,9,0],
    'zeichen': [
        "#","/","!","*","+","~","(",")","[",
        "]","?"
    ],
}

if __name__  == '__main__':
    l = input("Password Länge / Password length = ")  #Länge des Passworts
    os.system("cls")
    länge = int(l)
    sys.stdout.write("\r INFO: Passwort wird generiert / Generating Password..")
    sys.stdout.flush()
    passwort = passwort_generieren(länge)
    print("(+)")
    L = länge * 4 + 13
    W = []
    for i in range(L):
        W.append("-")
    wall = "".join(W)
    print("""\n\n
    Passwort: %s
    \n\n
    """%(passwort))

pc.copy(passwort)
print("INFO: Passwort wurde kopiert! / Copied to Clipboard!")    
input("")

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:18:29 2019

@author: Schaufler Christoph
         S1810632017
"""
import math
"""

Übungsaufgaben 1

Aufgabe 1:
Schreibe eine Funktion is_prime, 
die prüft ob eine Zahl eine Primzahl ist.
"""
print("Programm für Primzahl oder Skalarprodukt: is_prime(n) oder scalar(vector1,vector2) ")

def is_prime(n):
     
    if n < 2:print(n, "ist eine Primzahl.")
    elif n == 2:print(n, "ist eine Primzahl.")
    elif n % 2 == 0:print(n, "ist keine Primzahl.")
    else:
        for n in range(3, math.ceil(math.sqrt(n))):
            if n % n != 0:
                continue
            print(n, "ist keine Primzahl.")
            break
        else:
            print(n, "ist eine Primzahl.")
    
"""
Übungsaufgaben 2

Aufgabe 1:
Implementiere eine Funktion scalar, die das Skalarprodukt 
von zwei Vektoren berechnet (ohne numpy zu verwenden!).

"""
vector1=[1,2,3]
vector2=[4,5,6]

def scalar(vector1,vector2):
  
    if len(vector1)==len(vector2):
            
        scalar = 0
        for i in range(len(vector1)):
            scalar += vector1[i] * vector2[i]
        return(scalar)
    else:
        print("Falsche Eingabe")
        return(False)
        
   
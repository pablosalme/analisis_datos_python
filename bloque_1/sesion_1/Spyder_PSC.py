#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:29:41 2023

@author: pablo

2. Abrir el **Spyder**, crear un script de python **".py"** de al menos una línea ejecutable y guardarlo como ***Spyder_<iniciales_del_alumn@>.py***
"""

while True:
    nombre = input("Por favor, ingresa un nombre o 'Q' para salir: ")
    
    if nombre.lower() == "q":
        break
    
    print("Hola, " + nombre + "!")

print("Saliendo del programa. ¡Hasta luego!")

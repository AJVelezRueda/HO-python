#!/usr/bin/env python
#Ejercicio I
multiplos = []
for i in range(0,1000):
    if (i%3)==0:
        multiplos.append(i)
    elif (i%5) ==0:
        multiplos.append(i)
multiplos = set(multiplos)
suma = 0
for i in multiplos:
    suma = suma + i
print(suma)

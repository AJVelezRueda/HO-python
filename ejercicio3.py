#!/usr/bin/env python
#Ejercicio III
num = 600851475143
denom = 2

facprimos = []
while num > 1:
    while (num%denom) == 0:
        num = num/denom
        facprimos.append(denom)
    denom += 1
facprimos = list(set(facprimos))
max(facprimos)


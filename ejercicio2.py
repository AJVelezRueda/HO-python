#!/usr/bin/env python
#Ejercico 2 
a = 0
b = 1
fibronacci = []
while b<1000000:
    a,b = b , b+a
    fibronacci.append(b)
suma = 0
for i in fibronacci:
    if (i%2) != 0:
        suma = suma + i
print(suma)

# Hacer un programa que tome un nu ́mero entero y diga si el nu ́mero es par o impar. 
# Tip: El operador % da el resto de la divisi ́on entera. 
# Ejemplo: 17 ÷ 5 da da cociente 3 y resto 2. Osea, 17/5 = 3 y 17 %5 = 2, ya que % da el resto.

Num = int(input('ingrese un  numero: '))

if Num % 2 == 0:
     print('es par')
else:
     print('es impar')
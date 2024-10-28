# Cuando alguien se va a vivir solo, se le suele decir que tiene que saber cocinar un huevo duro. 
# Eso solo implica hervirlo cierta cantidad de tiempo. 
# Para eso, necesitamos un timer. La idea es crear dicho timer, osea, dada una cantidad de segundos,
# que haga una cuenta regresiva de esa cantidad de segundos. TIP: para que la computadora espere 1 segundo,
# basta con el comando time.sleep(1). Tienen que poner al principio del c ́odigo import time,
# que trae el m ́odulo necesario para que el comando descrito anteriormente funcione.
# Desaf ́ıo extra: ¿Que tal si en tiempo est ́a en minutos? Modificar el programa para que tome minutos y
# no segundos. Puede ser minutos no enteros, por ejemplo, 0,5 minutos son 30 segundos.

import time

def Segundos(segs):
    for i in  range (segs + 1):
        time.sleep(1)
        print(i)
        i+=1
    
def Minutos(mins):
    segs = int(mins * 60)
    for i in  range (segs + 1):
        time.sleep(1)
        print(i)
        i+=1

Minutos(0.2)
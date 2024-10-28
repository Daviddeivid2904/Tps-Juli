
# ’Donde est ́a Wally?’ es el famoso libro de dibujos donde hay que buscar a Wally, un personaje, 
# entre dibujos muy cargados de cosas. Resulta ahora que Wally decidi ́o salir a buscar un trabajo
# de programador de python y se termin ́o escondiendo en una lista.
# Hacer un programa que dada una lista devuelva la posici ́on en donde est ́a. 
# Si tengo la lista [’Hola’,’Otra cosa’,’Wally’,’Per ́on’,’ORT’], el programa debe devolver Wally est ́a en la
# posici ́on 2 (queda a criterio de ustedes si usan la indexaci ́on de python o si le suman uno para usar 
# la m ́as natural).
# Desaf ́ıo extra: Si Wally no est ́a en la lista, tienen que informarlo tambi ́en
#  (una u ́nica vez, no por cada elemento).

def DondeWally(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].lower()
    if "wally" in lista:
        print('siiii, encontraste a wally')
    else:
        print('noup, wally no esta')


eifo = ['JUAN','otra cosa','wally']

DondeWally(eifo)
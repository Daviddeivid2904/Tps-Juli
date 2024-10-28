# Agus arm ́o una app para la fiesta de egresados que encuentra a las parejas m ́as apropiadas. 
# Lula le pas ́o sus datos a Agus, y Agus nos pas ́o dos listas, de igual longitud, una con nombres 
# y otra con el porcentaje de compatibilidad. Las listas est ́an en el mismo orden, de tal forma que al 
# primer nombre le corresponde el primer porcentaje, al segundo nombre el segundo porcentaje, etc. 
# Tu misi ́on es hacer un programa que le diga a Lula qui ́en es su Wanted para la fiesta de egresados. 
# Ejemplo: Si Agus nos da las listas [‘Lauti’,‘Cami’,‘Mile’,‘Fran’,‘Agus’] y [34,56,48,78,70], 
# deber ́ıamos devolver ‘Fran’.
# Tip: Fijense de recorrer la lista de porcentajes. Si encuentro el  ́ındice del m ́aximo elemento, 
# ya tengo gran parte del problem a hecho.
# Desaf ́ıo extra: Resulta que a veces hay gente que tiene la misma compatibilidad. 
# Modificar el c ́odigo para que con- sidere que puede haber m ́as de un m ́aximo.
# Ejemplo: Si nos dan las listas [‘Lauti’,‘Cami’,‘Mile’,‘Fran’,‘Agus’] y [34,78,48,78,70], 
# deber ́ıamos devolver ‘Cami’,‘Fran’.

def Match(personas, porcentaje):
    mejor = 0
    match = []
    for i in porcentaje:
        if i >= mejor:
            mejor = i
    match.append(personas[porcentaje.index(mejor)])
    return match

print(Match(['Lauti','Cami','Mile','Fran','Agus'],[34,56,98,50,70]))
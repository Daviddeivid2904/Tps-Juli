# Para poder pasar el an ̃o, me tiene que dar el promedio de notas mayor a 7. 
# Hacer un programa al cual le pueda ingresar notas, y, no solo me calcule el promedio,
# sino que tambi ́en determine si a la vuelta del viaje de egresados me quede seguir sufriendo o
# si soy libre1. TIP: A priori uno no sabe cuantas notas va a promediar,
# entonces no se cuantos input tendr ́ıa que incluir. 
# Pid ́amosle al usuario cuantas notas quiere promediar antes de empezar2.


materias = int(input('ingrese cuantas materias quiere promediar '))

def Promediar(materias):
    total = 0
    for i in range (materias):
        total = total + int(input('ingrese su nota en una materia '))
    promedio = total/materias
    
    return promedio
        
print(str(Promediar(materias)))

"""
Agregar películas
El programa debe preguntar cuántas películas desea ingresar.
Por cada película, debe solicitar:
Título (texto)
Año de estreno (número)
Género (texto, como por ejemplo: acción, drama, comedia, etc.)
Cada película debe guardarse como una lista con tres elementos y agregarse a la lista principal peliculas.
Mostrar todas las películas registradas
Mostrar en pantalla todas las películas almacenadas, con su título, año y género.
Buscar películas por género
Pedir al usuario un género y mostrar todas las películas que pertenezcan a ese género.
Eliminar una película por título
Solicitar el título exacto de una película y eliminarla de la lista si existe.
Ver estadísticas del catálogo
Mostrar cuántas películas hay registradas.
Mostrar cuántas películas hay por género.
Mostrar cuál es la película más antigua (menor año de estreno).
Salir del programa
Cerrar el programa cuando el usuario lo indique.
"""


boot_menu = True

while boot_menu:
    menu_inpt = input("----------Bienvenido----------\n"
                      "\n1. Ingresar n números y mostrar"
                      "\n2. Calcular el área de un triángulo"
                      "\n3. Verificar si un número es par o impar"
                      "\n4. Calcular el promedio de n calificaciones"
                      "\n5. Ingresar n números y mostrar el mayor y el menor"
                      "\n6. Salir del programa\n\nSeleccione una opción: ")
    match menu_inpt:
        case "1":
            try:
                max = int(input("Coloque la cantidad de números que quiere colocar: "))
                multifunction_n(max)
            except ValueError:
                print("Ese no es un número")
        case "2":
            triarea()
        case "3":
            try:
                eve_xxx = int(input("Coloque el número: "))
                even_odd(eve_xxx)
            except ValueError:
                print("Ese no es un número")
        case "4":
            score_calc()
        case "5":
            max_min_calculataa()
        case "6":
            print("Gracias por usar el programa")
            key = False
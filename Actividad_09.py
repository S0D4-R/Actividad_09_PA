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

movies = [
    ["Tron Legacy", "Sci-Fi", 2012],
    ["Como agua para chocolate", "Romance", 1992],
    ["Gladiador", "Action", 2000]
]
def addmov():
    temp_list = []
    name = input("Coloque el nombre de la nueva película: ")
    temp_list.append(name)
    genre = input(
        "Escoja entre los siguientes géneros:\na. Action\nb. Romance\nc. Drama\nd.Sci-Fi\ne. Crime\nf. Terror\n\n")
    if genre.lower() == "a":
        temp_list.append("Action")
    elif genre.lower() == "b":
        temp_list.append("Romance")
    elif genre.lower() == "c":
        temp_list.append("Drama")
    elif genre.lower() == "d":
        temp_list.append("Sci-Fi")
    elif genre.lower() == "e":
        temp_list.append("Crime")
    elif genre.lower() == "f":
        temp_list.append("Terror")
    else:
        print("Opción no válida")
    year = int(input("Coloque el año de estreno"))
    temp_list.append(year)
    print("Película agregada exitosamente:\n {}, {}, {}\n\n".format(temp_list[0], temp_list[1], temp_list[2]))
    return temp_list
#


boot_menu = True

while boot_menu:
    menu_inpt = input("----------Bienvenido----------\n"
                      "\n1. Agregar película"
                      "\n2. Mostrar todas las películas registradas"
                      "\n3. Buscar películas por género"
                      "\n4. Eliminar una película por título"
                      "\n5. Ver estadísticas del catálogo"
                      "\n6. Salir del programa\n\nSeleccione una opción: ")
    match menu_inpt:
        case "1":
            try:
                movies.append(addmov())
            except ValueError:
                print("Ese no es un número")
        case "2":
            print("Este es el catálogo de películas: \n")
            for movie in movies:
                print(f"Película: {movie[0]}\nGénero: {movie[1]}\nAño: {movie[2]}\n\n")
        case "3":
            try:
                pass
            except ValueError:
                print("Ese no es un número")
        case "4":
            rem_mov = input("Coloque el nombre de la película que quiere eliminar: ")
            for movie in movies:
                if rem_mov.lower() == movie[0].lower():
                    print("La película {} ha sido eliminada".format(movie[0]))
                    movies.remove(movie)
                    break

        case "5":
            pass
        case "6":
            print("Gracias por usar el programa")
            boot_menu = False
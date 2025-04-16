bibloteca = []

def registrar_libros():
    libros = []
    nombre = str(input("dame el nombre del libro: "))
    autor = str(input("dame el autor del libro: "))
    año = int(input("dame el año del libro: "))
    precio = int(input("dame el precio del libro: "))

    libros.append(nombre)
    libros.append(autor)
    libros.append(año)
    libros.append(precio)
    bibloteca.append(libros)
    
    

def consultar_libro():
    nombres = str(input("dame el nombre del libro: "))
    for libro in bibloteca:
        if libro[0] == nombres:
            print("el libro si esta: ",libro[0])
            break
    else:
        print("no existe el libro")
    

def mostrar_todos_los_libros():
    for libros in bibloteca:
        print(libros)


def eliminar_libro():
    nombre_a_eliminar = str(input("dame el nombre del libro a eliminar: "))
    for libro in bibloteca:
        if libro[0] == nombre_a_eliminar:
            bibloteca.remove(libro)
            print("el libro fue eliminado")
            break
    else:
        print("no existe el libro")

def menu():
    print("----OPCIONES PARA ELEGIR----")
    print("1.Para registrar libros")
    print("2.Para consultar libros")
    print("3. Para eliminar libros")
    print("4.Para mostrar todos los libros")
    print("5.Para generar un reporte")
    print("6.Para salir")

def generar_reporte():
    total_de_libros = len(bibloteca)
    print("esto es el numero de libros:",total_de_libros)

    sumar_libros = (libros for libros in bibloteca)
    suma = sum(sumar_libros)
    print("la suma de los libros es:",suma)
    
    promedio = suma / total_de_libros
    print("el promedio es:", promedio)
        
    precios = (libros[3] for libros in bibloteca)
    maximo = max(precios)
    print("el precio mas caro de los libros es:",maximo)





while True:
    menu()
    opcion = int(input("dame una opcion: "))
    
    if opcion == 1:
        registrar_libros()
    elif opcion == 2:
        consultar_libro()
    elif opcion == 3:
        eliminar_libro()
    elif opcion == 4:
        mostrar_todos_los_libros()
    elif opcion == 5:
        generar_reporte()
    elif opcion == 6:
        break
    else:
        print("opcion no valida")


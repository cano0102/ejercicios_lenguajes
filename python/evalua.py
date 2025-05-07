from random import randint

animales = []

def menu_especie():
    print("--------------------")
    print("Opciones a elegir")
    print("1. Perro")
    print("2. Gato")
    print("3. Ave")
    print("4. Otro")

def registrar_animal():
    try:
        mascotas = {}
        codigo = randint(1000, 10000)
        mascotas["codigo"] = codigo

        nombre = input("DAME EL NOMBRE DE LA MASCOTA: ")
        mascotas["nombre"] = nombre

        menu_especie()
        opciones = int(input("DAME UNA OPCIÓN: "))

        if opciones == 1:
            mascotas["especie"] = "perro"
        elif opciones == 2:
            mascotas["especie"] = "gato"
        elif opciones == 3:
            mascotas["especie"] = "ave"
        elif opciones == 4:
            mascotas["especie"] = "otro"
        else:
            print("OPCIÓN INVÁLIDA")
            return

        edad = int(input("DAME LA EDAD: "))
        if edad > 0:
            mascotas["edad"] = edad
        else:
            print("no se puede registrar")

        nombre_dueño = input("DAME EL NOMBRE DEL DUEÑO: ")
        mascotas["nombre_dueño"] = nombre_dueño

        animales.append(mascotas)
        print("Mascota registrada con éxito.\n")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def consultar_mascota():
    try:
        nombre_a_buscar = input("DAME EL NOMBRE DE LA MASCOTA: ")
        encontrado = False
        for mascota in animales:
            if mascota["nombre"] == nombre_a_buscar:
                print(mascota)
                encontrado = True
                break
        if not encontrado:
            print("No está registrada esa mascota.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def eliminar_mascota():
    try:
        nombre_a_eliminar = input("DAME EL NOMBRE DE LA MASCOTA: ")
        for i, mascota in enumerate(animales):
            if mascota["nombre"] == nombre_a_eliminar:
                animales.pop(i)
                print("Mascota eliminada.")
                return
        print("No está registrada esa mascota.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def mostrar_todas_los_animales():
    try:
        for mascota in animales:
            print(mascota)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def guardar_informcion():
    try:
        with open("mascotas.txt", "w") as f:
            for mascota in animales:
                f.write(str(mascota) + "\n")
        print("Información guardada con éxito.")
    except Exception as e:
        print(f"No se pudo guardar la información: {e}")

def cargar_archivo_iniciar():
    try:
        with open("mascotas.txt", "r") as f:
            contenido = f.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo 'mascotas.txt' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")

def reporte():
    try:
        total_mascotas = len(animales)
        print("El total de las mascotas es:", total_mascotas)

        if total_mascotas == 0:
            print("No hay mascotas registradas para generar el reporte.")
            return

        suma = sum(mascota["edad"] for mascota in animales)
        print("La suma de las edades es:", suma)

        promedio = suma / total_mascotas
        print("Promedio de edad:", promedio)

        conteo = {"perro": 0, "gato": 0, "ave": 0, "otro": 0}
        for mascota in animales:
            especie = mascota.get("especie", "")
            if especie in conteo:
                conteo[especie] += 1

        print("Cantidad por especie:")
        for especie, cantidad in conteo.items():
            print(f"{especie}: {cantidad}")
    except Exception as e:
        print(f"Ocurrió un error en el reporte: {e}")

def menu():
    print("------------------------")
    print("--- OPCIONES A ELEGIR ---")
    print("1. Registrar un animal")
    print("2. Consultar un animal")
    print("3. Eliminar un animal")
    print("4. Mostrar todos los animales")
    print("5. Guardar la información")
    print("6. Generar reporte")
    print("7.Para leer archivo")
    print("8. salir")

while True:
    try:
        menu()
        opcion = int(input("DAME UNA OPCIÓN: "))

        if opcion == 1:
            registrar_animal()
        elif opcion == 2:
            consultar_mascota()
        elif opcion == 3:
            eliminar_mascota()
        elif opcion == 4:
            mostrar_todas_los_animales()
        elif opcion == 5:
            guardar_informcion()
        elif opcion == 6:
            reporte()
        elif opcion == 7:
            cargar_archivo_iniciar()
        elif opcion == 8:
            print("Programa finalizado.")
            break
        else:

            print("OPCIÓN NO VÁLIDA")
    except ValueError:
        print("Error: Debes ingresar un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
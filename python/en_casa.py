# Ejercicios con Listas
# Ejercicio 1: Gestión de Libros en una Biblioteca

# Escenario: Una biblioteca necesita administrar su colección de libros.
# Objetivo: Crear un sistema para agregar, prestar y mostrar libros disponibles.
# Requisitos:

#     Agregar nuevos libros (título, autor, ISBN)

#     Prestar libros (marcar como no disponible)

#     Mostrar libros disponibles

#     Buscar libros por autor o título
#     Restricciones:

#     No permitir libros con el mismo ISBN

#     Máximo 3 préstamos por usuario

#     Validar que el ISBN tenga 13 dígitos

# biblioteca = []

# def menu():
#     print("----OPCINES PARA ELEGIR----")
#     print("1.Mostar libros disponibles")
#     print("2.Para agregar libro")
#     print("3. Para prestar libro")
#     print("4.Para salir")




# def agregar_libro():
    
#         libros = []  
#         nombre = str(input("dame el titulo del libro: "))
#         libros.append(nombre)
#         estado = True
#         libros.append(estado)
#         autor = str(input("autor del libro: "))
#         libros.append(autor)
#         ISBN = int(input("dame el ISBN del libro: "))
#         libros.append(ISBN)
#         biblioteca.append(libros)
        

# def mostrar_libros():
#     for i, libro in enumerate(biblioteca, 1):
#         print(i,"titulo" ,{libro[0]},"estado",{libro[1]},"autor",{libro[2]},"ISBN",{libro[3]})



# while True:
#         menu()
#         opcion = int(input("dame una opcion: "))
#         if opcion == 1:
#             mostrar_libros()
#         elif opcion == 2:
#             agregar_libro()


        


    
# agregar_libro()





# Escribe un programa en Python que pida al usuario ingresar dos números y realice la división del primer número entre el segundo. Utiliza try y except para manejar posibles errores, como dividir por cero o ingresar datos no numéricos.

# Tu objetivo es mostrar un mensaje adecuado según el tipo de error y, si la operación es exitosa, mostrar el resultado de la división.





# try:
#     numero_uno = float(input("DAME EL PRIMIER NUMERO"))
#     numero_dos = float(input("DAME EL SEGUNDO NUMERO"))
#     total = numero_uno / numero_dos
    
# except (ZeroDivisionError,TypeError,ValueError ) as e:
#     print("ocurrio un error ", e)
# else:
#     print(total)
    


# Escribe un programa en Python que pida al usuario ingresar un número entero y verifique si es par o impar. Utiliza try y except para manejar posibles errores si el usuario ingresa algo que no sea un número entero.

# Tu objetivo es mostrar un mensaje adecuado si ocurre un error y, si no, mostrar si el número es par o impar.



# try:
#     numero_par = int(input("dame un numero par"))
#     if numero_par%2==0:
#         raise ValueError("el numero es inpar")
# except(ValueError,TypeError) as e:
#     print("es un error",e)
# else:
#     print("el numero es par")

# try:
#     numero= float(input("dame un numero: "))
#     raiz = numero ** 0.5
# except (ValueError,TypeError,Exception) as e:
#     print("mero error" , e)
# else:
#     print(raiz)



# GESTION DE GANADO
# animales = []
# def registrar_animales():
    


#         codigo = int(input("dame el codigo"))
#         nombre = str(input("dame el animal"))
#         peso = int(input("dame el peso del animal"))
        

        
#         animales.append([codigo,nombre,peso])
        
        

# def mostrar_todos_los_animales():
#     print("todo los animales")
#     if not animales:
#         print("no hay animales")
#     else:
#         for animal in animales:
#             print(animal)

# def calculalar_peso_total():
#     peso_total = sum(animal[2] for animal in animales)
#     print(peso_total)

# def menu():
#     print("--- DAME UNA OPCION---")
#     print("1. Para agregar animales")
#     print("2. Para mostra todos los animales")
#     print("3. Para mostrar el peso total del ganado")
#     print("4. Para salir")


# while True:
#     menu()
#     opcion = int(input("DAME UNA OPCION: "))

#     if opcion == 1:
#         registrar_animales()
#     elif opcion == 2:
#         mostrar_todos_los_animales()
#     elif opcion == 3:
#         calculalar_peso_total()
#     elif opcion == 4:
#         break
#     else:
#         print("opcion no conpatible")



# equipo_a = []
# equipo_b = []


# def menu():
#     print("---OPCINES  A ELGIR---")
#     print("1.Para agregar un jugador del equipo A")
#     print("2.Para agregar un jugador del equipo B")
#     print("3.Para ver el resultado")
#     print("4.Para salir")

# def registrar_jugadores_equipo_a():
    
#     nombre_de_pokemon = str(input("dame el nombre: "))
#     numero_poder = int(input("dame el numero de poder: "))
#     equipo_a.append([nombre_de_pokemon,numero_poder])
#     print(equipo_a)

    

# def registrar_jugadores_equipo_b():
#     nombre_de_pokemon = str(input("dame el nombre: "))
#     numero_poder = int(input("dame el numero de poder: "))
#     equipo_b.append([nombre_de_pokemon,numero_poder])
#     print(equipo_b)


# def combate():

#     if not equipo_a and not equipo_b:
#         print("no hay jugadores")
#     else:
#         total_a = sum(poder[1] for poder in equipo_a )
#         total_b = sum(pod[1] for pod in equipo_b)
        
    
#     if total_a == total_b:
#         print("quedaron en empate")
#     else:
#         if total_a > total_b:
#             print("el ganador es el el entrenador del equipo A con un poder de " , total_a )
#         else:
#             print("el ganador es el entrenador del equipo B con un poder de " , total_a )

    
# while True:
#     menu()
#     opcion = int(input("DAME UNA OPCION: "))

#     if opcion == 1:
#         registrar_jugadores_equipo_a()
#     elif opcion == 2:
#         registrar_jugadores_equipo_b()

#     elif opcion == 3:
#         combate()
#     elif opcion == 4:
#         break
#     else:
#         print("opcion invalidad")
    


# todas_las_motos = []


# def menu():
#     print("---ELIGE UNA OPCION---")
#     print("1.Para agregar motos")
#     print("2.Para mostrar todas las motos")
#     print("3.Para ver la velocicdad maxima")
#     print("4.Para salir")

# def agregar_motos():
#     while True:
#         motos = {}
#         moto = str(input("dame la el nombre de la moto(escribe fin para salir): ")).lower()
#         if moto == "fin":
#             print("ya las motos quedaron registradas , gracias")
#             break
#         else:
#             velocidad = float(input("Dame la velocidad de la moto: "))
#             motos["Moto"] = moto
#             motos["velocidad"] = velocidad
#             todas_las_motos.append(motos)
            

# def mostrar():

#     for moto in todas_las_motos:
#         print(moto)

# def velocidad_maxima():
#     mootos = max(todas_las_motos , key=lambda x: x["velocidad"])
    
#     print(mootos)

# while True:
#     menu()
#     opcion = int(input("DAME UNA OPCION: "))

#     if opcion == 1:
#         agregar_motos()

#     elif opcion == 2:
#         mostrar()
#     elif opcion == 3:
#         velocidad_maxima()
#     elif opcion == 4:
#         break
#     else:
#         print("error")





# bibloteca = []

# def registrar_libros():
#     libros = []
#     nombre = str(input("dame el nombre del libro: "))
#     autor = str(input("dame el autor del libro: "))
#     año = int(input("dame el año del libro: "))
#     precio = int(input("dame el precio del libro: "))

#     libros.append(nombre)
#     libros.append(autor)
#     libros.append(año)
#     libros.append(precio)
#     bibloteca.append(libros)
    
    

# def consultar_libro():
#     nombres = str(input("dame el nombre del libro: "))
#     for libro in bibloteca:
#         if libro[0] == nombres:
#             print("el libro si esta: ",libro[0])
#             break
#     else:
#         print("no existe el libro")
    

# def mostrar_todos_los_libros():
#     for libros in bibloteca:
#         print(libros)


# def eliminar_libro():
#     nombre_a_eliminar = str(input("dame el nombre del libro a eliminar: "))
#     for libro in bibloteca:
#         if libro[0] == nombre_a_eliminar:
#             bibloteca.remove(libro)
#             print("el libro fue eliminado")
#             break
#     else:
#         print("no existe el libro")

# def menu():
#     print("----OPCIONES PARA ELEGIR----")
#     print("1.Para registrar libros")
#     print("2.Para consultar libros")
#     print("3. Para eliminar libros")
#     print("4.Para mostrar todos los libros")
#     print("5.Para generar un reporte")
#     print("6.Para salir")

# def generar_reporte():
#     total_de_libros = len(bibloteca)
#     print("esto es el numero de libros:",total_de_libros)

#     sumar_libros = (libros for libros in bibloteca)
#     suma = sum(sumar_libros)
#     print("la suma de los libros es:",suma)
    
#     promedio = suma / total_de_libros
#     print("el promedio es:", promedio)
        
#     precios = (libros[3] for libros in bibloteca)
#     maximo = max(precios)
#     print("el precio mas caro de los libros es:",maximo)





# while True:
#     menu()
#     opcion = int(input("dame una opcion: "))
    
#     if opcion == 1:
#         registrar_libros()
#     elif opcion == 2:
#         consultar_libro()
#     elif opcion == 3:
#         eliminar_libro()
#     elif opcion == 4:
#         mostrar_todos_los_libros()
#     elif opcion == 5:
#         generar_reporte()
#     elif opcion == 6:
#         break
#     else:
#         print("opcion no valida")



# import random
# banco = []

# def registrar_usuario():
#     usuario = {}

#     nombre = str(input("Dame tu nombre: "))
#     usuario["nombre"] = nombre

#     cuenta = random.randint(10000,20000)
#     usuario["cuenta"] = cuenta

#     saldo_inicial = float(input("dame tu saldo inicial: "))
#     usuario["saldo_inicial"] = saldo_inicial

#     banco.append(usuario)

# def menu():
#     print("---DAME UNA OPCION---")
#     print("1.Para registrarse")
#     print("2.Para consultar saldo")
#     print("3.Para realizar algun movimiento")
#     print("4.Para ver todos los clientes")
#     print("5.Para generar un reporte")
#     print("6.Para salir")


# def consultar():
#     numero_de_cuenta = int(input("Dame el numero de cuenta:"))
#     for cuenta in banco:
#         if  numero_de_cuenta == cuenta[1] :
#             print("tu cuneta si esta")
#         else:
#             print("tu cuneta no esta")

# def movimientos():
#     cuenta_cliente = int(input("Dame el tumero de tu cuenta"))
#     depositar_o_retirar = int(input("1 para deposirar 2 para retirar: "))
#     if depositar_o_retirar == 1:
#         for clientes in banco:
#             if clientes["cuentas"] == cuenta_cliente:
#                 depositar = int(input("dame el monto a depositar: "))
#                 deposito = clientes["saldo_inicial"] + depositar
#                 clientes.update()
#                 print(deposito)
#     elif depositar_o_retirar == 2:
#         for client in banco:
#             if client["cuentas"] == cuenta_cliente:
#                 retiro = int(input("dame el monto a retirar: "))
#                 retirado  = client["saldo_inicial"] - retiro
#                 client.update()
#                 print(retirado)
        


# def mostrar():
#     for clientes in banco:
#         print(clientes)

# def reporte():
#     pass

# while True:
#     menu()
#     opcion = int("DAME UNA OPCION: ")
#     if opcion == 1:
#         registrar_usuario()
#     elif opcion == 2:
#         consultar()
#     elif opcion == 3:
#         movimientos()
#     elif opcion == 4:
#         mostrar()
#     elif opcion == 5:
#         reporte()
#     elif opcion == 6:
#         print("gracias")
#         break
#     else:
#         print("opcion invalida")

import random
tienda = []


def consultar_pedido():
    numero_pedido =  int(input("dame el numero de pedido: "))
    for platos in tienda:
        if numero_pedido in platos:
            print("pedido existente")
        else:
            print("pedido no es encontrado")
    
def cancelar_pedido():
    numero_pedido =  int(input("dame el numero de pedido a cancelar: "))

    for plato in tienda:
        if plato["numero_pedido"] == numero_pedido:
            plato.remove(numero_pedido)

def ver_todos_los_pedidos():
    for platos in tienda:
        print(platos)
def reporte():
    pass


def menu():
    print("---ELIGE UNA OPCION---")
    print("1.Para registrar pedido")
    print("2.Para consultar pedido")
    print("3.Para cancelar un pedido")
    print("4.Para el reporte")
    print("5.Para ver todos los pedidios")
    print("6.Para salir")



def menu_platos():
    print("---MENU DE PLATOS---")
    print("1. ARROZ CON HUEVO : 20000")
    print("2. ARROZ CON POLLO : 30000")
    print("3. ARROZ PAISA : 30000")
    print("4. ARROZ VENECO : 10000")
    print("5.ARROZ ROLO : 15000")
    print("6. PARA SALIR")


def registrar_pedido():
        pedido = {}
        nombre_cliente = str(input("nombre del cliente: ")) 
        pedido["nombre"] = nombre_cliente
        numero_de_pedido = random.randint(10000,20000)
        pedido["numero_de_pedido"] = numero_de_pedido
        
        

        platos = []
        while True:
            
            menu_platos()
            opcion = int(input("DAME UNA OPCION: "))
            
            
            if opcion == 1:
                plato = "arroz con huevo"
                precio = 20000

                platos.append(plato)
                platos.append(precio)

            elif opcion == 2:
                plato = "arroz con huevo"
                precio = 20000

                platos.append(plato)
                platos.append(precio)

            elif opcion == 3:
                plato = "arroz con huevo"
                precio = 20000

                platos.append(plato)
                platos.append(precio)

            elif opcion == 4:
                plato = "arroz con huevo"
                precio = 20000

                platos.append(plato)
                platos.append(precio)

            elif opcion == 5:

                plato = "arroz con huevo"
                precio = 20000
                
                platos.append(plato)
                platos.append(precio)

            elif opcion == 6:
                print("muchas gracias por tus pedidos")
                break
            else:
                print("opcion invalidad")

        pedido["platos"] = platos
        
        tienda.append(pedido)
        print(tienda)



while True:
    menu()
    opcion = int(input("DAME UNA OPCION: "))
    if opcion == 1:
        registrar_pedido()
    elif opcion == 2:
        consultar_pedido()
    elif opcion == 3:
        cancelar_pedido()
    elif opcion == 4:
        reporte()
    elif opcion == 5:
        ver_todos_los_pedidos()
    elif opcion == 6:
        print("gracias")
        break





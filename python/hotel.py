# 2. Sistema de Reservas de Hotel

# Descripción:
# Crear un programa para gestionar reservas de habitaciones en un hotel, con opciones para agregar, consultar y cancelar reservas, además de reportes.

# Requisitos:

#     Registrar una reserva solicitando:

#         Nombre del cliente (no vacío).

#         Tipo de habitación (Individual, Doble, Suite).

#         Noches (enter opositivo).

#         Precio por noche (mayor que cero).

#     Consultar reserva por nombre del cliente.

#     Cancelar reserva por nombre.

#     Mostrar todas las reservas ordenadas por noches.

#     Generar un reporte con:

#         Total de reservas activas.

#         Ingresos potenciales (suma de precios).

#         Reserva más larga y más corta (nombre y noches).

#     Menú con manejo de excepciones.

#     Usar diccionarios para almacenar reservas.

hotel = []
def menu_tipo_habitacion():
        print("---Tipos de habitaciones elige una--")
        print("1.Individual")
        print("2.Doble")
        print("3.Suit")

def registrar_reserva():
    reservas = {}

    nombre : str = str(input("DEME EL NOMBRE DE LA PERSONA QUE HIZO LA RESERVA: ")).capitalize()
    reservas["Nombre_cliente"] = nombre


    menu_tipo_habitacion()
    tipo_de_habitacion : int = int(input("DAME EL TYPO DE RESERVA: "))
   

    
    if tipo_de_habitacion == 1:
        tipo_de_habitacion = "Individual"
        reservas["Tipo_habitacion"] = tipo_de_habitacion
    elif tipo_de_habitacion == 2:
        tipo_de_habitacion = "Doble"
        reservas["Tipo_habitacion"] = tipo_de_habitacion

    elif tipo_de_habitacion == 3:
        tipo_de_habitacion = "Suit"
    else:
        print("opcion invalidad")
    
    
    noches :str = str(input("DAME EL NUMERO DE LA HABITACION: "))
    reservas["Noches"] = noches
    
    precio :int = int(input("DAME EL PRECIO: "))
    reservas["Precio"] = precio

    
    hotel.append(reservas)
    print(hotel)

    print("se registro correctamente ✅")

def consultar_reserva():
    nombre_cliente = str(input("DAME EL NOMBRE DEL CLIENTE A BUSCAR: ")).capitalize()

    for reserva in hotel:
        if reserva["Nombre_cliente"] == nombre_cliente:
            print("Typo de habitacion:",reserva["Tipo_habitacion"])
            print("Nches: ", reserva["Noches"])
            print("precio:",reserva["Precio"])
        else:
            print("✖️NO ESTA✖️")

def cancelar_reserva():
    nombre_cliente = str(input("DAME EL NOMBRE DEL CLIENTE A BUSCAR PARA CANCELAR: ")).capitalize()
    for reserva in hotel:
            if reserva["Nombre_cliente"] == nombre_cliente:
                del reserva["Tipo_habitacion"]
                del reserva["Noches"]
                del reserva["Precio"]
                print("SE CANCELO LA RESERVA✅")


def mostras_reservas():
    for reserva in hotel:
        print(reserva)


def reporte():
    total = len(hotel)
    print("numero de habitacines reservadas" , total)
    suma = sum(sumas for sumas in hotel["Precio"])
    print(suma)

def menu():
    print("---OPCIONES A ELEGR---")
    print("1.Para registrar reserva")
    print("2.Para consultar una reserva")
    print("3.Para cacelar reserva")
    print("4.Para mostrar todas las reservas")
    print("5.Para el repote")
    print("6.Para salir")

while True:
    menu()
    opcion : int =int(input("DAME UNA OPCION: "))


    if opcion == 1:
        registrar_reserva()
    elif opcion == 2:
        consultar_reserva()
    elif opcion == 3:
        cancelar_reserva()
    elif opcion == 4:
        mostras_reservas()
    elif opcion == 5:
        reporte()
    elif opcion == 6:
        print("Muchas gracias ✅")
        break
    
    


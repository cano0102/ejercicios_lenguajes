# ejercicio1

# lista_tareas = []

# def menu():
#     print('----- OPCINES DE TAREA-----')
#     print("1. Agregar nueva tarea a la lista")
#     print("2. Eliminar una tarea ")
#     print("3. Mostrar todas las tareas")
#     print("Aviso : no se persimite mas de 10 tareas , no se permite tareas duplicadas")


# while True:
#     menu()
#     opcion = int(input("Dame un opcion: "))

#     if opcion == 1:
#         if len(lista_tareas) <= 10:
#             tarea = str(input("dame la tarea que quieres agregar: "))
#             if tarea in lista_tareas:
#                print("ya la tarea esta agregada")
#             else:
#                 lista_tareas.append(tarea)

#         else:
#             break

#     elif opcion == 2:
#         tarea_completada = str(input("dame la tarea completada para eliminar"))
#         if tarea_completada in lista_tareas:
#             lista_tareas.remove(tarea_completada)
#         else:
#             print("no encontramos tareas  ")
#     elif opcion == 3:
#         for i in lista_tareas:
#             print(i)


# ejercicio2




# def menu():
#     print('----- OPCINES DE STOCK-----')
#     print("1. Agregar productos al stock.")
#     print("2. Vender productos y reducir su cantidad. ")
#     print("3. Mostrar el inventario actual..")



# stock = []
# inventario = {}

# while True:
#     menu()
#     opcion = int(input("dame la opcion: "))

#     if opcion == 1:

#         nombre_producto = str(input("dame el nombre del producto: "))
#         inventario["Nombre"] = nombre_producto
        

#         valor_del_producto = int(input("dame el valor del producto: "))
#         inventario["valor"] = valor_del_producto


#         cantidad_disponible = int(input("dame la cantidad disponible del producto: "))
#         inventario["cantidad"] = cantidad_disponible

#         stock.append(inventario)

#     elif opcion == 2:
#         productos_a_comprar = input("producto a comprar: ")
#         if inventario["Nombre"] == productos_a_comprar:
#             cantidad = int(input("dame la cantidad que deseas comprar: "))

#             inventario["cantidad"] -= cantidad

#     elif opcion == 3:
#         for producto in stock:
#             print(producto)

#     elif opcion == 4:
#         break

# ejercicio3

# tarifas = (15700,20300,2700,3000,3800)

# while True:
#     opcion = float(input("ingresa el peso en Kg de tu paquete"))
#     if opcion <= 0:
#         print("tu paquete no tiene un peso")
#     elif opcion >= 1 and opcion <= 10.5:
#         print(F"la tarifa de tu paquete es: {tarifas[0]}")
#     elif opcion > 10.5 and opcion <= 27.5:
#         print(F"la tarifa de tu paquete es: {tarifas[1]}")
#     elif opcion > 27.5 and opcion <= 30.2:
#         print(F"la tarifa de tu paquete es: {tarifas[2]}")
#     elif opcion > 30.2 and opcion <= 35.7:
#         print(F"la tarifa de tu paquete es: {tarifas[3]}")
#     elif opcion > 35.7 and opcion <= 45.5:
#         print(F"la tarifa de tu paquete es: {tarifas[4]}")
#     else:
#         print(F"el peso de tu paquete excede la capacidad de nuestros envios")



# ejercicio4

# dias_servicio = ("lunes","martes","miercoles","viernes")

# while True:
#     opcion = str(input("ingresa el dia que deseas consultar")).lower()
#     if opcion in dias_servicio :
#         print("hay servicio el dia")
#     else: 
#         print(F"no hay servicio el dia {opcion}")
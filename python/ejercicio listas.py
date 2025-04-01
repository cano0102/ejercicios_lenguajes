# tareas = []
# while True: 
#     print("""
#     que deseas hacer?
#     (1) ver tus tareas
#     (2) agregar tarea
#     (3) eliminar tarea
#     """)
#     opcion = int(input("elige tu opción"))
#     match opcion: 
#         case 1:
#             if len(tareas) == 0:
#                 print("no tienes tareas")
#             else: 
#                 contador = 1
#                 for tarea in tareas :
#                     print(contador,"nombre:", tarea[0])
#                     contador +=1
#                 opcion = int(input("que tarea deseas ver"))
#                 if opcion <= 0 or opcion > len(tareas):
#                     print("no has escogido una opción posible")
#                 else:
#                     tarea = tareas[opcion-1]
#                     print(tarea[0],":", tarea[1])
#         case 2:
#             if len(tareas)>=10:
#                 print("ya has llegado al tope de tareas (10), no puedes agregar más sin eliminar alguna primera")
#             else:
#                 nombre_tarea = str(input("cuál será el nombre de tu tarea?"))
#                 contador = 0
#                 for tarea in tareas :
#                     if tarea[0] == nombre_tarea :
#                         contador+=1 
#                         break
#                 if contador == 1:
#                     print("ya tienes una tarea llamada así, se cancelara la agregación de esta tarea")
#                 else: 
#                     descripcion_tarea = str(input("escribe la descripción de tu tarea"))
#                     tareas.append([nombre_tarea,descripcion_tarea])
#         case 3:
#             if len(tareas) == 0:
#                 print("no tienes tareas")
#             else: 
#                 contador = 1
#                 for tarea in tareas :
#                     print(contador,"nombre:", tarea[0])
#                     contador +=1
#                 opcion = int(input("que tarea deseas eliminar"))
#                 if opcion <= 0 or opcion > len(tareas):
#                     print("no has escogido una opción posible")
#                 else:
#                     tareas.pop(opcion-1)

# ejercici2

# almacen = []
# while True: 
#     print("""
#         (1) mostrar el inventario actual
#         (2) agregar producto
#         (3) vender procuto
#     """)
#     opcion = int(input("elige tu opción"))
#     match opcion: 
#         case 1:
#             if len(almacen) == 0:
#                 print("no tienes productos")
#             else: 
#                 contador = 1
#                 for producto in almacen :
#                     print(contador,"nombre:", producto[0])
#                     contador +=1
#                 opcion = int(input("que producto deseas revisar"))
#                 if opcion <= 0 or opcion > len(almacen):
#                     print("no has escogido una opción posible")
#                 else:
#                     producto = almacen[opcion-1]
#                     print(F" nombre:{producto[0]}  precio: {producto[1]} descripcion:{producto[2]} disponibles:{producto[3]})")
#         case 2:
#             nombre_producto = str(input("cuál será el nombre de tu producto?"))
#             contador = 0
#             for producto in almacen :
#                 if producto[0] == nombre_producto :
#                     contador = 1 
#                     break
#             if contador == 1:
#                 print("ya tienes un producto llamada así, se cancelara la agregación de este producto")
#             else: 
#                 precio_producto = int(input("escribe el precio de tu producto"))
#                 descripcion_producto = str(input("escribe la descripción de tu producto"))
#                 stock_producto = int(input("ingresa la cantidad disponible del producto"))
#                 almacen.append([nombre_producto,precio_producto,descripcion_producto,stock_producto])
#         case 3:
#             if len(almacen) == 0:
#                 print("no tienes productos")
#             else: 
#                 contador = 1
#                 for producto in almacen :
#                     print(contador,"nombre:", producto[0])
#                     contador +=1
#                 opcion = int(input("que producto deseas comprar"))
#                 if opcion <= 0 or opcion > len(almacen):
#                     print("no has escogido una opción posible")
#                 else:
#                     producto = almacen[opcion-1]
#                     cantidad = int(input(F"cuantas unidades de {producto[0]} deseas comprar?"))
#                     if cantidad <= 0:
#                         print("no puedes comprar productos en negativo")
#                     elif  cantidad > producto[3] :
#                         print(F"solo contamos con {producto[3]} unidades")
#                     else:
#                         producto[3] -= cantidad
#                         subtotal = producto[1] * cantidad
#                         iva = producto[1] * 0.19
#                         total = subtotal + iva
#                         almacen.pop(opcion-1)
#                         almacen.append(producto)
#                         print(F"haz comprado exitosamente {producto[1],producto[0]} tu total con un iva del 19% es de: {total}")

# #3

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

# #4
# dias_servicio = ("lunes","martes","miercoles","viernes")

# while True:
#     opcion = str(input("ingresa el dia que deseas consultar")).lower()
#     if opcion in dias_servicio :
#         print("hay servicio el dia")
#     else: 
#         print(F"no hay servicio el dia {opcion}")

# # 5

# def reserva(validar):
#     if validar == True :
#         return "reservado"
#     else :
#         return "no reservado"

# hotel = {
#     "phouse" : {
#         "numero_habitacion" : 1 ,
#         "precio" : 44000 ,
#         "reservado" : False ,
#         "persona" : "" ,
#         "capacidad" : "5"
#     },

#     "presidencial" : {
#         "numero_habitacion" : 2 ,
#         "precio" : 30500 ,
#         "reservado" : True ,
#         "persona" : "alfonso" ,
#         "capacidad" : "3"
#     },

#     "pool-bed" : {
#         "numero_habitacion" : 3 ,
#         "precio" : 23000 ,
#         "reservado" : False ,
#         "persona" : "" ,
#         "capacidad" : "3"
#     },

#     "sencilla" : {
#         "numero_habitacion" : 4 ,
#         "precio" : 15000 ,
#         "reservado" : False ,
#         "persona" : "" ,
#         "capacidad" : "2"
#     },

#     "ultra-mega sencilla" : {
#         "numero_habitacion" : 5,
#         "precio" : 5000 ,
#         "reservado" : True ,
#         "persona" : "brandon" ,
#         "capacidad" : "1"
#     }

# }

# while True:
#     print("""
#         que deseas hacer?
#         (1) reservar habitacion 
#         (2) cancelar reserva 
#         (3) consultar habitacion
#     """)
#     opcion = str(input("elige tu opcion"))
#     match opcion:
#         case 1:
#             print("habitaciones")
#             for habitacion in hotel :
#                 if habitacion["reservado"] == False:
#                     print(F"nombre:{habitacion} numero de habitacion: {habitacion["numero_habitacion"]} capacidad de habitacion:{habitacion["capacidad"]}")
#                 else :
#                     continue
#             opcion = str(input("que habitacion deseas reservar"))
#             nombre = str(input("a nombre de quien deseas reservar"))
#             hotel[opcion].update({"reservado" : True} , {"persona" : nombre })
#         case 2:
#             print("habitaciones")
#             for habitacion in hotel :
#                 if habitacion["reservado"] == True:
#                     print(F"nombre:{habitacion} numero de habitacion: {habitacion["numero_habitacion"]} capacidad de habitacion:{habitacion["capacidad"]}")
#                 else :
#                     continue
#             opcion = str(input("que habitacion deseas cancelar su reservacion?"))
#             habitacion[opcion].update({"reservado" : False}, {"persona" : ""})
#         case 3:
#             print("habitaciones")
#             for habitacion in hotel :
#                 print(F"nombre:{habitacion} estado: {reserva(habitacion["reservado"])}")
#             opcion = str(input("escribe la habitacion que deseas consultar"))
#             for habitacion in hotel[opcion] :
#                 print(habitacion)


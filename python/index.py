# ejercicio1


# def calculadora(num_uno, num_dos):

#  operador = int(input("elige una ona opcion: 1 para salir,1 sumar , 2 restar , 3 multiplicar ,4 dividir "))

#  while operador > 0:
#     total = 0
#     match operador:
#       case 0:
#         break
#       case 1:
#         total = num_uno+num_dos
#         print(total)
#         break
#       case 2:
#         total = num_uno-num_dos
#         print(total)
#         break
#       case 3:
#         total = num_uno*num_dos
#         print(total)
#         break
#       case 4:
#         total = num_uno/num_dos
#         print(total)
#         break
# calculadora(12,123)


# ejercicio2

# suma = 0

# while empleado < 6:
#     empleado = float(input("dame el numero del monto"))
#     suma += empleado

#     if empleado >= 1000000:
#         print("su comision es del 15%")
#     elif empleado >= 5000 and  empleado < 1000000:
#         print("su comision es del 5%")
#     elif empleado < 5000:
#         print("0 comision")
#     else:
#         break

# ejercicio3

# coverciones = 0
# suma_de_canversiones = 0
# while True:
#     dolar = float(input("ingrese los dolares a convertir"))
#     peso = 4900

#     convercion = dolar * peso 
#     print("resultado es " ,  convercion)

#     coverciones += 1
#     print("suma de converciones es", coverciones)

#     suma_de_canversiones += convercion
#     print("suma de converciones es", suma_de_canversiones)

#     opcion = input("elige una opcion de a para seguir c para cerrar")
     
#     if opcion == "a":
#         continue
#     elif opcion =="c":
#         break
#     else:
#         pass



# ejercicio4



# valor_bruto = 0
# IVA = 0
# valor_neto = 0

# productos = int(input("dame el numero de productos"))
# for i in range(productos):
#     nombre_del_producto = input("nombre del producto")
#     precio_unitario = int(input("dame el precio"))
#     cantidad_de_productos = int(input("cantidad de productos "))
#     valor_total = cantidad_de_productos*precio_unitario
#     print('el valor total del producto es de ', valor_total)

#     valor_bruto += valor_total
#     IVA = valor_bruto*0.19
#     valor_neto = valor_bruto + IVA

# print("fatura de compra")
# print("producto" , nombre_del_producto)
# print("precio unitario", precio_unitario)
# print("cantidad de productos",cantidad_de_productos)
# print("IVA",IVA)
# print("valor bruto", valor_bruto)
# print("valor neto", valor_neto)

# ejercicio5

# vocales = ['a','e','i','o','u']
# cadena = str(input("escribe el texto: "))
# contador = 0

# for vocal in vocales:
#     for texto in cadena:
#         if vocal == texto:
#             contador +=1 

# print("la cadena tiene " , contador,"vocales")



# ejercicio6
# minutos = [] #arrays de los minutos 
# def calcular_tiempos(minutos): #fun para ordenar los numero y encontrar el mayor y el menor
#     #inici de variables  
#     mayor = 0
#     menor = 0

#     minutos.sort(reverse = True) #esto ordena 
#     #esto encuentra el mayor y el menor con las posiciones del array 
#     print("el mayor tiempo mayor es ",minutos[0])
#     print("el menor tiempo mayor es ",minutos[-1])
# #esto piede el numero de ciclistas 
# numero_ciclistas = int(input("dame el numero de ciclistas: "))
# #esto para pedir los tiempos de los cilistas
# for ciclista in range(1,numero_ciclistas + 1):
    
#     print("tiempo ciclista: ",ciclista )
#     tiempo = int(input("dame el tiempo de demora de cada ciclista: "))
#     minutos.append(tiempo) # esto agraga al array

# calcular_tiempos(minutos) #llama a la funcion 





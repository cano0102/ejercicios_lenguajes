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





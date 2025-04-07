import random
banco = []

def registrar_usuario():
    usuario = {}

    nombre = str(input("Dame tu nombre: "))
    usuario["nombre"] = nombre

    cuenta = random.randint(10000,20000)
    usuario["cuenta"] = cuenta

    saldo_inicial = float(input("dame tu saldo inicial: "))
    usuario["saldo_inicial"] = saldo_inicial

    banco.append(usuario)

def menu():
    print("---DAME UNA OPCION---")
    print("1.Para registrarse")
    print("2.Para consultar saldo")
    print("3.Para realizar algun movimiento")
    print("4.Para ver todos los clientes")
    print("5.Para generar un reporte")
    print("6.Para salir")


def consultar():
    numero_de_cuenta = int(input("Dame el numero de cuenta:"))
    for cuenta in banco:
        if  numero_de_cuenta == cuenta[1] :
            print("tu cuneta si esta")
        else:
            print("tu cuneta no esta")

def movimientos():
    cuenta_cliente = int(input("Dame el tumero de tu cuenta"))
    depositar_o_retirar = int(input("1 para deposirar 2 para retirar: "))
    if depositar_o_retirar == 1:
        for clientes in banco:
            if clientes["cuentas"] == cuenta_cliente:
                depositar = int(input("dame el monto a depositar: "))
                deposito = clientes["saldo_inicial"] + depositar
                clientes.update()
                print(deposito)
    elif depositar_o_retirar == 2:
        for client in banco:
            if client["cuentas"] == cuenta_cliente:
                retiro = int(input("dame el monto a retirar: "))
                retirado  = client["saldo_inicial"] - retiro
                client.update()
                print(retirado)
        


def mostrar():
    for clientes in banco:
        print(clientes)

def reporte():
    pass

while True:
    menu()
    opcion = int("DAME UNA OPCION: ")
    if opcion == 1:
        registrar_usuario()
    elif opcion == 2:
        consultar()
    elif opcion == 3:
        movimientos()
    elif opcion == 4:
        mostrar()
    elif opcion == 5:
        reporte()
    elif opcion == 6:
        print("gracias")
        break
    else:
        print("opcion invalida")
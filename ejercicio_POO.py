class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años"

class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, salario):
        super().__init__(nombre, apellido, edad)
        self.salario = salario

    def __str__(self):
        return super().__str__() + f", Salario: ${self.salario}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, direccion):
        super().__init__(nombre, apellido, edad)
        self.direccion = direccion

    def __str__(self):
        return super().__str__() + f", Dirección: {self.direccion}"

class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f"{self.titulo} de {self.autor}, Precio: ${self.precio}"

class Libreria:
    def __init__(self):
        self.empleados = []
        self.clientes = []
        self.libros = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)


libreria = Libreria()

empleado1 = Empleado("Juan", "Pérez", 30, 50000)
empleado2 = Empleado("María", "González", 25, 40000)

cliente1 = Cliente("Carlos", "López", 35, "Calle 123")
cliente2 = Cliente("Ana", "Martínez", 28, "Avenida 456")

libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 200)
libro2 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", 150)


libreria.agregar_empleado(empleado1)
libreria.agregar_empleado(empleado2)
libreria.agregar_cliente(cliente1)
libreria.agregar_cliente(cliente2)
libreria.agregar_libro(libro1)
libreria.agregar_libro(libro2)


print("Empleados:")
libreria.mostrar_empleados()
print("\nClientes:")
libreria.mostrar_clientes()
print("\nLibros:")
libreria.mostrar_libros()
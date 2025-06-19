Ejercicio 1: Crear una clase simple 
Crea una clase Persona con propiedades nombre y edad, y un método saludar() que muestre un mensaje en consola.

Ejercicio 2: Constructor con parámetros 
Modifica la clase Persona para que el constructor reciba nombre y edad como argumentos.

Ejercicio 3: Crear múltiples instancias 
Crea tres instancias diferentes de la clase Persona con distintos valores y llama al método saludar() desde cada una.

Ejercicio 4: Método estático 
Agrega a la clase Persona un método estático esMayorDeEdad(edad) que retorne true si la edad es 18 o más, y false en caso contrario.

Ejercicio 5: Herencia
Crea una clase Estudiante que herede de Persona y tenga una propiedad adicional curso. Agrega un método presentarse() que incluya el nombre, edad y curso.

Ejercicio 6: Encapsulamiento
Modifica la clase Persona para que edad sea una propiedad privada (usando #edad) y crea métodos getEdad() y setEdad() para acceder y modificarla.

Ejercicio 7: Uso de super()
En la clase Estudiante, usa super(nombre, edad) dentro del constructor para inicializar los valores heredados de Persona.

Ejercicio 8: Clase con array de objetos
Crea una clase Curso que tenga un nombre y un arreglo de estudiantes (Estudiante). Agrega un método agregarEstudiante(est) para añadir estudiantes y otro listarEstudiantes() que imprima sus nombres.

Ejercicio 9: Método que recorra propiedades
Crea un método mostrarInfo() en la clase Persona que recorra sus propiedades (usando for...in) e imprima sus valores.

Ejercicio 10: Composición de objetos
Crea una clase Direccion con propiedades calle y ciudad, y agrégala como propiedad dentro de la clase Persona. Luego, imprime la dirección completa desde un método.

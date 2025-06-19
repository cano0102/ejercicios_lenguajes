// Ejercicio 1: Crear una clase simple 
// Crea una clase Persona con propiedades nombre y edad, y un método saludar() que muestre un mensaje en consola.



class Persona {

    // Ejercicio 6: Encapsulamiento
   // Modifica la clase Persona para que edad sea una propiedad privada (usando #edad) y crea métodos getEdad() y setEdad() para acceder y modificarla.

    #nombre; 
    #edad;
    // Ejercicio 2: Constructor con parámetros 
   // Modifica la clase Persona para que el constructor reciba nombre y edad como argumentos.
    constructor(nombre = "",edad = null) {

        this.#nombre = nombre;
        this.#edad = edad
    }
    
    saludar() {
        console.log(`hola ${this.#nombre}`)
    }

    getNombre() {
        return this.#nombre;
    }




    getEdad() {
        return this.#edad;
    }


     // Ejercicio 4: Método estático 
    // Agrega a la clase Persona un método estático esMayorDeEdad(edad) que retorne true si la edad es 18 o más, y false en caso contrario.

    static MayorDeEdad() {

        let edad = this.edad
        let mensaje = edad >= 18 ? "Eres mayor de edad" : "Eres menor de edad";
        console.log(mensaje);



    }

    //     Ejercicio 9: Método que recorra propiedades
    // Crea un método mostrarInfo() en la clase Persona que recorra sus propiedades (usando for...in) e imprima sus valores.

    mostrarInfo() {
        let datos = { nombre: this.#nombre, edad: this.#edad };
        for (const clave in datos) {
            console.log(`${clave}: ${datos[clave]}`);
        }
    }
}
    




// Ejercicio 3: Crear múltiples instancias 
// Crea tres instancias diferentes de la clase Persona con distintos valores y llama al método saludar() desde cada una.

let anderson =  new Persona("anderson",19);
anderson.saludar();
console.log(anderson.MayorDeEdad())

let brandon =  new Persona("brandon",19);
brandon.saludar();
console.log(brandon.MayorDeEdad())

let steven =  new Persona("steven",18);
steven.saludar();
console.log(steven.MayorDeEdad())

let valery =  new Persona("valery",17);
valery.saludar();
console.log(valery.MayorDeEdad())

let mateo =  new Persona("mateo",17);
valery.saludar();
console.log(mateo.MayorDeEdad())



// Ejercicio 5: Herencia
// Crea una clase Estudiante que herede de Persona y tenga una propiedad adicional curso. Agrega un método presentarse() que incluya el nombre, edad y curso.


class Estudiante extends Persona {
    #curso;
    constructor(nombre,edad,curso) {
        
        // Ejercicio 7: Uso de super()
        // En la clase Estudiante, usa super(nombre, edad) dentro del constructor para inicializar los valores heredados de Persona.

        super(nombre,edad)
        this.#curso = curso
    }
    presentarse(){
        
        console.log(`Hola mi nombre ${this.getNombre}, tengo ${this.getEdad} años de edad y estoy en el curso ${this.#curso}`)
    }
}


let gordo = new Estudiante("carlos", 17, "tecnoligia de Software");

gordo.presentarse();
gordo.saludar();     
console.log(gordo.verificarEdad());



// Ejercicio 8: Clase con array de objetos
// Crea una clase Curso que tenga un nombre y un arreglo de estudiantes (Estudiante). Agrega un método agregarEstudiante(est) para añadir estudiantes y otro listarEstudiantes() que imprima sus nombres.


// let Estudiantes = [
//     new Estudiante("Carlos", 17, "Tecnología de Software"),
//     new Estudiante("Anderson", 19, "Tecnología de Software"),
//     new Estudiante("Brandon", 19, "Tecnología de Software"),
//     new Estudiante("Steven", 18, "Tecnología de Software"),
//     new Estudiante("Valery", 17, "Tecnología de Software"),
//     new Estudiante("Mateo", 17, "Tecnología de Software")
// ]

class Curso {
    #nombre;
    #estudiante;
    constructor(nombre) {
        this.#nombre = nombre
        this.estudiantes = []

    }
    agregarEstudiante(){
        if (!(est instanceof Estudiante)) {
            throw new TypeError("Se esperaba una instancia de Estudiante");
        }
        this.estudiantes.push(est);
    }

    listaDeEstudiantes(){
        
        for (let i = 0; i < this.estudiantes.length; i++) {
            console.log(i)
            
        }
    }
}



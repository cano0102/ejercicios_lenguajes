// Crea un programa que compare dos edades ingresadas por el usuario y determine cuál persona es mayor, o si tienen la misma edad.

// function edades(edad1,edad2) {

//     if (edad1 >= edad2) {
        
//         console.log("el mayor es " . edad1)
        
//     }else{
//         console.log("el mayor es " , edad2)
//     }
    
// }

// edades(12,34)

//   Escribe un programa que tome un número entero ingresado por el usuario y determine si es par o impar.


// function par(x) {
    
    
//     if( x%2==0 ){
//         console.log("EL NUMERO ES PAR")
//     }else{
//         console.log("EL NUMERO ", x , "ES IMPAR")
    
//     }
// }

// par(3)


// Crea un programa que tome una temperatura en grados Celsius y determine si está en un rango bajo (menor de 10°C), medio (entre 10°C y 30°C), o alto (mayor de 30°C).


// function temperatura(a) {
//     if (a < 10) {
//             console.log("RANGO BAJO")
//     } else {
//         if (a >= 10 && a < 30) {
//             console.log("RANGO MEDIO ")
//         }else{
//             if (a >= 30) {
//                 console.log("RANGO ALTO")
//             } else {
//                 console.log("error")
//             }
//         }
//     }
// }
// temperatura(20)



// Escribe un programa que pida al usuario ingresar una contraseña y verifique si coincide con una contraseña predefinida. Si la contraseña es incorrecta, pide que la ingrese nuevamente hasta que sea correcta.
// function contraseña(a) {
    

//     while (true) {
        
//         if (a == "hola") {
//             console.log("bienvenido")
//             break
//         } else {
            
//             console.log("ingresa la contraseña de nuevo")
//         }
//     }
    
    
// }


// contraseña("hola")


// Crea un programa que tome una calificación numérica (entre 0 y 100) e imprima la letra correspondiente (A, B, C, D, o F) según una escala predeterminada.



// function calificacion(notas) {
//     if (notas > 0 && notas <= 20) {
//         console.log("tienes una F")
//     }
//     if (notas > 20 && notas <= 40) {
//         console.log("tienes una D")
//     }
//     if (notas > 40 && notas <= 60) {
//         console.log("tienes una C")
//     }
//     if (notas > 60 && notas <= 80) {
//         console.log("tienes una B")
//     }
//     if (notas > 80 && notas <= 100) {
//         console.log("tienes una A")
//     }
    
    
    
// }


// calificacion()



// Escribe un programa que tome las longitudes de tres lados de un triángulo y determine si forman un triángulo válido


// function triangulo(a = 0, b = 0, c = 0) {
//     if (a + b > c && a + c > b && b + c > a) {
//         console.log("triángulo válido");
//     } else {
//         console.log("no es válido el triángulo");
//     }
// }

// Crea un programa que actúe como una calculadora simple. El usuario debe ingresar dos números y una operación (+, -, *, /). El programa debe devolver el resultado de la operación indicada.

// function calculadora(operador,a,b) {
//     let total
//     switch (operador) {
//         case '+':
//             total = a+b 
//             console.log(total)
//             break;
//         case '-':
//             total = a-b 
//             console.log(total)
//             break
//         case '*':
//             total = a*b 
//             console.log(total)
//             break
//         case '/':
//             total = a/b 
//             console.log(total)
//             break
//         case '**':
//             total = a**b 
//             console.log(total)
//             break

//         default:
//             console.log("operador no valido")
//             break;
//     }
// }

// calculadora()


// Escribe un programa que tome un año como entrada y determine si es un año bisiesto o no. Recuerda que un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.

// function añoBisiesto(año) {
    
//     if (año%4==0 && año%100!==0) {
//         console.log("año  es bisiesto")
//     }else{

//         if (año%4==0 && año%100==0 && año%400==0 ) {
//             console.log("año es bisiesto")
//         }else{
//             console.log("no es bisiesto")
//         }
//     }
// }

// añoBisiesto(2016)
// Crea un programa que tome un carácter ingresado por el usuario y determine si es una vocal, una consonante, un número, o un carácter especial.


// function letra(a) {
//     if (typeof a == Number  ) {
//         console.log("tu caracter es un numero ")
//     }else {
//         if (typeof a == String) {
//             if ( a == "a" || a == "e" || a == "i" || a == "o"|| a == "u" ) {
//                 console.log("tu caracter es un vocal ")
//             } else {
//                 console.log("es una consonante")
//             }
//         }else{
//             console.log("carácter especial")
//         }
        
        
//     }
// }
// letra("a")

// // Escribe un programa que tome tres números como entrada y los ordene de mayor a menor sin utilizar funciones de ordenamiento.

// function ordenar(a,b,c) {
    
//     if (a > b && a > c ) {
//         if ( b> c) {
//             console.log( a,b,c)
//         }else{
//             console.log( a,c,b)
//         }
        

//     }else{
//         if (b > a && b > c ) {
//             if ( a> c) {
//                 console.log( b,a,c)
//             }else{
//                 console.log( b,c,a)
//             }
            
    
//         }  if (c > a && c > b ) {
//             if ( b> a) {
//                 console.log( c,b,a)
//             }else{
//                 console.log( c,a,b)
//             }
            
    
//         }
//     }
// }

// ordenar()


//ciclos

// Crea un programa que imprima los números del 1 al 10 en la consola.



// function numeros(a) {

//     for (let i = 1; i <= a ; i++) {
        
//         console.log(i)
        
//     }

// }

// numeros(10)

// Escribe un programa que calcule la suma de todos los números del 1 al 100.


// // function numeros(a) {

// //     suma = 0;


// //     for (let i = 1; i <= 100; i++) {
        
// //         suma += i

// //     }
// //     console.log(suma)

// // }


// // numeros()


// Crea un programa que cuente cuántos números pares hay entre 1 y 50


// function numeros(a) {

//     suma = 0;


//     for (let i = 1; i <= 50; i++) {

//         if (i%2==0) {
//             suma += i
//             console.log(suma)

            
//         }
        
        

//     }
//     console.log()

// }


// numeros()



// Escribe un programa que calcule el factorial de un número ingresado por el usuario.


// function calcularFactorial(a) {
    
//     let contador = 1;
//     for (let i = 1; i <= a ; i++) {


//         contador *= i
        
        
//     }
//     console.log(contador)
// }

// calcularFactorial(20)


// Escribe un programa que imprima todos los números primos entre 1 y 50.

// function NumerosPrimos(num) {

//     if (num <=1) {
//         return false
//     }

//     if (num === 2) {
//         return true
//     }

//     if (num%2==0) {
//         return false
//     }


//     for (let i = 0; i <= 50; i++) {

//         console.log(i)
        
//     }

//     return true
    
// }

// numero = 32

// if (NumerosPrimos(numero) ) {
    
//     console.log("es numero primo")
// } else {
//     console.log("no es numero primo")
// }


// Crea un programa que tome un número entero ingresado por el usuario e imprima el número en orden inverso. Por ejemplo, si el número ingresado es 1234, el programa debe imprimir 4321.


// function alReves(a) {
//     for (let i = a; i >1; i--) {
//         console.log(i)
        
//     }
// }


// Escribe un programa que imprima los primeros n términos de la secuencia de Fibonacci, donde n es un número ingresado por el usuario. 

// investigada

// function secuencia(num) {
//     let a = 0, b = 1;

//     for (let i = 0; i < num; i++) {
        
        
//         c = a + b
//         a = b;
//         b = c
//         console.log(b)
        
//     }
// }


// secuencia(5)


// Crea un programa que determine si un número ingresado por el usuario es un número perfecto. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo el propio número).

function SumaDivisores() {
    
    for (let i = 0; i < array.length; i++) {
        
        console.log(i)
        
    }
}




// Escribe un programa que tome un número n ingresado por el usuario y dibuje una pirámide de asteriscos con n filas. Por ejemplo, si n es 5, la salida debe ser:

//    *
//   ***
//  *****
// *******



// Crea un programa que imprima una serie de potencias de 2, desde 2^0 hasta 2^n, donde n es un número ingresado por el usuario.



// Escribe un programa que tome un número entero ingresado por el usuario y determine si es un palíndromo (un número que se lee igual al derecho y al revés).


// Crea una función que tome el nombre de una persona como argumento y devuelva un saludo personalizado, por ejemplo, "Hola, [nombre]".
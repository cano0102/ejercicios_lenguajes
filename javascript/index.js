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

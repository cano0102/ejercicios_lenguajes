// 1. Lea dos números y calcule el resultado de su suma, resta, multiplicación y división.


function suma(num1,num2) {
    
    return num1 + num2


}

suma()


// 2. Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura.

function promedio_notas(notas=0) {
    


    let todas_las_notas = []

    
    for (let i = 0; i < notas; i++) {
        
        let nota = Number(prompt("DAME UNA NOTA:",(i + 1)));
        todas_las_notas.push(nota)

    }

    let suma = todas_las_notas.reduce((a, b) => a + b, 0)
    console.log("LA SUMA DE TODAS LAS NOTAS ES " + suma)


    let promedio = suma / notas

    console.log( `el promedio de las notas  ${promedio}`)
        

}


// 3. Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura si la primera nota
// tiene un valor del 20%, la segunda del 30% y la última del 50%.


function PromedioDeNotas(num1,num2,num3) {
    
    let porcentaje_de_num1 = (num1 * 20) / 100 
    let porcentaje_de_num2 = (num2 * 30) / 100 
    let porcentaje_de_num3 = (num3 * 50) / 100 

    let promedio = porcentaje_de_num1 + porcentaje_de_num2 + porcentaje_de_num3
    
    

    console.log(`el pormedio de las notas es ${promedio}`)
    
}

PromedioDeNotas()



// 4. Lea la distancia (en kilómetros) recorrida por un auto, el tiempo (en horas) en que la recorrió
// y calcule la velocidad a la cual se desplazaba el auto (V=D/T).



function Kilometros(distancia,tiempo) {

    distancia = Number(prompt("DAME LA DISTANCIA RECORRICADA DEL VEHICULO:"));
    tiempo= Number(prompt("DAME LA CONTIDAD DE TIEMPO  DEL VEHICULO:"));

    let velocidad = distancia / tiempo

    console.log(`LA VALOCIDAD DEL VEHICULO ERA DE ${velocidad}`)



    
}


Kilometros()


// 5. Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), y
// el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10%
// (antes de aplicarle el IVA).




function calcular(valor) {
    
    
    valor = parseFloat(prompt("Ingrese el valor de la compra:"));

    let descuento = (valor * 10) / 100

    

    const iva = 0.19
    let SubTotal1 =  valor - descuento
    let SubTotal2 = SubTotal1 * iva

    Total =  SubTotal1 + SubTotal2

    console.log(`el valor de la compra es ${Total}`)

}


calcular()


// 6. Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos
// equivale.

function SegundosTotales() {

    let Horas  = Number(prompt("Ingrese la hora:"));
    let Minutos =  Number(prompt("Ingrese los minutos:"));
    let Segundos =  Number(prompt("Ingrese los segundos:"));
     
    let TotalDeHoras = Horas * 3600 
    let TotalDeMinutos = Minutos * 60

    let TotalDeSegundos = TotalDeHoras + TotalDeMinutos + Segundos

    console.log(`el total de los segundos es ${TotalDeSegundos}`)






}
SegundosTotales()



// 7. Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero
// ganará después de un mes si el banco paga a razón de 2% mensual.


function Banco() {
    Capital =   parseFloat(prompt("Ingrese su capital:"));

    let PorcentajeMensual = ( Capital * 2 ) / 100

    console.log(`el porcentaje mensual es de ${PorcentajeMensual}`)

}


Banco()

// 8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor
// desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que
// realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y
// comisiones.


function Comisiones() {

    let Sueldo =   parseFloat(prompt("Ingrese tu sueldo:"));
    let ComisionesDelMes =  Number(prompt("Ingrese el valor de las ventas del mes:"));
    let TotalDeComisiones = (ComisionesDelMes * 10) / 100
    let TotalDeSueldo = Sueldo + TotalDeComisiones
    
    console.log(`el total del sueldo que debes de recibir es : ${TotalDeSueldo}`)
}

Comisiones()


// 9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
// cuánto deberá pagar finalmente por su compra. 


function CompraTienda() {
    
    let Compra =   parseFloat(prompt("Ingrese el valor de tu compra:"));


    let TotalDescuento = (Compra * 15) / 100
    let Total = Compra - TotalDescuento

    console.log(`el total de la cuenta es  ${Total}`)

    
}

CompraTienda()

// 10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha
// calificación se compone de los siguientes porcentajes:
// 55% del promedio de sus tres calificaciones parciales.
// 30% de la calificación del examen final.

// 15% de la calificación de un trabajo final



function PromedioDeNotas() {
    
    let NotaParcial  =   parseFloat(prompt("Ingrese  el promedio de sus tres calificaciones parciales :"));
    let NotaExamen =  parseFloat(prompt("Ingrese  la calificación del examen final :"));
    let NotaProyectoFinal =  parseFloat(prompt("Ingrese la calificación del trabajo final  :"));
    
    NotaParcial = (NotaParcial * 55) / 100
    NotaExamen = (NotaExamen * 30) / 100
    NotaProyectoFinal = (NotaProyectoFinal * 15) / 100


    let total = (NotaProyectoFinal + NotaExamen + NotaParcial) 


    console.log(`el promedio de tu asignatura es ${total}`)


}

PromedioDeNotas()


// 11. Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un
// grupo de alumnos.


function PorcentajesDeAlumnos() {
    

    let Estudiantes = parseInt(prompt("DAME EL NUMERO DE ESTUDIANTES : "))
    let Hombres = parseInt(prompt("DAME EL NUMERO DE HOMBRES: "))

    let PorcentajesDeHombres = (Hombres / Estudiantes) * 100
    let Mujeres = Estudiantes - Hombres
    let PorcentajesDeMujeres = (Mujeres / Estudiantes) * 100

    console.log(`El PORCENTAJE DE LOS ES DE LOS HOMBRES ${PorcentajesDeHombres} Y EL PORCENTAJE DE LAS MUJERES ${PorcentajesDeMujeres}`)
    
    
}

PorcentajesDeAlumnos()


// 12. Dada las horas trabajadas de una persona y el valor por hora. Calcular su salario e imprimirlo.


function  HorasTrabajadas() {


    let Horas = parseFloat(prompt("Dame las horas trabajadas"));
    let ValorDeHora = parseInt(prompt("Dame las horas trabajadas"));

    let TotalSalario = Horas * ValorDeHora

    console.log(`El sulto tuyo es de ${TotalSalario}`)


    
}

HorasTrabajadas()


// 14. Suponga que tiene Ud. una tienda y desea registrar las ventas en una computadora. Diseñe
// un algoritmo en pseudocódigo que lea por cada cliente:

// ● El monto de la venta, calcule e imprima el IVA.
// ● calcule e imprima el total a pagar
// ● lea la cantidad con la que paga el cliente (solo efectivo), calcule e imprima el cambio. 2


function TotalAPagar() {

    let TotalDeProductos = parseFloat(prompt("DAME EL VALOR DE LOS PRODUCTOS"))

    const iva = 0.19

    let SubTotalIva = (TotalDeProductos * iva) 

    let Total = TotalDeProductos + SubTotalIva

    console.log(`EL TOTAL A PAGAR ES : ${Total}`)


    let PagoCliente =  parseInt(prompt("DAME EL DIMERO A PAGAR"))

    let CambioCliente = PagoCliente - Total
    console.log(`TU CAMBIO ES ${CambioCliente}`)
    
}














// 15. Suponga que un conductor le pide a usted que le haga un algoritmo para calcular cuánto le
// corresponde en un día trabajado, teniendo en cuenta que tiene derecho a el 19% del total
// recaudado.

function Conductor() {
    
    let recaudado = parseFloat(prompt("DAME LO RECAUDADO"))
    let porcentaje = 19

    let total = (recaudado * porcentaje) / 100
    
    console.log(`LO QUE TE CORRESPONDE ES ${total}`)

}



// 16. Desarrollar un algoritmo que permita generar la colilla de pago de los empleados de una
// empresa. La colilla debe mostrar:

// ● El Salario del Empleado
// ● El Valor de Ahorro mensual programado.
// ● La suma a deducir por aporte a la Salud (EPS) 12,5 %
// ● La suma a deducir por aporte al Fondo de Pensiones 16%
// ● Total a Recibir
// ● Toda la información que debe proveer el usuario del programa es el Salario del

// Empleado y el Valor de Ahorro mensual programado. El programa debe calcular y
// devolver el resto de los datos.



function Sueldo() {

    let Salario = parseFloat(prompt("DAME EL SALARIO"));
    let Ahorro = parseFloat(prompt("DAME EL AHORRO MENSUAL PROGRAMADO"));

    let SueldoConAhorro = Salario - Ahorro;

    let Salud = 12.5;
    let SaludSalario = (Salario * Salud) / 100;

    let Pension = 16;
    let PensionSalario = (Salario * Pension) / 100;

    let total = SueldoConAhorro - SaludSalario - PensionSalario;

    console.log("----- COLILLA DE PAGO -----");
    console.log("SALARIO DEL EMPLEADO: $" + Salario);
    console.log("AHORRO MENSUAL PROGRAMADO: $" + Ahorro);
    console.log("DESCUENTO POR SALUD (12.5%): $" + SaludSalario);
    console.log("DESCUENTO POR PENSIÓN (16%): $" + PensionSalario);
    console.log("TOTAL A RECIBIR: $" + total);
}

Sueldo()



// 17. En una universidad los estudiantes pueden pagar el valor de su matrícula en cuatro cuotas de
// la siguiente forma

// ● Primera cuota: 40%
// ● Segunda cuota: 25%
// ● Tercera cuota: 20%
// ● Cuarta cuota: 15%

// Diga cuanto es el valor que tiene que pagar por cuota un estudiante.

function Universidad() {
    
    let Matricula = parseFloat(prompt("Dame el valor de tu matrícula"))

    let PorcentajePrimeraCuota = (Matricula * 40) / 100
    let PorcentajeSegundaCuota = (Matricula * 25) / 100
    let PorcentajeTerceraCuota = (Matricula * 20) / 100
    let PorcentajeCuartaCuota = (Matricula * 15) / 100

    console.log(`El valor de tu primera cuota es: ${PorcentajePrimeraCuota} `)
    console.log(`El valor de tu segunda cuota es: ${PorcentajeSegundaCuota} `)
    console.log(`El valor de tu tercera cuota es: ${PorcentajeTerceraCuota} `)
    console.log(`El valor de tu cuarta cuota es: ${PorcentajeCuartaCuota} `)

}


// 18. Ingresar, para un estudiante, sus 5 notas de un curso, nombre, programa, ficha.
// Hacer un algoritmo que:

// • Muestre el nombre
// • Muestre el programa de formación
// Se debe calcular y mostrar su promedio final.



function PromedioDeNotas() {
    let CantidadDeNotas = 5
    let notas = []

    for (let i = 0; i < CantidadDeNotas; i++) {
        let nota = parseFloat(prompt(`DAME LA NOTA: ${i + 1}`))
        notas.push(nota)
    }

    let suma = notas.reduce((a, b) => a + b, 0)
    let promedio = suma / CantidadDeNotas
    return promedio
}

function datos() {
    let nombre = prompt("DAME EL NOMBRE DEL ESTUDIANTE")
    let programa = prompt("DAME EL NOMBRE DEL PROGRAMA") 
    let ficha = parseInt(prompt("DAME EL NUMERO DE FICHA"))

    let estudiante = {
        nombre: nombre,
        programa: programa,
        ficha: ficha,
        promedioNota: PromedioDeNotas()
    }

    console.log("Datos del estudiante:")
    console.log(estudiante)
}

datos()




// 19. Ingresar el precio de compra unitario de un producto y la cantidad de compra de
// dicho producto y un descuento. Calcular y mostrar el subtotal, el monto del IVA
// que es el 19% del subtotal, y el precio neto (precio parcial con el Monto del IVA).

function comparas() {

    let PrecioDeUnidades = parseFloat(prompt("DAME EL PRECIO DE LA UNIDAD:"));
    let CantidadDeUnidades = parseFloat(prompt("DAME LA CANTIDAD DE UNIDADES:"));
    let Descuento = parseInt(prompt("DAME EL DESCUENTO EN %:"));
    const iva = 0.19;

    let TotalBruto = PrecioDeUnidades * CantidadDeUnidades;

    let MontoDescuento = (TotalBruto * Descuento) / 100;
    let TotalConDescuento = TotalBruto - MontoDescuento;

    let MontoIVA = TotalConDescuento * iva;
    let TotalFinal = TotalConDescuento + MontoIVA;

    
    
    console.log("Precio unitario: $" + PrecioDeUnidades);
    console.log("Cantidad: " + CantidadDeUnidades);
    console.log("Subtotal (sin descuento): $" + TotalBruto);
    console.log("Descuento (" + Descuento + "%): -$" + MontoDescuento);
    console.log("Subtotal con descuento: $" + TotalConDescuento);
    console.log("IVA (19%): $" + MontoIVA);
    console.log("TOTAL A PAGAR: $" + TotalFinal);
}



// 20. Realice un algoritmo que permita realizar el cálculo del siguiente enunciado, se
// solicita el año de nacimiento del aprendiz, el nombre, la dirección, se requiere
// conocer la edad de la persona y la información completa ingresada.


function CálculoEdad() {
    
    let AñoDeNacimiento = parseInt(prompt("DAME TU AÑO DE NACIMIENTO"))
    let Nombre = prompt("DAME TU NOMBRE")
    let direccion =  prompt("DAME TU DIRECCION")

    let edad =   2025 - AñoDeNacimiento

    Estudiantes = {
        "edad": edad,
        "nombre" : Nombre,
        "direccion" : direccion
    }

    console.log(Estudiantes)




}



// 21. Se tienen tres baldes de agua, uno de cinco litros, otro de tres litros y otro de un
// litro; si el de un litro tarda una hora y media en llenarse, resuelva cuanto tiempo
// pueden tardar en llenarse los otros baldes.

// Si tiene tres baldes, pero se desconoce su tamaño debe de resolver igualmente el
// ejercicio.


function baldes() {
    
    hora = 90
    let Balde1 =  1
    let Balde3  = 3
    let Balde5 = 5

    let totalbalde1 = Balde1 * hora
    let totalbalde3 = Balde3 * hora
    let totalbalde5 = Balde5 * hora

    console.log(`el balde de 1 litro demora ${totalbalde1} , el balde de 3 litro demora ${totalbalde3}, el balde de 5 litro demora ${totalbalde5}`)

    
}


// 22. Una persona tarda 5 horas en subir una montaña de 7 metros, si un escalador
// desea subir más o menos de la montaña, cuanto tiempo tarda en subir. Debe de
// resolver el ejercicio.



function EscalarMontaña() {
    
    let MetroAsubir =  Number(prompt("DAME EL NUMERO DE METROS QUE DESEAS SUBIR"))
    
    let tiempo =  42.85
    
    
    let TiempoEstimado = MetroAsubir * tiempo

    console.log(`EL TIEMPO ESTIMO PARA SUBIR ${MetroAsubir} METROS ES ${TiempoEstimado}`)
}


EscalarMontaña()








// 23. Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de
// interés es del 5% anual, se debe solicitar el monto del préstamo y se desea
// calcular la siguiente información.

// • • Cuanto dinero se ha pagado de intereses en un año.
// • • Cuanto dinero se ha pagado de intereses en el tercer trimestre del año.
// • • Cuanto dinero se ha pagado de intereses en el primer mes.
// • • Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses.


function CalcularInterecesDuranteUnAño() {

    
    let MontoAPrestar = parseFloat(prompt("DAME EL MONTO QUE DESEAS PRESTAR: "));
    let interes = 5; 

   
    let porcentajeDePrestamo = (MontoAPrestar * interes) / 100;

    
    let trimestre = interes / 4;
    let interesTercerTrimestre = (MontoAPrestar * trimestre) / 100;

    
    let mensual = interes / 12;
    let interesPrimerMes = (MontoAPrestar * mensual) / 100;

    
    let MontoTotal = MontoAPrestar + (porcentajeDePrestamo * 5);

    
    console.log(`EL INTERÉS DE TU PRÉSTAMO ANUAL ES DE: ${porcentajeDePrestamo}`);
    console.log(`EL INTERÉS PAGADO EN EL TERCER TRIMESTRE ES DE: ${interesTercerTrimestre}`);
    console.log(`EL INTERÉS PAGADO EN EL PRIMER MES ES DE: ${interesPrimerMes}`);
    console.log(`EL MONTO TOTAL A PAGAR DESPUÉS DE 5 AÑOS ES DE: ${MontoTotal}`);
}

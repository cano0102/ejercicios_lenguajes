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




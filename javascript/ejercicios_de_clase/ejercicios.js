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


let cantidad = parseInt(prompt("Ingrese la cantidad de personas: "));
let personas = [];

for (let i = 0; i < cantidad; i++) {
    let nombre = prompt("Ingrese el nombre: ");
    let edad = parseInt(prompt("Ingrese la edad: "));
    let nota = parseFloat(prompt("Ingrese la nota: "));
    
    let persona = {
        "Nombre": nombre,
        "Edad": edad,
        "Nota": nota
    };
    
    personas.push(persona);
}

console.log("Listado ingresado:");
console.table(personas);

let mayorMenor =personas.sort((a, b) => b[2] - a[2]);;
console.log("Listado ordenado por nota:");
console.table(mayorMenor);




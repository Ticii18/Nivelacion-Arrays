def datos():
    personas = [];
    cantidad = int(input("Ingrese la cantidad de personas a cargar los datos"));

    for i in range (cantidad):
        nombre = input("ingrese el nombre de la persona");
        edad = int(input("ingrese la edad de la persona"));
        nota = int(input("Ingrese la nota de la persona"));

        persona ={
            "Nombre":nombre,
            "Edad": edad,
            "Nota":nota
            }
        personas.append(persona);

    return personas;

def mostrar_listado(personas):
    print("Listado ingresado:")
    for persona in personas:
        print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Nota: {persona['Nota']}")

def mostrar_ordenado(personas):
    # key=lambda x: x["Nota"] indica que se ordena según la clave "Nota". Y el reverse para indicar que es de mayor a menor
    ordenado = sorted(personas, key=lambda x: x["Nota"], reverse=True)

    print("Listado ordenado por nota:")
    for persona in ordenado:
        print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Nota: {persona['Nota']}")

personas = datos()
mostrar_listado(personas)
mostrar_ordenado(personas)

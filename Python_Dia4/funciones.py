
#funciones 


def agregarUsuario(opc):
    print("Crear artista")
    nuevoArtista= {
        "País de origen": input("País de origen: "),
        "Años de actividad": input("Años de actividad: "),
        "Año de lanzamiento del primer disco que llegó a las listas": int(input("Año de lanzamiento del primer disco que llegó a las listas: ")),
        "Género musical": input("Género musical: "),
        "Unidades certificadas totales": input("Unidades certificadas totales: "),
        "Ventas reclamadas": input("Ventas reclamadas: "),
        "Estado del artista (si está activo o no)": input("¿Está activo el artista? (sí/no): ")
    }
    return nuevoArtista
def informe ():
    pais = input("Ingresa el país: ")
    inicio = int(input("Año de inicio: "))
    fin = int(input("Año final: "))
    return pais, inicio, fin
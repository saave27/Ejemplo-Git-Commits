def mostrar_menu():
 menu = """
    Hola, bienvenido/a!

    Este es el sistema de clasificación de naves espaciales, a continuación encontrarás 4 tipos de naves espaciales:

    1 - Nave lanzadera
    2 - Nave no tripulada
    3 - Nave tripulada
    4 - Nave tripulada (Dragon)

    ¿Qué nave espacial deseas investigar?
    """
 return int(input(menu))

def mostrar_submenu(opciones):
    print("\nOpciones disponibles:")
    for key, value in opciones.items():
        print(f"{key} - {value['titulo']}")
    return int(input("\n¿Qué deseas investigar? "))

def obtener_info_nave(nave, opciones):
    print(f"\nSeleccionaste: {nave}\n")
    try:
        opcion = mostrar_submenu(opciones)
        if opcion in opciones:
            print(f"\n{opciones[opcion]['titulo']}:\n")
            print(opciones[opcion]['descripcion'])
        else:
            print("\nOpción no válida.")
    except ValueError:
        print("\nPor favor, ingresa un número válido.")


def main():
    naves = {
        1: {
            "nombre": "Nave Lanzadera",
            "opciones": {
                1: {"titulo": "Potencia", "descripcion": "Estos cohetes impulsores funcionan mediante combustible químico sólido o propelente líquido..."},
                2: {"titulo": "Capacidad", "descripcion": "El lanzador Energía medía 60 metros, pesaba 2400 toneladas y podía transportar 100 toneladas..."},
                3: {"titulo": "Actualidad", "descripcion": "Tanto Rusia como EE.UU emplean lanzaderas menos potentes pero más eficientes..."}
            }
        },
        2: {
            "nombre": "Nave no Tripulada",
            "opciones": {
                1: {"titulo": "Propósitos", "descripcion": "Su principal objetivo es estudiar otros cuerpos celestes..."},
                2: {"titulo": "ATV y sus Características", "descripcion": "El vehículo de transferencia automatizada (ATV) abastece, limpia y regula la EEI..."},
                3: {"titulo": "Estudios", "descripcion": "Se han estudiado Saturno, Marte, Mercurio, Plutón, Urano, Neptuno y el Sol..."}
            }
        },
        3: {
            "nombre": "Nave Tripulada",
            "opciones": {
                1: {"titulo": "Misiones", "descripcion": "Estas naves se han usado para misiones lunares, experimentación y mantenimiento de satélites..."},
                2: {"titulo": "Centros de Investigación", "descripcion": "El Skylab y Salyut fueron los primeros centros de investigación en órbita terrestre..."}
            }
        },
        4: {
            "nombre": "Nave Tripulada Dragon de SpaceX",
            "opciones": {
                1: {"titulo": "Diseño", "descripcion": "La cápsula Dragon tiene un escudo PICA-X y es reutilizable..."},
                2: {"titulo": "Misiones", "descripcion": "SpaceX C1, SpaceX 1 y SpaceX 4 son algunas de las misiones destacadas..."},
                3: {"titulo": "Producción", "descripcion": "En 2010, SpaceX fabricaba una cápsula cada tres meses y luego aumentó la producción..."},
                4: {"titulo": "Financiación", "descripcion": "SpaceX recibió financiamiento de la NASA y aportó más de $450 millones..."}
            }
        }
    }

    try:
        opcion_nave = mostrar_menu()
        if opcion_nave in naves:
            obtener_info_nave(naves[opcion_nave]["nombre"], naves[opcion_nave]["opciones"])
        else:
            print("\nOpción no válida.")
    except ValueError:
        print("\nPor favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
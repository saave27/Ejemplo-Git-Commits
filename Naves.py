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

"""
answer1_1 = """
Potencia:

Estos cohetes impulsores funcionan mediante combustible 
químico sólido o bien propelente líquido, o ambos.

El más potente jamás construido pertenecía a los EE.UU. 
y su nombre era Saturno V. Este gigante, de 3500 toneladas 
de empuje y 2900 toneladas de peso, era capaz de transportar 
118 toneladas en órbita baja terrestre, pero fue retirado en 
1973. Con más de 100 metros de altura y una potencia de 32000 por 5 
caballos, permitió transportar la nave tripulada Apolo hasta la Luna.

"""
answer1_2 = """
Capacidad:

El lanzador Energía medía 60 metros, pesaba 2400 toneladas, podía 
transportar 100 toneladas, y tenía un empuje de 3060 toneladas.

"""
answer1_3 = """
En la actualidad:

Tanto Rusia como EE.UU emplean lanzaderas menos potentes pero 
algo más eficientes. La NASA estudia la posibilidad de contribuir 
energéticamente al despegue de los vehículos lanzadera mediante 
cañones electromagnéticos, dejando, de momento, la fisión atómica 
para el ámbito de la ciencia-ficción.

"""

answer2 = """
Seleccionaste Nave no Tripulada!

Esta categoría resulta la más nutrida, pese a 
que no se incluyen aquí los numerosísimos satélites 
artificiales que orbitan geoestacionariamente.

Hay tres cosas que investigar de esta Nave no Tripulada.

1- Propositos
2- El ATV y sus Caracteristicas
3- Estudios

Que deseas investigar?

"""
answer2_1 = """
Propositos:

Su principal objetivo estriba en estudiar otros cuerpos celestes. 
Por eso las primeras de la historia tenían como finalidad estudiar 
a nuestro satélite natural, es decir, inmediaciones y superficie 
lunares, por su proximidad.

"""
answer2_2 = """
ATV y sus caracteristicas:

De esta categoría, el más importante, y activo actualmente, 
es el vehículo de transferencia automatizada (ATV) que sirve para abastecer, 
limpiar y regular periódicamente la elevación de la EEI. Esta nave robótica 
cuenta con cuatro motores de combustión de monometilhidracina (MMH) y óxido 
nítrico, que le dan un empuje de 0,2 toneladas.

"""
answer2_3 = """
Estudios:

Con el tiempo la investigación aeroespacial se preparó para abordar 
aquellos planetas del sistema solar que más fascinación han suscitado 
siempre a la humanidad, por interés puramente científico. Para estudiar:
Saturno y sus lunas, Jupitaer Marte, Mercurio, Pluton, Urano y Neptuno, y por supuesto el Sol

"""

answer3 = """
Seleccionaste Nave Tripulada!

Wow! Resulta meridiano que su propósito consiste en mandar 
seres humanos al espacio para tareas de reparación, mantenimiento 
o investigación, en misiones donde se precisa de la destreza y de 
la toma de decisiones de personas, en detrimento de las máquinas.

Hay tres cosas que investigar de esta Nave Tripulada

1- Misiones
2- Centros de Investigacion

Que deseas investigar?

"""
answer3_1 = """
Misiones:

A lo largo de la historia se han empleado para tres fines:

1) misiones lunares

2) experimentación y estudio del comportamiento humano en 
condiciones ingrávidas y en el exterior de la cápsula.

3) mantenimiento de satélites, probar acoplamientos con 
otras naves y equipos electrónicos

"""
answer3_2 = """
Centro de Investigacion:


los grandes centros de investigación espaciales en órbita terrestre. 

El primero fue el Skylab estadounidense, actualmente destruido, pesaba 
77 toneladas y orbitaba a 435 km. 

El segundo de la historia, el Salyut soviético, también destruido, 
pesaba 19,8 toneladas y orbitaba a una media de 248,9 km de distancia 
sobre la superficie terrestre.

"""

answer4 = """
Seleccionaste Nave Tripulada Dragon de SpaceX!

La SpaceX Dragon, también conocida como Dragon 1 o Cargo Dragon, 
fue una clase de nave espacial reutilizable de carga desarrollada 
por SpaceX, una empresa de transporte espacial estadounidense.

Hay tres cosas que investigar de esta Nave no Tripulada.

1- Diseño
2- Misiones
3- Produccion
4- Financiacion

Que deseas investigar?

"""
answer4_1 = """
Diseño:

La cápsula Dragon consiste en una tapa frontal en forma de cono, la cápsula 
balística tradicional y un módulo de carga no presurizado con dos paneles solares.

La cápsula utiliza un escudo de PICA-X basado en una variante propietaria del PICA 
de la NASA que protege a la cápsula durante la reentrada incluso a velocidades 
encontradas en misiones Lunares o Marcianas.

También es reutilizable con posibilidad de varias misiones.

"""
answer4_2 = """
Misiones:

Antes que nada hay que aclarar que la han habido cerca de 35 lanzamientos de
esta capsula Dragon, pero veremos los tres mas destacados a continuacion.

SpaceX C1: Primera misión de la Dragon, segundo lanzamiento del Falcon 9. 
Se probaron las maniobras orbitales y la reentrada de la Dragon. D
espués de ser recuperada la cápsula se expuso en las oficinas de SpaceX.

SpaceX 1: Primera misión operacional en el CRS para la NASA. El Falcon 9 sufrió un 
problema parcial en un motor pero pudo llevar la Dragon a la órbita correcta. 
Una carga secundaria no tuvo tanta suerte.

SpaceX 4: Primer lanzamiento con una carga viva, 20 ratones como parte de un 
experimento de la NASA para estudiar los efectos de vuelos de larga duración.

"""
answer4_3 = """
Produccion:

En diciembre de 2010 la línea de producción fabricaba una cápsula Dragon y un 
cohete Falcon 9 cada tres meses. En 2010 Elon Musk declaró que planeaba aumentar 
la cantidad a una cápsula cada seis semanas para 2012. Los materiales compuestos 
se utilizan extensamente en la nave para reducir su peso y mejorar la integridad estructural.

"""
answer4_4 = """
Financiacion:

Aca hay algo muy importante que resaltar, ya que SpaceX es una empresa privada que
se decica a trabajar en la industria espacial con el apoyo del gobierno de los EE.UU.

En 2014 SpaceX publicó los costes totales combinados de desarrollo para el Falcon 9 
y la cápsula Dragon. La NASA aportó US$396 millones mientras SpaceX aportó más de 
US$450 millones en ambos esfuerzos de desarrollo.

"""

option = int(input(menu))

if option == 1:
    print(answer1)
    option = int(input())
    if option == 1:
        print(answer1_1)
    elif option == 2:
        print(answer1_2)
    elif option == 3:
        print(answer1_3)    
    else:
        print("Selecciona una opcion correcta")

elif option == 2:
    print(answer2)
    option = int(input())
    if option == 1:
        print(answer2_1)
    elif option == 2:
        print(answer2_2)
    elif option == 3:
        print(answer2_3)    
    else:
        print("Selecciona una opcion correcta")

elif option == 3:
    print(answer3)
    option = int(input())
    if option == 1:
        print(answer3_1)
    elif option == 2:
        print(answer3_2)
    elif option == 3:
        print(answer3_3)    
    else:
        print("Selecciona una opcion correcta")

elif option == 4:
    print(answer4)
    option = int(input())
    if option == 1:
        print(answer4_1)
    elif option == 2:
        print(answer4_2)
    elif option == 3:
        print(answer4_3)
    elif option == 4:
        print(answer4_4)    
    else:
        print("Selecciona una opcion correcta")

else:
    print("Selecciona una opcion correcta")
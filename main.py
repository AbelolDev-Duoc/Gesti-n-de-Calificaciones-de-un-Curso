import os
validacion_salida = False

def limpiar_pantalla():
    # Detecta el sistema operativo
    sistema_operativo = os.name
    
    if sistema_operativo == 'posix':
        # Sistemas Unix/Linux/Mac
        os.system('clear')
    elif sistema_operativo == 'nt':
        # Sistemas Windows
        os.system('cls')

while validacion_salida == False:
    limpiar_pantalla()
    print("Bienvenido a la gestión de calificaciones")
    print("Elija la opción a realizar: ")
    print("1-) Leer calificaciones")
    print("2-) Calcular nota final")
    print("3-) Clasificar alumnos")
    print("4-) Salir del programa")
    try:
       opcion = int(input(">>> "))
       match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Hasta pronto...")
            validacion_salida = True
        case _:
            print("Opción no válida")
            input("Presione ENTER para continuar")
    except ValueError:
        print("Ingrese una opción númerica")
        input("Presione ENTER para continuar")

import os, csv
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

def leer_calificaciones():
    datos = []
    with open('calificaciones.csv', newline='', encoding='utf-8') as archivo_csv:
        archivo = csv.DictReader(archivo_csv, delimiter=';')
        for fila in archivo:
            datos.append = {
                'Apellidos': str(fila['Apellidos']),
                'Nombre': str(fila['Nombre']),
                'Asistencia': str(fila['Asistencia'].replace('%','')),
                'Parcial1': float(fila['Parcial1'].replace(',','.')),
                'Parcial2': float(fila['Parcial2'].replace(',','.')),
                'Ordinario1': float(fila['Ordinario1'].replace(',','.')),
                'Ordinario2': float(fila['Ordinario2'].replace(',','.')),
                'Practicas': float(fila['Practicas'].replace(',','.')),
                'OrdinarioPracticas': float(fila['OrdinarioPracticas'].replace(',','.'))
            }
    input("Presione ENTER para continuar")
    return datos


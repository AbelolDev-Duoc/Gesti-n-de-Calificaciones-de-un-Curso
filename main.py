import csv

# Función 1: Leer el fichero de calificaciones y devolver una lista de diccionarios
def leer_calificaciones(nombre_fichero):
    def ordenar_por_apellidos(alumno):
        return alumno['Apellidos']

    lista_alumnos = []
    with open(nombre_fichero, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile, delimiter=';')
        for fila in lector:
            # Convertir asistencia a número
            fila['Asistencia'] = float(fila['Asistencia'].replace('%', ''))
            # Convertir calificaciones a números (y manejar los vacíos)
            for clave in ['Parcial1', 'Parcial2', 'Ordinario1', 'Ordinario2', 'Practicas', 'OrdinarioPracticas']:
                fila[clave] = float(fila[clave].replace(',', '.')) if fila[clave] else None
            lista_alumnos.append(fila)
    # Ordenar la lista por apellidos usando una función
    lista_alumnos.sort(key=ordenar_por_apellidos)
    return lista_alumnos

# Función 2: Calcular la nota final del curso y añadirla a cada diccionario
def calcular_nota_final(lista_alumnos):
    for alumno in lista_alumnos:
        # Determinar la nota final de cada examen parcial y prácticas
        parcial1 = alumno['Parcial1']
        if parcial1 < 4 and alumno['Ordinario1'] is not None:
            parcial1 = alumno['Ordinario1']

        parcial2 = alumno['Parcial2']
        if parcial2 < 4 and alumno['Ordinario2'] is not None:
            parcial2 = alumno['Ordinario2']

        practicas = alumno['Practicas']
        if practicas < 4 and alumno['OrdinarioPracticas'] is not None:
            practicas = alumno['OrdinarioPracticas']
        
        # Comprobar si todas las notas necesarias están presentes
        notas_presentes = parcial1 is not None and parcial2 is not None and practicas is not None
        
        if notas_presentes:
            # Calcular la nota final ponderada
            nota_final = (0.3 * parcial1) + (0.3 * parcial2) + (0.4 * practicas)
            alumno['NotaFinal'] = round(nota_final, 2)
        else:
            alumno['NotaFinal'] = None
    
    return lista_alumnos

# Función 3: Clasificar los alumnos en aprobados y suspensos
def clasificar_alumnos(lista_alumnos):
    aprobados = []
    suspensos = []
    for alumno in lista_alumnos:
        if (alumno['Asistencia'] >= 75 and
            alumno['Parcial1'] >= 4 and
            alumno['Parcial2'] >= 4 and
            alumno['Practicas'] >= 4 and
            alumno['NotaFinal'] >= 5):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos

# Uso de las funciones
nombre_fichero = 'calificaciones.csv'

# Leer y procesar el fichero de calificaciones
alumnos = leer_calificaciones(nombre_fichero)
alumnos_con_notas = calcular_nota_final(alumnos)
aprobados, suspensos = clasificar_alumnos(alumnos_con_notas)

# Mostrar resultados
print("Alumnos aprobados:")
for alumno in aprobados:
    print(f"{alumno['Apellidos']}, {alumno['Nombre']}: Nota Final {alumno['NotaFinal']}")

print("\nAlumnos suspensos:")
for alumno in suspensos:
    print(f"{alumno['Apellidos']}, {alumno['Nombre']}: Nota Final {alumno['NotaFinal']}")

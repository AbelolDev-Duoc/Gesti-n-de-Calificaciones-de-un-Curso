# Gestión de Calificaciones de un Curso

Este repositorio contiene un programa para gestionar las calificaciones de un curso. El fichero `calificaciones.csv` incluye las notas de los alumnos en dos exámenes parciales de teoría y un examen de prácticas. Aquellos alumnos que obtuvieron menos de 4 en alguno de estos exámenes tuvieron la oportunidad de repetirlo al final del curso (convocatoria ordinaria).

## Estructura del Proyecto

El programa está compuesto por tres funciones principales:

1. **Leer Calificaciones**: Esta función lee el fichero `calificaciones.csv` y devuelve una lista de diccionarios con la información de los exámenes y la asistencia de cada alumno, ordenados por apellidos.
2. **Calcular Nota Final**: Esta función recibe la lista de diccionarios y añade a cada diccionario una nueva clave con la nota final del curso. La nota final se calcula con un peso del 30% para cada parcial de teoría y un 40% para el examen de prácticas.
3. **Clasificar Alumnos**: Esta función recibe la lista de diccionarios y devuelve dos listas: una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar, los alumnos deben cumplir con los siguientes criterios:
    - Asistencia mayor o igual al 75%
    - Nota mayor o igual a 4 en cada examen
    - Nota final mayor o igual a 5

## Archivos del Repositorio

- `calificaciones.csv`: Contiene las calificaciones de los alumnos.
- `main.py`: Contiene la implementación del programa con las tres funciones principales.
- `README.md`: Este archivo, que proporciona una visión general del proyecto.

## Ejecución del Programa

Para ejecutar el programa, sigue los siguientes pasos:

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Clona este repositorio en tu máquina local.
    ```sh
    git clone https://github.com/tu-usuario/gestion-calificaciones.git
    ```
3. Navega al directorio del proyecto.
    ```sh
    cd gestion-calificaciones
    ```
4. Ejecuta el programa principal.
    ```sh
    python main.py
    ```

## Detalles de las Funciones

### 1. Leer Calificaciones

Esta función lee el fichero `calificaciones.csv` y devuelve una lista de diccionarios. Cada diccionario contiene la siguiente información:

- `nombre`: Nombre del alumno
- `apellidos`: Apellidos del alumno
- `parcial_1`: Nota del primer parcial de teoría
- `parcial_2`: Nota del segundo parcial de teoría
- `practicas`: Nota del examen de prácticas
- `asistencia`: Porcentaje de asistencia

La lista se devuelve ordenada alfabéticamente por los apellidos de los alumnos.

### 2. Calcular Nota Final

Esta función recibe la lista de diccionarios generada por la función anterior y añade a cada diccionario una nueva clave `nota_final`, que se calcula de la siguiente manera:

- `nota_final` = 0.3 * `parcial_1` + 0.3 * `parcial_2` + 0.4 * `practicas`

### 3. Clasificar Alumnos

Esta función recibe la lista de diccionarios con las notas finales añadidas y clasifica a los alumnos en dos listas:

- **Aprobados**: Alumnos que cumplen con los criterios de aprobación.
- **Suspensos**: Alumnos que no cumplen con los criterios de aprobación.

---

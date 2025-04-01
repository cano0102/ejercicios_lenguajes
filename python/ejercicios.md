Ejercicios con Listas
Ejercicio 1: Gestión de Libros en una Biblioteca

Escenario: Una biblioteca necesita administrar su colección de libros.
Objetivo: Crear un sistema para agregar, prestar y mostrar libros disponibles.
Requisitos:

    Agregar nuevos libros (título, autor, ISBN)

    Prestar libros (marcar como no disponible)

    Mostrar libros disponibles

    Buscar libros por autor o título
    Restricciones:

    No permitir libros con el mismo ISBN

    Máximo 3 préstamos por usuario

    Validar que el ISBN tenga 13 dígitos

Ejercicio 2: Control de Asistencia a Eventos

Escenario: Organización de un evento con lista de invitados.
Objetivo: Registrar asistencia y gestionar invitados.
Requisitos:

    Registrar nuevos invitados (nombre, documento, empresa)

    Marcar asistencia al evento

    Generar lista de asistentes

    Buscar invitado por documento
    Restricciones:

    Máximo 100 invitados

    No permitir documentos duplicados

    Validar formato de documento (8-10 dígitos)

Ejercicios con Tuplas
Ejercicio 3: Sistema de Puntuación de Videojuegos

Escenario: Plataforma que registra puntuaciones de jugadores.
Objetivo: Almacenar y mostrar rankings de juegos.
Requisitos:

    Registrar nueva puntuación (jugador, juego, puntos, fecha)

    Mostrar top 5 puntuaciones por juego

    Calcular promedio de puntos por juego
    Restricciones:

    Puntuaciones deben ser entre 0 y 1000

    Fecha en formato YYYY-MM-DD

    No permitir modificar puntuaciones registradas

Ejercicio 4: Horario de Clases Universitarias

Escenario: Sistema para consultar horarios de materias.
Objetivo: Permitir a estudiantes verificar horarios.
Requisitos:

    Almacenar horarios (materia, profesor, días, hora)

    Consultar materias por día

    Buscar materias por profesor
    Restricciones:

    Días válidos: Lunes a Viernes

    Horas en formato 24h (8:00 - 20:00)

    No permitir solapamiento de horarios

Ejercicios con Diccionarios
Ejercicio 5: Sistema de Gestión de Proyectos

Escenario: Equipo que necesita organizar proyectos y tareas.
Objetivo: Administrar proyectos, asignar tareas y miembros.
Requisitos:

    Crear proyectos (nombre, fecha inicio, fecha fin)

    Asignar miembros a proyectos

    Agregar tareas con prioridad (alta, media, baja)

    Mostrar estado de proyectos
    Restricciones:

    Fechas deben ser válidas (inicio < fin)

    Prioridades solo pueden ser los valores definidos

    Máximo 5 miembros por proyecto

Ejercicio 6: Traductor de Palabras Básico

Escenario: Aplicación para aprender vocabulario en otro idioma.
Objetivo: Traducir palabras entre idiomas.
Requisitos:

    Agregar nuevas palabras (palabra, idioma_origen, idioma_destino, traducción)

    Buscar traducción de palabra

    Mostrar todas las palabras de un idioma

    Generar test de práctica aleatorio
    Restricciones:

    No permitir palabras duplicadas en mismo idioma

    Idiomas soportados: español, inglés, francés

    Validar que palabras solo contengan letras

Ejercicios con Conjuntos (Sets)
Ejercicio 7: Sistema de Intereses de Usuarios

Escenario: Red social que gestiona intereses de usuarios.
Objetivo: Encontrar coincidencias entre intereses.
Requisitos:

    Registrar usuarios (nombre, edad, intereses)

    Encontrar usuarios con intereses similares

    Mostrar intereses únicos en la plataforma

    Sugerir nuevos intereses basados en coincidencias
    Restricciones:

    Intereses deben ser palabras de 3-20 caracteres

    Máximo 10 intereses por usuario

    No permitir intereses duplicados por usuario

Ejercicio 8: Control de Acceso a Laboratorio

Escenario: Sistema de seguridad para laboratorio informático.
Objetivo: Gestionar acceso de personas autorizadas.
Requisitos:

    Registrar personal autorizado (nombre, documento, área)

    Registrar acceso (fecha, hora, persona)

    Generar reporte de accesos por día

    Detectar accesos no autorizados
    Restricciones:

    Solo permitir acceso en horario 7:00-19:00

    Documento debe ser válido (prefijo + número)

    Máximo 20 personas en laboratorio simultáneamente

Ejercicio Integrador Avanzado
Ejercicio 9: Sistema de Vuelos y Reservas

Escenario: Aerolínea que necesita gestionar vuelos y pasajeros.
Objetivo: Sistema completo de reservas de vuelos.
Requisitos:

    Registrar vuelos (número, origen, destino, hora, asientos)

    Reservar asientos (pasajero, documento, vuelo, asiento)

    Cancelar reservas

    Mostrar disponibilidad de vuelos

    Generar tarjeta de embarque
    Restricciones:

    Asientos en formato A1, B2, etc. (máx. 5 filas A-E, 10 columnas 1-10)

    No permitir asientos duplicados en mismo vuelo

    Validar formato de hora HH:MM

    Documentos deben ser únicos por vuelo

Ejercicio 10: Plataforma de Cursos Online

Escenario: Sistema para administrar cursos virtuales.
Objetivo: Gestionar cursos, estudiantes y calificaciones.
Requisitos:

    Crear cursos (nombre, código, profesor, cupo)

    Matricular estudiantes (nombre, documento, email)

    Registrar calificaciones (curso, estudiante, notas)

    Generar certificados de aprobación

    Mostrar estadísticas por curso
    Restricciones:

    Código de curso: 3 letras + 3 números (ej: MAT123)

    Email debe tener formato válido

    Notas entre 0.0 y 5.0

    Cupo máximo por curso: 30 estudiantes

Buenas Prácticas a Implementar:

    Validación de datos de entrada

    Manejo de errores con try-except

    Documentación de funciones

    Modularización del código

    Uso apropiado de estructuras de datos

    Interfaz de usuario clara (menús, opciones)

    Persistencia de datos (guardar/leer archivos)

Estos ejercicios cubren una variedad de escenarios del mundo real y permiten practicar con todas las estructuras de datos principales de Python, aplicando restricciones y validaciones para asegurar código robusto.
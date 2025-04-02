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






EJERCICIOS DE PRACTICA


1. Sistema de Gestión de Estudiantes

Descripción:
Desarrollar una aplicación para gestionar el registro de estudiantes de una institución educativa, permitir consultar, verificar, eliminar y generar reportes.

Requisitos:

    Registro de la Acreditación solicitando:

        Nombre (no vacío)

        Edad (entero positivo)

        Promedio de notas (número entre 0,0 y 5.0)

        Carrera (lista predefinida: Ingeniería, Ciencias, Arte).

    Estudiante Estudiante por nombre.

    Estudiante por nombre.

    Mostrar todos los estudiantes por medio.

    Generar un reporte con:

        Total de estudiantes.

        Promedio general de notas.

        Estudiante con el mejor y peor medio (nombre y nota).

    Menú interactivo con validaciones (intento-excepto).

    Usar listas o diccionarios para almacenar datos.

2. Sistema de Reservas de Hotel

Descripción:
Crear un programa para gestionar reservas de habitaciones en un hotel, con opciones para acordar, y cancelar reservas, además de reportes.

Requisitos:

    Secretario de reserva solicitando:

        Nombre del cliente (no vacío).

        Tipo de habitación (Individual, Doble, Suite).

        Noches (entero positivo).

        Precio por noche (mayor que cero).

    Consultora reserva por nombre de cliente.

    Cancelar reserva por nombre.

    Mostrar todas las reservas ordenadas por noches.

    Generar un reporte con:

        Total de reservas activas.

        ingresos potenciales (suma de precios).

        Reserva más larga y más corta (nombre y noches).

    Menú con manejo de excepciones.

    Usar diccionarios para almacenar reservas.

3. Gestión de Tareas Pendientes

Descripción:
Aplicación para administrar tareas personales, con funciones para agregar, completar y priorizar tareas.

Requisitos:

    Agregar tarea solicitando:

        Descripción (no vacía).

        Prioridad (Alta, Medios, Baja).

        Fecha límite (formato dd/mm/aaaaa).

    Marcar tarea como completada.

    Embaracción por descripción.

    Las tareas más raras por la prioridad y la fecha.

    Generar un reporte con:

        Total de tareas pendientes/completadas.

        Tarea más urgente (prioridad Alta y fecha próxima).

    Menú interactivo con validaciones (ej.: fecha incorrecta).

    Usar listas de diccionarios para almacenar tareas.

4. Sistema de Ventas de Tienda

Descripción:
Programa para gestionar ventas de una tienda, registrardo productos vendidos y generando estadísticas.

Requisitos:

    Secretario de venta solicitando:

        Nombre del producto (no vacío).

        (Entero positivo).

        Precio unitario (alcalde que cero).

    Consultador sales por producto.

    Mostrar todas las ventas ordenadas por fecha.

    Generar un reporte con:

        Total de ventas (en dinero).

        Producto más vendido (nombre y cantidad).

        Promedio de ventas por producto.

    Menú con try-except para precios/cantidades inválidas.

    Usar una lista de tuplas para almacenar ventas.

Nota: Todos los ejercicios debe incluir:

    Modularización con funciones.

    Validación de entradas.

    Colecciones (listas, diccionarios o tuplas).

    Ciclos y condicionales.

Ejercicios con Listas
Ejercicio 11: Simulador de Carrito de Compras
Escenario: Tienda en línea que gestiona compras de clientes.
Objetivo: Permitir agregar, eliminar y ver productos en el carrito.
Requisitos:

Agregar productos (nombre, cantidad, precio).

Eliminar productos del carrito.

Mostrar el total de la compra.

Aplicar descuentos si el total supera cierto umbral.
Restricciones:

No permitir cantidades negativas.

El precio debe ser mayor que 0.

Ejercicio 12: Simulador de Elecciones
Escenario: Sistema para registrar y contar votos en una elección.
Objetivo: Gestionar votos y determinar el ganador.
Requisitos:

Registrar candidatos.

Permitir a los votantes elegir un candidato.

Contar votos y mostrar el ganador.
Restricciones:

Un votante no puede votar más de una vez.

Solo se puede votar por candidatos registrados.

Ejercicios con Tuplas
Ejercicio 13: Registro de Marcas en Atletismo
Escenario: Competencia de atletismo que almacena los tiempos de los corredores.
Objetivo: Determinar los mejores tiempos de la competencia.
Requisitos:

Registrar corredores (nombre, tiempo en segundos).

Determinar el mejor tiempo.

Mostrar los tres mejores corredores.
Restricciones:

No se permiten tiempos negativos.

Ejercicio 14: Control de Gastos Mensuales
Escenario: Aplicación para registrar los gastos personales.
Objetivo: Permitir visualizar gastos de forma ordenada.
Requisitos:

Registrar gastos (categoría, monto, fecha).

Mostrar los gastos por categoría.

Calcular el total gastado en el mes.
Restricciones:

No permitir montos negativos.

Fechas en formato válido (DD/MM/AAAA).

Ejercicios con Diccionarios
Ejercicio 15: Registro de Pacientes en un Hospital
Escenario: Hospital que maneja la información de los pacientes.
Objetivo: Permitir registrar, modificar y consultar pacientes.
Requisitos:

Registrar pacientes (nombre, edad, diagnóstico).

Modificar información de un paciente.

Buscar pacientes por nombre.
Restricciones:

La edad debe ser un número positivo.

No permitir nombres duplicados.

Ejercicio 16: Sistema de Inventario de Almacén
Escenario: Una empresa almacena productos en un inventario.
Objetivo: Gestionar el stock de productos.
Requisitos:

Agregar productos al inventario.

Modificar cantidades de productos.

Mostrar el inventario completo.
Restricciones:

No permitir cantidades negativas.

Ejercicios con Conjuntos (Sets)
Ejercicio 17: Sistema de Control de Placas de Vehículos
Escenario: Estacionamiento que registra placas de autos.
Objetivo: Detectar si un auto ya ha ingresado.
Requisitos:

Registrar placas de autos.

Verificar si un auto ya está dentro.

Mostrar todos los autos dentro del estacionamiento.
Restricciones:

No permitir placas duplicadas.

Ejercicio 18: Control de Asistencias en una Universidad
Escenario: Universidad que gestiona asistencia a clases.
Objetivo: Registrar quiénes asistieron a una clase.
Requisitos:

Registrar asistencia por materia.

Mostrar lista de estudiantes que asistieron.

Comparar asistencia entre clases.
Restricciones:

No permitir nombres duplicados en la misma clase.

Ejercicios Integradores Avanzados
Ejercicio 19: Sistema de Gestión de Pedidos para una Pizzería
Escenario: Restaurante que toma y entrega pedidos de pizza.
Objetivo: Permitir a los clientes hacer pedidos y al restaurante gestionarlos.
Requisitos:

Registrar pedidos (cliente, tipo de pizza, cantidad).

Mostrar los pedidos pendientes.

Marcar pedidos como entregados.
Restricciones:

No aceptar pedidos con cantidades negativas.

Ejercicio 20: Simulador de Bolsa de Valores
Escenario: Plataforma que permite comprar y vender acciones.
Objetivo: Gestionar transacciones de acciones.
Requisitos:

Registrar empresas y sus precios de acciones.

Permitir comprar y vender acciones.

Mostrar ganancias o pérdidas de cada usuario.
Restricciones:

No permitir comprar más acciones de las disponibles.

# EJERCICIOS CORTOS
Ejercicios con Listas
21. Sistema de Registro de Notas
Registra calificaciones de estudiantes y calcula el promedio de cada uno.

22. Gestión de Inventario de Librería
Almacena libros disponibles y permite actualizar el stock.

23. Planificador de Viajes
Crea un itinerario de viaje con destinos y fechas.

24. Lista de Contactos
Almacena contactos con nombre, teléfono y correo electrónico.

25. Simulador de Compras en Línea
Permite agregar productos al carrito y calcular el total.

26. Historial de Transacciones Bancarias
Registra depósitos y retiros con fechas y montos.

27. Control de Asistencias en un Curso
Lleva la lista de estudiantes y registra quiénes asistieron a clase.

28. Generador de Tablas de Multiplicar
Crea y almacena en una lista las tablas de multiplicar del 1 al 10.

29. Sistema de Gestión de Talleres Mecánicos
Lista de autos en reparación con dueño y tipo de avería.

30. Control de Pedidos en un Restaurante
Guarda pedidos y marca cuáles han sido entregados.

Ejercicios con Tuplas
31. Registro de Puntuaciones en Deportes
Guarda las mejores marcas de atletas en diferentes pruebas.

32. Horarios de Atención Médica
Lista de horarios disponibles para consulta médica.

33. Ranking de Películas Favoritas
Guarda una lista de películas con puntuaciones de 1 a 10.

34. Sistema de Reservas de Teatro
Asientos reservados con nombre del cliente y ubicación.

35. Control de Asistencias en Reuniones
Guarda en tuplas la asistencia a reuniones empresariales.

36. Registro de Gastos de la Semana
Guarda los gastos con fecha, monto y descripción.

37. Historial de Clima Diario
Almacena temperaturas máximas y mínimas por día.

38. Ranking de Mejores Libros
Lista de libros con calificación promedio de lectores.

39. Control de Producción en Fábrica
Registra el número de productos fabricados por día.

40. Registro de Historial de Vehículos
Guarda información sobre revisiones técnicas con fecha y detalles.

Ejercicios con Diccionarios
41. Registro de Empleados
Guarda información de empleados con su ID, cargo y salario.

42. Gestión de Materias Universitarias
Almacena materias con su respectivo profesor y horario.

43. Traductor de Frases
Crea un diccionario con frases en español y su traducción.

44. Agenda Electrónica
Guarda contactos con nombre, teléfono y dirección.

45. Registro de Mascotas en una Veterinaria
Almacena datos de mascotas, dueño y última consulta.

46. Sistema de Control de Stock
Gestiona productos con código, nombre y cantidad en inventario.

47. Base de Datos de Clientes
Almacena clientes con historial de compras.

48. Historial de Consultas Médicas
Registra diagnósticos por paciente.

49. Control de Puntuaciones en un Concurso
Registra los puntajes obtenidos por cada participante.

50. Sistema de Tareas Pendientes
Lista tareas con su estado (pendiente, en progreso, completada).

Ejercicios con Conjuntos (Sets)
51. Control de Participantes en un Evento
Lista de personas registradas sin duplicados.

52. Comparador de Listas de Canciones
Compara listas de reproducción para ver qué canciones coinciden.

53. Sistema de Gestión de Permisos
Guarda los permisos de acceso de usuarios en una empresa.

54. Base de Datos de Placas Vehiculares
Registra matrículas sin duplicados.

55. Sistema de Control de Materiales en un Laboratorio
Guarda qué materiales están disponibles.

56. Comparador de Respuestas en un Examen
Compara respuestas correctas con las dadas por los estudiantes.

57. Identificación de Clientes Frecuentes en un Negocio
Lista de clientes que han comprado más de una vez.

58. Control de Títulos de Libros en una Biblioteca
Almacena los títulos disponibles sin duplicados.

59. Análisis de Datos de Encuestas
Determina las respuestas únicas de una encuesta.

60. Control de Equipos en un Torneo
Registra los equipos participantes sin repetir nombres.

Ejercicios Integradores Avanzados
61. Sistema de Gestión de Alquiler de Autos
Registro de autos disponibles y reservas de clientes.

62. Plataforma de Publicaciones de Noticias
Gestión de artículos con autores y fecha de publicación.

63. Control de Accesos en un Edificio
Sistema que registra entradas y salidas de empleados.

64. Plataforma de Gestión de Propiedades en Venta
Registra propiedades con precios, ubicación y dueño.

65. Aplicación de Gestión de Proyectos
Permite asignar tareas a empleados y dar seguimiento.

66. Sistema de Venta de Boletos para Conciertos
Registra la compra de boletos con asientos asignados.

67. Simulación de un Cajero Automático
Realiza operaciones como retiro, depósito y consulta de saldo.

68. Plataforma de Gestión de Cursos Online
Permite inscribir estudiantes y registrar calificaciones.

69. Sistema de Control de Producción Agrícola
Registra cosechas, cultivos y fechas de producción.

70. Simulación de una Bolsa de Empleo
Permite a empleadores y candidatos registrarse e interactuar.

Ejercicios Extras (Lógica y Algoritmos)
71. Generador de Contraseñas Seguras
Crea contraseñas aleatorias con mayúsculas, minúsculas y números.

72. Simulación de Juego de Dados
Lanza dos dados y muestra los resultados.

73. Conversor de Temperatura
Convierte grados entre Celsius, Fahrenheit y Kelvin.

74. Cifrado de Mensajes con Código César
Permite cifrar y descifrar mensajes.

75. Contador de Palabras en un Texto
Analiza la frecuencia de cada palabra en un texto dado.

76. Identificador de Números Primos
Determina si un número es primo o no.

77. Simulación de Carrera de Autos
Cada auto avanza un número aleatorio de metros por turno.

78. Generador de Series Fibonacci
Calcula los primeros n términos de la serie.

79. Simulación de un Semáforo
Cambia entre verde, amarillo y rojo con tiempos definidos.

80. Juego del Ahorcado
El jugador intenta adivinar una palabra letra por letra.

Ejercicios con Listas
81. Ordenador de Números
Ordena una lista de números en orden ascendente y descendente.

82. Eliminador de Duplicados
Elimina valores repetidos de una lista y devuelve una lista única.

83. Fusión de Listas
Une dos listas eliminando elementos repetidos.

84. Simulador de Lotería
Genera seis números aleatorios entre 1 y 49 sin repetir.

85. Rotación de Lista
Rota los elementos de una lista una posición a la derecha o izquierda.

86. Búsqueda de un Elemento
Determina si un número está dentro de una lista.

87. Calculadora de Estadísticas
Calcula la media, mediana y moda de una lista de números.

88. Generador de Números Pares
Crea una lista de los primeros n números pares.

89. Inversor de Lista
Invierte el orden de los elementos de una lista sin usar .reverse().

90. Filtrado de Valores
Elimina los valores negativos de una lista de números.

Ejercicios con Tuplas
91. Conversión de Lista a Tupla
Convierte una lista en una tupla inmutable.

92. Extracción de Subconjunto de Tupla
Toma los primeros n elementos de una tupla y los almacena en otra.

93. Identificación de Índice en Tupla
Encuentra la posición de un elemento específico en una tupla.

94. Comparador de Tuplas
Compara dos tuplas y determina cuál tiene mayor suma de valores.

95. Conversor de Tuplas a Diccionario
Convierte una lista de tuplas (clave, valor) en un diccionario.

96. Unión y Diferencia de Tuplas
Une dos tuplas y elimina los valores repetidos.

97. División de Tuplas en Variables
Desempaqueta una tupla en variables individuales.

98. Mezclador de Tuplas
Intercala elementos de dos tuplas en una nueva.

99. Convertidor de Tuplas a Cadenas
Convierte una tupla de caracteres en una cadena de texto.

100. Recuento de Elementos en Tupla
Cuenta cuántas veces aparece un valor en una tupla.

Ejercicios con Diccionarios
101. Contador de Caracteres en Texto
Cuenta cuántas veces aparece cada letra en una frase.

102. Conversor de Diccionario a Lista
Transforma un diccionario en una lista de tuplas clave-valor.

103. Diccionario de Estudiantes
Almacena estudiantes con su promedio y permite buscar por nombre.

104. Unión de Dos Diccionarios
Une dos diccionarios sin perder información.

105. Conversión de Unidades
Guarda factores de conversión en un diccionario y permite consultas.

106. Historial de Compras
Registra compras con fecha, productos y precios en un diccionario.

107. Sistema de Gestión de Stock
Controla productos y su cantidad disponible.

108. Diccionario de Teléfonos
Guarda nombres y números de contacto en un diccionario.

109. Buscador de Sinónimos
Guarda palabras con sus sinónimos y permite buscar equivalencias.

110. Diccionario de Notas de Clase
Almacena materias con el nombre del profesor y horario de clases.

Ejercicios con Sets (Conjuntos)
111. Eliminador de Palabras Repetidas
Filtra palabras únicas de un texto.

112. Comparador de Listas de Contactos
Muestra contactos comunes entre dos listas.

113. Identificación de Visitantes Frecuentes
Determina qué personas han visitado un sitio más de una vez.

114. Control de Accesos a un Sistema
Registra usuarios únicos que han iniciado sesión.

115. Simulador de Bingo
Genera 15 números aleatorios sin repetir.

116. Eliminación de Duplicados en Lista
Convierte una lista en un conjunto para eliminar duplicados.

117. Comparador de Intereses
Encuentra coincidencias entre hobbies de diferentes personas.

118. Control de Palabras en un Diccionario Personalizado
Guarda palabras aprendidas en un idioma sin duplicarlas.

119. Registro de Alumnos Inscritos en Cursos
Determina qué alumnos están inscritos en más de un curso.

120. Diferencia entre Grupos de Usuarios
Encuentra usuarios exclusivos en dos listas de participantes.

Ejercicios de Algoritmos y Lógica
121. Validación de Contraseñas
Comprueba si una contraseña cumple con requisitos de seguridad.

122. Simulación de un Semáforo
Cambia entre colores verde, amarillo y rojo con tiempos definidos.

123. Juego de Piedra, Papel o Tijeras
Crea una versión básica contra la computadora.

124. Ordenador de Palabras en una Frase
Ordena las palabras de una oración alfabéticamente.

125. Identificación de Año Bisiesto
Determina si un año dado es bisiesto o no.

126. Conversor de Horas
Convierte una hora en formato de 12h a 24h y viceversa.

127. Cálculo del Factorial de un Número
Calcula el factorial de un número dado.

128. Simulación de Dados
Lanza dos dados y muestra los valores obtenidos.

129. Conversor de Números Romanos
Convierte un número arábigo a romano.

130. Simulación de Cajero Automático
Permite depositar, retirar y consultar saldo.

Ejercicios Avanzados
131. Simulación de Red Social
Permite seguir usuarios, publicar posts y dar "me gusta".

132. Generador de Código QR
Crea un código QR con una URL ingresada.

133. Procesador de Texto con Análisis de Frecuencia
Cuenta la frecuencia de palabras en un documento.

134. Chatbot Básico
Responde preguntas comunes usando un diccionario.

135. Cálculo de Trayectoria de un Proyectil
Simula la trayectoria de un objeto lanzado con velocidad inicial.

136. Sistema de Evaluación de Sentimientos en Comentarios
Detecta palabras positivas o negativas en una reseña.

137. Predicción de Ventas con Regresión Lineal
Simula un modelo de predicción de ventas en base a datos previos.

138. Cifrado de Mensajes con Base64
Codifica y decodifica textos en Base64.

139. Simulador de Bolsa de Valores
Genera precios aleatorios y permite invertir virtualmente.

140. Sistema de Registro de Pacientes en Hospital
Guarda información de pacientes, historial y tratamientos.

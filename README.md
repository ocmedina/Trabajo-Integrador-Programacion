# Sistema de Gestión de Datos de Países

## 📋 Descripción del Programa

El **Sistema de Gestión de Datos de Países** es una aplicación de consola desarrollada en Python que permite analizar, filtrar y visualizar información sobre países de todo el mundo. Este sistema fue diseñado como Trabajo Práctico Integrador para la materia Programación 1.

### Características Principales

- **Carga de Datos**: Importa información de países desde archivos CSV
- **Búsqueda Avanzada**: Busca países por nombre con coincidencias parciales
- **Filtros Múltiples**: Filtra por continente, población y superficie
- **Ordenamiento**: Ordena países por nombre, población o superficie (ascendente/descendente)
- **Estadísticas**: Calcula promedios, máximos, mínimos y distribución por continente
- **Interfaz Amigable**: Menú interactivo con validación de entradas
- **Visualización Clara**: Presenta datos en formato tabular fácil de leer

### Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Librerías estándar**: `csv`, `os`
- **Codificación**: UTF-8 para soporte de caracteres especiales

---

## 🚀 Instrucciones de Uso

### Requisitos Previos

- Python 3.6 o superior instalado en su sistema
- Archivo CSV con datos de países (formato requerido más abajo)

### Instalación

1. Clone o descargue este repositorio
2. Asegúrese de tener el archivo `Paises.csv` en el mismo directorio que el script
3. No se requieren instalaciones adicionales (usa librerías estándar de Python)

### Formato del Archivo CSV

El archivo CSV debe tener la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,45195777,2780400,América
Brasil,212559417,8515767,América
España,46754783,505990,Europa
```

**Columnas requeridas:**

- `nombre`: Nombre del país (texto)
- `poblacion`: Población en habitantes (número entero)
- `superficie`: Superficie en km² (número entero)
- `continente`: Continente al que pertenece (texto)

### Ejecución del Programa

#### En Windows:

```bash
python Gestion_Datod_Paises.py
```

#### En Linux/Mac:

```bash
python3 Gestion_Datod_Paises.py
```

### Navegación por el Menú

Al iniciar el programa:

1. Se le solicitará el nombre del archivo CSV
2. Aparecerá el menú principal con 10 opciones (0-9)
3. Ingrese el número de la opción deseada
4. Siga las instrucciones específicas de cada función
5. Presione ENTER para continuar después de cada operación
6. Seleccione opción 0 para salir

### Validación de Entradas

El sistema incluye validación robusta:

- ✅ No permite entradas vacías (presionar ENTER sin texto)
- ✅ Valida que los números sean enteros válidos
- ✅ Verifica rangos mínimos y máximos
- ✅ Solicita reintentar en caso de error sin cerrar el programa

---

## 💡 Ejemplos de Entradas y Salidas

### Ejemplo 1: Iniciar el Programa

**Entrada:**

```
Ingrese el nombre del archivo CSV (ej: paises.csv): Paises.csv
```

**Salida:**

```
✓ Se cargaron 195 países correctamente.

======================================================================
           SISTEMA DE GESTIÓN DE DATOS DE PAÍSES
======================================================================

 MENÚ PRINCIPAL:
  1. Buscar país por nombre
  2. Filtrar países por continente
  3. Filtrar países por rango de población
  4. Filtrar países por rango de superficie
  5. Ordenar países por nombre
  6. Ordenar países por población
  7. Ordenar países por superficie
  8. Mostrar estadísticas generales
  9. Mostrar todos los países
  0. Salir
======================================================================

➤ Seleccione una opción: _
```

### Ejemplo 2: Buscar País por Nombre

**Entrada:**

```
➤ Seleccione una opción: 1

 Ingrese el nombre del país a buscar: arg
```

**Salida:**

```
==========================================================================================
NOMBRE                    POBLACIÓN      SUPERFICIE (km²) CONTINENTE
==========================================================================================
Argentina                    45,195,777           2,780,400 América
Argelia                      43,851,044           2,381,741 África
==========================================================================================
Total de países: 2
```

### Ejemplo 3: Filtrar por Continente

**Entrada:**

```
➤ Seleccione una opción: 2

 Ingrese el continente: Europa
```

**Salida:**

```
==========================================================================================
NOMBRE                    POBLACIÓN      SUPERFICIE (km²) CONTINENTE
==========================================================================================
Albania                       2,877,797              28,748 Europa
Alemania                     83,783,942             357,022 Europa
Andorra                          77,265                 468 Europa
Austria                       9,006,398              83,871 Europa
...
==========================================================================================
Total de países: 44
```

### Ejemplo 4: Filtrar por Rango de Población

**Entrada:**

```
➤ Seleccione una opción: 3

 Filtrar por rango de población:
   Población mínima: 100000000
   Población máxima: 300000000
```

**Salida:**

```
==========================================================================================
NOMBRE                    POBLACIÓN      SUPERFICIE (km²) CONTINENTE
==========================================================================================
Brasil                      212,559,417           8,515,767 América
Bangladesh                  164,689,383             148,460 Asia
Rusia                       145,934,462          17,098,242 Europa/Asia
México                      128,932,753           1,964,375 América
Japón                       126,476,461             377,915 Asia
...
==========================================================================================
Total de países: 9
```

### Ejemplo 5: Ordenar por Población

**Entrada:**

```
➤ Seleccione una opción: 6

 Ordenar por población:
  1. Ascendente (menor a mayor)
  2. Descendente (mayor a menor)
Seleccione: 2
```

**Salida:**

```
==========================================================================================
NOMBRE                    POBLACIÓN      SUPERFICIE (km²) CONTINENTE
==========================================================================================
China                     1,439,323,776           9,596,961 Asia
India                     1,380,004,385           3,287,263 Asia
Estados Unidos              331,002,651           9,833,517 América
Indonesia                   273,523,615           1,904,569 Asia
Pakistán                    220,892,340             881,913 Asia
...
==========================================================================================
Total de países: 195
```

### Ejemplo 6: Mostrar Estadísticas Generales

**Entrada:**

```
➤ Seleccione una opción: 8
```

**Salida:**

```
======================================================================
                    ESTADÍSTICAS GENERALES
======================================================================

 POBLACIÓN:
   • Mayor población: China (1,439,323,776 hab.)
   • Menor población: Ciudad del Vaticano (801 hab.)
   • Promedio: 39,685,321 habitantes

  SUPERFICIE:
   • Promedio: 695,845 km²

 DISTRIBUCIÓN POR CONTINENTE:
   • África: 54 país(es)
   • América: 35 país(es)
   • Asia: 48 país(es)
   • Europa: 44 país(es)
   • Oceanía: 14 país(es)
======================================================================
```

### Ejemplo 7: Manejo de Entradas Inválidas

**Entrada vacía (presionar ENTER sin escribir):**

```
➤ Seleccione una opción: [ENTER]
```

**Salida:**

```
 Por favor ingrese un número (no deje vacío).
➤ Seleccione una opción: _
```

**Entrada no numérica:**

```
➤ Seleccione una opción: abc
```

**Salida:**

```
 Entrada inválida. Ingrese un número entero válido.
➤ Seleccione una opción: _
```

**Entrada fuera de rango:**

```
➤ Seleccione una opción: 15
```

**Salida:**

```
 El valor no puede ser mayor que 9
➤ Seleccione una opción: _
```

### Ejemplo 8: Salir del Programa

**Entrada:**

```
➤ Seleccione una opción: 0
```

**Salida:**

```
 ¡Gracias por usar el sistema! Hasta luego.
```

---

## 👥 Participación de los Integrantes

Este trabajo integrador fue desarrollado de manera colaborativa.

Integrante N°1: Brian Rampone (Investigación y Desarrollo)
Integrante N°2: Octavio Medina(Desarrollo)
Integrante N°3: Juan Deliberto(Investigación y Desarrollo)

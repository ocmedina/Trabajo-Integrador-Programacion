"""
Sistema de Gestión de Datos de Países
Trabajo Práctico Integrador - Programación 1
"""

import csv
import os


# ============================================================================
# FUNCIONES DE CARGA Y VALIDACIÓN DE DATOS
# ============================================================================

def cargar_paises_desde_csv(nombre_archivo):
    """
    Carga los datos de países desde un archivo CSV.
    
    Args:
        nombre_archivo (str): Ruta del archivo CSV
        
    Returns:
        list: Lista de diccionarios con información de países
    """
    paises = []
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for linea_numero, fila in enumerate(lector, start=2):
            # Validar y convertir datos
            pais = {
                'nombre': fila['nombre'].strip(),
                'poblacion': int(fila['poblacion']),
                'superficie': int(fila['superficie']),
                'continente': fila['continente'].strip()
            }
            paises.append(pais)
                
    print(f"✓ Se cargaron {len(paises)} países correctamente.\n")
    return paises


# ============================================================================
# FUNCIONES DE BÚSQUEDA Y FILTRADO
# ============================================================================

def buscar_pais_por_nombre(paises, nombre_busqueda):
    """
    Busca países cuyo nombre contenga el texto proporcionado.
    
    Args:
        paises (list): Lista de países
        nombre_busqueda (str): Texto a buscar
        
    Returns:
        list: Países que coinciden con la búsqueda
    """
    nombre_busqueda = nombre_busqueda.lower()
    resultados = [p for p in paises if nombre_busqueda in p['nombre'].lower()]
    return resultados


def filtrar_por_continente(paises, continente):
    """
    Filtra países por continente.
    
    Args:
        paises (list): Lista de países
        continente (str): Nombre del continente
        
    Returns:
        list: Países del continente especificado
    """
    continente = continente.lower()
    resultados = [p for p in paises if p['continente'].lower() == continente]
    return resultados


def filtrar_por_rango_poblacion(paises, poblacion_min, poblacion_max):
    """
    Filtra países por rango de población.
    
    Args:
        paises (list): Lista de países
        poblacion_min (int): Población mínima
        poblacion_max (int): Población máxima
        
    Returns:
        list: Países dentro del rango especificado
    """
    resultados = [p for p in paises 
                  if poblacion_min <= p['poblacion'] <= poblacion_max]
    return resultados


def filtrar_por_rango_superficie(paises, superficie_min, superficie_max):
    """
    Filtra países por rango de superficie.
    
    Args:
        paises (list): Lista de países
        superficie_min (int): Superficie mínima en km²
        superficie_max (int): Superficie máxima en km²
        
    Returns:
        list: Países dentro del rango especificado
    """
    resultados = [p for p in paises 
                  if superficie_min <= p['superficie'] <= superficie_max]
    return resultados


# ============================================================================
# FUNCIONES DE ORDENAMIENTO
# ============================================================================

def ordenar_por_nombre(paises, descendente=False):
    """
    Ordena países alfabéticamente por nombre.
    
    Args:
        paises (list): Lista de países
        descendente (bool): Si True, ordena de Z a A
        
    Returns:
        list: Lista ordenada de países
    """
    return sorted(paises, key=lambda p: p['nombre'], reverse=descendente)


def ordenar_por_poblacion(paises, descendente=False):
    """
    Ordena países por población.
    
    Args:
        paises (list): Lista de países
        descendente (bool): Si True, ordena de mayor a menor
        
    Returns:
        list: Lista ordenada de países
    """
    return sorted(paises, key=lambda p: p['poblacion'], reverse=descendente)


def ordenar_por_superficie(paises, descendente=False):
    """
    Ordena países por superficie.
    
    Args:
        paises (list): Lista de países
        descendente (bool): Si True, ordena de mayor a menor
        
    Returns:
        list: Lista ordenada de países
    """
    return sorted(paises, key=lambda p: p['superficie'], reverse=descendente)


# ============================================================================
# FUNCIONES DE ESTADÍSTICAS
# ============================================================================

def pais_con_mayor_poblacion(paises):
    """
    Encuentra el país con mayor población.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        dict: País con mayor población
    """
    if not paises:
        return None
    return max(paises, key=lambda p: p['poblacion'])


def pais_con_menor_poblacion(paises):
    """
    Encuentra el país con menor población.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        dict: País con menor población
    """
    if not paises:
        return None
    return min(paises, key=lambda p: p['poblacion'])


def promedio_poblacion(paises):
    """
    Calcula el promedio de población de los países.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        float: Promedio de población
    """
    if not paises:
        return 0
    total = sum(p['poblacion'] for p in paises)
    return total / len(paises)


def promedio_superficie(paises):
    """
    Calcula el promedio de superficie de los países.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        float: Promedio de superficie
    """
    if not paises:
        return 0
    total = sum(p['superficie'] for p in paises)
    return total / len(paises)


def cantidad_por_continente(paises):
    """
    Cuenta la cantidad de países por continente.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        dict: Diccionario con continentes y cantidad de países
    """
    conteo = {}
    for pais in paises:
        continente = pais['continente']
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo


# ============================================================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================================================

def mostrar_pais(pais):
    """
    Muestra la información de un país de forma formateada.
    
    Args:
        pais (dict): Diccionario con datos del país
    """
    print(f"\n{'─' * 60}")
    print(f"  País: {pais['nombre']}")
    print(f"  Población: {pais['poblacion']:,} habitantes")
    print(f"  Superficie: {pais['superficie']:,} km²")
    print(f"  Continente: {pais['continente']}")
    print(f"{'─' * 60}")


def mostrar_lista_paises(paises):
    """
    Muestra una lista de países de forma tabular.
    
    Args:
        paises (list): Lista de países a mostrar
    """
    if not paises:
        print("\n No se encontraron países.")
        return
    
    print(f"\n{'=' * 90}")
    print(f"{'NOMBRE':<25} {'POBLACIÓN':>15} {'SUPERFICIE (km²)':>18} {'CONTINENTE':<20}")
    print(f"{'=' * 90}")
    
    for pais in paises:
        print(f"{pais['nombre']:<25} {pais['poblacion']:>15,} "
              f"{pais['superficie']:>18,} {pais['continente']:<20}")
    
    print(f"{'=' * 90}")
    print(f"Total de países: {len(paises)}\n")


def mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales de los países.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("\n No hay datos para calcular estadísticas.")
        return
    
    print("\n" + "=" * 70)
    print("                    ESTADÍSTICAS GENERALES")
    print("=" * 70)
    
    # País con mayor y menor población
    mayor_pob = pais_con_mayor_poblacion(paises)
    menor_pob = pais_con_menor_poblacion(paises)
    
    print(f"\n POBLACIÓN:")
    print(f"   • Mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab.)")
    print(f"   • Menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab.)")
    print(f"   • Promedio: {promedio_poblacion(paises):,.0f} habitantes")
    
    # Promedio de superficie
    print(f"\n  SUPERFICIE:")
    print(f"   • Promedio: {promedio_superficie(paises):,.0f} km²")
    
    # Cantidad por continente
    print(f"\n DISTRIBUCIÓN POR CONTINENTE:")
    conteo = cantidad_por_continente(paises)
    for continente, cantidad in sorted(conteo.items()):
        print(f"   • {continente}: {cantidad} país(es)")
    
    print("=" * 70 + "\n")


# ============================================================================
# FUNCIONES DEL MENÚ
# ============================================================================

def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Lee un número entero validado del usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar
        minimo (int): Valor mínimo permitido
        maximo (int): Valor máximo permitido
        
    Returns:
        int: Número entero validado
    """
    while True:
        entrada = input(mensaje)
        # No cerrar si el usuario presiona ENTER sin ingresar nada
        if entrada.strip() == "":
            print(" Por favor ingrese un número (no deje vacío).")
            continue

        try:
            valor = int(entrada)
        except ValueError:
            print(" Entrada inválida. Ingrese un número entero válido.")
            continue

        if minimo is not None and valor < minimo:
            print(f" El valor debe ser al menos {minimo}")
            continue
        if maximo is not None and valor > maximo:
            print(f" El valor no puede ser mayor que {maximo}")
            continue
        return valor


def menu_principal():
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + "=" * 70)
    print("           SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 70)
    print("\n MENÚ PRINCIPAL:")
    print("  1. Buscar país por nombre")
    print("  2. Filtrar países por continente")
    print("  3. Filtrar países por rango de población")
    print("  4. Filtrar países por rango de superficie")
    print("  5. Ordenar países por nombre")
    print("  6. Ordenar países por población")
    print("  7. Ordenar países por superficie")
    print("  8. Mostrar estadísticas generales")
    print("  9. Mostrar todos los países")
    print("  0. Salir")
    print("=" * 70)


def ejecutar_opcion(opcion, paises):
    """
    Ejecuta la opción seleccionada del menú.
    
    Args:
        opcion (int): Número de opción seleccionada
        paises (list): Lista de países
    """
    if opcion == 1:
        # Buscar país por nombre
        nombre = input("\n Ingrese el nombre del país a buscar: ")
        resultados = buscar_pais_por_nombre(paises, nombre)
        mostrar_lista_paises(resultados)
        
    elif opcion == 2:
        # Filtrar por continente
        continente = input("\n Ingrese el continente: ")
        resultados = filtrar_por_continente(paises, continente)
        mostrar_lista_paises(resultados)
        
    elif opcion == 3:
        # Filtrar por rango de población
        print("\n Filtrar por rango de población:")
        pob_min = leer_entero("   Población mínima: ", minimo=0)
        pob_max = leer_entero("   Población máxima: ", minimo=pob_min)
        resultados = filtrar_por_rango_poblacion(paises, pob_min, pob_max)
        mostrar_lista_paises(resultados)
        
    elif opcion == 4:
        # Filtrar por rango de superficie
        print("\n Filtrar por rango de superficie:")
        sup_min = leer_entero("   Superficie mínima (km²): ", minimo=0)
        sup_max = leer_entero("   Superficie máxima (km²): ", minimo=sup_min)
        resultados = filtrar_por_rango_superficie(paises, sup_min, sup_max)
        mostrar_lista_paises(resultados)
        
    elif opcion == 5:
        # Ordenar por nombre
        print("\n Ordenar por nombre:")
        print("  1. Ascendente (A-Z)")
        print("  2. Descendente (Z-A)")
        orden = leer_entero("Seleccione: ", minimo=1, maximo=2)
        resultados = ordenar_por_nombre(paises, descendente=(orden == 2))
        mostrar_lista_paises(resultados)
        
    elif opcion == 6:
        # Ordenar por población
        print("\n Ordenar por población:")
        print("  1. Ascendente (menor a mayor)")
        print("  2. Descendente (mayor a menor)")
        orden = leer_entero("Seleccione: ", minimo=1, maximo=2)
        resultados = ordenar_por_poblacion(paises, descendente=(orden == 2))
        mostrar_lista_paises(resultados)
        
    elif opcion == 7:
        # Ordenar por superficie
        print("\n  Ordenar por superficie:")
        print("  1. Ascendente (menor a mayor)")
        print("  2. Descendente (mayor a menor)")
        orden = leer_entero("Seleccione: ", minimo=1, maximo=2)
        resultados = ordenar_por_superficie(paises, descendente=(orden == 2))
        mostrar_lista_paises(resultados)
        
    elif opcion == 8:
        # Mostrar estadísticas
        mostrar_estadisticas(paises)
        
    elif opcion == 9:
        # Mostrar todos los países
        mostrar_lista_paises(paises)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal del programa.
    """
    print("\n" + "" * 35)
    print("  Bienvenido al Sistema de Gestión de Datos de Países")
    print("" * 35 + "\n")
    
    # Cargar datos desde CSV
    nombre_archivo = input("Ingrese el nombre del archivo CSV (ej: paises.csv): ")
    paises = cargar_paises_desde_csv(nombre_archivo)
    
    if not paises:
        print("\n No se pudieron cargar los datos. El programa terminará.")
        return
    
    # Bucle principal del programa
    while True:
        menu_principal()
        opcion = leer_entero("\n➤ Seleccione una opción: ", minimo=0, maximo=9)
        
        if opcion == 0:
            print("\n ¡Gracias por usar el sistema! Hasta luego.\n")
            break
        
        ejecutar_opcion(opcion, paises)
        input("\n⏎ Presione ENTER para continuar...")


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()
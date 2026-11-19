"""
Módulo: M2S8 - Entrega final del proyecto (Fundamentos de Python)
Descripción: Consolidación del Reto 1 (Generador y Validador de Contraseñas) 
y Reto 2 (Plano Cartesiano y Cuadrantes) mediante un menú interactivo y 
manejo robusto de excepciones.
Autor: Fabian Calvache
"""

def mostrar_menu():
    """Muestra el menú principal de opciones para navegar entre los retos."""
    print("\n" + "=" * 45)
    print("      MENÚ PRINCIPAL - PROYECTO M2")
    print("=" * 45)
    print("1. Reto 1: Generador y Validador de Contraseñas")
    print("2. Reto 2: Localizador de Cuadrantes en el Plano")
    print("3. Salir del programa")
    print("=" * 45)


def reto_contraseñas():
    """Ejecuta el Reto 1: Generación a partir de palabras y validación de longitud."""
    print("\n--- RETO 1: GENERADOR Y VALIDADOR DE CONTRASEÑAS ---")
    
    # Captura de palabras dadas por el usuario (siguiendo el ejemplo base)
    palabra1 = input("Introduce la primera palabra: ")
    palabra2 = input("Introduce la segunda palabra: ")
    palabra3 = input("Introduce la tercera palabra: ")

    # Validación y relleno si la palabra tiene menos de 2 caracteres
    if len(palabra1) < 2:
        palabra1 = palabra1.ljust(2, "x")
    if len(palabra2) < 2:
        palabra2 = palabra2.ljust(2, "x")
    if len(palabra3) < 2:
        palabra3 = palabra3.ljust(2, "x")

    # Generación de la contraseña combinada
    contrasena = (palabra1[0] + palabra2[0] + palabra3[0] + 
                  palabra1[1] + palabra2[1] + palabra3[1])
    
    print(f"\n[+] La contraseña generada es: {contrasena}")

    # Validación interactiva con el usuario
    print("\nValidación de longitud de contraseña:")
    contrasena_usuario = input("Introduce una contraseña para verificar: ")
    
    # Estructuras de control condicionales para comparar longitudes
    if len(contrasena_usuario) < len(contrasena):
        faltan = len(contrasena) - len(contrasena_usuario)
        print(f"Faltan {faltan} caracteres.")
    elif len(contrasena_usuario) > len(contrasena):
        sobran = len(contrasena_usuario) - len(contrasena)
        print(f"Sobran {sobran} caracteres.")
    else:
        print("¡La contraseña es correcta en longitud!")


def reto_cuadrantes():
    """Ejecuta el Reto 2: Coordenadas cartesianas, casting y validación de excepciones."""
    print("\n--- RETO 2: LOCALIZADOR DE CUADRANTES ---")
    print("Ingrese las coordenadas del punto en el plano cartesiano.")

    # Uso de estructuras try-except para demostrar dominio de casting (string a float/int)
    try:
        x = float(input("Ingrese la coordenada X: "))
        y = float(input("Ingrese la coordenada Y: "))
    except ValueError:
        print("[ERROR] Debe ingresar valores numéricos válidos (enteros o decimales).")
        return

    # Lógica de evaluación de cuadrantes y ejes
    print(f"\nCoordenada ingresada: P({x}, {y})")

    if x == 0 and y == 0:
        print("El punto se encuentra en el ORIGEN (0, 0).")
    elif x == 0:
        print("El punto se encuentra sobre el EJE Y.")
    elif y == 0:
        print("El punto se encuentra sobre el EJE X.")
    elif x > 0 and y > 0:
        print("El punto se encuentra en el CUADRANTE I (+, +).")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el CUADRANTE II (-, +).")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el CUADRANTE III (-, -).")
    else:
        print("El punto se encuentra en el CUADRANTE IV (+, -).")


def main():
    """Controlador principal del programa mediante bucle while."""
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            
            if opcion == 1:
                reto_contraseñas()
            elif opcion == 2:
                reto_cuadrantes()
            elif opcion == 3:
                print("\n¡Gracias por usar el programa! Saliendo...")
                break
            else:
                print("\n[ADVERTENCIA] Opción inválida. Por favor, elija entre 1 y 3.")
        
        except ValueError:
            print("\n[ERROR] Entrada inválida. Ingrese un número entero.")


if __name__ == "__main__":
    main()
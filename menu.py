def mostrar_menu():
    print("Seleccione una opción para continuar:")
    print("1. Préstamos Recientes")
    print("2. Últimos libros ingresados")
    print("3. Salir")

def prestamos_recientes():
    print("Mostrando los préstamos recientes...")

def ultimos_libros_ingresados():
    print("Mostrando los últimos libros ingresados...")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            prestamos_recientes()
        elif opcion == "2":
            ultimos_libros_ingresados()
        elif opcion == "3":
            print("¡Nos Vemos!")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name__ == "Biblioteca":
    main()
# Función que convierte metros a otras unidades
def convertir_unidades(metros):
    # Aquí utilizo un tipo de dato float para almacenar las conversiones.
    kilometros = metros / 1000.0  # Convierto metros a kilómetros
    centimetros = metros * 100.0  # Convierto metros a centímetros
    milimetros = metros * 1000.0  # Convierto metros a milímetros
    
    return kilometros, centimetros, milimetros

# Función para mostrar los resultados
def mostrar_resultados(metros, kilometros, centimetros, milimetros):
    # Aquí utilizo el tipo de dato string para mostrar los resultados de manera legible
    print(f"{metros} metros equivalen a:")
    print(f"{kilometros:.3f} kilómetros")
    print(f"{centimetros} centímetros")
    print(f"{milimetros} milímetros")

# Función principal que ejecuta el programa
def main():
    # Utilizo un tipo de dato booleano para controlar si el usuario quiere continuar
    continuar = True
    
    while continuar:
        # Aquí uso un tipo de dato float para pedirle al usuario la cantidad de metros
        metros = float(input("Ingresa la cantidad de metros que deseas convertir: "))
        
        # Llamo a la función de conversión para obtener las equivalencias en otras unidades
        kilometros, centimetros, milimetros = convertir_unidades(metros)
        
        # Llamo a la función para mostrar los resultados de la conversión
        mostrar_resultados(metros, kilometros, centimetros, milimetros)
        
        # Aquí pregunto al usuario si desea continuar con otra conversión
        respuesta = input("¿Deseas realizar otra conversión? (s/n): ")
        if respuesta.lower() != 's':  # Si la respuesta no es 's', salgo del bucle
            continuar = False
            print("¡Gracias por usar el conversor de unidades!")

# Llamo a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()

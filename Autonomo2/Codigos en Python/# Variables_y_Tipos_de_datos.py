# Variables_y_Tipos_de_datos.py - Traducción del pseudocódigo PSeInt
# Relacionado con "Variables" y "Tipos de datos"

def registrar_estudiantes():
    print("=== REGISTRO DE ESTUDIANTES ===")
    
    continuar = 1
    estudiantes = []
    
    while continuar == 1:
        print("\n--- Nuevo Estudiante ---")
        
        # Solicitar datos del estudiante
        id_estudiante = input("Ingrese ID (Número de cédula): ")
        nombre = input("Ingrese su nombre: ")
        
        # Validar edad
        edad_valida = False
        while not edad_valida:
            try:
                edad = int(input("Ingrese su edad: "))
                if edad <= 0:
                    print("¡Error! La edad debe ser mayor que 0. Intente de nuevo.")
                else:
                    edad_valida = True
            except ValueError:
                print("¡Error! Debe ingresar un número válido.")
        
        # Registrar estudiante
        estudiante = {
            'id': id_estudiante,
            'nombre': nombre,
            'edad': edad
        }
        estudiantes.append(estudiante)
        
        print(f"\n✓ Estudiante registrado: {id_estudiante} - {nombre} - {edad} años")
        
        # Preguntar si desea continuar
        print("\n¿Desea registrar otro estudiante?")
        respuesta = input("1 = Sí, 0 = No: ")
        
        while respuesta not in ['0', '1']:
            print("Opción no válida. Por favor ingrese 1 o 0.")
            respuesta = input("1 = Sí, 0 = No: ")
        
        continuar = int(respuesta)
    
    # Mostrar resumen
    print("\n" + "="*50)
    print("RESUMEN DEL REGISTRO")
    print("="*50)
    print(f"Total de estudiantes registrados: {len(estudiantes)}")
    
    if len(estudiantes) > 0:
        print("\nLista de estudiantes:")
        for i, estudiante in enumerate(estudiantes, 1):
            print(f"{i}. ID: {estudiante['id']} | Nombre: {estudiante['nombre']} | Edad: {estudiante['edad']}")
    
    print("\n¡Programa finalizado!")

# Ejecutar el programa
if __name__ == "__main__":
    registrar_estudiantes()
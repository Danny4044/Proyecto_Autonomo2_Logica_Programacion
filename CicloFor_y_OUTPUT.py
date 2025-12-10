# CicloFor_y_OUTPUT.py - Traducción del pseudocódigo PSeInt
# DEMOSTRACIÓN SIMPLE DE FOR Y OUTPUT (salida)

def demostracion_ciclo_for():
    print("="*50)
    print("     DEMOSTRACIÓN DE CICLO FOR Y OUTPUT")
    print("="*50)
    
    # 1. FOR con OUTPUT básico
    print("\n1. CONTANDO DEL 1 AL 3:")
    print("-" * 30)
    
    for i in range(1, 4):  # range(1, 4) genera [1, 2, 3]
        print(f"   Iteración #{i}")
    
    # 2. FOR con cálculos
    print("\n" + "="*50)
    print("2. CUADRADOS DEL 1 AL 5:")
    print("-" * 30)
    
    for i in range(1, 6):  # range(1, 6) genera [1, 2, 3, 4, 5]
        cuadrado = i * i
        print(f"   {i}² = {cuadrado}")
    
    # 3. FOR con lista (arreglo)
    print("\n" + "="*50)
    print("3. LISTA DE FRUTAS:")
    print("-" * 30)
    
    # Crear lista de frutas (en Python los índices comienzan en 0)
    frutas = ["Manzana", "Banana", "Naranja", "Uva"]
    
    # Mostrar frutas usando ciclo for
    print("   Lista completa de frutas:")
    for i in range(len(frutas)):
        print(f"   {i+1}. {frutas[i]}")
    
    # Alternativa: usando enumerate (más pythonico)
    print("\n   Usando enumerate (índice y valor):")
    for indice, fruta in enumerate(frutas, 1):
        print(f"   {indice}. {fruta}")
    
    # 4. FOR con lista de estudiantes
    print("\n" + "="*50)
    print("4. LISTA DE ESTUDIANTES:")
    print("-" * 30)
    
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "promedio": 8.5},
        {"nombre": "Luis", "edad": 22, "promedio": 7.8},
        {"nombre": "María", "edad": 21, "promedio": 9.2},
        {"nombre": "Carlos", "edad": 23, "promedio": 6.5}
    ]
    
    print("   Información de estudiantes:")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"\n   Estudiante #{i}:")
        print(f"     Nombre: {estudiante['nombre']}")
        print(f"     Edad: {estudiante['edad']} años")
        print(f"     Promedio: {estudiante['promedio']}")
        
        # Determinar estado según promedio
        if estudiante['promedio'] >= 7:
            estado = "APROBADO"
        elif estudiante['promedio'] >= 5:
            estado = "RECUPERACIÓN"
        else:
            estado = "REPROBADO"
        
        print(f"     Estado: {estado}")
    
    # RESUMEN
    print("\n" + "="*50)
    print("RESUMEN DE LA DEMOSTRACIÓN")
    print("="*50)
    
    total_ciclos_for = 4
    lineas_output = 35  # Aproximadamente
    
    print(f"Ciclos FOR utilizados: {total_ciclos_for}")
    print(f"Líneas de OUTPUT generadas: {lineas_output}")
    print(f"Elementos procesados: {len(frutas)} frutas y {len(estudiantes)} estudiantes")
    
    # Estadísticas adicionales
    print("\nEstadísticas adicionales:")
    print(f"- Rango más usado: range(1, n)")
    print(f"- Listas procesadas: {len(frutas) + len(estudiantes)}")
    print(f"- Total de iteraciones: {3 + 5 + len(frutas)*2 + len(estudiantes)}")
    
    print("\n" + "="*50)
    print("¡DEMOSTRACIÓN COMPLETADA EXITOSAMENTE!")
    print("="*50)

# Función adicional para mostrar diferentes tipos de FOR
def tipos_de_ciclo_for():
    print("\n" + "="*50)
    print("TIPOS DE CICLO FOR EN PYTHON")
    print("="*50)
    
    # FOR con paso (incremento)
    print("\n1. For con paso de 2:")
    for i in range(0, 11, 2):
        print(f"   Número: {i}")
    
    # FOR descendente
    print("\n2. For descendente:")
    for i in range(10, 0, -1):
        print(f"   Cuenta regresiva: {i}")
    
    # FOR con lista de strings
    print("\n3. For con lista de strings:")
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Morado"]
    for color in colores:
        print(f"   Color: {color}")

# Ejecutar el programa
if __name__ == "__main__":
    demostracion_ciclo_for()
    
    # Preguntar si desea ver tipos adicionales
    respuesta = input("\n¿Desea ver tipos adicionales de ciclo FOR? (s/n): ")
    if respuesta.lower() == 's':
        tipos_de_ciclo_for()
    
    print("\n" + "="*50)
    print("PROGRAMA FINALIZADO")
    print("="*50)
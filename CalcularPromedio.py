# CalcularPromedio.py - Traducción del pseudocódigo PSeInt
# Demuestra estructura de decisión y uso de operadores relacionales

def calcular_promedio_estado():
    print("="*45)
    print("       CALCULADORA DE PROMEDIO Y ESTADO")
    print("="*45)
    print("\nINSTRUCCIONES:")
    print("• Ingrese las notas del estudiante (debe estar entre 0 y 10)")
    print("• Para finalizar, ingrese: -1")
    print("-"*45)
    
    # Variables para el cálculo
    suma = 0
    cantidad_notas = 0
    notas = []
    
    # Bucle principal para ingresar notas
    while True:
        try:
            # Mostrar número de nota actual
            entrada = input(f"\nIngrese la nota #{cantidad_notas + 1}: ")
            nota = float(entrada)
            
            # Verificar si el usuario quiere terminar
            if nota == -1:
                if cantidad_notas > 0:
                    print("\n✓ Finalizando ingreso de notas...")
                    break
                else:
                    print("❌ ERROR: Debe ingresar al menos una nota antes de terminar.")
                    print("   Por favor, ingrese una nota entre 0 y 10.")
                    continue
            
            # Validar que la nota esté en el rango 0-10
            if nota < 0 or nota > 10:
                print("❌ ERROR: La nota debe estar entre 0 y 10.")
                print("   Por favor, ingrese un valor válido.")
                continue
            
            # Nota válida, procesar
            notas.append(nota)
            suma += nota
            cantidad_notas += 1
            
            print(f"✓ Nota #{cantidad_notas} registrada: {nota}")
            
        except ValueError:
            print("❌ ERROR: Debe ingresar un número válido.")
    
    # Verificar que haya notas para calcular
    if cantidad_notas == 0:
        print("\n" + "="*45)
        print("No se ingresaron notas para calcular el promedio.")
        print("="*45)
        return
    
    # Calcular y mostrar resultados
    print("\n" + "="*45)
    print("RESULTADOS:")
    print("="*45)
    
    promedio = suma / cantidad_notas
    
    print(f"Cantidad de notas ingresadas: {cantidad_notas}")
    print(f"Suma total de notas: {suma}")
    print(f"Promedio calculado: {promedio:.2f}")
    
    # Mostrar todas las notas
    print("\nNotas ingresadas:")
    for i, nota in enumerate(notas, 1):
        print(f"  Nota #{i}: {nota}")
    
    # Determinar estado según el promedio
    print("\n" + "-"*45)
    print("ESTADO ACADÉMICO:")
    
    if promedio >= 7:
        estado = "APROBADO"
        mensaje = "✓ ¡Felicidades! Has aprobado."
    elif promedio >= 5:
        estado = "RECUPERACIÓN"
        mensaje = "⚠️  Necesitas rendir examen de recuperación."
    else:
        estado = "REPROBADO"
        mensaje = "❌ Debes repetir la materia."
    
    print(f"  Promedio: {promedio:.2f}")
    print(f"  Estado: {estado}")
    print(f"  {mensaje}")
    
    print("\n" + "="*45)
    print("¡Proceso completado!")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_promedio_estado()
# Ingresar_Calificaciones.py - Traducción del pseudocódigo PSeInt
# Demuestra bucle while y control de entrada

def ingresar_calificaciones():
    print("=== SISTEMA DE INGRESO DE CALIFICACIONES ===")
    
    # Ingresar ID del estudiante
    id_estudiante = input("\nIngrese ID del estudiante: ")
    
    # Simular búsqueda en base de datos
    encontrado = True  # En un sistema real, esto consultaría una base de datos
    
    if not encontrado:
        print(f"\n❌ Estudiante con ID '{id_estudiante}' no encontrado.")
        return
    
    print(f"\n✅ Estudiante {id_estudiante} encontrado.")
    print("\n" + "="*60)
    print("INSTRUCCIONES:")
    print("- Ingrese notas en el rango de 0.0 a 10.0")
    print("- Para finalizar, ingrese: -1")
    print("="*60)
    
    # Lista para almacenar notas
    notas = []
    contador_notas = 0
    
    # Bucle para ingresar notas
    while True:
        try:
            # Solicitar nota
            entrada = input(f"\nIngrese la nota #{contador_notas + 1} (o -1 para finalizar): ")
            nota = float(entrada)
            
            # Verificar si el usuario quiere finalizar
            if nota == -1:
                if len(notas) > 0:
                    print("\n⚠️  Finalizando ingreso de notas...")
                    break
                else:
                    print("⚠️  Debe ingresar al menos una nota antes de finalizar.")
                    continue
            
            # Validar rango de la nota
            if nota < 0 or nota > 10:
                print("❌ Error: La nota debe estar entre 0.0 y 10.0")
                print("   Por favor, ingrese un valor válido.")
                continue
            
            # Nota válida, agregar a la lista
            notas.append(nota)
            contador_notas += 1
            print(f"✓ Nota #{contador_notas} registrada: {nota}")
            
        except ValueError:
            print("❌ Error: Debe ingresar un número válido (ej: 8.5, 7, 9.0)")
    
    # Mostrar resumen
    print("\n" + "="*50)
    print("RESUMEN DE CALIFICACIONES")
    print("="*50)
    print(f"ID del Estudiante: {id_estudiante}")
    print(f"Total de notas ingresadas: {len(notas)}")
    
    if len(notas) > 0:
        print("\nNotas ingresadas:")
        for i, nota in enumerate(notas, 1):
            print(f"  Nota #{i}: {nota}")
        
        # Calcular estadísticas
        promedio = sum(notas) / len(notas)
        nota_max = max(notas)
        nota_min = min(notas)
        
        print("\nEstadísticas:")
        print(f"  • Promedio: {promedio:.2f}")
        print(f"  • Nota más alta: {nota_max}")
        print(f"  • Nota más baja: {nota_min}")
    
    print("\n¡Proceso completado exitosamente!")

# Ejecutar el programa
if __name__ == "__main__":
    ingresar_calificaciones()
Proceso CalcularPromedioYEstado
	// Demuestra estructura de decisión y uso de operadores relacionales.
    // Versión con validación de rango 0-10 por cada nota
    Definir suma, promedio, nota Como Real;
    Definir cantidad_notas, i Como Entero;
    Definir continuar Como Logico;
    suma <- 0;
    cantidad_notas <- 0;
    continuar <- Verdadero;
	Escribir "";
    Escribir "======== BIENVENIDO ======";
	Escribir "";
    Escribir "Ingrese las notas del estudiante (debe estar entre 0 y 10)";
    Escribir "===DEBE INGRESAR -1 PARA FINALIZAR EL INGRESO DE NOTAS===";
    Escribir "";
    
    Mientras continuar Hacer
        // Mostrar el número de la nota actual
        Escribir "Ingrese la nota ", cantidad_notas+1, ": ";
        Leer nota;
        // Verificar si el usuario quiere terminar
        Si nota = -1 Entonces
            // Solo permitir terminar si ya hay al menos una nota válida
            Si cantidad_notas > 0 Entonces
                continuar <- Falso;
            Sino
                Escribir "ERROR: Debe ingresar al menos una nota antes de terminar.";
                Escribir "Por favor, ingrese una nota entre 0 y 10.";
            FinSi
        Sino
            // Validar que la nota esté en el rango 0-10
            Si (nota >= 0) Y (nota <= 10) Entonces
                // Nota válida, agregar a la suma
                suma <- suma + nota;
                cantidad_notas <- cantidad_notas + 1;
                Escribir "Nota ", cantidad_notas, " registrada: ", nota;
            Sino
                // Nota fuera de rango, mostrar error
                Escribir "Error: La nota debe estar entre 0 y 10.";
                Escribir "Por favor, ingrese un valor válido.";
            FinSi
        FinSi
		
    FinMientras
    
    Escribir "";
    Escribir "=========================================";
    
    // Calcular y mostrar el resultado
    Si cantidad_notas > 0 Entonces
        promedio <- suma / cantidad_notas;
        Escribir "RESULTADOS:";
        Escribir "Cantidad de notas ingresadas: ", cantidad_notas;
        Escribir "Suma total de notas: ", suma;
        Escribir "Promedio: ", promedio;
        
        // Validar que el promedio esté en rango 0-10
        Si (promedio >= 0) Y (promedio <= 10) Entonces
            // Ahora evaluar el estado
            Si promedio >= 7 Entonces
                Escribir "Estado: APROBADO";
            Sino
                Si promedio >= 5 Entonces
                    Escribir "Estado: RECUPERACIÓN";
                Sino
                    Escribir "Estado: REPROBADO";
                FinSi
            FinSi
        Sino
            Escribir "Error: El promedio calculado está fuera del rango 0-10.";
        FinSi
    Sino
        Escribir "No se ingresaron notas para calcular el promedio.";
    FinSi
    
    Escribir "=========================================";
FinProceso

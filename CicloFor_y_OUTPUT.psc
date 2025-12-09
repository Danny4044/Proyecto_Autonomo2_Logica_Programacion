Proceso CicloFor
    // DEMOSTRACIÓN SIMPLE DE FOR Y OUTPUT (salida)
    
    Definir i Como Entero;
    
    // 1. FOR con OUTPUT
    Escribir "1. Contando del 1 al 3:";
    Para i <- 1 Hasta 3 Hacer
        Escribir "   Iteración #", i;
    FinPara
    
    // 2. FOR con cálculos
    Escribir "";
    Escribir "2. Cuadrados del 1 al 5:";
    Para i <- 1 Hasta 5 Hacer
        Escribir "   ", i, "² = ", i*i;
    FinPara
    
    // 3. FOR con arreglo (CORREGIDO: índices comienzan en 1)
    Escribir "";
    Escribir "3. Lista de frutas:";
    Dimension frutas[4];
    frutas[1] <- "Manzana";  // Índice 1
    frutas[2] <- "Banana";   // Índice 2
    frutas[3] <- "Naranja";  // Índice 3
    frutas[4] <- "Uva";      // Índice 4
    
    // Ciclo FOR: de 1 a 4
    Para i <- 1 Hasta 4 Hacer
        Escribir "   ", i, ". ", frutas[i];
    FinPara
    
    // RESUMEN
    Escribir "";
    Escribir "=== RESUMEN ===";
    Escribir "Ciclos FOR usados: 3";
    Escribir "Líneas de OUTPUT: 13";
    
FinProceso
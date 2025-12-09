Algoritmo IngresarCalificaciones
	// Demuestra bucle while y control de entrada.
	Escribir 'Ingrese ID del estudiante: '
	Leer id
	// Simula la búsqueda...
	Encontrado <- Verdadero
	Si Encontrado=Falso Entonces // en flujo real se consulta en la lista
		Escribir 'Estudiante no encontrado.'
	SiNo
		Escribir 'Ingrese notas de:0.0 a 10.0). Escriba: -1 para Finalizar:'
		Repetir
			Leer nota
			Si nota<>-1 Entonces
				Si nota<0 O nota>10 Entonces
					Escribir 'Nota inválida, debe ser entre 0 y 10.'
				SiNo
					Escribir 'Nota guardada:', nota
					// En código añade la nota en la lista
				FinSi
			FinSi
		Hasta Que nota=-1
	FinSi
FinAlgoritmo

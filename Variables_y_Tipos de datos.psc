Algoritmo RegistrarEstudiantes
	// Relacionado con "Variables" y "Tipos de datos"
	Definir continuar Como Entero
	continuar <- 1
	Mientras continuar=1 Hacer
		Escribir 'Ingrese ID (Número de cédula): '
		Leer id
		Escribir 'Ingrese su nombre: '
		Leer nombre
		Escribir 'Ingrese su edad: '
		Leer edad
		// Validación simple: edad > 0
		Si edad<=0 Entonces
			Escribir 'Edad inválida. Intente de nuevo.'
		SiNo
			Escribir 'Estudiante registrado:', id, '-', nombre, '-', edad
			// Aquí se llamaría al procedimiento GuardarEstudiante
		FinSi
		Escribir 'Registrar otro? 1=Si 0=No: '
		Leer continuar
	FinMientras
FinAlgoritmo

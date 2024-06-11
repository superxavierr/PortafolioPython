#Alumno: Cazares Godinez Brian Xavier
#Fecha: 26 de Abril del 2023
#Descripción: programa que calcula el IMC acorde al género, peso y estatura.

#Solicitar al usuario su peso y estatura.
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en mts: "))

#Calcular el IMC.
imc = peso / (estatura ** 2)

#Determinar en qué rango se encuentra la persona según el IMC.
if imc <= 18:
    peso_tipo = "Debajo de lo normal"
elif imc <= 25:
    peso_tipo = "Peso Normal"
elif imc <= 30:
    peso_tipo = "Sobrepeso"
elif imc <= 35:
    peso_tipo = "Obesidad grado 1"
else:
    peso_tipo = "Obesidad grado 2"

#Calcular el peso ideal según el género de la persona.
estatura_cm = estatura * 100
if input("¿Es usted hombre o mujer? (h/m): ") == "h":
    f1 = 2.7
    f2 = 47.75
else:
    f1 = 2.25
    f2 = 45
peso_ideal = ((estatura_cm - 152.4) / 2.54) * f1 + f2

#Determinar si la persona está en su peso ideal.
if abs(peso - peso_ideal) <= 0.1 * peso_ideal:
    peso_ideal_tipo = "Peso Ideal"
elif peso < peso_ideal:
    peso_ideal_tipo = "Debajo de su peso ideal"
else:
    peso_ideal_tipo = "Sobrepeso"

#Imprimir los resultados.
print("Su IMC es:", imc)
print("Su peso se encuentra en la categoría de:", peso_tipo)
print("Su peso ideal es:", peso_ideal)
print("Usted tiene:", peso_ideal_tipo)
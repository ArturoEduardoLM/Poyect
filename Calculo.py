gradoPolinomio = 0
coeficientesPolinomio = []
coeficientes = 0
contador= 0
contadorc = 0

gradoPolinomio = int(input("Ingresa el valor máximo del polinomio: "))
contador = gradoPolinomio
while contador <= gradoPolinomio and contador>=0:
    exponenteM = input("Coeficiente del grado " + str(contador) + " :")
    coeficientesPolinomio.insert(contadorc, exponenteM)
    contadorc+=1
    contador-=1
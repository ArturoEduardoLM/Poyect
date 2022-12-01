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

polinomio = 0;
contadorf = 0;
exponente = gradoPolinomio
x = int(input("Ingresa el valor de x: "))
while contadorf <= gradoPolinomio:
    coeficiente = coeficientesPolinomio[contadorf]
    funcion = (int(coeficiente)*int(x))**int(exponente)
    polinomio = polinomio + int(funcion)
    contadorf+=1
    exponente-=1
    
print("Los coeficientes son: " + str(coeficientesPolinomio))
print("EL resultado del polinomio evaluado en " + "(" + str(x) + ")" + " es: " + str(polinomio) )
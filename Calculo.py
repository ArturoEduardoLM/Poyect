Polinomiogra = 0
coeficientesPoli = []
coeficientes = 0
contador= 0
contador2 = 0

Polinomiogra = int(input("Ingresa el valor mas alto del polinomio: "))
contador = Polinomiogra
while contador <= Polinomiogra and contador>=0:
    exponenteM = input("Coeficiente y el grado " + str(contador) + " :")
    Polinomio.insert(contadorc, exponenteM)
    contador2+=1
    contador-=1
polinomio = 0;
contadorf = 0;
exponente = Polinomiogra
x = int(input("Ingresa el valor de x: "))
while contadorf <= gradoPolinomio:
    coeficiente = coeficientesPoli[contadorf]
    funcion = (int(coeficiente)*int(x))**int(exponente)
    polinomio = polinomio + int(funcion)
    contadorf+=1
    exponente-=1
    print("Los coeficientes son: " + str(coeficientesPoli))
print("EL resultado del polinomio evaluado en " + "(" + str(x) + ")" + " es: " + str(polinomio) )
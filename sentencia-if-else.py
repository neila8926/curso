condicion=False


print("Condicion Verdadera") if condicion else print("Codicion Falsa")


if condicion==True:
    print("La Condicion es Verdadera")
elif condicion==False:
    print("La condicion es Falsa")
else:
    print("Condicion no Reconocida")
    
    

numero=int(input("Proporciona un numero entre 1 y 3: "))

if numero==1:
    numeroTexto="numero uno"
elif numero==2:
    numeroTexto="numero dos"
elif numero==3:
    numeroTexto="numero tres"
else:
    numeroTexto="Valor fuera de Rango"

print("Numero Proporcionado: ",numeroTexto)

    
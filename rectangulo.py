try: 
    alto=float(input("Proporciona el alto: "))
    ancho=float(input("Proporciona el ancho: "))

    area=alto*ancho
    perimetro=(alto+ancho)*2
    print("Area: ",area)
    print("Perímetro: ",perimetro)

except:
    print("NO ES UN NUMERO")
    
numero1=int(input("Digite Primer Numero: "))
numero2=int(input("Digite Segundo numero: "))

if(numero1>numero2):
    print("El numero mayo es ",numero1)
elif(numero1<numero2):
    print("El numero mayo es: ",numero2)
else:
    print("SON IGUALES")
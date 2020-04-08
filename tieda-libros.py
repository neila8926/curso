print("PROPORCIONA LOS SIGUIENTES DATOS DEL LIBRO")
nombre=input("Proporciona el nombre: ")
id=int(input("Proporciona el Id: "))
precio=float(input("Proporciona el precio: "))
envioGratuito=input("Indica si el envio es Gratuito (True/False): ")

if envioGratuito=="True" or envioGratuito=="true":
    envioGratuito=True
elif envioGratuito=="False" or envioGratuito=="false":
    envioGratuito=False
else:
    envioGratuito="Valor Incorrecto debe ser True o False"
print("Nombre: ",nombre)
print("Id: ",id)
print("Precion: ",precio)
print("Envio Gratuito?: ",envioGratuito)
print(type(envioGratuito))
    
    
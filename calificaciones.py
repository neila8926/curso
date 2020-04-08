valor=int(input("Digita valor entre 0 y 10: "))
calificacion=None

if valor>=9 and valor<=10:
    calificacion="A"
elif valor>=8 and valor<9:
    calificacion="B"
elif  valor>=7 and valor<8:
    calificacion="C"
elif valor>=6 and  valor<7:
    calificacion="D"
elif valor>=0 and valor<6:
    calificacion="F"
else: 
    calificacion="Valor desconocido"

print(calificacion)
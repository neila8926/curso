a=int(input("Proporciona un Valor: 10"))
valorMinimo=0
valorMaximo=5
dentroRango=(a>=valorMinimo and a<=valorMaximo)
if dentroRango:
    print("Dentro del Rango")
else:
    print("Fuera del Rango")
        
vacaciones=True
descanso=True
if not(vacaciones or descanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")
 
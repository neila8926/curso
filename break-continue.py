#imprimir solo letras A
for letras in "Holanda":
    if letras=="a":
        print("Hola Letra",letras)
        
else:
    print("Fin ciclo For")  

print("Continua...")


#imprimir solo numeros pares
""" for i in range(6):
    if i%2==0:
        print(i) """
    
for i in range(6):
    if i%2!=0:
        
        continue
    print("Este: ",i) 
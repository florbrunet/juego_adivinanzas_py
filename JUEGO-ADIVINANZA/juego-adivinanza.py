
import random

numero_secreto = random.randint(0,100)
cantidad_intentos= 0
cantidad_max_intentos=5
adivinado= False

print("Bienvenido al juevo de adivinar el numero secreto")

while not adivinado:
    if not cantidad_intentos < cantidad_max_intentos:
        print("GAME OVER") 
        break 
        
    entrada = input("Introduce un numero del 0 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:        
        print("Felicitaciones, has adivinado el numero secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero secreto el mayor al numero ingresado")
    else:
        print("El numero secreto el menor al numero ingresado")
    
    cantidad_intentos+=1

    



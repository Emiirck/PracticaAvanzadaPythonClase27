
import random

rango_min = int(input("Elige el límite inferior del rango: "))
rango_max = int(input("Elige el límite superior del rango: "))
intentos_max = int(input("Elige el número máximo de intentos: "))
numero_secreto = random.randint(rango_min, rango_max)

def pedir_adivinanza():
    try:
        return int(input(f"Adivina el número (entre {rango_min} y {rango_max}): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return pedir_adivinanza()

def juego_adivinanza():
    intentos = 0
    while intentos < intentos_max:
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

def main():
    juego_adivinanza()

main()

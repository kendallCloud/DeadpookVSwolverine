from time import sleep
from colorama import Fore, Back, Style
import random

wolverine = {"nombre": "Wolverine", "vida": 0, "minDMG": 10, "maxDMG": 120, "probSkip": 20}
deadpool = {"nombre": "Deadpool", "vida": 0, "minDMG": 10, "maxDMG": 100, "probSkip": 25}

def pintarLetras(nombre):
    if nombre == "Wolverine":
        print( Fore.BLACK + Back.YELLOW + Style.BRIGHT)
    else:
        print( Fore.BLACK + Back.RED + Style.BRIGHT)

def asignar_vida(personaje):
    pintarLetras(personaje['nombre'])
    personaje["vida"] = int(input(f"Inserta la vida de {personaje['nombre']}: "))
    print(Style.RESET_ALL)



print("||=========WOLVERINE VS DEADPOOL!=========||")
def atacar(atacante):
    dmg = getRandomNumber(atacante['minDMG'], atacante['maxDMG'])
    atacado = deadpool if atacante["nombre"] != "Deadpool" else wolverine
    pintarLetras(atacante['nombre'])
    if atacante["nombre"] == atacado["nombre"]:
        print(f"you idiot!!")
    print(f"{atacante["nombre"]} ataca a {atacado["nombre"]} con {dmg} de daño")
    if getRandomNumber(0, 100) <= atacado['probSkip']:
        pintarLetras(atacado["nombre"])
        print(f"{atacado['nombre']} ha esquivado el ataque!")
    else:
        atacado["vida"] -= dmg
        pintarLetras(atacado["nombre"])
        print(f"{atacado['nombre']} ha recibido {dmg} de daño")
        print(f"Vida de {atacado['nombre']}: {atacado['vida']}")

def hayGanador():
    if wolverine['vida'] <= 0:
        pintarLetras(deadpool['nombre'])
        print(f"{deadpool['nombre']} ha ganado!")
        return True
    elif deadpool['vida'] <= 0:
        pintarLetras(wolverine['nombre'])
        print(f"{wolverine['nombre']} ha ganado!")
        return True
    return False


pintarLetras(wolverine['nombre'])
asignar_vida(wolverine)
pintarLetras(deadpool['nombre'])
asignar_vida(deadpool)

print(Style.RESET_ALL)
print(Fore.GREEN + "||=========COMIENZA LA BATALLA!=========||")

def getRandomNumber(min, max):
    return random.randint(min, max)

def Pelea():
    #primer turno 
    if getRandomNumber(0,1) == 0:
        pintarLetras(wolverine['nombre'])
        print(f"{wolverine['nombre']} ataca primero!")
    else:
        pintarLetras(deadpool['nombre'])
        print(f"{deadpool['nombre']} ataca primero!")

    while not hayGanador():
        sleep(3)
        if getRandomNumber(0,1) == 0:
            atacar(wolverine)
        else:
            atacar(deadpool)

Pelea()
    

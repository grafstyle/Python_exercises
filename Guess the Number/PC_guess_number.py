import random

print("\nBienvenido al juego!\nEspero estes listo\n")
number = int(input("Elige un nivel\n(10) Facil\n(50)Medio\n(100)Dificil\n(1000)Insano\n"))

def guess_game(number):
    random_number = random.randint(1, number) 
    x = 0
    while x != random_number:
        x = int(input("Cual es el numero que estoy pensando?\n"))
        if x > random_number:
            print("Ufff pasaste volando mio, devuelvete")
        elif x < random_number:
            print("Te caiste fue? Pa donde va para alla abajo? dale pa arriba")
    print(f"Builao! el numero {x} tenia en mente!")
        

guess_game(number)

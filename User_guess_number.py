import random


number = int(input("Elige un nivel\n(10) Facil\n(50)Medio\n(100)Dificil\n(1000)Insano\n"))
def define_num(number):
    high = number
    low = 1
    feedback = ''
    while feedback.lower() != "c":
        if low != high:
            random_number = random.randint(low, high)
        feedback = input(f"This is your number {random_number} Correct (C), this is to high (H), this is to low (L)" )
        if feedback.lower() == "h":
            high = random_number - 1
        elif feedback.lower() == "l":
            low = random_number + 1
    print("Okay!")
                    
        
      
      
define_num(number)
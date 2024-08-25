import fade
import time
import pygame
import os
import random

def check_if_string(variable):
    return isinstance(variable, str)
time.sleep(0.5)
def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_cmd()
time.sleep(0.5)

text = """ 
 █████╗ ██╗   ██╗███████╗██████╗  █████╗  ██████╗ ███████╗     █████╗ ██╗  ██╗███████╗    ██╗   ██╗███████╗███████╗██████╗ 
██╔══██╗██║   ██║██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗╚██╗██╔╝██╔════╝    ██║   ██║██╔════╝██╔════╝██╔══██╗
███████║██║   ██║█████╗  ██████╔╝███████║██║  ███╗█████╗      ███████║ ╚███╔╝ █████╗      ██║   ██║███████╗█████╗  ██████╔╝
██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██║██║   ██║██╔══╝      ██╔══██║ ██╔██╗ ██╔══╝      ██║   ██║╚════██║██╔══╝  ██╔══██╗
██║  ██║ ╚████╔╝ ███████╗██║  ██║██║  ██║╚██████╔╝███████╗    ██║  ██║██╔╝ ██╗███████╗    ╚██████╔╝███████║███████╗██║  ██║
╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝




"""
print(fade.purplepink(text))
time.sleep(0.5)

# Initialize pygame mixer
pygame.mixer.init()



# Load the music file
pygame.mixer.music.load("lib/music.mp3")

# Play the music file on loop
pygame.mixer.music.play(-1) 

text = "There is a sixth dimension beyond that which is known to man."
print(fade.purplepink(text))
time.sleep(3)

text = "It is a dimension as vast as space, and as timeless as infinity."
print(fade.purplepink(text))
time.sleep(3)


text = "It is the middle ground between light and shadow;"
print(fade.purplepink(text))
time.sleep(3)

text = "between man's grasp and his reach;"
print(fade.purplepink(text))
time.sleep(2)

text = "between science and superstition;"
print(fade.purplepink(text))
time.sleep(2)

text = "between the pit of his fears and the sunlight of his knowledge."
print(fade.purplepink(text))
time.sleep(3)

text = "This is the dimension of imagination.."
print(fade.purplepink(text))
time.sleep(3)

text = "It is an area that might be called..."
print(fade.purplepink(text))
time.sleep(3)


text = "The Simple Calculator V2"
print(fade.purplepink(text))
time.sleep(8)

pygame.mixer.music.stop()

pygame.mixer.music.load("lib/music1.mp3")

pygame.mixer.music.play(-1)

calculator_status = input(fade.purpleblue("Are you ready to use Simple Calculator V2?"))

clear_cmd()

text = """
███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗     ██╗   ██╗██████╗ 
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██║   ██║╚════██╗
███████╗██║██╔████╔██║██████╔╝██║     █████╗      ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    ██║   ██║ █████╔╝
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║     ╚████╔╝ ███████╗
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═══╝  ╚══════╝




"""
print(fade.water(text))
time.sleep(4)

while True:
    number_of_numbers = input(fade.water("How many numbers would you like to enter for this calculation?"))
    try:
        number_of_numbers = int(number_of_numbers)
        if number_of_numbers <= 0:
            print(fade.water("I can't calculate numbers below or equal to 0. Please enter a value above 0!"))
        elif number_of_numbers > 0:
            break
    except ValueError:
        print(fade.water("Please enter an integer!"))

while True:
    operator = input(fade.water("What operator would you like to use?"))
    if operator == "+" or operator == "-" or operator == "*":
        break
    else:
        print(fade.water("Please enter a valid mathematical operator! (division isn't allowed)"))

calculation = 0
calc_list = []
for i in range(number_of_numbers):
    num = int(input(fade.water(f"Number {i + 1}?")))
    calc_list.append(num)

if operator == "*":
    calculation = 1

for i in range(number_of_numbers):
    if operator == "+":
        calculation += calc_list[i]
    if operator == "-":
        calculation -= calc_list[i]
    if operator == "*":
        calculation *= calc_list[i]

print(fade.water(f"The sum of the entered calculation is: {calculation + random.randint(1, 1000000000000000000000000)}"))
time.sleep(5)
print("")
correct_status = input(fade.water("Is the calculation correct? (y/n)"))

print(fade.water("""
Perfect!"""))

time.sleep(4)
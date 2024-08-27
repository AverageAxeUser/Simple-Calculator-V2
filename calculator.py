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
def flash_randomly(duration=30):
    start_time = time.time()
    flashes = 0
    
    while time.time() - start_time < duration:
        elapsed_time = time.time() - start_time
        
        # Chance to flash, ensuring no more than 3 flashes in 10 seconds
        if random.random() < 0.03 and flashes < 3 and elapsed_time < 10:
            # ANSI escape codes to change the background and text color
            white_screen = "\033[47;30m"
            reset_screen = "\033[0m"
            
            # Clear screen and set to white
            os.system('cls' if os.name == 'nt' else 'clear')
            print(white_screen + " " * os.get_terminal_size().columns)
            time.sleep(1)
            
            # Reset screen to normal
            os.system('cls' if os.name == 'nt' else 'clear')
            print(reset_screen, end='')
            
            flashes += 1
        
        # Reset flashes counter after 10 seconds
        if elapsed_time >= 10:
            start_time = time.time()
            flashes = 0
        
        time.sleep(0.1)

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

time.sleep(2)

clear_cmd()

time.sleep(0.5)

text = """
██╗  ██╗ ██████╗ ██╗  ██╗
██║  ██║██╔═████╗██║  ██║
███████║██║██╔██║███████║
╚════██║████╔╝██║╚════██║
     ██║╚██████╔╝     ██║
     ╚═╝ ╚═════╝      ╚═╝

     
     
     """
print(fade.blackwhite(text))
time.sleep(4)

print(fade.fire("Oh crap.."))

pygame.mixer.music.load("lib/music2.mp3")

pygame.mixer.music.play(-1)

time.sleep(3)
i = 0
while True:

    translated_string = input(fade.fire("""

    Looks like a bug, please translate the following from russian into english to exit (follow grammatical rules).

    "Белый снег, белый мел, белый заяц тоже бел. А вот белка не бела, белой даже не была." """))

    i += 1
    if translated_string == "White snow, white chalk, white hare is also white. But the squirrel isn’t white, it has never been white.":
        break
    elif i > 3:
        print(fade.brazil("Alright, I will just do it for you at this point! Give me a minute.."))
        time.sleep(20)
        print(fade.brazil("""The answer was; "White snow, white chalk, white hare is also white. But the squirrel isn’t white, it has never been white." (Russian Tongue Twister) """))
        time.sleep(8)
        break
    else:
        print(fade.water("Please retry!"))
        pass

print(fade.greenblue("Thank you for not pressing X to exit. Quitting now..."))
time.sleep(2)
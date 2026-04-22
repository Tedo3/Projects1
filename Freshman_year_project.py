from time import sleep
import random

points = 0

player = input("What is your name? ")
print(f"Welcome {player}, your game in the Mysterious Quiz starts now!")
sleep(2)
print("You will be asked 5 questions that you must answer.")
sleep(2)
print("For every correct answer, you will receive 1 point.")
sleep(2)
print("You have a choice of four categories from which the questions will be asked.")
sleep(2)

category = ["H", "S", "G", "L"]
categories_list = random.choice(category)
print(categories_list)

if categories_list == "H":
    sleep(2)
    print("Your category is History.")
    sleep(2)
    print("Question 1: In which century was 'Slav-Bulgarian History' written?")
    sleep(2)
    print("A) 19th")
    print("B) 18th")
    print("C) 12th")
    print("D) 14th")
    answer = input("Your answer: ")
    if answer != "B)":
        print(f"Sorry, your game ends here with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 2: Who was the first president of the USA?")
    print("A) Abraham Lincoln")
    print("B) Thomas Jefferson")
    print("C) Barack Obama")
    print("D) George Washington")
    answer = input("Your answer: ")
    if answer != "D)":
        print(f"Game over with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 3: In which year was the European Union created?")
    print("A) 1976")
    print("B) 1993")
    print("C) 2001")
    print("D) 1950")
    answer = input("Your answer: ")
    if answer != "B)":
        print(f"Wrong answer. You leave with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 4: When did World War I begin?")
    print("A) 1954")
    print("B) 1900")
    print("C) 1914")
    print("D) 1976")
    answer = input("Your answer: ")
    if answer != "C)":
        print(f"Game over with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 5: Which was the last dynasty in China?")
    print("A) Qing")
    print("B) Han")
    print("C) Shang")
    print("D) Sui")
    answer = input("Your answer: ")
    if answer != "A)":
        print(f"You lost at the final question with {points} points.")
    else:
        print("Congratulations! You won the game!")
        points = 5


elif categories_list == "S":
    print("Your category is Sport.")
    print("Question 1: Which of the following athletes is a basketball player?")
    print("A) Lionel Messi")
    print("B) James Harden")
    print("C) Grigor Dimitrov")
    print("D) Anthony Joshua")
    answer = input("Your answer: ")
    if answer != "B)":
        print("Game over.")
        exit()
    points += 1
    print("Correct!")

    print("Question 2: Which sport does NOT require gym training?")
    print("A) Chess")
    print("B) Football")
    print("C) Athletics")
    print("D) Kickboxing")
    answer = input("Your answer: ")
    if answer != "A)":
        print(f"Game over with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 3: How often is the Football World Cup held?")
    print("A) Every 2 years")
    print("B) Every 6 years")
    print("C) Every 4 years")
    print("D) Every 10 years")
    answer = input("Your answer: ")
    if answer != "C)":
        print(f"Game over with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 4: What is the nickname of coach Stanimir Stoilov?")
    print("A) The Professor")
    print("B) Gundi")
    print("C) Gonzo")
    print("D) Murry")
    answer = input("Your answer: ")
    if answer != "D)":
        print(f"Game over with {points} points.")
        exit()
    points += 1
    print("Correct!")

    print("Question 5: What do the Olympic rings symbolize?")
    print("A) The five continents")
    print("B) Human strength")
    print("C) Five circles in sports")
    print("D) Nothing")
    answer = input("Your answer: ")
    if answer != "A)":
        print(f"You lost with {points} points.")
    else:
        print("Congratulations! You won!")
        points = 5


elif categories_list == "G":
    print("Your category is Geography.")
    print("Question 1: On which continent is Bulgaria located?")
    print("A) Asia")
    print("B) Europe")
    print("C) North America")
    print("D) Africa")
    answer = input("Your answer: ")
    if answer != "B)":
        print("Game over.")
        exit()
    points += 1

    print("Question 2: What is the most common natural zone in Africa?")
    print("A) Savannas")
    print("B) Deserts")
    print("C) Evergreen forests")
    print("D) Jungles")
    answer = input("Your answer: ")
    if answer != "B)":
        print(f"Game over with {points} points.")
        exit()
    points += 1

    print("Question 3: Which ocean separates Asia and North America?")
    print("A) Pacific")
    print("B) Atlantic")
    print("C) Arctic")
    print("D) Indian")
    answer = input("Your answer: ")
    if answer != "A)":
        print(f"Game over with {points} points.")
        exit()
    points += 1

    print("Question 4: Which is one of the Seven Wonders of the World?")
    print("A) Eiffel Tower")
    print("B) Great Wall of China")
    print("C) Hanging Gardens of Babylon")
    print("D) Statue of Liberty")
    answer = input("Your answer: ")
    if answer != "C)":
        print(f"Game over with {points} points.")
        exit()
    points += 1

    print("Question 5: Which country has purple in its flag?")
    print("A) Zambia")
    print("B) Vatican")
    print("C) DR Congo")
    print("D) Dominica")
    answer = input("Your answer: ")
    if answer != "D)":
        print(f"You lost with {points} points.")
    else:
        print("Congratulations! You won!")
        points = 5


elif categories_list == "L":
    print("Your category is Literature.")
    print("Question 1: Which Bulgarian writer is known as the Patriarch of Bulgarian Literature?")
    print("A) Veselin Hanchev")
    print("B) Yordan Yovkov")
    print("C) Ivan Vazov")
    print("D) Hristo Smirnenski")
    answer = input("Your answer: ")
    if answer != "C)":
        print("Game over.")
        exit()
    points += 1

    print("Question 2: Who is known as the master of the short story?")
    print("A) Elin Pelin")
    print("B) Ran Bosilek")
    print("C) Ivan Vazov")
    print("D) Hristo Botev")
    answer = input("Your answer: ")
    if answer != "A)":
        print(f"Game over with {points} points.")
        exit()
    points += 1

    print("Question 3: What does Bay Ganyo sell?")
    print("A) Stamps")
    print("B) Rose oil")
    print("C) Rakia")
    print("D) Banitsa")
    answer = input("Your answer: ")
    if answer != "B)":
        print(f"Game over with {points} points.")
        exit()
    points += 1

    print("Question 4: What is Baba Iliitsa's goal?")
    print("A) Walk in the mountain")
    print("B) Collect herbs")
    print("C) Pray in monastery")
    print("D) Take her grandson to the priest")
    answer = input("Your answer: ")
    if answer != "D)":
        print(f"Game over with {points} points.")
        exit()
    points += 1

    print("Question 5: What is the name of the sick girl in 'Along the Wire'?")
    print("A) Nonka")
    print("B) Milka")
    print("C) Maria")
    print("D) Ivanka")
    answer = input("Your answer: ")
    if answer != "A)":
        print(f"You lost with {points} points.")
    else:
        print("Congratulations! You won!")
        points = 5































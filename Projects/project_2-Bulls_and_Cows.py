# Bulls & Cows
# Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.
# Program musí splňovat tyto požadavky:
# Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:

# """
# project_2-Bulls_and_Cows.py: druhý projekt do Engeto Online Python Akademie
# author: Peter Lipovsky
# email: pe.lipovsky@gmail.com
# """

# program pozdraví užitele a vypíše úvodní text  (viz. níže v ukázkách),
# program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
# hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,
# program vyhodnotí tip uživatele,
# program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows),
# zápis organizovaný do krátkých a přehledných funkcí.

# Uložiště, nebo také repozitář, kam projekt odevzdáš, bude splňovat následující:
# Tvoje řešení nahraješ do souboru main.py (pokud pojmenuješ soubor jinak, nebude uznaný),
# repozitář bude obsahovat jedinný .py soubor s výstupem (pokud jej třeba rozdělíš jako main_1.py a main_2.py, nebude uznaný).
# každý projekt má svůj vlastní, oddělený repozitář (zvlášť repozitář pro 1. projekt, zvlášť repozitář pro další projekt, ...).


# Úvodní text:
# Hi there!
# -----------------------------------------------
# I've generated a random 4 digit number for you.
# Let's play a bulls and cows game.
# -----------------------------------------------
# Enter a number:
# -----------------------------------------------

# Příklad hry s číslem 2017:

# Hi there!
# -----------------------------------------------
# I've generated a random 4 digit number for you.
# Let's play a bulls and cows game.
# -----------------------------------------------
# Enter a number:
# -----------------------------------------------
# >>> 1234
# 0 bulls, 2 cows
# -----------------------------------------------
# >>> 6147
# 1 bull, 1 cow
# -----------------------------------------------
# >>> 2417
# 3 bulls, 0 cows
# -----------------------------------------------
# >>> 2017
# Correct, you've guessed the right number
# in 4 guesses!
# -----------------------------------------------
# That's amazing!

# Program toho může umět víc. Můžeš přidat například:
# počítání času, za jak dlouho uživatel uhádne tajné číslo
# uchovávat statistiky počtu odhadů jednotlivých her

import random

secret_numbers = str(random.randint(1111, 9999))

user_numbers = print(
"""Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")

def get_user_number():
    while True: 
            user_numbers = input("Enter a number: ")
            if user_numbers.isnumeric() == False:
                print("Input number must be number")
            elif int(len(user_numbers)) > 4:
                print("Input number can not be longer than 4 digits")
            elif int(len(user_numbers)) < 4:
                print("Input number must be at list 4 digits number")
            elif int((user_numbers)[0]) == 0:
                print("Input number can not start with 0")
            else: 
                print(f"Secret number: {secret_numbers}")

            bulls = 0 
            cows  = 0  
            count = 0

            for number in range(len(secret_numbers)):
                count += 1
                if user_numbers[number] == secret_numbers[number]:
                    bulls += 1
                elif user_numbers[number] in secret_numbers:
                    cows += 1

            print(f"Bulls: {bulls}, Cows: {cows}")

            if bulls == 4:
                print(f"""Correct, you've guessed the right number in {count} guesses!
            That's amazing!""")
                break
                
user_number = get_user_number()

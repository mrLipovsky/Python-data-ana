# """
# projekt_1.py: první projekt do Engeto Online Python Akademie

# author: Peter Lipovsky
# email: lipovsky@jtbank.cz
# poznamka: bez AI
# """

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

lenTexts = len(TEXTS)

# USER
users = {"bob": "123", "ann": "pass123", "mike":"password123", "liz":"pass123", "Peter":"lipo77"}

usernameInput = input("Name: ")
passwordInput = input("Password: ")
authenticated = False

for username, password in users.items():
    if username == usernameInput and password == passwordInput:
        print(F'Welcome to the app, {username}. We have {lenTexts} texts to be analyzed.')
        selectedText = input(F"Enter a number btw. 1 and {lenTexts} to select: ")
        authenticated = True
        break

if authenticated == False:
    print(F"""username: {username} \b
password: {password} \b
unregistered user, terminating the program..""")
    quit()

def selectedInput(input):
    if input == '1':
        word = len(''.join(TEXTS[0]).split())
        return word
    elif input == "2":
        word = len(''.join(TEXTS[1]).split())
        return word
    elif input == "3":
        word = len(''.join(TEXTS[2]).split())
        return word
    elif input.isnumeric() == False:
        print("input must by number, terminating the program..")
        quit()
    else:
        print("wrong number, terminating the program..")
        quit()

# TEXT
def selectedTextFunction(input, TEXTS):
    if input == '1':
        words = ''.join(TEXTS[0]).split()
        return words
    elif input == "2":
        words = ''.join(TEXTS[1]).split()
        return words
    elif input == "3":
        words = ''.join(TEXTS[2]).split()
        return words

word = selectedInput(selectedText)
words = selectedTextFunction(selectedText, TEXTS)

numberUpercaseWord = 0
numberUpercases = 0
numberLowercases = 0
numberNumbers = 0
numberSum = 0

print(F'Počet slov {word}')      

for textStartUpercases in words:
    if textStartUpercases[0].isupper() == True and textStartUpercases.isnumeric() == False and textStartUpercases[1].isupper() == False: 
        numberUpercaseWord += 1
print(F"Počet slov začínajících velkým písmenem, pro text 1: {numberUpercaseWord}")

for textUpercases in words:
    if textUpercases.isupper() == True and textUpercases.isnumeric() == False:
        numberUpercases += 1
print(F"Počet slov psaných velkými písmeny, pro text 1: {numberUpercases}") 

for textLowercases in words:
    if textLowercases.islower() == True and textLowercases.isnumeric() == False:
        numberLowercases += 1
print(F"Počet slov psaných velkými písmeny, pro text 1: {numberLowercases}") 

for numbers in words:
    if numbers.isnumeric() == True:
        numberNumbers += 1
print(F"Počet čísel (ne cifer) v textu.: {numberNumbers}") 

for numbers in words:
    if numbers.isnumeric() == True:
        numbers = int(numbers)
        numberSum += numbers
print(F"Suma všech čísel (ne cifer) v textu.: {numberSum}") 

for sloupcovyGraf in words:
    delka = len(sloupcovyGraf)
    print(F"{delka} " + delka * "*")

quit()

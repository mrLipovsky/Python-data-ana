# """
# projekt_1.py: první projekt do Engeto Online Python Akademie

# author: Peter Lipovsky
# email: lipovsky@jtbank.cz
# poznamka: bez AI
# """

# Pojmenování proměnných: Názvy proměnných jako numberUpercaseWord a numberUpercases mají nekonzistentní pravopis ("Upercase" by mělo být "Uppercase"). - upraveno
# Formátování kódu: Kód postrádá konzistentní formátování, jako jsou mezery kolem operátorů a konzistentní odsazení, což ovlivňuje čitelnost. - upraveno
# Řádky 54-56: Použití \b v příkazu print je nesprávné a vede k neočekávanému výstupu. Mělo by být odstraněno pro jasnost. - upraveno
# Řádek 112: Příkaz print nesprávně uvádí "Počet slov psaných velkými písmeny" pro slova malými písmeny, což by mělo být opraveno na "Počet slov psaných malými písmeny". - upraveno
# Řádky 125-127: Výstup sloupcového grafu není formátován podle referenčního výstupu. Měl by obsahovat záhlaví a správně zarovnat výskyty. - upraveno
# Řádky 59-74: Funkce selectedInput je repetitivní. Může být optimalizována převedením vstupu na celé číslo a jeho přímým použitím jako indexu pro seznam TEXTS. 
# Řádky 77-86: Podobně může být funkce selectedTextFunction optimalizována použitím vstupu jako indexu, čímž se sníží opakování. - upraveno
# Řádky 99-127: Více cyklů for je použito k iteraci přes stejný seznam words. Tyto cykly lze kombinovat do jednoho pro zlepšení efektivity.  - upraveno

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

len_texts = len(TEXTS)

# USER 
users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike":"password123", 
    "liz":"pass123", 
    "Peter":"lipo77"
    }

username_input = input("username: ")
password_input = input("password: ")
authenticated = False

for username, password in users.items():
    if username == username_input and password == password_input:
        print(
            '----------------------------------------\n'
            f'Welcome to the app, {username} \n'
            f'We have {len_texts} texts to be analyzed.\n'
            '----------------------------------------'
            )
        selectedText = input(f'Enter a number btw. 1 and {len_texts} to select: ')
        print('----------------------------------------')
        authenticated = True
        break

if authenticated == False:
    print(
        f'username: {username} \npassword: {password} \n'
        'unregistered user, terminating the program..'
        )
    quit()

# USER INPUT
def selectedInput(input, TEXTS):
    user_input = int(input)
    if user_input == 1:
        word = len(''.join(TEXTS[0]).split())
        words = ''.join(TEXTS[0]).split()
        return word, words
    elif user_input == 2:
        word = len(''.join(TEXTS[1]).split())
        words = ''.join(TEXTS[1]).split()
        return word, words
    elif user_input == 3:
        word = len(''.join(TEXTS[2]).split())
        words = ''.join(TEXTS[2]).split()
        return word, words
    elif user_input():
        print('input must by number, terminating the program..')
        quit()
    else:
        print('wrong number, terminating the program..')
        quit()

word, words = selectedInput(selectedText, TEXTS)

number_uppercases = 0
number_lowercases = 0
number_numbers = 0
number_titlecase = 0
number_sum = 0

print(f'There are {word} words in the selected text.')      

for word in words:
    if word.isnumeric():
        number_numbers += 1
        number_sum += int(word)
    elif word.isupper():
        number_uppercases += 1
    elif word.islower():
        number_lowercases += 1
    elif word.istitle():
        number_titlecase += 1

print(f'There are {number_titlecase} titlecase words.')
print(f'There are {number_uppercases} uppercase words.')
print(f'There are {number_lowercases} lowercase words.')
print(f'There are {number_numbers} numeric strings.')
print(
    f'The sum of all the numbers {number_sum}\n'
    '----------------------------------------\n'
    'LEN|  OCCURENCES  |NR.\n'
    '----------------------------------------'
    ) 

for index, barGraph in enumerate(words):
    length_word = len(barGraph)
    print(f'{index} |{ '*' * length_word}|{length_word}')

quit()

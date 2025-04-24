"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Štefaník
email: stefanik.david@seznam.cz
"""

# Slovník uživatelů a jejich hesel
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Analyzované texty
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

# Oddělovač 
separator = "-" * 40

# Zadání uživatelského jména a hesla
username = input("Enter your username: ")
password = input("Enter your password: ")

# Kontrola správného zadání přihlašovacích údajů
if username in users and users[username] == password:
    print(f"username: {username}")
    print(f"password: {password}")
    print(separator)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed")
    print(separator)

    # Výběr textu k analýze
    choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
    print(f"Enter a number btw. 1 and {len(TEXTS)} to select: {choice}")

    # Kontrola, zda je vstup platné číslo a v rozsahu
    if choice.isdigit() and 1 <= int(choice) <= len(TEXTS):
        text = TEXTS[int(choice) - 1]  
        words = [w.strip(".,") for w in text.split()]
        num_words = len(words)  

        # Analýza slov podle zadaných kritérií
        titlecase_words = [w for w in words if w.istitle()]  
        uppercase_words = [w for w in words if w.isupper()]  
        lowercase_words = [w for w in words if w.islower()]  
        numeric_strings = [w for w in words if w.isdigit()]  
        sum_numbers = sum(int(w) for w in words if w.isdigit())  

        print(separator)
        print(f"There are {num_words} words in the selected text.")
        print(f"There are {len(titlecase_words)} titlecase words.")
        print(f"There are {len(uppercase_words)} uppercase words.")
        print(f"There are {len(lowercase_words)} lowercase words.")
        print(f"There are {len(numeric_strings)} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers}")
        print(separator)

        # Statistika délky slov
        lengths = {}
        for w in words:
            l = len(w)
            if l == 0:
                continue
            lengths[l] = lengths.get(l, 0) + 1

        # Výpis tabulky četnosti délek slov
        print("LEN| OCCURENCES        |NR.")
        print(separator)
        for l in sorted(lengths):
            stars = '*' * lengths[l]
            print(f"{l:>3}|{stars:<18}|{lengths[l]}")
    else:
        print("This is an invalid input number, terminating the program!")
else:
    print(f"username: {username}")
    print(f"password: {password}")
    print("Unregistered user, terminating the program...")
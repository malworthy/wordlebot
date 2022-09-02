from random import randint
from colorama import init, Fore, Back, Style

def get_words(filename):
    file = open(filename,'r')
    result = file.readlines()
    file.close()
    
    return [x.strip().replace('\n','').replace('\r','') for x in result]

def find_all(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def print_letter(colour, letter):
    print(f"{Fore.WHITE}|{colour}{letter.upper()}{Fore.WHITE}", end="")

init()

words = get_words('wordlist.txt')
allowed_words = get_words('five_letter_words.txt')

index = randint(0,len(words)-1)
word = words[index]
while word not in allowed_words:
    index = randint(0,len(words)-1)
    word = words[index]

notused = ""

for r in range(1,7):
    guess = input(f"Enter Guess {r}: ")
    while guess not in allowed_words:
        print("Word not in dictionary.  Try again...")
        guess = input("Enter Guess: ")

    
    used_letters = ""
    print("+=+=+=+=+=+")
    for i in range(5):
        found_indexes = find_all(word, guess[i])
        if i in found_indexes:
            print_letter(Fore.GREEN, guess[i])
            used_letters += guess[i]
        elif len(found_indexes) > 0 and len(find_all(used_letters, guess[i])) < len(found_indexes):
            print_letter(Fore.YELLOW, guess[i])
            used_letters += guess[i]
        else:
            print_letter(Fore.WHITE, guess[i])
            if guess[i] not in notused:
                notused += guess[i]
    print("|")
    print("+=+=+=+=+=+")
    print(Style.RESET_ALL)

    if (guess == word):
        print(f"You got it in {r} guesses")
        break

    if notused != "":
        print(f"Letters not in word: {''.join(sorted(notused.upper()))}")

print("The word was: " + word.upper())
print(Style.RESET_ALL)

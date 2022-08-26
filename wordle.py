from english_words import english_words_set
from random import randint

words = [x for x in english_words_set if len(x) == 5 and x == x.lower() and "'" not in x]

words2 = [x for x in english_words_set if "word" in x]

print(words2)

index = randint(0,len(words)-1)
word = words[index]
notused = ""

for r in range(1,6):
    guess = input("Enter Guess: ")
    while guess not in words:
        print("Word not in dictionary.  Try again...")
        guess = input("Enter Guess: ")

    if (guess == word):
        print("You got it")
        break

    for i in range(5):
        found_index = word.find(guess[i])
        if found_index == i:
            print(guess[i] + " is in the correct position")
        elif found_index >=0:
            print(guess[i] + " is in the word")
        else:
            notused += guess[i]
    if notused != "":
        print("Letters not in word: " + notused.upper())

print("The word was " + word)
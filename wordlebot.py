from english_words import english_words_set
from random import randint

def split_input(csv):
    if csv in ['end','quit','exit','fin','done']:
        return [-1]
    return [int(i) for i in csv.split(',') if i!='']

def process_matches(indexes, words):
    for i in indexes:
        letter_index = int(i)-1
        words = [x for x in words if x[letter_index]==word[letter_index] and x != word]
    return words

def process_contains(indexes, words):
    for i in indexes:
        letter_index = int(i)-1
        words = [x for x in words if word[letter_index] in x and x != word and x[letter_index] != word[letter_index]]
    return words


words = [x for x in english_words_set if len(x) == 5 and x == x.lower() and "'" not in x]

for r in range(1,6):
    print('Starting row ' + str(r))

    index = randint(0,len(words)-1)
    word = words[index]
    
    print(word.upper())

    correct=split_input(input("In correct position: "))
    contains=split_input(input("Incorrect position: "))
    if -1 in correct+contains:
        break;

    words = process_matches(correct, words) 
    words = process_contains(contains, words)
    contains_letters = [word[x-1] for x in correct + contains]
    #print(contains_letters)

    for i in range(1,6):
        if not str(i) in correct and not str(i) in contains and not word[i-1] in contains_letters:
            words = [x for x in words if word[i-1] not in x]

    if len(words)==0:
        print("I give up")
        break

print("Program ends")



from random import randint
import sys

def get_words(filename):
    file = open(filename,'r')
    result = file.readlines()
    file.close()
    
    return [x.strip().replace('\n','').replace('\r','') for x in result]

def split_input(csv):
    if csv in ['end','quit','exit','fin','done']:
        return [-1]
    if csv == 'oops':
        return [-2]
    return [int(i) for i in csv.split(',') if i!='']

def process_matches(indexes, words, word):
    for i in indexes:
        letter_index = int(i)-1
        words = [x for x in words if x[letter_index]==word[letter_index] and x != word]
    return words

def process_contains(indexes, words, word):
    for i in indexes:
        letter_index = int(i)-1
        words = [x for x in words if word[letter_index] in x and x != word and x[letter_index] != word[letter_index]]
    return words

def play_game(word, words):
    for r in range(1,7):
        print('Starting row ' + str(r))
        
        print(word.upper())
        again = True
        while again:
            correct=split_input(input("In correct position (GREEN LETTERS): "))
            if -1 in correct:
                return;
            contains=split_input(input("Incorrect position (ORANGE LETTERS): "))
            if -1 in correct+contains:
                return;
            if not -2 in correct+contains:
                again = False

        words = process_matches(correct, words, word) 
        words = process_contains(contains, words, word)
        contains_letters = [word[x-1] for x in correct + contains]
        

        for i in range(1,6):
            if not str(i) in correct and not str(i) in contains and not word[i-1] in contains_letters:
                words = [x for x in words if word[i-1] not in x]

        if len(words)==0:
            print("I give up")
            return

        index = randint(0,len(words)-1)
        word = words[index]

all_words = get_words("five_letter_words.txt")
words = [x.strip().replace('\n','').replace('\r','') for x in all_words if len(x.strip().replace('\n','').replace('\r','')) == 5]

index = randint(0,len(words)-1)
initial_word = words[index]

# check for command line and set first word
if len(sys.argv) == 2 and sys.argv[1] in words:
    initial_word = sys.argv[1]

play_game(initial_word, words)

print("Program ends")



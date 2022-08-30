# wordlebot
A simple python script that can play wordle - still a work in progress.

Install Dependencies:

pip install english_words

Usage:
  python wordlebot.py
  
Example of use:
```
Starting row 1
QUIET <- the guess, use this in wordle
In correct position: 4,5 <- the position of any letter that wordle shows as GREEN. Blank if none, otherwise a command separated list.
Incorrect position: 1 <- the position of any letter that wordle shows as ORANGE. Blank if none, otherwise a command separated list.

If the guess it correct, then enter the word 'fin' to exit.
The bot will loop 6 times.
```

wordle.py is an (incomplete) implementation of wordle to test the bot with.


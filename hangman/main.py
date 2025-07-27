import random
from wordslist import words # import word from wordlist.py

# Hangman Art
hangman_art = {0: ("   ",
                   "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

# for dislaying hangman art on wrong guess
def display_man(wrong_guesses):
   print("----------------")
   for line in hangman_art[wrong_guesses]:
      print(line)
   print("----------------")

# for displaying wright answer on loosing or wining
def diasplay_answer(answer):
    print(" ".join(answer))

#for displaying hint
def display_hint(hint):
    print(" ".join(hint))

def main():
    answer = random.choice(words) #choose random words from list
    wrong_guesses = 0 # inital guess
    hint = ["_"]* len(answer) #hint 
    guessed_letter = set()
    is_running = True  # code is runing

    while is_running:
        display_man(wrong_guesses) # to display guess
        display_hint(hint) #to display hint
        guess = input("Enter a letter").lower() # to input guesses 

        if len(guess) != 1 or not guess.isalpha(): # cheaking guess is not a word or number
            print("Invalid input")
            continue
        
        if guess in guessed_letter: # does not add wrong point on already guessed letter 
            print(f"{guess} is already guessed")
            continue
        
        guessed_letter.add(guess) # adding letter to guessed letter

        if guess in answer: # cheaking guess in answer
            for i in range(len(answer)): 
                if answer[i] == guess: 
                    hint[i] = guess
        else:
            wrong_guesses += 1 # adding 1 wrong guess 

        if "_" not in hint: # when hint bar is full 
            diasplay_answer(answer) #displaying answer on wining
            display_man(wrong_guesses) # displaying hangmain art
            print("You Won!") 
            is_running = False # break the code
        elif wrong_guesses >= len(hangman_art) -1: 
            display_man(wrong_guesses)   # displaying hangman art
            diasplay_answer(answer)  #displaying answer
            print("You Loose")
            is_running = False #break the code

if __name__ == "__main__":
    main() # run the code
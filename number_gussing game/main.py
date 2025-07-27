import random

num = random.randint(1, 100) # Choose random number between 1 to 100

def main(): # main function
    is_running = True # code is running
    chance = 10 # total chances

    while is_running:
        guess = input("Enter a number between 1 to 100: ")

        try:
            guess = int(guess)  # convert guess into integer
            
            if 1 <= guess <= 100: # if guess is between 1 and 100

                if guess == num: # if guess is equal to number
                    print("You Won!")
                    is_running = False # Code is stoped

                elif guess > num: # if guess is greater then number
                    print(f"The number {guess} is too high") 
                    chance -= 1 # decrease the chance

                else: # if guess is less than number
                    print(f"The number {guess} is too low")
                    chance -= 1 # decreate chance

                if chance == 0: # when all chances gets 0
                    print(f"You Lose! The correct number was {num}.")
                    is_running = False # code is stoped
            else:
                print("Please enter a number between 1 and 100.") 
        
        except ValueError:
            print("Invalid Input: Please enter a valid number.")

if __name__ == "__main__":
    main() # run the code

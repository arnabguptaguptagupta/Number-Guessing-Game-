#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def number_guess():
    min_no = 1
    max_no = 100
    rounds = 3
    attempts = 0
    total = 0

    print("Guess the Number!")
    print(f"Guess a number between {min_no} and {max_no} ")

    for round_num in range(1, rounds + 1):
        print(f"\nRound : {round_num} ")

        target = random.randint(min_no, max_no)
        attempts = 0
        score = 0

        while attempts < 3:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == target:
                if attempts == 1:
                    score = 10
                elif attempts == 2:
                    score = 8
                else:
                    score = 6
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                print(f"Round {round_num} score: {score}")
                break
            elif user_guess < target:
                print("Your Guessed Number is lower than Actual Number. Try Again!")
            else:
                print("Your Guessed Number is higher than Actual Number. Try Again!")

            if attempts == 2:
                first_digit = str(target)[0]
                print(f"Clue: The number starts with {first_digit}")

        if score == 0:
            print(f"Round {round_num} - Sorry! You could not guess the number in 3 attempts.")
            print(f"The correct number was: {target}")
        total += score

    print("\nGame over!")
    print(f"Total score: {total} out of 30")

if __name__ == "__main__":
    number_guess()


# In[ ]:





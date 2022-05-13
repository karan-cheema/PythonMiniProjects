import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"[HINT] the correct answer is {chosen_word}")

#To Do-2 - Ask user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Make a guess: ")

#To Do-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in guess:
    if guess == chosen_word:
        print("Correct")
    else:
        print("Incorrect")
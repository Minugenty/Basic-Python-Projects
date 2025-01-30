import random

fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Jackfruit', 'Kiwi', 
          'Lemon', 'Mango', 'Nectarine', 'Orange', 'Papaya', 'Quince', 'Raspberry', 'Strawberry', 'Tangerine', 
          'Ugli', 'Vanilla', 'Watermelon', 'Ximenia', 'Yuzu', 'Zucchini']

selected_fruit = random.choice(fruits).lower()
number_of_guesses = len(selected_fruit) + 3

print("Welcome to Hangman!")
print("You have to guess the name of a fruit.")
print("You have", number_of_guesses, "guesses to get the correct answer.")
for _ in selected_fruit:
    print("_", end="\n")
print()

correct_guesses = []
while number_of_guesses > 0:
    guess = input("Enter a letter: ").lower()
    if guess in selected_fruit:
        correct_guesses.append(guess)
        print("Correct guess!")
    else:
        print("Incorrect guess!")
        
    number_of_guesses -= 1
    print("You have", number_of_guesses, "guesses left.")
    for letter in selected_fruit:
        if letter in correct_guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print()
    if "_" not in [letter if letter in correct_guesses else "_" for letter in selected_fruit]:
        print("Congratulations! You have guessed the correct fruit!")
        break
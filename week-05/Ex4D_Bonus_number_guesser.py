numbers = [0, 1, 2, 3, 4, 5]
correct_number = numbers[4]

guesses = []
total_guess = 0
print("Guess a number between 0 and 5")
guess = int(input("Guess the number:"))
while guess != correct_number:
    guesses.append(guess)  # Add each guess to the list 
    total_guess = total_guess + 1 # Add 1 to the total guesse
    if guess < correct_number:
        print("Higher")
    else:
        print("Lower")
    guess = int(input("Guess the number:"))
guesses.append(guess)
total_guess = total_guess + 1
print("You guessed it right!")
print("Total guesses are:", total_guess)
print("Your guesses:", guesses)
if total_guess < 5:
    print("You're awesome!2")

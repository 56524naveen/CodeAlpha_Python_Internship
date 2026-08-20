import random

# List of 5 predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

# Display word with underscores
display_word = ["_"] * len(word)

print("=" * 40)
print("       WELCOME TO HANGMAN GAME")
print("=" * 40)

print(f"\nYou have {max_wrong_guesses} incorrect guesses available.")
print("Guess the word one letter at a time.\n")

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    # Display current progress
    print("Word:", " ".join(display_word))

    # Display guessed letters
    if guessed_letters:
        print("Guessed letters:", ", ".join(guessed_letters))

    # Take input
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one alphabetic letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    # Check whether letter exists in word
    if guess in word:
        print("Correct guess!")

        # Reveal all occurrences of the letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        remaining = max_wrong_guesses - wrong_guesses

        print("Wrong guess!")
        print("Remaining incorrect guesses:", remaining)

    print("-" * 40)

# Final result
if "_" not in display_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
    print("You won the game!")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
    print("Better luck next time!")

print("\nThank you for playing Hangman!")

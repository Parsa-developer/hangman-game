import random

words = [
    "python", "programming", "computer", "algorithm", "database", "network", "software", "developer",
    "coding", "interface"
]

HANGMAN_PICS = [
    """
     ------
     |    |
          |
          |
          |
          |
    ==========""",
    """
     ------
     |    |
     O    |
          |
          |
          |
    ==========""",
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    ==========""",
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    ==========""",
    """
     ------
     |    |
     O    |
    /|\   |
          |
          |
    ==========""",
    """
     ------
     |    |
     O    |
    /|\   |
    /     |
          |
    ==========""",
    """
     ------
     |    |
     O    |
    /|\   |
    / \   |
          |
    =========="""
]

def get_random_choice():
    return random.choice(words).upper()

def display_board(word, guessed_letters, incorrect_guesses):
    print(HANGMAN_PICS[incorrect_guesses])
    print("\nincorrect guesses:", " ".join(guessed_letters - set(word)))
    print("word:", " ".join(letter if letter in guessed_letters else "_" for letter in word))
    print()

def play_hangman():
    word = get_random_choice()
    guessed_letters = set()
    incorrect_guesses = 0

    max_guesses = len(HANGMAN_PICS) - 1

    print("WELCOME TO OUR HANGMAN GAME!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_guesses:
        display_board(word, guessed_letters, incorrect_guesses)
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter just a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that one :)")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("That is a good guess ")
            if all(letter in guessed_letters for letter in word):
                display_board(word, guessed_letters, incorrect_guesses)
                print(f"Congratulations! You guessed the {word}.")
                return
        else:
            incorrect_guesses += 1
            print(f"Wrong guess :( You have {max_guesses - incorrect_guesses} guesses left.")
    display_board(word, guessed_letters, incorrect_guesses)
    print(f"Gameover! the word was {word}.")

def main():
    while True:
        play_hangman()
        play_again = input("would you like to play this game again? (yes/no): ").lower()
        if play_again != "yes":
            print("thanks for playing :)")
            break

if __name__ == "__main__":
    main()
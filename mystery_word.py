def play_game():
    import random

    with open('words.txt') as file:
        main_list = file.read()
        full_list = main_list.split()

        temp_word = random.choice(full_list)

    guesses = 8

    mystery_word = temp_word
    guess_container = []
    num_letters = len(mystery_word)
    mystery_letters = []
    print(mystery_word)
    for mystery_letter in mystery_word:
        mystery_word.split()
    while guesses > 0:
        letter = input(
            "Guess a letter, your mystery word has " + str(num_letters))
        if letter in mystery_word:
            print("That letter is in the word!")
        else:
            print("Nope, that letter is not part of the mystery word!")
            guesses -= 1
            print("You have " + str(guesses) + "remaining guesses.")


if __name__ == "__main__":
    play_game()

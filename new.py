import random


def play_game():

    with open('words.txt') as file:
        main_list = file.read()
    full_list = main_list.split()

    temp_word = random.choice(full_list)
    letters = []
    blanks = []
    num_letters = len(temp_word)
    guesses = 8

    for letter in temp_word:
        letters.append(letter)
    # while keys < value_length:
    print(letters)
    #     keys.append()
    for letter in temp_word:
        blanks.append('_ ')
    print(blanks)

    while guesses > 0:
        guess = input(
            "Guess a letter, your mystery word has " + str(num_letters))
        if letter in temp_word:
            for i in range(len(temp_word)):
                if letters[i] == guess:
                    blanks[i] = guess
            print("That letter is in the word!" + ' '.join(blanks))
        else:
            print("Nope, that letter is not part of the mystery word!")
            guesses -= 1
            print("You have " + str(guesses) + "remaining guesses.")


if __name__ == "__main__":
    play_game()

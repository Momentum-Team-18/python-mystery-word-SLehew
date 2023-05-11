import random


def play_game():

    with open('words.txt') as file:
        main_list = file.read()
        full_list = main_list.split()

        temp_word = random.choice(full_list)
        letters = []
        blanks = []

        guesses = 8

        for letter in temp_word:
            letters.append(letter)
        # while keys < value_length:
        print(letters)
        #     keys.append()
        for letter in temp_word:
            blanks.append('_ ')
        print(blanks)


if __name__ == "__main__":
    play_game()

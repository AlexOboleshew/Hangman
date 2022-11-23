import random
import sys


def input_check(user_input, input_buffer):
    state = True
    if len(user_input) != 1:
        state = False
        print("Please, input a single letter.")
    if not user_input.islower() or not user_input.isalpha():
        state = False
        print("Please, enter a lowercase letter from the English alphabet.")
    if state and user_input in input_buffer:
        print("You've already guessed this letter.")
    else:
        input_buffer.add(user_input)
    return state


def start_game():
    global win_counter
    global lost_counter
    correct_word = list(random.choice(correct_word_list))
    mask_word = list("-" * len(correct_word))
    user_input_buffer = set()
    is_exit = False
    num_attempts = 8
    while num_attempts > 0 and not is_exit:
        print("".join(mask_word))
        user_guess = input("Input a letter: ")
        if input_check(user_guess, user_input_buffer):
            if user_guess in correct_word:
                for letter in range(0, len(correct_word)):
                    if user_guess == correct_word[letter]:
                        if mask_word[letter] != user_guess:
                            mask_word[letter] = user_guess
                            if "-" not in mask_word:
                                win("".join(correct_word))
                                win_counter += 1
                                is_exit = True
                                break
                        else:
                            break
            else:
                print("That letter doesn't appear in the word.\n")
                num_attempts -= 1
        print()

    if num_attempts == 0:
        lost_counter += 1
        print("\nYou lost!")


def win(word):
    print(f"\nYou guessed the word {word}!\nYou survived!")


# Initial config
correct_word_list = "python", "java", "swift", "javascript"
menu_commands = ("play", "results", "exit")
win_counter = 0
lost_counter = 0

print("H A N G M A N ")

while True:
    user_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    while user_command in menu_commands:
        if user_command == "play":
            start_game()
            break
        elif user_command == "results":
            print(f"You won: {win_counter} times\nYou lost: {lost_counter} times")
            break
        elif user_command == "exit":
            sys.exit()

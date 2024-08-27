'''
Christine, Ellie, Misha
9 August 2024
Hangman Game
'''

from random import choice

"""
INPUT: None
RETURN: None
PURPOSE: To greet the user and tell them the rules.
"""
def greet_user():  
    print("Welcome to hangman, type 'exit' any time to leave the game.")  
    print("How to play: Guess a letter and continue guessing until you have all the letters in the given word. Guess until you want to leave the game.")  

"""
INPUT: None
RETURN: Str
PURPOSE: To pick a random word from a list of words.
"""
def get_word(): 
    pool_of_words = ['flower', 'octopus', 'hockey', 'popcorn', 'elephant', 'giraffe', 'volleyball']  
    random_word = choice(pool_of_words)  
    return random_word  

"""
INPUT: None
RETURN: Str
PURPOSE: To ask the user for teir guess
"""
def user_input_func():  
    user_guess = input("Please guess a letter: ")  
    return user_guess  

"""
INPUT: Str
RETURN: Str
PURPOSE: To check if the user guessed a letter.
"""
def check_letter(user_guess):  
    while True:  
        x = len(user_guess)  
        y = user_guess.isalpha()  
        if x != 1:  
            print("That is an invalid guess. Try again.")  
            user_guess = user_input_func()  
        elif not y:  
            print("That is an invalid guess. Try again.")  
            user_guess = user_input_func()  
        else: 
            return user_guess  

"""
INPUT: Str, str
RETURN: Bool
PURPOSE: To check if the letter the user guessed is in the randomly chosen word.
"""
def check_user_guess(user_guess, word):  
    return user_guess in word 

"""
INPUT: List, str, str
RETURN: Bool
PURPOSE: To add the user guess to a list if they guessed correctly.
"""
def check_1(correct_user_guesses, user_guess, word):  
    if check_user_guess(user_guess, word):  
        correct_user_guesses.add(user_guess)  
    else:  
        return False  
    return correct_user_guesses  

"""
INPUT: List, str
RETURN: List
PURPOSE: To add the user guess to a list of all their guesses and print it.
"""
def check_2(all_guesses, user_guess):  
    all_guesses.append(user_guess)  
    a = ", ".join(all_guesses) 
    print("You've guessed " + a + ".")  
    return all_guesses  

"""
INPUT: Str
RETURN: Bool
PURPOSE: To check if the user inputted 'exit'.
"""
def check_exit(user_input): 
    return user_input == "exit" 

"""
INPUT: Str, list
RETURN: List
PURPOSE: To add the correct sequence of letters and underscores to word_list for display.
"""
def update_display(word, correct_user_guesses): 
    word_list = []  
    for c in word: 
        if c in correct_user_guesses:  
            word_list.append(c)  
        else:  
            word_list.append("_")  
    return word_list  

"""
INPUT: None
RETURN: None
PURPOSE: To keep track of how many guesses the user has made.
"""
def count_guesses():  
    global num  
    num += 1  
    if num == 1:  
        print("You've used " + str(num) + " guess.")
    else:  
        print("You've used " + str(num) + " guesses.")  

num = 0 
all_guesses = []  
correct_user_guesses = set()  

"""
INPUT: None
RETURN: None
PURPOSE: To combine the above functions to make a working hangman game.
"""
def start_game():
    global correct_user_guesses  
    word = get_word()  
    play = True  
    print("The word has " + str(len(word)) + " letters.")  
    while play:  
        user_guess = user_input_func()  
        if check_exit(user_guess):  
            print("Goodbye, thanks for playing!") 
            return 
        user_guess = check_letter(user_guess) 
        if check_user_guess(user_guess, word):  
            correct_user_guesses = check_1(correct_user_guesses, user_guess, word)  
        check_2(all_guesses, user_guess)  
        word_list = update_display(word, correct_user_guesses)  
        count_guesses()  
        print(" ".join(word_list)) 
        if "_" not in word_list:  
            print("Congratulations! You've guessed the word.") 
            return 

greet_user() 
start_game() 
   
        

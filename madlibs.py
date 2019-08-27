import math
import random

thismadlib = {
"number" : 0,
"occupation1" : "",
"occupation2" : "",
"place1" : "",
"male" : "",
"place2" : "",
"occupation3" : "",
"bodypart1" : "",
"adjective" : "",
"noun" : "",
"bodypart2" : "",
"celebrity": "",
"verbing": "",
"adverb" : "",
"verbs" : ""
}

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

    
running = True
while running:
    selection = user_input(
        "Press A to Add to list, R to Read from list, L to Display list, U to Update item, D to Destroy item, M to Mark Complete/Incomplete, and Q to quit: ")
    selection_both_cases = selection.lower()
    running = select(selection_both_cases)
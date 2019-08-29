from termcolor import colored

mad_lib = list()

def number():
    while True:
        user_number  = input("Enter a number: ")
        if( user_number.isdigit()):
            mad_lib.append(user_number.strip())
            break
        else:
            print("Error: User input is string ")

def occupation():
    while True:
        user_occupation  = input("Enter a occupation: ")
        if(user_occupation.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_occupation.strip())
            break
def place():
    while True:
        user_place = input("Enter a place: ")
        if(user_place.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_place.strip())
            break
def male():
    while True:
        user_male  = input("Enter a male name: ")
        if(user_male.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_male.strip())
            break
def bodypart():
    while True:
        user_bodypart  = input("Enter a body part: ")
        if(user_bodypart.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_bodypart.strip())
            break
def celebrity():
    while True:
        user_celebrity  = input("Enter a celebrity name: ")
        if(user_celebrity.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_celebrity.strip())
            break
def verbing():
    while True:
        user_verbing  = input("Enter a verb with -ing: ")
        if(user_verbing.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_verbing.strip())
            break
def adjective():
    while True:
        user_adjective  = input("Enter an adjective: ")
        if(user_adjective.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_adjective.strip())
            break
def verbs():
    while True:
        user_verbs  = input("Enter a verb with -s: ")
        if(user_verbs.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_verbs.strip())
            break
def adverb():
    while True:
        user_adverb  = input("Enter an adverb: ")
        if(user_adverb.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_adverb.strip())
            break
def noun():
    while True:
        user_noun  = input("Enter a noun: ")
        if(user_noun.isdigit()):
            print("User input is Number ")
        else:
            mad_lib.append(user_noun.strip())
            break

number()
occupation()
occupation()
place()
male()
place()
occupation()
bodypart()
adjective()
noun()
bodypart()
celebrity()
verbing()
adverb()
verbs()


madlib = colored(mad_lib[0], 'red') + " years after the end of Rush Hour 2, James Carter is no longer a " + colored(mad_lib[1],'blue') + ", but a " + colored(mad_lib[2], 'green') + " on the streets of " + colored(mad_lib[3], 'grey') + \
    ". Lee is now the bodyguard for his friend " + colored(mad_lib[4], 'magenta') + ". Lee is still upset with Carter about an incident in " + colored(mad_lib[5], 'magenta') + " when Carter accidentally shot Lee`s girlfriend," + colored(mad_lib[6],'blue') + \
    " Isabella Molina, in the " + colored(mad_lib[7], 'yellow') + ". During the World Criminal Court discussions, as " + colored(mad_lib[4], 'magenta') + " addresses the importance to fight the Triad, he announces that he knows the " + colored(mad_lib[8], 'magenta') + \
    " of the Triad leadership known as the Shy Shen. Suddenly, " + colored(mad_lib[4],'grey') + " takes a " + colored(mad_lib[9], 'cyan') + " in the " + colored(mad_lib[10], 'white') + ", disrupting the conference. Lee pursues the assassin and corners him, discovering that the assassin is his brother, " + colored(mad_lib[11], 'red') + \
    ". When Lee hesitates to shoot " + colored(mad_lib[13], 'green') + ", Carter shows up " + colored(mad_lib[13], 'yellow') + " " + colored(mad_lib[14],'blue') + " Lee over, allowing " + colored(mad_lib[13], 'white') +" to escape. "
print(madlib)
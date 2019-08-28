mad_lib = []


while (True):
    number = input("Give me a number to use: ")
    occupation1 = input ("Give me an occupation: ")
    occupation2 = input ("Give me another occupation: ")
    occupation3 = input ("Give me another another occupation: ")
    place1 = input ("Give me a location: ")
    place2 = input ("Give me another location: ")
    male = input ("Give me a boyish name: ")
    bodypart1 = input ("Give me one body part: ")
    bodypart2 = input ("Give me one more body part: ")
    celebrity = input ("Give me a relevant celebrity: ")
    verbing = input ("Give me a verb that ends with -ing: ")
    verbs = input ("Give me a verb that end with -s: ")
    adverb = input ("Give me an adverb please: ")

    mad_lib.append({
            "number": number,
            "occupation1": occupation1,
            "occupation2": occupation2,
            "occupation3": occupation3,
            "place1": place1,
            "place2": place2,
            "male": male,
            "bodypart1": bodypart1,
            "bodypart2": bodypart2,
            "celebrity": celebrity,
            "verbing": verbing,
            "verbs": verbs,
            "adverb": adverb

        })
    break;


print(mad_lib)
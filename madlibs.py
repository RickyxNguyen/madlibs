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

while (true):
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




print(thismadlib.keys())
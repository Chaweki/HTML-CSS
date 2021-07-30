 # -*- coding: utf8 -*-
import random
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = ["alvin et les Chipmunks", "Babar","betty boop","calimero","casper","le chat potté", "Kirikou"]
def get_random_item_in(my_list):
    rand_nmb=random.randint(0,len(my_list)-1)
    item = my_list[rand_nmb]
    return item
def capatilase(words) :
    for word in words :
        word.capitalize()
def message(character,quotes):
    capatilase(character)
    capatilase(quotes)
    return "{} dit : ' {} '  ".format(character,quotes)
user_anserw =input("what's up doc u wanna a quotes 'b' neither a : ")
while user_anserw !="b":
    get_random_item_in(quotes)
    print(message(get_random_item_in(characters),get_random_item_in(quotes)))
    user_anserw = input("what's up doc u wanna a quotes 'b' neither a : ")

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:29:35 2020

@author: austin.kellum
"""

### EXAMPLE PYTHON MODULE
# Define some variables:
numberone = 1
ageofqueen = 78


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]



# define some functions
def printhello():
    print ("hello")
    
def timesfour(input):
    return input * 4 
    
# define a class
class Piano:
    def __init__(self):
        self.type = input("What type of piano? ")
        self.height = input("What height (in feet)? ")
        self.price = input("How much did it cost? ")
        self.age = input("How old is it (in years)? ")
	
    def printdetails(self):
        print ("This piano is a/an " + self.height + " foot"),
        print (self.type, "piano, " + self.age, "years old and costing\
 " + self.price + " dollars.")
    
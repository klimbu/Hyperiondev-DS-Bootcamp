''' 
import random 
create a list of jokes
use random number generator between 0 and len(jokes)
print jokes using random number as index
'''
import random

#list of jokes 
jokes = ["What’s the best thing about Switzerland?\n I don’t know, but the flag is a big plus.",
        "I invented a new word!\n Plagiarism!",
        "Did you hear about the mathematician who’s afraid of negative numbers?\nHe’ll stop at nothing to avoid them.",
        "Why do we tell actors to “break a leg?”\nBecause every play has a cast.",
        "Helvetica and Times New Roman walk into a bar./n“Get out of here!” shouts the bartender. “We don’t serve your type.”",
        "Hear about the new restaurant called Karma?\nThere’s no menu: You get what you deserve.",
        "What did one ocean say to the other ocean?\nNothing, it just waved.",
        "Do you want to hear a construction joke?\nSorry, I’m still working on it.",
        "Why do ducks have feathers?\nTo cover their butt quacks!"]

indexno = random.randint(0,(len(jokes)-1)) #picks a random number between 0 and len of jokes

print (jokes[indexno]) #prints jokes at random every time its run
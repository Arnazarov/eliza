# # -*- coding: utf-8 -*-
""" Eliza homework. Computer therapist """
__author__= "Ovezmyrat Arnazarov"

import re

print("Eliza the Computer Therapist")
print("----------------------------------------------------------")
print("You can talk to Eliza by typing in plain English, using")
print("upper-case and lower-case letters along with punctuation.")
print('Enter "bye" when done.')
print("----------------------------------------------------------")
print("Hello! My name is Eliza. What is your name?")
response = input()

def name(response):
    p = re.search("(.*)?My name is (.*)|(.*)I'm (.*)|(.*)", response, re.I)
    if p.group(2):    
        return(p.group(2))
    elif p.group(4):
        return(p.group(4))
    else:
        return(p.group(5))

def you(response):
    p = re.search("You (.*)", response, re.I)
    if p:    
        return(p.group(1))

def is_happy(response):
    p = re.search("(hap[piestyrl]{1,6})", response, re.I)
    if p:
        return True

def is_sad(response):
    p = re.search('sa[ntesd]{1,7}', response, re.I)
    if p:
        return True

def is_good(response):
    p = re.search("(great|ok|good|fine|all\s?right|satisfactory)", response, re.I)
    if p:
        return True

def is_bad(response):
    p = re.search("(bad|poor|so so|awful|unsatisfactory)", response, re.I)
    if p:
        return True

def is_joyous(response):
    p = re.search("(joy[ousflne]{1,7})", response, re.I)
    if p:
        return True

def i_feel(response):
    p = re.search("I feel (.*)", response, re.I)
    if p:    
        return(p.group(1))

def i_want(response):
    p = re.search("I want (.*)", response, re.I)
    if p:    
        return(p.group(1))

def i_need(response):
    p = re.search("I need (.*)", response, re.I)
    if p:    
        return(p.group(1))

def i_have(response):
    p = re.search("I have (.*)", response, re.I)
    if p:    
        return(p.group(1))

def sorry(response):
    p = re.search("(.*) sorry (.*)", response, re.I)
    if p:    
        return(p.group(1))

def verb(response):
    p = re.search("\w*(ed)", response, re.I)
    if p:
        return(p.group(0).replace("ed",""))

def is_there(response):
    p = re.search("Is there (.*)", response, re.I)
    if p:    
        return(p.group(1))

def is_it(response):
    p = re.search("Is it (.*)", response, re.I)
    if p:    
        return(p.group(1))

def why_dont_you(response):
    p = re.search("Why don\'t you (.*)", response, re.I)
    if p:    
        return(p.group(1))

def why_cant_i(response):
    p = re.search("Why can\'t I (.*)", response, re.I)
    if p:    
        return(p.group(1))

def what(response):
    p = re.search("What (.*)", response, re.I)
    if p:    
        return(p.group(1))

def are_you(response):
    p = re.search("Are you (.*)", response, re.I)
    if p:    
        return(p.group(1))

def can_you(response):
    p = re.search("Can you (.*)", response, re.I)
    if p:    
        return(p.group(1))

def how(response):
    p = re.search("How (.*)", response, re.I)
    if p:    
        return(p.group(1))

def because(response):
    p = re.search("Because (.*)", response, re.I)
    if p:    
        return(p.group(1))

def i_think(response):
    p = re.search("I think (.*)", response, re.I)
    if p:    
        return(p.group(1))

def is_mother(response):
    p = re.search("(mom|mommy|mother|mama|mamma)", response, re.I)
    if p:
        return True

def is_father(response):
    p = re.search("(dad|daddy|father|papa|pa)", response, re.I)
    if p:
        return True

def is_child(response):
    p = re.search("(kid|child[ishren]{1,3})", response, re.I)
    if p:
        return True

def is_sibling(response):
    p = re.search("(sis|sister|brother)", response, re.I)
    if p:
        return True

def is_friend(response):
    p = re.search("(bro|buddy|pal|friend|comrade|mate|chum)", response, re.I)
    if p:
        return True

def creator(response):
    p = re.search("who created you|who created you|who made you", response, re.I)
    if p:    
        return True

def i_am(response):
    p = re.search("I am (.*)", response, re.I)
    if p:
        return(p.group(1))

def you_are(response):
    p = re.search("You are (.*)", response, re.I)
    if p:
        return(p.group(1))

def yes(response):
    p = re.search("yes|correct", response, re.I)
    if p:    
        return(p.group(1))

def it_is(response):
    p = re.search("It is (.*)", response, re.I)
    if p:    
        return(p.group(1))

def my(response):
    p = re.search("My (.*)", response, re.I)
    if p:    
        return(p.group(1))

if name(response):
        print("Nice to meet you {}! How are you feeling?".format(name(response)))
        response = input()

while response != "bye":

    if creator(response):
        print("ELIZA was invented in 1966 by Weizenbaum. Why?")
        response = input()
    elif is_happy(response):
        print("Good, what is the source of your happinness?")
        response = input()
    elif is_sad(response):
        print("Do you often feel sad?")
        response = input()
    elif is_good(response):
        print("Good, tell me more about these nice feelings.")
        response = input()
    elif is_bad(response):
        print("When you feel this way, what do you do?")
        response = input()
    elif is_joyous(response):
        print("When do you usually feel joyous?")
        response = input()
    elif i_feel(response):
        print("Hmm. Do you frequently feel {}?".format(i_feel(response)))
        response = input()
    elif i_want(response):
        print("Why do you want it or what would it mean to you if you got {}?".format(i_want(response)))
        response = input()
    elif i_need(response):
        print("Why do you need {}?".format(i_need(response)))
        response = input()
    elif i_have(response):
        print("Why do you tell me that you've {}?".format(i_have(response)))
        response = input()
    elif sorry(response):
        print("There are many times when no apology is needed.")
        response = input()
    elif verb(response):
        print("When did it {}?".format(verb(response)))
        response = input()
    elif is_there(response):
        print("Would you like there to be {}?".format(is_there(response)))
        response = input()
    elif is_it(response):
        print("Perhaps it's {} -- what do you think?".format(is_it(response)))
        response = input()
    elif why_dont_you(response):
        print("Perhaps eventually I will {}".format(why_dont_you(response)))
        response = input()
    elif why_cant_i(response):
        print("If you could {}, what would you do?".format(why_cant_i(response)))
        response = input()
    elif what(response):
        print("How would an answer to that help you?")
        response = input()
    elif are_you(response):
        print("Why does it matter whether I am {}?".format(are_you(response)))
        response = input()
    elif can_you(response):
        print("If I could {}, then what?".format(can_you(response)))
        response = input()
    elif how(response):
        print("Perhaps you can answer your own question.")
        response = input()
    elif because(response):
        print("Is that the real reason?")
        response = input()
    elif i_think(response):
        print("Do you really think so?")
        response = input()
    elif is_mother(response):
        print("What was your relationship with your mother like?")
        response = input()
    elif is_father(response):
        print("How do you feel about your father?")
        response = input()
    elif is_child(response):
        print("How do you think your childhood experiences relate to your feelings today?")
        response = input()
    elif is_sibling(response):
        print("Did you have close bonds with your sibling?")
        response = input()
    elif is_friend(response):
        print("I see. Can you elaborate on that?")
        response = input()
    elif i_am(response):
        print("How does being {} make you feel?".format(i_am(response)))
        response = input()
    elif you_are(response):
        print("Does it please you to think that I'm {}?".format(you_are(response)))
        response = input()
    elif yes(response):
        print("You seem quite sure. Can you elaborate a bit?")
        response = input()
    elif it_is(response):
        print("You seem very certain.")
        response = input()
    elif my(response):
        print("I see, your {}.".format(my(response)))
        response = input()
    elif you(response):
        print("We should be discussing you, not me.")
        response = input()
    else:
        print("Interesting. Please tell me more.")
        response = input()


print("Thank you for talking with me. Bye!")
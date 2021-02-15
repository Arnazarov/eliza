# Implementation of eliza in python only using regex library:

  Agent:
  
  • asks for the user’s name and greet that user using her/his name
  
  • recognizes the following feelings: sadness,happyness and joy and its derivates (e.g. sad, happy, joyful, joyfulness, saddened, etc.) within the
  user’s input, and respond accordingly. 
  
  • recognizes when a person says they are: ok, good and bad   within a user’s response and responds accordingly.
  
  • recgonizes verbs ending in 'ed' and use the verb in its natural form (infinitive) in the response.
  
  • recognizes some relationship labels like "mother", "mom", "father", "dad", "brother", "sister", "friend" and respond appropriately: 
  
  • uses regular expressions for all detections.
  
  • is able to maintain a dialogue no matter what the user input is, except for “bye”, which should terminate the dialogue.


*ELIZA is an early natural language processing computer program created from 1964 to 1966[1] at the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum.[2] 
Created to demonstrate the superficiality of communication between humans and machines, Eliza simulated conversation by using a "pattern matching" 
and substitution methodology that gave users an illusion of understanding on the part of the program, but had no built in framework for contextualizing events.

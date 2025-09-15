#Welcome the player 
print("Welcome to the Mad Libs Generator!")
print("Please enter your words: ")

#Get words from the user and store them in variables 
adjective = input("An Adjective: ")
noun = input("A plural noun: ")
verb_past_tense = input("A verb (past tense) : ")
adverb = input("An Adverb: ")
animal = input("An animal: ")

#The story an f-string that will hold our silly story.
story = f"""
Today was a truly {adjective} day. I saw a group of {noun}
who had just {verb_past_tense} all over the park.
They were moving so {adverb}! The strangest part was that
their leader was a giant {animal}. It was a day I'll never forget.
"""

#Print the final story 
print("\n-- Here is your story ! --")
print(story)
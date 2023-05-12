# Sentence structure: Subject + Verb + Adverb + Preposition + Article + Adjective + Object
import random

noun_subjects = ["i", "you", "he", "she", "it", "they"]
verbs = ["ran", "walked", "talked", "slept", "jumped", "ate", "hid", "fell", "sat", "barked"]
adverbs = ["quickly", "loudly", "slowly", "proudly", "suspiciously", "innocently", "extremely", "sadly", "secretly", "easily"]
prepositions = ["beneath", "beside", "between", "from", "in front of", "inside", "near", "off", "out of", "through", "toward", "under", "within"]
articles = ["a", "an", "the"]
adjectives = ["attractive", "agreeable", "angry", "big", "bald", "ambitious", "bewildered", "colossal", "beautiful", "brave"]
noun_objects = ["building", "cake", "shoes", "bus", "dog", "cat", "table", "chair", "bag", "pen"]

noun_subject = random.choice(noun_subjects)
verb = random.choice(verbs)
adverb = random.choice(adverbs)
preposition = random.choice(prepositions)
article = random.choice(articles)
adjective = random.choice(adjectives)
noun_object = random.choice(noun_objects)

text = noun_subject + " " + verb + " " + adverb + " " + preposition + " " + article + " " + adjective + " " + noun_object + "."

print(text.capitalize())
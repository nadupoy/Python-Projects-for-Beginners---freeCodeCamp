# Find out how the Mad Libs game works.
# 'Mad Libs are stories with words removed & replaced by blank spaces.' - madlibslive.com
# Source material is from the first paragraph of the 4th chapter of the book 'The Chemical Wedding'. The book can be found on smallbeerpress.com:
''' I was awake and lying in *bed* next morning, looking idly at the
    wonderful *images* and *inscriptions* all around my *room*, when
    suddenly I heard the sound of *trumpets*, as if a *procession* were
    already underway. My *page* jumped out of *bed* as if crazed,
    looking more *dead* than *alive*, and you can imagine how I felt
    when he cried, “They’re already being presented to the king!”'''
# Start with an empty string & append as the story unfolds

word1 = input("I was awake and lying in ")
word2 = input("next morning, looking idly at the wonderful ")
word3 = input("and ")
word4 = input("all around my ")
word5 = input("when suddenly I heard the sound of ")
word6 = input("as if a ")
word7 = input("were already underway. My ")
word8 = input("jumped out of ")
word9 = input("as if crazed, looking more ")
word10 = input("than ")


story = f"""I was awake and lying in {word1} next morning, looking idly at the
wonderful {word2} and {word3} all around my {word4}, when
suddenly I heard the sound of {word5}, as if a {word6} were
already underway. My {word7} jumped out of {word8} as if crazed,
looking more {word9} than {word10}, and you can imagine how I felt
when he cried, \"They're already being presented to the king!\""""

print(story)
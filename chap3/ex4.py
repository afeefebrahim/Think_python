#Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

n = repeat_lyrics()

# Define a function that print a lyrics and a function that repeat first operation 5 times.

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repl_lyrics():
    for i in range(5):
        print_lyrics()

def main():
    print_lyrics()
    repl_lyrics()
    exit(0)

main()

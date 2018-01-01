# Exercise 2
# Write a while loop that starts at the last character in the string and works
# its way backwards to the first character in the string, printing each letter
# on a separate line, except backwards.

def print_reverse( word ):

    index = len( word ) - 1
    while  index > -1:
        print word[ index ]
        index -= 1

def main( ):
    print_reverse( raw_input( 'Insert a word->' ) )
    quit( 0 )

main( )

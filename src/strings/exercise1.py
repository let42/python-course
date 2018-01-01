#Exercise 1: print with while every single letter of a fruit.

def main( ):
    index = 0
    fruit = raw_input('Insert a fruit>>')
    while index < len(fruit):
        print fruit[index]
        index += 1
        quit( 0 )
main( )

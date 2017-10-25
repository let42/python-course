# Examples of iterations in python

def main( ):
    # Creating an array with some elements
    # scrolling it with a 'for loop'
    # and print a phrase containin' the pulled
    # element
    friends = ['John', 'Mary', 'Robert', 'Raph']
    for friend in friends:
        print 'Hello', friend
    print 'done!'

    # Creating and assigning a value to x
    # with the 'while loop' print the actual value of x
    # and decreased
    x = 5
    while x > 0:
        print x
        x -= 1
    print 'done!'

    # Using the True value in a while loop
    # with user input if line contains 'quit'
    # the loop breaks, if first character of line
    # is '#', it considered a comment and it won't
    # print elsewhere print line until true doesn't
    # change
    line = ''
    while True:
        line = raw_input('>>> ')
        if line[0] == '#':
            continue
        if line == 'quit':
            break
        print line
    # Testing the for loop applied to a range of values
    count = 0
    for intervar in [3,42, 12, 35, 24]:
        count = count + 1 + intervar
        print 'Count:', count
    print 'done!'

    #
    

    exit(0)

main( )

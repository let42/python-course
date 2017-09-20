# give two values in input check if one of this is smaller than / greater than the other and:
# if greater than - sum the two values and multipy for 3.14
# if smaller than - multiply them and divides the results by 2

alpha = raw_input('Enter a number > ')
alpha = float(alpha)
beta = raw_input('Enter another number > ')
beta = float(beta)
gamma = 0

if(alpha > beta):
    gamma = ( alpha + beta ) * 3.14
    print '( ', alpha, ' + ', beta, ') x 3.14 = ', gamma
elif (alpha < beta):
    gamma = ( alpha * beta ) / 2
    print '( ', alpha, ' x ', beta, ') / 2 = ', gamma
else:
    print 'WTF?'

quit()
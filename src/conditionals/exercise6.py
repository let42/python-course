# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the
# score is between 0.0 and 1.0, print a grade using the following table



score = raw_input('Type the score: ')
try:
    score = float(score)
except:
    print 'Bad Score'

if( score >=0.90 ):
    print 'A'
elif( score >=0.80 ):
    print 'B'
elif( score >=0.70 ):
    print 'C'
elif( score >=0.60 ):
    print 'D'
elif( score < 0.60 ):
    print 'F'
else:
    print 'Bad Score'

exit()
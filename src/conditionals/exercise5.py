# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by
# printing a message and exiting the program. The following shows two executions of the program

hours = raw_input('Enter Hours: ')
try:
    hours = float(hours)
except:
    print 'Please type numeric input'
    exit()
pay_rate = raw_input('Enter Pay Rate: ')
try:
    pay_rate = float(pay_rate)
except:
    print 'Please type numeric input'
    exit()
if hours > 40:
    cachet = (pay_rate * 40) + ((pay_rate * 1.5 ) * (hours - 40))
elif hours <=40:
    cachet = (pay_rate * hours)

print 'Your cachet: ', cachet

exit()

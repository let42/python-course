# Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.

hours = int(raw_input('Enter the hours: '))
pay_rate = raw_input('Enter your pay rate: ')
pay_rate = float(pay_rate)
if hours > 40:
    cachet = (pay_rate * 40) + ((pay_rate * 1.5 ) * (hours - 40))
elif hours <=40:
    cachet = (pay_rate * hours)

print 'Your cachet: ', cachet

exit()

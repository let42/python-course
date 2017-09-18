# Exercise 3 Write a program to prompt the user for hours and rate per hour to compute gross

hours = int(raw_input('Inser the number of hours which have you worked >>>'))
payrate = float(raw_input('Insert your pay rate >>>'))

gross_pay = (payrate * hours)
net_pay = (payrate * hours) * 0.75

print 'Gross pay: ', gross_pay, '\n'
print 'Net pay: ', net_pay, '\n'

quit()

# Exercise 1 of Chapter 5: Write a program which repeatedly reads numbers until
# the user enters "done".
# Once "done" is entered, print out the total, count and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using 
# try and except and print an error message and skip to the next number.


def guess_and_calc( ):
	counter = 0
	total = 0
	average = 0
	myinput = 'ls'
	while (myinput != 'done'):
		try:
			myinput = raw_input('Insert a number>>>')
			myinput = float(myinput)
		except:
			if myinput != 'done':
				print "Please, insert a number, not anything else"
				continue
			else:
				break
		counter += 1
		total = total + myinput
		average = total / counter

	print "Typed numbers: ", counter
	print "Total: ", total
	print "Average: ", average


def main():

	guess_and_calc( )
	quit( 0 )

main( )
	

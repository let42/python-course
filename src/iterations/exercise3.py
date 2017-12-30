# Print The Message "Happy new Year" followed by the name of a person
# taken from a list for all people mentioned in the list.

def print_Happy_New_Year_to( listOfPeople ):
	
	for user in listOfPeople:
		print 'Happy New Year, ', user

	print 'Done!'

def main( ):

	listOfPeople=['John', 'Mary', 'Luke']
	print_Happy_New_Year_to( listOfPeople )
	quit(0)

main( )
# Exercise 4
# Create method that take a word, a letter that you want put instead of a letter
# in a specific position request to the user and create a new string that con-
# tains this new letter.

def _change_letter_into_a_string_( word, letter, position ):

	word = word[ :position ] + letter + word[ ( position + 1 ) : ]
	return word

def main( ):

	word = raw_input('Insert a word->')
	letter = raw_input('Insert a letter that you want change->')
	position = raw_input('Insert the position to insert a new letter->')
	try:
		position = int(position)
	except:
		print 'Error exiting'
		quit(1)
	print _change_letter_into_a_string_( word, letter, position )
	quit( 0 )

main( )

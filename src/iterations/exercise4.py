# Print every single letter of a word with 'for' iteration and with 'while' iteration
# Also create a method for all single iteration required. Finally with main method
# require a word to be printed, until isn't typed 'done!'
#

def print_letters_with_for( word ):

	for w in word:
		print w
	print '\n'

def print_letters_with_while( word ):
	length = len( word )
	i = 0
	while i < length:
		print word[i]
		i += 1
	print '\n'


def main( ):

	word = raw_input('>>')
	while True:
		if word != 'done!':
			print_letters_with_for( word )
			print_letters_with_while( word )
			word = raw_input('>>')
		else:
			break

	quit(0)

main( )
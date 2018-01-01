# Exercise-4-bis
# Create a method that take a sentence and a word with the position that you
# want insert instead of.

def _substitute_word_( sentence, word, position, word_length ):

	sentence = sentence[ 0:position ]+ word + sentence[( ( position + 1 ) + 
		(word_length - 1) ) : ]

	return sentence


def main( ):

	sentence = raw_input('Insert a sentence->')
	word = raw_input('Insert a word that you want insert->')
	position = raw_input('Insert the position to insert the new word->')
	word_length = raw_input( 'Insert the legnth of the word that u want chan->')
	try:
		position = int(position)
		word_length = int(word_length)
	except:
		print 'Error exiting'
		quit(1)
	print _substitute_word_( sentence, word, position, word_length )
	quit( 0 )


main( )
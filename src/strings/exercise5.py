# Exercise 5
# Encapsulate this code in a function named count, and generalize it so that
# it accepts the string and the letter as arguments.

def count( word, letterToBeCount ):
	
	count = 0
	for letter in word:
		if letter == letterToBeCount:
			count += 1
	return count

def main( ):

	word = raw_input('Enter the word->')
	letterToBeCount = raw_input('Enter the word that you want count->')
	print count(word, letterToBeCount)

main( )
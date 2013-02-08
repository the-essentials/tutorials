def palrecursive(word):
	if len(word) < 2:
		print "Is a palindrome!!"
		return True
	else:
		if word[0] != word[-1]:
			print "Not a palindrome..."
			return False
		else:
			return palrecursive(word[1:-1])
			

def paliterative(word):

	for i in range(len(word)//2):
		if word[i] != word[-(i+1)]:
			print "Not a palindrome"
			

	print "Is a palindrome!"

def main():
	paliterative("word")
	palrecursive("racecar")
main()
class Node(object):
	def __init__(self, item=None):
		self.cargo = item
		self.next = {}

class Trie(object):
	def __init__(self):
		self.root = Node()

	def insert(self, item):
		currentNode = self.root

		for i in item:
			if currentNode.next.hasKey(item[i]):
				currentNode = currentNode.next[item[i]]
			else:
				currentNode.next[item[i]] = Node(i)
				currentNode = currentNode.next[item[i]]

	def display(self):
		
def main():
	print "Hello"
	print "Why"

if __name__ == '__main__':
	main()
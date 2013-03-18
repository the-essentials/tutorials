"""
Double Linked List
Author: Clayton Rieck
v1.0
"""

class Node:

	def __init__(self, cargo, previous=None, next=None):
		self.cargo = cargo
		self.previous = previous
		self.next = next

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def insert(self, item):
		if self.head == None:
			self.head = Node(item)
			self.tail = self.head
			self.size += 1

		else:
			currentNode = self.head
			while currentNode.next != None:
				currentNode = currentNode.next

			currentNode.next = Node(item, currentNode)
			self.tail = currentNode.next
			self.size += 1



	def search(self, item):
		if self.head == None:
			return "There's nothing in the List!"

		else:
			currentNode = self.head
			index = 0
			while currentNode != None:
				if currentNode.cargo == item:
					return "Found item at index "+ str(index)
				else:
					currentNode = currentNode.next
					index += 1

			return "Item is not in the list!"

	def delete(self, item):
		if self.head == None:
			return "Nothing is in the List!"
		else:
			currentNode = self.head
			while currentNode.next != None:
				
				if currentNode.cargo == item:
					
					if currentNode == self.head:
						self.head = currentNode.next
						self.head.previous = None
						self.size -= 1
					
					elif currentNode == self.tail:
						self.tail = currentNode.previous
						self.tail.next = None
						size -= 1

					else:
						currentNode.previous.next = currentNode.next
						currentNode.next.previous = currentNode.previous
						self.size -= 1

					return "Deleted the Node holding "+str(item)
				
				else:
					currentNode = currentNode.next

			return "That number doesn't exist in the list"


	def displayForwards(self):
		currentNode = self.head
		while currentNode != None:
			print currentNode.cargo
			currentNode = currentNode.next

	def displayBackwards(self):
		currentNode = self.tail
		while currentNode != None:
			print currentNode.cargo
			currentNode = currentNode.previous

def main():
	myLList = LinkedList()

	myLList.insert(1)
	myLList.insert(2)

	myLList.delete(1)

	myLList.displayBackwards()

if __name__ == '__main__':
	main()


"""
Author: Clayton Rieck	
Data Structure: Singly Linked List
Language: Python 2.7
Prerequsites: Knows Python syntax and has some knowledge of OOP (Object Oriented Programming)
Difficulty: Easy/Moderate
Version: 1.0

Provides a walk through of the implementation of a simple data structure,
a singly linked list.
"""
#-----------------------------------------------------------------------------
"""
If you're reading this you have probably heard of the term 'encapsulation' and if
not it's rather easy to understand. Encapsulation is the bundling of data with methods
that operate on that data. So we encapsulate the data and the methods that manipulate
that data. Another way to think of encapsulation is this:
	
	You have a box and you label it something (lets say "Toys" for this example).
	You shouldn't put things in that box that don't pertain to "Toys" because
	you won't be able to find what you're looking for down the road. So you put
	in some toys and that box holds those toys for you and everything that has to
	do with toys you put in there as well.

This "box" is referred to as an "Object" in the coding world, and that's what we'll
be creating and manipulating.

NOTE: You can think of Objects as any shape you'd like.

Now you know what encapsulation is but why do we want to use OOP? It helps us
when it comes to code reduction. For example, when you were starting to program
you may have repeated lines and lines of code that do the same thing and your teacher
may have told you "Don't repeat your code!" so you put it into a method. When you
do that those multiple lines of repeated code are now condensed into one spot. From
there you can edit it with ease intead of going through and fixing all of the repeats.

We're doing the same thing here except now we're putting all of the methods and
data that go with those methods in one "box" or "Object." This Object can be recreated
as many times as we want too! (Which is why we use OOP as you'll see later)

NOTE: There are times where OOP is NOT the way to go about solving a problem.
	Use your discretion!

Lets get started now
"""
#------------------------------------------------------------------------------
"""
A Linked List is a set of Nodes that are linked together like so
		__ __
Node = |__|__|-->
						 __ __     __ __     __ __
						|__|__|-->|__|__|-->|__|__|-->
	
Where the last arrow points to nothing.

NOTE: These nodes hold 2 things, but you have have them hold any number of things.

We refer to the first node as the "head" of the Linked List (more on that later),
but first we have to make the nodes that will make up our Linked List.

When creating this object we come across a new keyword, 'class'. This is our box
and the word that comes after it is the label we're giving our box.

Every class has a basic format in any language. You define your class (label your box)
and then you must have an 'initializer' function. This comes in different forms as you
change languages. In Python we define this function as 'def __init__(self)' and it works
like any other function EXCEPT it is never called directly (More on that later). For
now, though, lets set up our Node class and our initializer.
"""
class Node:

	def __init__(self, item):
		self.cargo = item
		self.next = None

	"""
	Now what does this function do? Well when we create a new node and pass it an item,
	the initialize function is implicitly called and creates new data members (the toys in our box),
	'cargo' and 'next', and sets cargo equal to the item we passed it and sets 'next' to
	None because the node is all by itself. It doesn't connect to anything.

	Now you're probably wondering... what is this 'self' argument/keyword that I see in all of the method
	arguments? Well that's a long explanation that I'll condense down:
		
		Python decided to do methods in a way that makes the instance (a specific copy of an Object) to which the method belongs 
		be passed automatically, but not received automatically: the first parameter of methods is the instance the method is 
		called on. That makes methods entirely the same as functions, and leaves the actual name to use up to you. 'self' is not 
		special to the code, it's just another object.
		Python is all for making things explicit, making it obvious what's what, and although it doesn't do it entirely everywhere,
		it does do it for instance attributes. That's why assigning to an instance attribute needs to know what instance to assign to,
		and that's why it needs self..

		Still confused? I'll condense it more...

		It literally means "myself". self.cargo is the same as saying the cargo that belongs to myself.
		def getCargo(self) is the same as saying get the cargo that belongs to myself
		def __init__(self, item) is the same as saying create a new, unique, copy of me with my own special cargo equaling the item

		Later on, methods get more complex. When you see this: methodName(self), just think this: do this action on myself

	We have our toys in our box named "Node" now but we need something to let us get
	things in the box and change things in the box. The methods below will let us do that

	================================ METHODS ===================================
	Method getCargo: Gives us back what the "cargo" is in the box
	Method getNext: Gives us back what the next node is
	Method setNext(arg1): sets 'next' equal to whatever is passed to this method 
	============================================================================
	"""
	def getCargo(self):
		return self.cargo

	def getNext(self):
		return self.next

	def setNext(self, nextThing):
		self.next = nextThing


# The end of our class definition

"""
Now we have to make the actual Linked List. We have the nodes that will make
the linked list but we don't have a box to hold all of the components of the 
linked list (a.k.a. the nodes). You can imagine that the Linked List is a box that
holds other boxes. So if our nodes are smaller boxes that the Linked List holds,
then the Linked List looks like this:
					 ________________________________
   					|  __ __     __ __     __ __	 |
   					| |__|__|-->|__|__|-->|__|__|--> |
   					|________________________________|

Where the Linked List is the big box that encapsulates the sequence of nodes.

In a Linked List we care about a few of things and, sometimes, other things
(which we won't cover in this implementation). Mostly, we care about which
node marks the beginning of the list and the size of the list. Since these are
the things that make up a linked list (other than the nodes) lets put them in our
initializer method so that when we create a new linked list we have those things in
our box ready for us to use.

Why do we set 'head' equal to None? Because when we initialize the linked list there
isn't anything in it just like when you set up an array like so
	
								array = []

There's nothing in it and therefore there's no 'head' element and the size is 0
since there is nothing in it.

So lets make our Linked List box and make the __init__ method
"""
class LList:

	def __init__(self):
		self.head = None
		self.size = 0


	"""
	Now it's time for the other methods in the list. In an array we can search
	for elements, remove elements, insert elements and get the size of our array.
	Those are the methods we'll be implementing along with a 'display' method that
	will output the list to the user.

	================================ METHODS =======================================
	Method size: Give us back the size of the list
	Method insert: Insert the item passed in into the list
	Method search: Searches the list for the item passed in and returns its position
	Method remove: Removes the item passed in from the list
	Method display: Displays the list starting at the beginning to the end
	================================================================================

	There will be a line by line walkthrough of the more complex methods below
	"""
	def size(self):
		return self.size

	def insert(self, item):
		if self.head == None: # A check to see if there is anything in the linked list
			# If not...
			"""
			Explantion of Line 192: Here we are setting the 'head' of the Linked
			List. The 'head' is a NEW Node (or box) that holds the toy, item, which
			we passed to this method. The syntax 'Node(item)' calls the 
			initialize method of the Node class and passes in 'item' to that method.

			Saying Node(item) replaces '__init__' if you remember from above, the __init__
			method is never called directly. The class name with parenthesis after it is what calls that
			method. So when you see 'Node(item)' you can think of it as
			'Node.__init__(item)'.		
			"""
			self.head = Node(item)
			self.size += 1 # Increase the size of the list by 1

		else: # If there is something in the list
			current = self.head # The local variable 'current' will be a copy of the 'head' node

			"""
			Explanation of 'while loop' below: Lets draw this out
			We have a linked list for example:
 					 ________________________________
   					|  ___ __     ___ __     		 |
   					| |_a_|__|-->|_b_|__|--> 		 |
   					|________________________________|

			We want to insert a 'c', so we pass the 'insert' method 
			a 'c'. We set 'current' equal to the head node above, so
					   ___ __ 
			current = |_a_|__|-->

			Then the program says, is the next thing of the current node None?
								  				  ___ __
			Lets check that: current.getNext() = |_b_|__|-->

			Since the next thing is a node and not None we set the 'current'
			variable equal to the next node in the list. So,
					   ___ __ 
			current = |_b_|__|-->

			This is how we iterate through a linked list. The program will 
			keep doing this until the current node's next variable equals None.
			When the current node's next is None it will break out of the while 
			loop and continue.
			"""
			while current.getNext() != None:
				current = current.getNext()
			

			current.setNext(Node(item)) # We set the next node to a new Node containing the item passed in
			self.size += 1 # Increases the size variable by 1

			# This method is equivalent to the append() method. It will add an item at
			# the end of the list always
		
	

	def search(self, item):
		current = self.head # Just like in the insert method, we start at the head
		counter = 0 # Will keep track of which node we're at (will be important)

		if self.size == 0: # If the list is empty...
			print "There's nothing in the list" # Tell the user there's nothing in the list
		else:
			"""
			Look at the while loop below...
			Question: Why do we say 'while current != None' instead of
			'while current.getNext() != None' like in the insert? Lets draw 
			this out again using the example list from above in the insert method:
			
			Lets say we're searching for 'b'
			If we said 'while current.getNext() != None' this is what would happen
					   ___ __ 
			current = |_a_|__|-->

			The next thing is a node so we continue into the loop.
			Then we check to see if the current node is holding the 'b'.
			It's not so we increase the 'counter' by 1 and set 'current'
			equal to the next node in the list. So now
					   ___ __ 
			current = |_b_|__|-->

			Then the while loop checks to see if the next thing is None or not
			Since current.getNext() equals None, the loop breaks and skips over
			the node that is holding our 'b'.
			So having 'while current.getNext() != None' will skip over the last node
			in the list. Having 'while current != None' will result in this:
			Check if current is None
					   ___ __ 
			current = |_a_|__|-->
			It's not, so go into loop.
			Check if it's holding 'b'.
			It's not so continue on.
					   ___ __ 
			current = |_b_|__|-->
			Check if it's holding 'b'.
			It is! Tell the user!

			NOTE: Lets see what would happen if we looped one more time... 
			current = current.getNext()
				==> current.getNext() = None so...
			Check if current is None
			current = None
			It is! So break from while loop
			"""
			while current != None: # if current variable does not equal None, loop
				if current.getCargo() == item: # check to see if the current node is holding the item being searched for
					# If it is...
					print "Found item at position "+str(counter) # Tell user which position it's at
					return
				# If not...
				counter += 1 # Increase counter by 1
				current = current.getNext() # Set current to next thing
			
			# If you break out of the loop that means you searched the whole
			# list and didn't find the item... So tell the user it doesn't exist
			# in the list
			print "Item doesn't exist"

	def remove(self, item):
		current = self.head # Same as above
		previous = None # Will explain this later

		if current == None: # If there is nothing in the list tell the user
			return "There's nothing in the list"
		else:
			while current != None: # Explanation from above
				"""
				This is where things can get a little confusing so I'll draw
				a lot of diagrams. Lets look at the first 'if' statement.

				So if the current node is holding the item we're looking for AND
				it's the head of the list, make the new head the next node...

				In essence we're sorta cheating because we aren't actually 'removing'
				the node but we're making it seem like we are. It will become clearer
				in the diagrams.
				"""
				if current.getCargo() == item and current == self.head:
					self.head = current.getNext()
					return "Removed Node"
	
					"""
					Now lets look at the 'elif' statement:

					If the current node is holding the item we want to remove,
					set the previous node's 'next' variable equal to the current
					node's 'next' value.	
					"""
	
				elif current.getCargo() == item:
					previous.setNext(current.getNext())
					return "Removed Node"

				"""
				If those checks don't happen, set the previous node to the current
				node and set the current node to the next node in the list	
				"""
				previous = current
				current = current.getNext()

				"""
				Diagram time!!
				Lets say we have this linked list:
					 _______________________________________
   					|  ___ __     ___ __      ___ __		|
   					| |_a_|__|-->|_b_|__|--> |_c_|__|-->	|
   					|_______________________________________|

   				First example: Removing the head
   					   	   ___ __ 
				current = |_a_|__|-->
				previous = None (this is because there is no node before the first node)

				while loop
					check to see if current node is holding item we want to remove
					It is!
				So this is what happens...
				We say, "Instead of removing it, lets make it seem like it has been removed
				by setting the next node equal to the "head" so our list will look like this
						 _______________________________________
   						|  				 ___ __     ___ __    	|
   						| 				|_b_|__|-->|_c_|__|-->	|
   						|--------------------------------------	|
   						|	Ignored space in Linked list 		|
   						|	 ___ __ 							|
   						|	|_a_|__|--> 						|
   						|_______________________________________|
				So, in essence, that node containing 'a' is still in the area where
				the Linked List is, but we just tell the computer "Ignore it. That's
				no longer the head." So removing a node is equivalent to ignoring a node

				Second example: Removing a middle node
					 _______________________________________
   					|  ___ __     ___ __      ___ __		|
   					| |_a_|__|-->|_b_|__|--> |_c_|__|-->	|
   					|_______________________________________|

   				Now lets say we want to remove 'b'. This is where that 'previous'
   				variable comes in. We check the current node which equals the head.
   						   ___ __ 
				current = |_a_|__|-->
				previous = None

   				Does it have the item we're looking for? No..
   				So NOW this is what happens...
   				   		   ___ __ 
				current = |_b_|__|-->
				   		    ___ __ 
				previous = |_a_|__|-->
				
				We set the previous node to what the current node used to be
				and the current node equal to the next node in the list so now
				you're keeping track of 2 nodes and you'll see why this is important

				We check if the current is None. It's not so go into the while loop.
				Skip the first 'if' because we're not at the head anymore.
				NOW, the current is holding the thing we want to delete.. So lets "remove" it
				
				What does the program do in the 'elif' statement? It says:
					Set the previous node's 'next' variable equal to the current node's 'next' value.
					What is that doing? Lets look at the diagram:

						We want to "remove" the node holding 'b' (a.k.a. we want to ignore it)
						by doing the procedure above	
						 _______________________________________
   						|  ___ __	  ___ __     ___ __    		|
   						| |_a_|__|-->|_b_|__|-->|_c_|__|-->		|
   						|--------------------------------------	|
   						|	Ignored space in Linked list 		|
   						|			 							|
   						| 										|
   						|_______________________________________|

						We ignore the node holding 'b' by setting the previous node's next value to
						the 'next' value of the node we just ignored (the current node), so the linked
						list looks like this 
   						 _______________________________________
   						|  	 ___ __      			 ___ __    	|
   						| 	|_a_|__|--------------->|_c_|__|-->	|
   						|--------------------------------------	|
   						|	Ignored space in Linked list 		|
   						|	 			 ___ __ 				|
   						|				|_b_|__|--> 			|
   						|_______________________________________|

   						That arrow of the previous node now works its way around the middle node so it
   						seems like we're deleting the middle node but we actually aren't

   				Third Example: Removing the last node

   				This is just like the second example, but, instead, we're set the previous node's 'next' value to None because
   				the current node's next value is None. It's that simple!			
				"""

	def display(self):
		"""
		I won't go through the display method in detail because it's just like the search
		method in terms of the while loop, but what we're doing is we're printing out the
		cargo of the node when we arrive at it and that's how the list is getting displayed.
		"""
		current = self.head # Set current to head
		print current.getCargo() # Print out the cargo in the head
		current = current.getNext() # set current node equal to the next node in the list

		while current != None: # while current isn't None
			print current.getCargo() # print cargo the node
			current = current.getNext() # set current equal to the next node	

# Here you can experiment inserting, removing, searching, and displaying the Linked List. Try it out and have fun!
# Thanks for reading my walkthrough and I hope it was helpful!
def main():
	list = LList()
	list.insert("a")
	list.insert("c")
	list.insert("p")
	list.display()
	list.remove("p")
	print "---------- After removal ------------"
	list.display()
	list.search("c")
	print list.size
main()

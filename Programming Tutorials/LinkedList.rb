=begin
Author: Clayton Rieck	
Data Structure: Singly Linked List
Language: Ruby
Prerequsites: Knows Ruby syntax and has some knowledge of OOP (Object Oriented Programming)
Difficulty: Easy/Moderate
Version: 1.0

Provides a walk through of the implementation of a simple data structure,
a singly linked list.
=end
#-----------------------------------------------------------------------------
=begin
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
=end
#------------------------------------------------------------------------------
=begin
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
and then you must hav an 'initializer' function. This comes in different forms as you
change languages. In Ruby we define this function as 'def initialize' and it works
like any other function EXCEPT it is never called directly (More on that later). For
now, though, lets set up our Node class and our initializer.
=end
class Node

	def initialize(item)
		@cargo = item
		@next = nil
	end

=begin
Now what does this function do? Well when we create a new node and pass it an item,
the initialize function is implicitly called and creates new data members (the toys in our box),
'cargo' and 'next', and sets cargo equal to the item we passed it and sets 'next' to
nil because the node is all by itself. It doesn't connect to anything.

We have our toys in our box named "Node" now but we need something to let us get
things in the box and change things in the box. The methods below will let us do that

================================ METHODS ===================================
Method getCargo: Gives us back what the "cargo" is in the box
Method getNext: Gives us back what the next node is
Method setNext(arg1): sets 'next' equal to whatever is passed to this method 
============================================================================
=end
	def getCargo
		return @cargo
	end

	def getNext
		return @next
	end

	def setNext(nextThing)
		@next = nextThing
	end	

end # Tells the computer that is the end of our class definition

=begin
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

Why do we set 'head' equal to nil? Because when we initialize the linked list there
isn't anything in it just like when you set up an array like so
	
								array = []

There's nothing in it and therefore there's no 'head' element and the size is 0
since there is nothing in it.

So lets make our Linked List box and make the initialize method
=end
class LList

	def initialize
		@head = nil
		@size = 0
	end

=begin
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
=end
	def size
		return @size
	end

	def insert(item)
		if @head == nil # A check to see if there is anything in the linked list
			# If not...
=begin
			Explantion of Line 177: Here we are setting the 'head' of the Linked
			List. The 'head' is a NEW Node (or box) that holds the toy, item, which
			we passed to this method. The syntax 'Node.new(item)' calls the 
			initialize method of the Node class and passes in 'item' to that method.

			'new' replaces 'initialize' if you remember from above, the initialize
			method is never called directly. The 'new' keyword is what calls that
			method. So when you see 'Node.new(item)' you can think of it as
			'Node.initialize(item)'.		
=end
			@head = Node.new(item)
			@size += 1 # Increase the size of the list by 1

		else # If there is something in the list
			current = @head # The local variable 'current' will be a copy of the 'head' node

=begin
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

			Then the program says, is the next thing of the current node nil?
								  				___ __
			Lets check that: current.getNext = |_b_|__|-->

			Since the next thing is a node and not nil we set the 'current'
			variable equal to the next node in the list. So,
					   ___ __ 
			current = |_b_|__|-->

			This is how we iterate through a linked list. The program will 
			keep doing this until the current node's next variable equals nil.
			When the current node's next is nil it will break out of the while 
			loop and continue.
=end
			while current.getNext != nil
				current = current.getNext
			end

			current.setNext(Node.new(item)) # We set the next node to a new Node containing the item passed in
			@size += 1 # Increases the size variable by 1

			# This method is equivalent to the append() method. It will add an item at
			# the end of the list always
		end
	end

	def search(item)
		current = @head # Just like in the insert method, we start at the head
		counter = 0 # Will keep track of which node we're at (will be important)

		if @size == 0 # If the list is empty...
			puts "There's nothing in the list" # Tell the user there's nothing in the list
		else
=begin
			Look at the while loop below...
			Question: Why do we say 'while current != nil' instead of
			'while current.getNext != nil' like in the insert? Lets draw 
			this out again using the example list from above in the insert method:
			
			Lets say we're searching for 'b'
			If we said 'while current.getNext != nil' this is what would happen
					   ___ __ 
			current = |_a_|__|-->

			The next thing is a node so we continue into the loop.
			Then we check to see if the current node is holding the 'b'.
			It's not so we increase the 'counter' by 1 and set 'current'
			equal to the next node in the list. So now
					   ___ __ 
			current = |_b_|__|-->

			Then the while loop checks to see if the next thing is nil or not
			Since current.getNext equals nil, the loop breaks and skips over
			the node that is holding our 'b'.
			So having 'while current.getNext != nil' will skip over the last node
			in the list. Having 'while current != nil' will result in this:
			Check if current is nil
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
			current = current.getNext
				==> current.getNext = nil so...
			Check if current is nil
			current = nil
			It is! So break from while loop
=end
			while current != nil # if current variable does not equal nil, loop
				if current.getCargo == item # check to see if the current node is holding the item being searched for
					# If it is...
					puts "Found item at position "+(counter).to_s # Tell user which position it's at
					return
				end
				# If not...
				counter += 1 # Increase counter by 1
				current = current.getNext # Set current to next thing
			end
			# If you break out of the loop that means you searched the whole
			# list and didn't find the item... So tell the user it doesn't exist
			# in the list
			puts "Item doesn't exist"
		end
	end

	def remove(item)
		current = @head # Same as above
		previous = nil # Will explain this later

		if current == nil # If there is nothing in the list tell the user
			return "There's nothing in the list"
		else
			while current != nil # Explanation from above
=begin
				This is where things can get a little confusing so I'll draw
				a lot of diagrams. Lets look at the first 'if' statement.

				So if the current node is holding the item we're looking for AND
				it's the head of the list, make the new head the next node...

				In essence we're sorta cheating because we aren't actually 'removing'
				the node but we're making it seem like we are. It will become clearer
				in the diagrams.
=end
				if current.getCargo == item && current == @head
					@head = current.getNext
					return "Removed Node"
=begin
				Now lets look at the 'elsif' statement:

				If the current node is holding the item we want to remove,
				set the previous node's 'next' variable equal to the current
				node's 'next' value.	
=end

				elsif current.getCargo == item
					previous.setNext(current.getNext)
					return "Removed Node"
				end
=begin
				If those checks don't happen, set the previous node to the current
				node and set the current node to the next node in the list	
=end
				previous = current
				current = current.getNext
=begin
				Diagram time!!
				Lets say we have this linked list:
					 _______________________________________
   					|  ___ __     ___ __      ___ __		|
   					| |_a_|__|-->|_b_|__|--> |_c_|__|-->	|
   					|_______________________________________|

   				First example: Removing the head
   					   	   ___ __ 
				current = |_a_|__|-->
				previous = nil (this is because there is no node before the first node)

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
				previous = nil

   				Does it have the item we're looking for? No..
   				So NOW this is what happens...
   				   		   ___ __ 
				current = |_b_|__|-->
				   		    ___ __ 
				previous = |_a_|__|-->
				
				We set the previous node to what the current node used to be
				and the current node equal to the next node in the list so now
				you're keeping track of 2 nodes and you'll see why this is important

				We check if the current is nil. It's not so go into the while loop.
				Skip the first 'if' because we're not at the head anymore.
				NOW, the current is holding the thing we want to delete.. So lets "remove" it
				
				What does the program do in the 'elsif' statement? It says:
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

   				This is just like the second example, but, instead, we're set the previous node's 'next' value to nil because
   				the current node's next value is nil. It's that simple!

				
=end

			end
		end
	end

	def display
=begin
		I won't go through the display method in detail because it's just like the search
		method in terms of the while loop, but what we're doing is we're printing out the
		cargo of the node when we arrive at it and that's how the list is getting displayed.
=end
		current = @head # Set current to head
		puts current.getCargo # Print out the cargo in the head
		current = current.getNext # set current node equal to the next node in the list

		while current != nil # while current isn't nil
			puts current.getCargo # print cargo the node
			current = current.getNext # set current equal to the next node	
		end
	end

end

# Here you can experiment inserting, removing, searching, and displaying the Linked List. Try it out and have fun!
# Thanks for reading my walkthrough and I hope it was helpful!
list = LList.new
list.insert("a")
list.insert("c")
list.insert("p")
list.display
list.remove("p")
puts "---------- After removal ------------"
list.display
list.search("c")
puts list.size

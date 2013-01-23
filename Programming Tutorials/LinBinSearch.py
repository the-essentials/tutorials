"""
Author: Clayton Rieck	
Program: Linear Search and Binary Search
Language: Python 2.7
Prerequsites: Knows Python syntax
Difficulty: Easy
Version: 1.0

Provides a walkthrough of the implementation of the linear search and
binary search algorithms along with explanation of the efficiency of each
"""
#---------------------------------------------------------------------------------------------------------------------
"""
I'm going to go over 2 different searching algorithms, linear and binary search. Searching
is an important concept and there's a lot research that goes in to finding the best possible
searching algorithm. We search for things almost every day (i.e. Google) so it's important that
we use an algorithm that'll give us what we're searching for as fast as possible. I will go
through the efficiency of each search as I cover the code.

Some things you should know before we begin:

What is an algorithm?
It is a process or set of rules to be followed in calculations or other problem-solving operations, 
especially by a computer.

How do we classify an algorithm in computer science?
I will only gloss over this topic since algorithmic classification is a long discussion and rather complex...
When we classify an algorithm (like a search algorithm) we set up a graph of time versus number of items, n,
like so:

								|
								|								
								|
								|
						Time	|
								|
								|
								|
								|____________________

										  n

And we then ask ourselves "hm, how much time will this algorithm take based on how many items I have?"
Well "time" is sort of broad in this context because how do we classify it? In seconds? Milliseconds?
The answer to that question is we classify "time" as "number of iterations". Think back to when you were
first learning about loops. You learned about the for loop and how it could do some block of code a certain
number of times. Every time that certain block of code executes that's what we call an "iteration".
For example:
		Our for loop ----> for i in range(10):
		That one line says a lot. For our purposes, though, it tells us to do 10
		iterations. How do we know it's 10? Because it's 'in range(10)'. That one part of
		the for loop tells us the number of iterations which also tells us our "time" since
		"time" = "number of iterations" as mentioned above.
So now we know what our time is equal to. So what's our 'n'? Our 'n' is simply the number of items we have as
mentioned above. That's all you need to know for now and I will continue going more in depth as we go through the
algorithms. Lets get started.
"""
#---------------------------------------------------------------------------------------------------------------------
"""
Method linearSearch: As you'll see later in the description, the name implies its efficiency but for now
lets go through the code. 

We start with the parameters. The first thing we pass to it is an array we want to search in. This can be of any size,
and the second parameter is a number (in this case) that we want to search for.
NOTE: The array can have anything in it whether it be integers, characters, strings, etc.
Now the function knows of the array it has to search and what it has to search for. Lets find what we're looking for, shall we?
"""
def linearSearch(array, itemToLookFor):
	
	"""
	We need to start the searching now. Lets stop and think for a second. Say I wanted you to
	print out all of the elements of an array only using 1 print statement. How would you do this?
	You might just say "Lets loop through the list and print out each element" which is exactly right!
	We're doing the same thing here except now, instead of printing each element out, we're looking
	for a certain element. So here's how we're going to appraoch this problem...

	We have an example list like so:

								[20, -7, 8, 13, 9, 24, -3]

	NOTE: There isn't any rhyme or reason to the numbers selected

	Now say we want to search for the number 9 in the list. We pass the array and the number 9 into our
	method and it goes directly into the for loop.

	We want to search our entire list for the number 9 and we know where it is. It's at position 4, but the
	computer doesn't know that so we tell it "Start at the beginning of the list and check every element of
	the list and if you find the number tell us. If not, tell us that number isn't in the list. Drawn out, it
	looks like this:
		Iteration 1: i = 0
								[20, -7, 8, 13, 9, 24, -3]	
								 ^	
								 |
							  array[i]

		On the first iteration, i = 0 so array[i] equals 20. Well lets see if that number equals the number
		we're looking for. 20 =?= 9. No, 20 =/= 9. So since 20 does not equal 9 we continue on.

		Iteration 2: i = 1
								[20, -7, 8, 13, 9, 24, -3]	
								   	  ^	
								 	  |
							  	   array[i]

		Now we're on the second iteration so i = 1 which implies that array[i] = -7. We, again, check to see
		if -7 equals 9. -7 =?= 9. -7 =/= 9. Since -7 does not equal 9 we continue on.

		We keep doing this until the 5'th iteration (in this example) which I will skip to

		Iteration 5: i = 4
								[20, -7, 8, 13, 9, 24, -3]	
								 				^	
								 				|
							  				 array[i]

		Now things get more interesting. We check to see if array[i] is equal to 9. 9 =?= 9. 9 == 9. Awesome!
		We found our number in the list so we tell the user "We found the number you were looking for at this
		position!"
	"""
	for i in range(len(array)): # Will ensure that we loop through the entire list and check every element
		if itemToLookFor == array[i]: # Checks to see if the number we're looking for equals the current element we're on
			# If it is...
			print "Found number at position "+str(i) # Tell the user the number was found at the position it was found at which is i 
			return # End the method because we don't want to keep looking if we already found it

	"""
	What if the number wasn't found? How do we determine if the number could be found?
	If the number isn't found lets just tell the user that it wasn't found using a print
	statement. Determining if the number couldn't be found is rather simple. Our for loop above
	will loop through the entire list and check every element. Well what happens when it's at the
	end of the list and has already checked the last element? It breaks out of the for loop and executes
	any code after that. In this case, it's our print statement telling the user the number couldn't
	be found which is why this print statement is here at the end of the method outside of the for loop.
	"""
	print "That number isn't in the list"

	"""
	Analysis: Now you know how this algorithm works, so lets analyze its efficiency. Something you
	need to know before we do that is the notation we use. We use something called Big Oh notation
	and it looks like this:
											O()
	We'll figure out what goes into the parenthesis and what it actually means later. But for now, lets recap. We iterate 
	over every element until we find the number we're looking for. So that's 1 iteration per 1 element. Let's fill in the 
	graph from above:
	
								|
								|								
							   .|
							   .|
						Time   .|              .
							   4|          .
							   3|      .
							   2|  .
							   1|____________________
							       1   2   3   4   ...
										  n
	
	If we connect the dots we can see that the equation of the line made has a slope of 1 making
	the equation of this line y = 1x. But x = n if we look at our graph so we can say y = 1n. So
	how can we use this and our Big Oh notation? Lets define Big Oh.

	Big Oh: It's the upper bound of the growth rate of this algorithm.
	What does that mean? Growth rate is just the slope. So how fast time increases as your 'n' increases.
	What does upper bound mean? There's a more technical definition, but you can think of it as the worst
		possible performance of this algorithm. 
	There is a lower bound and tight bound to algorithms but we won't cover those. Big Oh is a good measurement
	of algorithms since we want to know what our worst performance is so that we can work on making that better.

	Now, what goes in those parenthesis? Look at our equation, y = 1n. Everything to the right of the '=' goes in
	the parenthesis so for the linear search we have:

											O(n)

	Which tells us that this algorithm is in n-time or linear in growth, hence LINEAR search.

	NOTE: What if we had y = 1n + 7 for example? We would still have O(n) as our Big Oh because the '+ 7'
	doesn't affect our growth. The growth is the slope and that's what we care about. 
	"""

def binarySearch(array, itemToLookFor):
	"""
	The binary search algorithm is definitely more efficient than the linear search and it's definitely
	best to visualize this algorithm than for me to write prose.

	The first thing we MUST do before we do a binary search is to sort the list. If the list is not sorted
	then it won't work and you'll see why. But lets start with this array:

										[20, -7, 8, 13, 9, 24, -3]

	The first thing we so is sort it so our new array looks like this:

										[-7, -3, 8, 9, 13, 20, 24]

	Ok. We have a sorted array so now lets continue. The way a binary search works is instead of looking 
	through the entire list, lets only look at the relevant values. How do we determine which values are relevent?
	That's what the next few diagrams will show:
	We start with our list:
										[-7, -3, 8, 9, 13, 20, 24]

			Lets say we're searching for 8 this time. Instead of starting from the beginning we're going to
			start from the middle. Why the middle? You'll see why...

		So lets start searching:
			
			Iteration 1:

			We get the middle value
										[-7, -3, 8, 9, 13, 20, 24]
													^
													|

			We check and see if that value equals what we're looking for. 9 =?= 8. 9 =/= 8, so
			we keep going. But this is where things become interesting and this is the key as to
			why binary searching is more efficient than a linearly searching.

			We then check and see if what we're looking for is greater than or equal to the middle value..
			If it is greater, we ignore the lesser values INCLUDING the middle value. And if it's lesser,
			we ignore the greater values INCLUDING the middle value. So, 8 < 9 so now this is what happens...

							  [-7, -3, 8, 9, 13, 20, 24] ==> [-7, -3, 8]

			So now we have condensed our list into a much smaller list. This will make searching A LOT easier.

			Iteration 2:

			Our list now
												[-7, -3, 8]

			Get the middle value

												[-7, -3, 8]
													  ^
													  |

			We check to see if that value equals what we're looking for. -3 =?= 8. -3 =/= 8 so we
			check and see if -3 is greater than or less that 8. It is less than 8 so we condense our list accordingly:

											[-7, -3, 8] ==> [8]

			Iteration 3:

			Our list now

													 [8]

			Get the middle value

													 [8]
													  ^
													  |

			Check to see if the middle value equals the value we're looking for. 8 =?= 8. Yes! 8 == 8 and we're done!

			That took 3 iterations to complete. Turns out that that would be the same as the linear search in this case.
			But lets say we were searching for 13 instead. It would only take 3 iterations for the binary search instead
			of the 4 it would take with the linear search. That may not seem like a big difference but think of it this way...
			If we had a list of a billion numbers and we had to search for one specific number, which search would you choose?
			I'll let you decide.

			NOTE: There are best cases and worst cases for both algorithms. 
				Best case: Linear --> If the element we're looking for is the first thing in the list
						   Binary --> If the element we're looking for is the middle value in the list

				Worst Case: Linear AND Binary --> If the element we're looking for is at the end of the list

				Draw these out if you don't grasp as to why this is and follow the algorithm like I did above.
	"""

	beginningOfArray = 0 # Determines which position is the beginning of the array
	endOfArray = len(array) # Determines the position is the end of the array

	while beginningOfArray < endOfArray: # while the list still has a size
		
		middlePosition = (beginningOfArray+endOfArray)/2 # The middle position is the beginning position + the last position divided by 2 
		middleValue = array[middlePosition] # The middle value is at the middle position of the array

		if middleValue < itemToLookFor: # if the middle value is less than the item being searched for
			beginningOfArray = middlePosition+1 # ignore the left side of the array INCLUDING the middle

		elif middleValue > itemToLookFor: # if the middle value is grater than the item being searched for
			endOfArray = middleValue+1 # ignore the right side of the array INCLUDING the middle

		else: # When the list only has one item left it must be the item being searched for so...
			print "Number was found!" # tell the user the number was found
			return
			

	print "Number isn't in the list"

	"""
	Now you know how this algorithm works, but the analysis can get a little confusing. So I will
	say this: Big Oh of binary searching is O(log n). Much much better than the linear search.
	"""

# Thanks for using my guide! Feel free to experiment with different arrays.
# I hope it was helpful!
def main():

	array = [-3, 5, 8, 2, 0, -20, 3, 8, 10, 7]

	linearSearch(array, 5)

	binarySearch(array, 8)

main()
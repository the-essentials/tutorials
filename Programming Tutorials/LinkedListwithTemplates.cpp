/*
Author: Clayton Rieck	
Data Structure: Singly Linked List
Language: C++
Prerequsites: Knows C++ syntax and has knowledge of OOP (Object Oriented Programming)
	and knows how to implement a Linked List.
Difficulty: Easy/Moderate
Version: 1.0

Goes over Templating, a feature of C++.
*/
// ----------------------------------------------------------------------------------------------
/*
I'm assuming that if you're reading this you know what a Linked List is
and that you're comfortable implementing the functions of a Linked List.

Note: I did not implement a remove function. You may implement your own if
	you would like though :)

I'm going to go over Templating in C++. It gives your programs the power of generality
which is a huge deal. Why is it a big deal? Well...

Templating, in a nutshell, allows for the operation of generic types. What does that
mean? Pretty much, we can tell our objects that we create what 'types' they hold/are.

For example, if we make a 'Node' class, we would need to declare the data type of
	our 'cargo'. This could be an int, string, bool, etc.

If our classes are templated, we can declare what data 'type' they hold upon instantiation.
This makes our lives more convenient because we can write one class definition that will be 
able to utilize any data type instead of having to create the same class over and over again
for ints, doubles, bools, etc.
*/
#include <iostream>

using namespace std;

template <class type> // This is the syntax for a templated declaration of a class
/*
Whoa. What does this mean? Well, we're making a templated class so the 'template' keyword sets that up
for us. But what is the '<class type>' thing all about? That's what we call a 'template parameter'.
The template parameter is what give us the power to declare what type we want our Nodes and Linked List (in this case)
to be. You can think of it this way:

Lets say we have a method called 'square' which squares a number we give it. We would make it like so:

			int square(int x){
				return x ** 2;
			}

This method says it is looking for an 'int' to be passed in to it and it will return an 'int'
that is the square of the number passed in. Easy enough, right? We say that the parameter of that function
is 'x' and the 'type' that 'x' is is an int.

Now, going back to our template, the template parameter actually takes in a 'type' as opposed to a variable
like 'x'. Instead, our template parameter would take in the 'int' part. That would make our class hold an
'int'. We could pass it any type as a matter of fact. We could pass it a 'bool', 'double', 'string', etc. The
'type' you see after 'class' in <class type> gets assigned to whatever type we pass it. Like in our example
function above, if we passed our square function a 4, 'x' (the parameter) would be assigned a value of 4. It's
the same deal here. 'type' gets assigned to whatever type we pass it. It will become clearer as we go through
the tutorial. So what is this 'class' keyword before it? For now lets just say that it's the type's declaration
and it can be interchanged with the keyword 'typename'. Why choose class then? Simply because you can. Both
'typename' and 'class' do the same thing. A type's declaration???? Huh? Think of it this way, we declare variables
by telling the computer its type then name, so 'int x' means x is an integer and it can be assigned any integer
value. Here, we're just declaring the type where 'type' is acting like a variable.
*/
class Node
{
private:
	type cargo;
	Node* next;
public:
	Node() {}; // copy constructor
	Node(type item) {this->cargo = item;} // constructor
	/*
	type item? Wha? Remember the template parameter we set up above? Remember how 'int x' means x is an integer? 
	Here, 'type' is the data type we passed in as the template parameter, so it gets replaced with whatever type we sent
	in. So if we replace 'type' with a type we passed in (lets say an int) it would be 'int item' as the parameter. This is why
	templating is so great. We only have to declare the type once in the main function and the templating will do the rest. This
	also applies to return values of methods like in the function below, getCargo(). It should return a variable of whatever type
	you passed in to the class. 
	(To see how we declare these templated classes scroll down to the main function)
	*/
	type getCargo() {return this->cargo;} // return cargo
	Node* getNext() {return next;} // return next node
	void setNext(Node* newNode) {this->next = newNode;} // set next node
};

template <class type>
class LinkedList
{
private:
	Node<type>* head;
public:
	LinkedList() {head = NULL;} // constructor
	void search(type item); // search for item in list
	void insert(type item); // insert item into list
	void display(); // display list
};

template <class type>
void LinkedList<type>::search(type item)
{
	int positionTracker = 0; // keep track of what position you're on
	Node<type>* current = head; // current node = head

	while(current != NULL) // while the current node isn't null
	{
		if((*current).getCargo() == item) // if cargo matches item in node, tell user at which position and end
		{
			cout << "Found item at position " << positionTracker << endl;
			return;
		}
		else
		{
			current = (*current).getNext(); // iterate over list
			positionTracker += 1; // increase position by 1
		}
	}

	cout << "The item isn't in the list" << endl; // if not found, tell user
}

template <class type>
void LinkedList<type>::insert(type item)
{
	if(head == NULL) // if nothing in the list
	{
		head = new Node<type>(item); // make new head
	}
	else
	{
		Node<type>* current = head; // current node = head
		while ((*current).getNext() != NULL) // while the next thing isn't null
		{
			current = (*current).getNext(); // iterate through list
		}

		// when at end of list, create new node containing item and append
		Node<type>* newNode = new Node<type>(item);
		(*current).setNext(newNode);
	}
	
	return;

}

template <class type>
void LinkedList<type>::display()
{
	Node<type>* current = head; // start at head of list
	while(current != NULL) // while current node doesn't equal null
	{
		cout << (*current).getCargo() << endl; // output cargo of node
		current = (*current).getNext(); // iterate over list
	}
}

int main()
{
	LinkedList<int>* myLList = new LinkedList<int>(); // new LinkedList
	/*
	So now you know how to implement a templated class. Now how do we declare it? Well, it's actually
	the same exact way we would normally do it except now we have to tell it what type it is holding.
	To do this we use diamond notation. That's just a way for the computer to tell that what's being
	passed in is a template parameter as opposed to an initializer parameter for instance. What goes in the
	diamons braces? Simply the data type (int, bool, long, you name it!). Above is an example on how to
	do it. 
	*/	
	int randomNumber; // int to hold random number
	srand(time(NULL)); // set up random number generator

	for (int i = 0; i < 100; i++)
	{
		randomNumber = rand() % 100+1; // generate random number between 0 and 100
		(*myLList).insert(randomNumber); // insert number into list
	}

	(*myLList).display(); // display list
	(*myLList).search(63); // test search function
	return 0;
}
// Thanks for reading my walkthrough and I hope it was helpful!
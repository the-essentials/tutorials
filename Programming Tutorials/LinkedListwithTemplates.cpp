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

template <class type>
class Node
{
private:
	type cargo;
	Node* next;
public:
	Node() {}; // copy constructor
	Node(type item) {this->cargo = item;} // constructor
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
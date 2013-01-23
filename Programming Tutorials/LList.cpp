#include <iostream>

using namespace std;

class Node
{
	int cargo;
	Node* next;

public:
	Node(); // copy constructor
	Node(int item) {this->cargo = item;}
	int getCargo() {return this->cargo;}
	Node* getNext() {return this->next;}
	void setNext(Node* newNode) {next = newNode;}
};

class LinkedList
{
	Node* head;

public:
	LinkedList() {head = NULL;}
	void insert(int item);
	void display();
	void remove(int item);
};

void LinkedList::insert(int item)
{
	if(head == NULL)
	{
		head = new Node(item);
	}
	else
	{
		Node* current = head;

		while ((*current).getNext() != NULL)
		{
			current = (*current).getNext();
		}

		(*current).setNext(new Node(item));
	}
}

void LinkedList::display()
{
	if(head == NULL)
	{
		cout << "There's nothing in the list" << endl;
	}
	else
	{
		Node* current = head;

		while(current != NULL)
		{
			cout << (*current).getCargo() << endl;
			current = (*current).getNext();
		}
	}
	
}
// --------------------------------------Option 1-----------------------------------------
void LinkedList::remove(int item)
{
	if(head == NULL){
		cout << "There's nothing in the list" << endl;
	}
	else{
		Node* current = head;

		if((*current).getCargo() == item)
		{
			head = (*current).getNext();
		}
		else
		{
			while ((*current).getNext() != NULL){
				if ((*(*current).getNext()).getCargo() == item){
				
					(*current).setNext((*(*current).getNext()).getNext());
					cout << "item has been found and removed" << endl;
				}
				else{
					current = (*current).getNext();
				}
			}
		}
	}
}

/*
----------------------------Option 2-------------------------------------
void LinkedList::remove(int item)
{
	if(head == NULL)
	{
		cout << "Nothng here" << endl;
	}
	else
	{
		Node* current = head;
		Node* previous = NULL;

		while(current != NULL)
		{
			if((*current).getCargo() == item)
			{
				if(current == head)
				{
					head = (*current).getNext();
					return;
				}

				else
				{
					(*previous).setNext((*current).getNext());
					return;
				}
			}
			else
			{
				previous = current;
				current = (*current).getNext();
			}
		}
	}
}*/

int main()
{
	LinkedList* myList = new LinkedList();
	int randomNumber;

	srand(time(NULL));

	for(int i = 0; i < 100; i++)
	{
		randomNumber = rand() % 100;
		(*myList).insert(i);
	}

	//(*myList).display();
	(*myList).remove(0);
	(*myList).display();
	return 0;
}
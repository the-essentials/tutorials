/*
Please let me know if you find any bugs at any time!
*/

#include <iostream>

using namespace std;

class Node
{
private:
	Node* left;
	int cargo;
	Node* right;

public:
	Node();
	Node(int item);
	Node* getLeft() {return left;}
	int getCargo() {return this->cargo;}
	Node* getRight() {return right;}
	void setLeft(Node* newLeft) {this->left = newLeft;}
	void setRight(Node* newRight) {this->right = newRight;}

};

Node::Node(int item)
{
	cargo = item;
	left = NULL;
	right = NULL;
}

class binaryTree
{
private:
	Node* root;
	void doInorder (Node *) const;

public:
	binaryTree() {root = NULL;}
	void insert(int item);
	void search(int item);
	void display() const {doInorder(root); cout << endl;}

};

void binaryTree::insert(int item)
{
	if(root == NULL)
	{
		root = new Node(item);
	}
	else
	{
		Node* current = root;

		while(true)
		{
			if(item == (*current).getCargo())
			{
				cout << "That number already exists" << endl;
				break;
			}
			else if(item > (*current).getCargo())
			{
				if((*current).getRight() == NULL)
				{
					Node* newNode = new Node(item);
					(*current).setRight(newNode);
					break;
				}
				else
				{
					current = (*current).getRight();
				}
				
			}
			else
			{
				if((*current).getLeft() == NULL)
				{
					Node* newNode = new Node(item);
					(*current).setLeft(newNode);
					break;
				}
				else
				{
					current = (*current).getLeft();
				}
			}
		}
	}
}

void binaryTree::search(int item)
{
	if(root == NULL)
	{
		cout << "There's nothing in the tree" << endl;
	}
	else
	{
		Node* current = root;

		while(true)
		{
			if(item == (*current).getCargo())
			{
				cout << "Found!" << endl;
				break;
			}

			else if((*current).getRight() == NULL && (*current).getLeft() == NULL)
			{
				cout << "Item doesn't exist in the tree" << endl;
				break;
			}

			else if(item > (*current).getCargo())
			{
				current = (*current).getRight();	
			}

			else
			{
				current = (*current).getLeft();
			}

		}
	}
	return;
}

void binaryTree::doInorder(Node *current) const
{

   if(current)
   {
      doInorder(current->getLeft());
      cout << current->getCargo() << ", ";
      doInorder(current->getRight());
   }

   return;
}

int main()
{
	binaryTree myTree;
	myTree.insert(10);
	myTree.insert(11);
	myTree.insert(1);
	myTree.insert(2);
	myTree.insert(-10);
	myTree.insert(10);
	myTree.display();
	myTree.search(-10);
	return 0;
}
// Begin implementation of Tri

import java.util.*;

// Node for trie
class Node
{
	char cargo;
	Map<String, Node> next; // Dictionary

	Node(char item)
	{
		cargo = item;
		next = new HashMap<String, Node>();
	}

	Map getNext()
	{
		return next;
	}
}

class A_Trie
{
	private Node root;

	A_Trie()
	{
		root = new Node(' ');
	}

	void insert(char item)
	{
		Node newNode = new Node(item);

	}
}

public class Trie
{
	public static void main(String args[])
	{
		return;
	} 
}
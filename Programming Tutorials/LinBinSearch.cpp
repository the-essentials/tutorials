#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void linearSearch(vector<int> array, int itemToLookFor)
{
	for(int i = 0; i < array.size(); i++)
	{
		if(array[i] == itemToLookFor)
		{
			cout << "Found at position " << i << endl;
			return;
		}
		
	}

	cout << "Item not in the list" << endl;

	return	;
}

int binarySearch(vector<int> array, int itemToLookFor)
{
	return 0;
}

int main()
{
	vector<int>* array = new vector<int>;
	for(int i = 0; i < 10; i++)
	{
		(*array).push_back(i);
	}

	linearSearch((*array), 5);

	binarySearch((*array), 5);
}
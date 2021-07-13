#include <iostream>
#include <set>
using namespace std;

int	main()
{
	set<int>	unique;
	int	n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int	item;
		cin >> item;
		unique.insert(item);
	}
	for (auto item : unique)
	{
		cout << item << endl;
	}
	return (0);
}

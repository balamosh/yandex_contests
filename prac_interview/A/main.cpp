#include <iostream>
#include <set>
using namespace std;

int	main()
{
	string	J, S;
	cin >> J >> S;
	set<char>	jewels; 
	for (auto c : J)
	{
		jewels.insert(c);
	}
	int count = 0;
	for (auto c : S)
	{
		if (jewels.count(c))
			count++;
	}
	cout << count << endl;
	return (0);
}

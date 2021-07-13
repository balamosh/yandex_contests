#include <iostream>
#include <set>
#include <map>
#include <string>
using namespace std;

map<char, int>	MapString(string str)
{
	map<char, int>	str_map;
	for (auto c : str)
	{
		str_map[c]++;
	}
	return (str_map);
}

int	main()
{
	string	s1, s2;
	cin >> s1 >> s2;
	if (MapString(s1) == MapString(s2))
		cout << 1 << endl;
	else
		cout << 0 << endl;
	return (0);
}

#include <iostream>
#include <vector>
using namespace std;

int	main()
{
	int	n;
	vector<bool>	v;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		bool in;
		cin >> in;
		v.push_back(in);
	}
	int	max = 0;
	int	curr = 0;
	for (int i = 0; i < n; i++)
	{
		if (v[i])
			curr++;
		else
			curr = 0;
		if (curr > max)
			max = curr;
	}
	cout << max << endl;
	return (0);
}

#include <iostream>
#include <vector>
using namespace std;

int	main(void)
{
	int	n;
	cin >> n;
	vector<int>	res(n);
	for(int i = 0; i < n; i++)
		cin >> res[i];
	int	counter = 0;
	int	current = res[0];
	for(int i = 1; i < n; i++)
	{
		if (res[i] > current)
		{
			counter += res[i] - current;
			current = res[i];
		}
		else if(res[i] < current)
		{
			counter = -1;
			break ;
		}
	}
	cout << counter << endl;
	return (0);
}
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

void	Print(const vector<int>& v)
{
	for (auto i : v)
		cout << i << " ";
	cout << endl;
}

int	Dist(int x, const vector<int>& v)
{
	int	sum = 0;
	for (auto i : v)
	{
		sum += abs(x - i);
	}
	return (sum);
}

int	DistK(int x, const vector<int>& v, int k)
{
	int	sum = 0;
	for (int i = 0; i < k; i++)
	{
		sum += abs(x - v[i]);
	}
	return (sum);
}

int	main(void)
{
	int	n, k;
	cin >> n >> k;
	vector<int>	arr(n);
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < n - 1; i++)
	{
		vector<int>	arr_cpy = arr;
		arr_cpy.erase(arr_cpy.begin() + i);
		//int	key = arr[i];
		//sort(arr_cpy.begin(), arr_cpy.end(), [key](int a, int b) { return (abs(a - key) < abs(b - key)); });
		//vector<int>	set;
		int sum = 0;
		for (int j = 0; j < k; j++)
		{
			int	min = abs(arr[i] - arr_cpy[0]);
			int	min_i = 0;
			for (int item = 1; item < arr_cpy.size(); item++)
			{
				int	curr = abs(arr[i] - arr_cpy[item]);
				if (curr < min)
				{
					min = curr;
					min_i = item;
				}
			}
			sum += min;
			arr_cpy.erase(arr_cpy.begin() + min_i);
			//set.push_back(curr)
		}
		//arr_cpy.resize(k);
		
		//cout << DistK(arr[i], arr_cpy, k) << ' ';
		cout << sum << ' ';
	}
	int i = n - 1;
	if (i > 0)
	{
		vector<int>	arr_cpy = arr;
		arr_cpy.erase(arr_cpy.begin() + i);
		//int	key = arr[i];
		//sort(arr_cpy.begin(), arr_cpy.end(), [key](int a, int b) { return (abs(a - key) < abs(b - key)); });
		//vector<int>	set;
		int sum = 0;
		for (int j = 0; j < k; j++)
		{
			int	min = abs(arr[i] - arr_cpy[0]);
			int	min_i = 0;
			for (int item = 1; item < arr_cpy.size(); item++)
			{
				int curr = abs(arr[i] - arr_cpy[item]);
				if (curr < min)
				{
					min = curr;
					min_i = item;
				}
			}
			sum += min;
			arr_cpy.erase(arr_cpy.begin() + min_i);
			//set.push_back(curr)
		}
		//arr_cpy.resize(k);
		
		//cout << DistK(arr[i], arr_cpy, k) << ' ';
		cout << sum;
	}

	return (0);
}
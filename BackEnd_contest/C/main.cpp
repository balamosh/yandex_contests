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

/*
int	MinDist(int x, const vector<int>& v, int k)
{
	int	min = 0;
	for (int i = 0; i < k; i++)
	{
		min += abs(x - v[i]);
	}
	for (int j = 1; j < v.size() - k; j++)
	{
		int sum = 0;
		for (int i = j; i < k + j; i++)
		{
			sum += abs(x - v[i]);
		}
		if (sum < min)
			min = sum;
	}
	return (min);
}
*/


int	MinDist(int x, const vector<int>& v, int k)
{
	vector<int>	sub = {v.begin(), v.end() - k};
	int	min = Dist(x, sub);
	//Print(sub);
	int prev = min;
	for (int i = 1; i <= k; i++)
	{
		sub = {v.begin() + i, v.end() - k + i};
		//Print(sub);
		int	dist = Dist(x, sub);
		if (dist > prev)
			return (min);
		if (dist < min)
			min = dist;
	}
	//cout << "min = " << min << endl;
	return (min);
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
	for (int i = 0; i < n; i++)
	{
		vector<int>	arr_cpy = arr;
		arr_cpy.erase(arr_cpy.begin() + i);
		int	key = arr[i];
		sort(arr_cpy.begin(), arr_cpy.end(), [key](int a, int b) { return (abs(a - key) < abs(b - key)); });
		/*
		sort(arr_cpy.begin(), arr_cpy.end());
		int	j = 0;
		while (j < arr_cpy.size())
		{
			if (arr_cpy.size() == k)
				break ;
			if (arr[i] > arr_cpy[j])
				arr_cpy.erase(arr_cpy.begin() + j);
			else
				j++;
		}
		*/
		arr_cpy.resize(k);
		//Print(arr);
		//Print(arr_cpy);
		//MinDist(arr[i], arr_cpy, arr_cpy.size() - k);
		//cout << MinDist(arr[i], arr_cpy, arr_cpy.size() - k);
		/*
		int	min_sub = abs(arr[i] - arr_cpy[k - 1]);
		int	min_k = 0;
		for (int sub = k; sub < arr_cpy.size(); sub++)
		{
			int	curr = abs(arr[i] - arr_cpy[sub]);
			if (curr < min_sub)
			{
				min_sub = curr;
				min_k = sub - k + 1;
			}
			//else if (curr > min_sub)
			//	break ;
		}
		cout << "\nsub:" << endl;
		Print({arr_cpy.begin() + min_k, arr_cpy.begin() + min_k + k});
		cout << "---------\n";
		*/
		cout << Dist(arr[i], arr_cpy);
		//cout << Dist(arr[i], {arr_cpy.begin() + min_k, arr_cpy.begin() + min_k + k});
		//cout << MinDist(arr[i], arr_cpy, arr_cpy.size() - k);
		if (i < n - 1)
			cout << ' ';
	}

	/*
	vector<int>	arr_cpy;
	arr_cpy = arr;
	arr_cpy.erase(arr_cpy.begin() + 2);
	Print(arr);
	Print(arr_cpy);
	*/

	return (0);
}
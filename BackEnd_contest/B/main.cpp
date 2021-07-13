#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

string	std_lane = "ABC DEF";

void	PrintPlane(const vector<map<char, char>>& v)
{
	for (const auto& lane : v)
	{
		for (int j = 0; j < 7; j++)
		{
			char c = std_lane[j];
			cout << lane.at(c);
		}
		cout << endl;
	}
	//cout << endl;
}

int	FindRow(vector<map<char, char>>& v, string mask)
{
	for (int i = 0; i < v.size(); i++)
	{
		bool	found = true;
		for (auto c : mask)
		{
			if (v[i].at(c) != '.')
				found = false;
		}
		if (found)
			return (i);
	}
	return (-1);
}

void	PrintInfo(string mask, int row)
{
	sort(mask.begin(), mask.end());
	for (auto c : mask)
	{
		cout << " " << row + 1 << c;
	}
	cout << endl;
}

void	VizRow(vector<map<char, char>>& v, string mask, int row)
{
	for (auto c : mask)
	{
		v[row].at(c) = 'X';
	}
}

void	FillRow(vector<map<char, char>>& v, string mask, int row)
{
	for (auto c : mask)
	{
		v[row].at(c) = '#';
	}
}

int	Find(vector<map<char, char>>& v, int num, string side, string pos)
{
	int	row = -1;
	string	mask;

	if (side == "left")
	{
		if (pos == "window")
			mask = "ABC";
		else
			mask = "CBA";
	}
	else
	{
		if (pos == "window")
			mask = "FED";
		else
			mask = "DEF";
	}

	row = FindRow(v, mask);
	if (row != -1)
	{
		cout << "Passengers can take seats:";
		PrintInfo(mask, row);
		VizRow(v, mask, row);
		PrintPlane(v);
		FillRow(v, mask, row);
		//FillPlane(plane, row);
	}
	else
		cout << "Cannot fulfill passengers requirements" << endl;
	return (row);
}

int	main(void)
{
	int	size;
	cin >> size;
	vector<map<char, char>>	plane(size);
	for (int i = 0; i < size; i++)
	{
		string	lane;
		cin >> lane;
		for (int j = 0; j < 7; j++)
		{
			plane[i][std_lane[j]] = lane[j];
		}
	}
	int	op_amount;
	cin >> op_amount;
	for (int i = 0; i < op_amount; i++)
	{
		int	num;
		string	side;
		string	position;
		cin >> num >> side >> position;
		int	row = Find(plane, num, side, position);
	}
	//PrintPlane(plane);

	return (0);
}
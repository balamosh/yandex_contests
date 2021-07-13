#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define PI 3.14159265
#define LINES 100
#define NBRS 1000
#define EPS 0.00000001

struct Point
{
	double	x;
	double	y;
};

double	Avg(const vector<int>& v)
{
	double	sum = 0;
	for (int i = 0; i < v.size(); i++)
	{
		sum += v[i];
	}
	return (sum / v.size());
}

int	main(void)
{
	vector<vector<int>>	answer;
	/*answer.resize(LINES);
	for (auto a : answer)
		a.resize(NBRS);*/
	for (int line = 0; line < LINES; line++)
	{
		//vector<Point>	points(NBRS);
		//bool	first = true;
		answer.push_back({});
		for (int i = 0; i < NBRS; i++)
		{
			//cin >> points[i].x >> points[i].y;
			double	x, y;
			cin >> x >> y;
			//if (!first)
			//	continue ;
			double	a = sqrt(x * x + y * y);
			double	two_pi_b;
			if (abs(x) < EPS && abs(y) < EPS)
			{
				//answer[line][i] = 2;
				answer[line].push_back(1);
				continue ;
			}
			if (abs(x) > EPS)
				two_pi_b = atan(y / x);
			else if (abs(x) > EPS)
			{
				//first = false;
				//answer[line][i] = 1;
				answer[line].push_back(2);
				continue ;
			}
			double	new_x = a * cos(two_pi_b);
			double	new_y = a * sin(two_pi_b);
			//cout << "new_x = " << new_x << endl;
			//cout << "new_y = " << new_y << endl;
			if (abs(new_x - x) > EPS || abs(new_y - y) > EPS)
			{
				//first = false;
				//answer[line][i] = 1;
				answer[line].push_back(2);
			}
			else
			{
				//answer[line][i] = 2;
				answer[line].push_back(1);
			}
		}
		/*
		if (first)
			answer[line] = 1;
		else
			answer[line] = 2;
		*/
	}
	for (auto a : answer)
		cout << (int) Avg(a) << endl;

	return (0);
}

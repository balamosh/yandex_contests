#include <iostream>
#include <set>
#include <map>
#include <string>
using namespace std;

struct Point
{
	int	x;
	int	y;
};

int	Dist(Point p1, Point p2)
{
	return (abs(p1.x - p2.x) + abs(p1.y - p2.y));
}

int	MinRoads(int current, int finish, map<int, Point> cities, int size, int k, int len)
{
	if (Dist(cities[current], cities[finish]) <= k)
		return (len + (current != finish));
	if (size == 0)
		return (-1);
	int	min = -1;
	Point	curr_xy = cities[current];
	//curr_xy.x = cities[current].x;
	//curr_xy.y = cities[current].y;
	cities.erase(current);
	for (auto city : cities)
	{
		int	dist = Dist(curr_xy, city.second);
		if (dist > k)
			continue ;
		int	path_len = MinRoads(city.first, finish, cities, size - 1, k, len + 1);
		if (path_len < min || min < 0)
			min = path_len;
	}
	return (min);
}

int	main()
{
	int	n;
	cin >> n;
	map<int, Point>	cities;
	for (int i = 0; i < n; i++)
	{
		cin >> cities[i].x;
		cin >> cities[i].y;
	}
	int	k;
	cin >> k;
	int	start, finish;
	cin >> start >> finish;
	cout << MinRoads(start - 1, finish - 1, cities, n, k, 0) << endl;
	return (0);
}

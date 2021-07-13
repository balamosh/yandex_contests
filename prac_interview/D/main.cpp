#include <iostream>
#include <set>
#include <string>
using namespace std;

void	RecGenParenthesis(int n, int open, int close, string s)
{
	if (open == n && close == n)
	{
		cout << s << endl;
		return ;
	}
	if (open < n)
	{
		RecGenParenthesis(n, open + 1, close, s + "(");
	}
	if (open > close)
	{
		RecGenParenthesis(n, open, close + 1, s + ")");
	}
}

int	main()
{
	int	n;
	string	s = "";
	cin >> n;
	RecGenParenthesis(n, 0, 0, s);
	return (0);
}

//BaekJoon 2587 대표값2

#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	list<int> li;
	int sum = 0;
	for (int i = 0; i < 5; i++) {
		int tmp = 0;
		cin >> tmp;
		li.push_back(tmp);
		sum += tmp;
	}
	li.sort();
	list<int> ::iterator iter;
	iter = li.begin();
	iter++;
	iter++;
	cout << sum / 5 << "\n";
	cout << *iter;
	return 0;
}
//BaekJoon 2752 세수정렬

#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	list<int> li;
	int a, b, c;
	cin >> a >> b >> c;
	li.push_back(a);
	li.push_back(b);
	li.push_back(c);
	li.sort();

	list<int>::iterator iter;
	for (iter = li.begin(); iter != li.end(); ++iter) {
		cout << *iter << " ";
	}

	return 0;
}
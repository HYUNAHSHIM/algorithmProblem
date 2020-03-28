//BaekJoon 2753 윤년

#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int year;
	cin >> year;

	if (year % 4 == 0 && year % 100 != 0) {
		cout << 1;
		return 0;
	}
	if (year % 400 == 0) {
		cout << 1;
		return 0;
	}

	cout << 0;

	return 0;
}
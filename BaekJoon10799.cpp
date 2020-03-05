//BaekJoon 10799 ¼è¸·´ë±â

#include <iostream>
#include <string.h>

using namespace std;

int top = 0;
int result = 0;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	string arr;
	cin >> arr;

	int n = arr.length();
	for (int i = 0; i < n; i++) {
		if (arr.at(i) == '(') {
			top++;
		}
		else {
			top--;
			if (arr.at(i - 1) == '(') result += top;
			else {
				result++;
			}
		}
	}

	cout << result;
	return 0;
}
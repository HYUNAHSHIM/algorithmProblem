//SW Expert Academy 2072 홀수만 더하기

#include <iostream>

using namespace std;

int main(void)
{
	int n = 0; //number of test cases
	cin >> n;

	for (int i = 0; i < n; i++) {
		int result = 0;
		for (int j = 0; j < 10; j++) {
			int tmp = 0;
			cin >> tmp;
			if (tmp % 2 != 0)    result += tmp;
		}

		cout << "#" << i + 1 << " " << result << endl;
	}
}
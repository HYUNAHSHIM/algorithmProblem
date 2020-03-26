//BaekJoon 2562 최댓값

#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int num[9];
	int max = 0;

	for (int i = 0; i < 9; i++) {
		cin >> num[i];
		max = max < num[i] ? num[i] : max;
	}
	cout << max << "\n";
	for (int i = 0; i < 9; i++) {
		if (max == num[i]) cout << i + 1 << "\n";
	}

	return 0;
}
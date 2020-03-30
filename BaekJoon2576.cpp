//BaekJoon 2576 홀수

#include <iostream>
#include <string>

using namespace std;

const int NUM = 7;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int sum = 0;
	int min = 100;
	int arr[NUM];
	
	for (int i = 0; i < NUM; i++) {
		cin >> arr[i];
		if (arr[i] % 2 == 0) continue;
		sum += arr[i];
		min = min > arr[i] ? arr[i] : min;
	}
	if (sum == 0) cout << -1;
	else {
		cout << sum << "\n" << min;
	}

	return 0;
}
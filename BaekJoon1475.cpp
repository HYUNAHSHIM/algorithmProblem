//BaekJoon 1475 방번호

#include <iostream>
#include <string>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int arr[10], max = 0;
	string num;
	cin >> num;

	for (int i = 0; i < 10; i++) {
		arr[i] = 0;
	}
	for (int i = 0; i < num.length(); i++) {
		if (num[i] == '9' || num[i] == '6') {
			arr[6]++;
		}
		else arr[num[i] - 48]++;
	}

	arr[9] = arr[6] / 2;
	if (arr[6] % 2 != 0) {
		arr[6] /= 2;
		arr[6]++;
	}
	else arr[6] /= 2;

	max = arr[0];
	for (int i = 1; i < 10; i++) {
		if (max < arr[i]) max = arr[i];
	}

	cout << max;

	return 0;
}
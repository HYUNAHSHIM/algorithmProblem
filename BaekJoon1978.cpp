//BaekJoon 1978 소수 찾기

#include <string.h>
#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int n; cin >> n;
	int num = 0;
	for (int i = 0; i < n; i++) {
		int input; cin >> input;
		bool isPrime = true;
		if (input == 1) continue;
		for (int j = 2; j < input; j++) {
			if (input % j == 0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime) num++;
	}
	cout << num;
	return 0;
}
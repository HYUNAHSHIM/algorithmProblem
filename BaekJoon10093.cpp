//BaekJoon 10093 숫자

#include <string.h>
#include <iostream>

using namespace std;

void result(long long a, long long b) {
	cout << b - a - 1 << "\n";
	for (long long i = a + 1; i < b; i++) {
		cout << i << " ";
	}
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	long long a, b;
	cin >> a >> b;
	if (a < b) result(a, b);
	else if (a > b) result(b, a);
	else cout << 0; return 0;
	
	return 0;
}
//BaekJoon 2869 달팽이는 올라가고 싶다

#include <string.h>
#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int a, b, v; cin >> a >> b >> v;
	int days = (v - b - 1) / (a - b) + 1;
	cout << days;
	return 0;
}
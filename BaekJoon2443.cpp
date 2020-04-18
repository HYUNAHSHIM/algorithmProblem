//BaekJoon 2443 별 찍기 - 6

#include <string.h>
#include <iostream>

using namespace std;


int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n = 0; cin >> n;
	for (int j = 1; j <= n; j++) {
		for (int i = 0; i < j - 1; i++) {
			printf(" ");
		}
		for (int k = 0; k < (n - j) * 2 + 1; k++) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
//BaekJoon 2442 별찍기 - 5

#include <string.h>
#include <iostream>

using namespace std;


int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n = 0; cin >> n;
	for (int j = 1; j <= n; j++) {
		for (int i = 0; i < n - j; i++) {
			printf(" ");
		}
		for (int k = 0; k < (j - 1) * 2 + 1; k++) {
			printf("*");
		}
		printf("\n");
	}
	for (int i = 0; i < n; i++) {
		printf(" ");
	}

	return 0;
}
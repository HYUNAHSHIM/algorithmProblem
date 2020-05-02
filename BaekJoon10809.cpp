//BaekJoon 10809 알파벳 찾기

#include <string.h>
#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	string input; cin >> input;
	int len = input.length();
	int alpabet[26]; fill_n(alpabet, 26, -1);
	for (int i = 0; i < len; i++) {
		int point = input.at(i) - 97;
		if (alpabet[point] == -1) alpabet[point] = i;
	}
	for (int i = 0; i < 26; i++) cout << alpabet[i] << " ";
	cout << "\n";

	return 0;
}
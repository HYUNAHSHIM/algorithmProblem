//BaekJoon 11328 Strfry

#include <iostream>
#include "string"

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n = 0;
	cin >> n;
	int length = 'z' - 'a' + 1;//알파벳 개수
	int* cntA = new int[length];
	int* cntB = new int[length];

	while (n--) {
		string a, b;
		cin >> a >> b;

		//cntA, cntB를 0으로 초기화
		for (int i = 0; i < length; i++) {
			cntA[i] = 0;
			cntB[i] = 0;
		}

		for (int j = 0; j < a.length(); j++) {
			cntA[a[j] - 'a']++;
		}
		for (int j = 0; j < b.length(); j++) {
			cntB[b[j] - 'a']++;
		}
		int i = 0;
		while (i < length && cntA[i] == cntB[i]) i++;
		cout << (i == length ? "Possible" : "Impossible") << endl;
	}
	return 0;
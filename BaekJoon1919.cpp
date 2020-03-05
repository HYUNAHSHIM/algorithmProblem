//BaekJoon 1919 애너그램

#include <iostream> 
#include <string>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int arrA[26];
	int arrB[26];
	string A, B;
	cin >> A >> B;

	for (int i = 0; i < 26; i++) {
		arrA[i] = 0;
		arrB[i] = 0;
	}

	for (int i = 0; i < A.length(); i++) {
		arrA[A[i] - 'a']++;
	}
	for (int i = 0; i < B.length(); i++) {
		arrB[B[i] - 'a']++;
	}

	int result = 0;
	for (int i = 0; i < 26; i++) {
		if (arrA[i] != arrB[i])
			result += abs(arrA[i] - arrB[i]);
	}
	cout << result << endl;
	return 0;
}
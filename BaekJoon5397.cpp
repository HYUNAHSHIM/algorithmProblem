//BaekJoon 5397 키로거

#include <iostream> 
#include <list>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	while (n--) {
		string L;
		cin >> L;
		list<char> arr;
		list<char>::iterator iter = arr.begin();
		int L_len = L.size(), L_idx = 0;

		while (L_idx < L_len) {
			switch (L[L_idx]) {
			case '<':
				if (iter != arr.begin()) iter--;
				break;
			case '>':
				if (iter != arr.end()) iter++;
				break;
			case '-':
				if (iter != arr.begin()) arr.erase((--iter)++);
				break;
			default:
				arr.insert(iter, L[L_idx]);
				break;
			}
			L_idx++;
		}
		for (auto x : arr) printf("%c", x);
		printf("\n");
	}
	return 0;
}
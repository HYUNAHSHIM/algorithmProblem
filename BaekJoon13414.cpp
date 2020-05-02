//BaekJoon 13414 수강신청

#include <string.h>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int maxP, click; cin >> maxP >> click;
	vector<string> li;
	vector<string> result;
	set<string> s;

	for (int i=0;i < click; i++) {
		string tmp; cin >> tmp;
		li.push_back(tmp);
	}
	for (int i = click - 1; i >= 0; --i) {
		string tmp = li[i];
		if (s.find(tmp) == s.end()) {
			s.insert(tmp);
			result.push_back(tmp);
		}
	}
	int size = result.size();
	for (int i = size - 1; i >= size - maxP && i >= 0; --i)
		cout << result[i] << "\n";
	return 0;
}
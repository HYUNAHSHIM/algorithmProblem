//BaekJoon 5430 AC

#include <iostream>
#include <string.h>
#include <deque>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int testCase = 0; cin >> testCase;

	while (testCase--) {
		string func, arr; int num = 0;
		bool back = false, error = false;
		deque<int> dq;
		cin >> func >> num >> arr;

		//initialize deque
		arr.erase(0, 1); arr.pop_back();
		int len = arr.length(), tmp = 0;
		for (int i = 0; i < len; i++) {
			if (arr[i] == ',') {
				dq.push_back(tmp);
				tmp = 0;
			}
			else {
				tmp = tmp * 10 + arr[i] - 48;
			}
		}
		if (tmp != 0) {
			dq.push_back(tmp);
		}

		//reverse and delete array
		int n = func.length();
		for (int i = 0; i < n; i++) {
			//if function is 'R'
			if (func[i] == 'R') {
				if (back == false) {
					back = true;
				}
				else {
					back = false;
				}
			}
			//if function is 'D'
			else {
				int size = dq.size();
				if (size == 0) {
					cout << "error\n";
					error = true;
					break;
				}
				else {
					if (back == false) dq.pop_front();
					else dq.pop_back();
				}
			}
		}
		//print
		if (error == true) continue;
		cout << "[";
		//if reversed
		while (!dq.empty() && back == true) {
			cout << dq.back();
			dq.pop_back();
			if (!dq.empty()) cout << ",";
		}
		//if not reversed
		while (!dq.empty() && back == false) {
			cout << dq.front();
			dq.pop_front();
			if (!dq.empty()) cout << ",";
		}
		cout << "]\n";
	}
	return 0;
//BaekJoon 1021번 회전하는 큐

#include <iostream>
#include <string>
#include <deque>

using namespace std;

deque<int> dq;
deque<int>::iterator iter;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	//get inputs
	int n, m, i; cin >> n >> m;
	int cnt = 0;

	//initialize
	for (i = 1; i <= n; i++) {
		dq.push_back(i);
	}
	
	//pop elements
	for(i = 0 ; i < m ; i++) {
		//get element
		int element; cin >> element;
		int size = dq.size();
		//element position
		int idx = 1;

		//check where element is placed
		for (iter = dq.begin(); iter < dq.end(); iter++) {
			if (*iter == element) break;
			idx++;
		}

		//calculate left or right
		//+1 to right, bcz have to pop_front
		int left = idx - 1;
		int right = size - idx + 1;

		//move left
		if (left < right) {
			//pop front and push it to back
			for (int j = 0; j < left; j++) {
				dq.push_back(dq.at(0));
				dq.pop_front();
				cnt++;
			}
			//pop element
			dq.pop_front();
		}
		//move right
		else {
			//pop back and push it to front
			for (int j = 0; j < right; j++) {
				dq.push_front(dq.at(size - 1));
				dq.pop_back();
				cnt++;
			}
			//pop element
			//bcz of condition, pop_back now allowed
			dq.pop_front();
		}
	}
	cout << cnt << "\n";
	return 0;
}
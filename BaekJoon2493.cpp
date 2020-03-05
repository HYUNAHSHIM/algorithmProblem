//BaekJoon 2493 ž

#include <iostream>
#include <string>
#include <stack>
#include <utility>

using namespace std;

int tmp, n;
stack<pair<int, int>> stk;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	//number of top
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		//if stack is not empty check the top with input
		while (!stk.empty()) {
			if (stk.top().second > tmp) {
				//if top is bigger than input print index of top
				//+1 bcz stack starts from 0
				cout << stk.top().first + 1 << " ";
				break;
			}
			//if top is not bigger than input pop the top
			stk.pop();
			//and then check the next one (under the top)
			//if there's no more element that is bigger than input stack'll be empty
		}
		//if stack is empty print 0
		if (stk.empty()) cout << 0 << " ";
		//push the current top
		stk.push(make_pair(i, tmp));
	}

	return 0;
}
//BaekJoon 13549 숨바꼭질 3

#include <iostream>
#include <queue>
#include <utility>

#define MAXNUM 100001

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int n, k; cin >> n >> k;
	bool visited[MAXNUM] = { false, };
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> qu;
	qu.push(make_pair(0, n));
	visited[n] = true;

	while (!qu.empty()) {
		int sec = qu.top().first;
		int loc = qu.top().second;
		qu.pop();

		if (loc == k) {
			cout << sec;
			return 0;
		}
		if (loc * 2 < MAXNUM && visited[loc * 2] == false) {
			qu.push(make_pair(sec, loc * 2));
			visited[loc * 2] = true;
		}
		if (loc + 1 < MAXNUM && visited[loc + 1] == false) {
			qu.push(make_pair(sec + 1, loc + 1));
			visited[loc + 1] = true;
		}
		if (loc - 1 >= 0 && visited[loc - 1] == false) {
			qu.push(make_pair(sec + 1, loc - 1));
			visited[loc - 1] = true;
		}
	}

	return 0;
}
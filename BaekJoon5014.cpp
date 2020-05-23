//BaekJoon 5014 스타트링크

#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int f, s, g, u, d; cin >> f >> s >> g >> u >> d;
	bool visited[1000001] = { false };
	queue<pair<int, int>> qu;
	qu.push(make_pair(s, 0));
	visited[s] = true;
	while (!qu.empty()) {
		int point = qu.front().first;
		int num = qu.front().second;
		qu.pop();
		if (point == g) {
			cout << num;
			return 0;
		}
		int up = point + u;
		int down = point - d;
		if (up <= f && visited[up] == false) {
			qu.push(make_pair(up, num + 1));
			visited[up] = true;
		}
		if (down > 0 && visited[down] == false) {
			qu.push(make_pair(down, num + 1));
			visited[down] = true;
		}
	}
	cout << "use the stairs";
	return 0;
}
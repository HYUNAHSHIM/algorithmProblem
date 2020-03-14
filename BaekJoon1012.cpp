//BaekJoon 1012 유기농배추

#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <utility>

using namespace std;

int T, m, n, k, cnt;
int arr[50][50];
bool visited[50][50];
queue<pair<int, int>> qu;

void isNear(int a, int b) {
	if (a < 0 || b < 0 || a >= n || b >= m) return;
	if (visited[a][b] == false && arr[a][b] == 1) {
		qu.push(make_pair(a, b));
		visited[a][b] = true;
	}
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> T;
	while (T--) {
		cin >> m >> n >> k;
		//initialize
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr[i][j] = 0;
				visited[i][j] = false;
			}
		}
		vector <pair<int, int>> loc;
		cnt = 0;
		for (int i = 0; i < k; i++) {
			int a, b;
			cin >> a >> b;
			arr[b][a] = 1;
			loc.push_back(make_pair(b, a));
		}
		for (int i = 0; i < k; i++) {
			int a = loc.at(i).first;
			int b = loc.at(i).second;
			if (visited[a][b]) continue;
			qu.push(make_pair(a, b));
			visited[a][b] = true;
			cnt++;
			while (!qu.empty()) {
				pair<int, int> cur = qu.front();
				a = cur.first;
				b = cur.second;
				qu.pop();
				isNear(a, b - 1);
				isNear(a + 1, b);
				isNear(a - 1, b);
				isNear(a, b + 1);
			}
		}
		cout << cnt << "\n";
	}
	
	return 0;

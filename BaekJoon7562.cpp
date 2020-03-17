//BaekJoon 7562 나이트의 이동

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

const int MAX = 301;
int T = 0;
int dx[] = { 1,2,2,1,-1,-2,-2,-1 };
int dy[] = { 2,1,-1,-2,-2,-1,1,2 };

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> T;
	while (T--) {
		int l = 0, curx, cury;
		queue<pair<pair<int, int>, int>> qu;
		pair<int, int> goal;
		bool visited[MAX][MAX] = { false, };

		cin >> l;
		cin >> curx >> cury >> goal.first >> goal.second;
		if (curx == goal.first && cury == goal.second) {
			cout << 0 << "\n";
			continue;
		}
		
		qu.push(make_pair(make_pair(curx, cury), 0));
		visited[curx][cury] = true;

		while (!qu.empty()) {
			int a = qu.front().first.first;
			int b = qu.front().first.second;
			int c = qu.front().second;
			qu.pop();
			if (a == goal.first && b == goal.second) {
				cout << c;
				if (T != 0) cout << "\n";
				break;
			}
			for (int i = 0; i < 8; i++) {
				int x = a + dx[i];
				int y = b + dy[i];
				if (x < 0 || y < 0 || x >= l || y >= l) continue;
				if (!visited[x][y]) {
					qu.push(make_pair(make_pair(x, y), c + 1));
					visited[x][y] = true;
				}
			}
		}
	}
	return 0;
}
//BaekJoon 6593 상범 빌딩

#include <iostream>
#include <queue>
#include <utility>

#define MAXNUM 30

using namespace std;

int dx[] = { 0, 0, 1, -1, 0, 0 };
int dy[] = { 1, -1, 0, 0, 0, 0 };
int dz[] = { 0, 0, 0, 0, 1, -1 };

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int l, r, c; cin >> l >> r >> c;
	char arr[MAXNUM][MAXNUM][MAXNUM];
	int visited[MAXNUM][MAXNUM][MAXNUM];
	queue<pair<pair<int, int>, int>> qu;

	while (l != 0 || r != 0 || c != 0) {
		while (!qu.empty()) qu.pop();
		for (int i = 0; i < l; i++) {
			for (int j = 0; j < r; j++) {
				for (int k = 0; k < c; k++) {
					cin >> arr[i][j][k];
					visited[i][j][k] = -1;
					if (arr[i][j][k] == 'S') {
						qu.push(make_pair(make_pair(i, j), k));
						//      z  x  y
						visited[i][j][k] = 0;
					}
				}
			}
		}
		bool escaped = false;
		while (!qu.empty()) {
			int x = qu.front().first.second;
			int y = qu.front().second;
			int z = qu.front().first.first;
			qu.pop();

			if (arr[z][x][y] == 'E') {
				cout << "Escaped in " << visited[z][x][y] << " minute(s)." << "\n";
				escaped = true;
				break;
			}

			for (int i = 0; i < 6; i++) {
				int tmpz = z + dz[i];
				int tmpx = x + dx[i];
				int tmpy = y + dy[i];

				if (tmpx < 0 || tmpx >= r || tmpy < 0 || tmpy >= c || tmpz < 0 || tmpz >= l) continue;
				if (arr[tmpz][tmpx][tmpy] != '#' && visited[tmpz][tmpx][tmpy] == -1) {
					qu.push(make_pair(make_pair(tmpz, tmpx), tmpy));
					visited[tmpz][tmpx][tmpy] = visited[z][x][y] + 1;
				}
			}
		}
		if (escaped == false) cout << "Trapped!" << "\n";
		cin >> l >> r >> c;
	}

	return 0;
}
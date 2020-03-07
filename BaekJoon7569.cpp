//BeakJoon 7569 토마토

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int h, m, n, maxN = 0;
int x, y, z;
int arr[100][100][100];
int dist[100][100][100];
bool visited[100][100][100];
queue<pair<pair<int, int>, int>> qu;
pair<pair<int, int>, int> cur;

void isNear(int c, int a, int b) {
	if (a < 0 || b < 0 || c < 0 || a >= n || b >= m || c >= h) return;
	if (arr[c][a][b] == 0 && visited[c][a][b] == false) {
		qu.push(make_pair(make_pair(c, a), b));
		dist[c][a][b] = dist[z][x][y] + 1;
		visited[c][a][b] = true;
		maxN = (maxN < dist[c][a][b]) ? dist[c][a][b] : maxN;
	}
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> m >> n >> h;
	for (int k = 0; k < h; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> arr[k][i][j];
			}
		}
	}
	for (int k = 0; k < h; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[k][i][j] == 1) {
					qu.push(make_pair(make_pair(k, i), j));
					visited[k][i][j] = true;
					dist[k][i][j] = 0;
				}
			}
		}
	}

	if (qu.empty()) {
		cout << 0;
		return 0;
	}
	while (!qu.empty()) {
		cur = qu.front();
		x = cur.first.second;
		y = cur.second;
		z = cur.first.first;
		qu.pop();
		isNear(z + 1, x, y);
		isNear(z - 1, x, y);
		isNear(z, x, y-1);
		isNear(z, x, y + 1);
		isNear(z, x + 1, y);
		isNear(z, x - 1, y);
	}
	for (int k = 0; k < h; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[k][i][j] != -1 && visited[k][i][j] == false) {
					cout << -1;
					return 0;
				}
			}
		}
	}
	cout << maxN;	
	return 0;
}
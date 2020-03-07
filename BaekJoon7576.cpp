//BaekJoon 7576 토마토

#include <iostream>
#include <stdio.h>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int m, n, maxN = 0;
int arr[1000][1000];
bool visited[1000][1000] = { false, };
queue<pair<pair<int, int>, int>> qu;
pair<pair<int, int>, int> cur;

void isNear(int a, int b) {
	if (a < 0 || b < 0 || a >= n || b >= m) return;
	if (arr[a][b] == 0 && visited[a][b] == false) {
		qu.push(make_pair(make_pair(a, b), cur.second + 1));
		visited[a][b] = true;
		maxN = (maxN < cur.second + 1) ? cur.second + 1 : maxN;
	}
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> m >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] == 1) {
				qu.push(make_pair(make_pair(i, j), 0));
				visited[i][j] = true;
			}
		}
	}

	if (qu.empty()) {
		cout << 0;
		return 0;
	}
	while (!qu.empty()) {
		cur = qu.front();
		int x = cur.first.first;
		int y = cur.first.second;
		qu.pop();
		isNear(x, y-1);
		isNear(x, y + 1);
		isNear(x + 1, y);
		isNear(x - 1, y);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] != -1 && visited[i][j] == false) {
				cout << -1;
				return 0;
			}
		}
	}
	cout << maxN;	
	return 0;
}
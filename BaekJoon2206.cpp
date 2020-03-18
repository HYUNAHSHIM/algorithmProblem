//BaekJoon 2206 벽 부수고 이동하기

#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <utility>

using namespace std;

const int MAX = 1001;
int n, m;
int dx[] = { 0, 1, 0, -1 };
int dy[] = { -1, 0, 1, 0 };
int arr[MAX][MAX] = { 0, };
bool visited[MAX][MAX][2];
struct Node {
	int x;
	int y;
	int distance;
	int wallDestroyed;
};
queue<Node> qu;

int bfs() {
	if (n == 1 && m == 1) return 1;
	qu.push({ 0,0,1,0 });
	visited[0][0][0] = true;

	while (!qu.empty()) {
		Node node = qu.front();
		qu.pop();
		if (node.x == n - 1 && node.y == m - 1) {
			return node.distance;
		}
		for (int i = 0; i < 4; i++) {
			int x = node.x + dx[i];
			int y = node.y + dy[i];

			if (x < 0 || y < 0 || x >= n || y >= m) continue;
			if (arr[x][y] == 0 && visited[x][y][node.wallDestroyed] == false) {
				qu.push({ x, y, node.distance + 1, node.wallDestroyed });
				visited[x][y][node.wallDestroyed] = true;
			}
			else if (arr[x][y] == 1 && node.wallDestroyed == 0) {
				qu.push({ x,y,node.distance + 1, node.wallDestroyed + 1 });
				visited[x][y][node.wallDestroyed + 1] = true;

			}
		}
	}
	return -1;
}

int main(void)
{
	//ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}
	cout << bfs();
	
	return 0;
}
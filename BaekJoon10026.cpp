//BaekJoon 10026 적록색약

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int n = 0;
int arr[100][100] = { 0, };
int arr2[100][100] = { 0, };
queue <pair<int, int>> qu;
int res = 0;
bool visited[100][100] = { false, };
pair<int, int> cur;

void isNear(int x, int y, int rgb[100][100]) {
	if (x < 0 || y < 0 || x >= n || y >= n) return;
	if (visited[x][y] == false && rgb[x][y] == rgb[cur.first][cur.second]) {
		qu.push(make_pair(x, y));
		visited[x][y] = true;
	}
}

void bfs(int rgb[100][100]) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visited[i][j] = false;
		}
	}
	res = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0;j < n; j++) {
			if (visited[i][j]) continue;
			qu.push(make_pair(i, j));
			visited[i][j] = true;
			res++;
			while (!qu.empty()) {
				cur = qu.front();
				qu.pop();
				int a = cur.first;
				int b = cur.second;
				isNear(a + 1, b, rgb);
				isNear(a, b - 1, rgb);
				isNear(a, b + 1, rgb);
				isNear(a - 1, b, rgb);
			}
		}
	}
	cout << res << " ";
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char tmp;
			cin >> tmp;
			if (tmp == 'R') {
				arr[i][j] = 0;
				arr2[i][j] = 0;
			}
			else if (tmp == 'G') {
				arr[i][j] = 1;
				arr2[i][j] = 0;
			}
			else if (tmp == 'B') {
				arr[i][j] = 2;
				arr2[i][j] = 2;
			}
		}
	}
	bfs(arr);
	bfs(arr2);
	return 0;
}
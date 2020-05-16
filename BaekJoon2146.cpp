//BaekJoon 2146 다리 만들기

#include <string.h>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int n, min_length = 10000;
int** map;
bool** visited;
queue<pair<pair<int, int>, int>> qu; //x, y, length
int dx[] = { 0, 1, 0, -1 };
int dy[] = { -1, 0, 1, 0 };


void bfs(int num) {
	while (!qu.empty()) {
		int x = qu.front().first.first;
		int y = qu.front().first.second;
		qu.pop();
		for (int i = 0; i < 4; i++) {
			int tmpx = x + dx[i];
			int tmpy = y + dy[i];
			if (tmpx < 0 || tmpx >= n || tmpy < 0 || tmpy >= n) continue;
			if (map[tmpx][tmpy] == 1 && visited[tmpx][tmpy] == false) {
				qu.push(make_pair(make_pair(tmpx, tmpy), 0));
				map[tmpx][tmpy] = num;
				visited[tmpx][tmpy] = true;
			}
		}
	}
}

void bfs_search(int num) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == num) {
				qu.push(make_pair(make_pair(i, j), 0));
				visited[i][j] = true;
			}
		}
	}
	while (!qu.empty()) {
		int x = qu.front().first.first;
		int y = qu.front().first.second;
		int length = qu.front().second;
		qu.pop();
		for (int i = 0; i < 4; i++) {
			int tmpx = x + dx[i];
			int tmpy = y + dy[i];
			if (tmpx < 0 || tmpx >= n || tmpy < 0 || tmpy >= n) continue;
			if (map[tmpx][tmpy] == num) continue;
			if (map[tmpx][tmpy] == 0 && visited[tmpx][tmpy] == false) {
				qu.push(make_pair(make_pair(tmpx, tmpy), length + 1));
				visited[tmpx][tmpy] = true;
			}
			if (map[tmpx][tmpy] != 0) {
				if (min_length > length) min_length = length;
				return;
			}
		}
	}
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n;
	map = new int* [n];
	visited = new bool* [n];
	for (int i = 0; i < n; i++) {
		map[i] = new int[n];
		visited[i] = new bool[n];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			visited[i][j] = false;
		}
	}
	int num = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 1 && visited[i][j] == false) {
				qu.push(make_pair(make_pair(i, j), 0));
				map[i][j] = num;
				visited[i][j] = true;
				bfs(num);
				num++;
			}
		}
	}
	for (int k = 1; k <= num - 1; k++) {
		while (!qu.empty()) qu.pop();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				visited[i][j] = false;
			}
		}
		bfs_search(k);
	}
	cout << min_length;
	return 0;
}
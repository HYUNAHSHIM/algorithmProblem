//BaekJoon 2178 ¹Ì·ÎÅ½»ö

#include <iostream>
#include <stdio.h>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int n, m, minDist = 2147483647;
int** arr;
bool** visited;
queue<pair<pair<int, int>, int>> qu;

int isNear(int p, int q, int dist) {
	if (p < 0 || q < 0 || p >= n || q >= m) return 0;
	if (arr[p][q] == 1 && visited[p][q] == false) {
		qu.push(make_pair(make_pair(p, q), dist + 1));
		visited[p][q] = true;
		return 1;
	}
	return 0;
}

int main(void)
{
	cin.tie(0);

	cin >> n >> m;
	arr = new int* [n];
	for (int i = 0; i < n; i++) {
		arr[i] = new int[m];
	}
	visited = new bool* [n];
	for (int i = 0; i < n; i++) {
		visited[i] = new bool[m];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &arr[i][j]);
			visited[i][j] = false;
		}
	}

	qu.push(make_pair(make_pair(0, 0), 1));
	visited[0][0] = true;

	while (!qu.empty()) {
		pair<pair<int, int>, int> cur = qu.front();
		qu.pop();
		int p = cur.first.first;
		int q = cur.first.second;
		int dist = cur.second;
		isNear(p, q - 1, dist);
		isNear(p - 1, q, dist);
		isNear(p, q + 1, dist);
		isNear(p + 1, q, dist);
		if (cur.first == make_pair(n - 1, m - 1)) {
			if (minDist > dist) {
				minDist = dist;
			}
		}
	}

	cout << minDist;

	return 0;
}
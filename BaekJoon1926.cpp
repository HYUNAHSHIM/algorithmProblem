//BaekJoon 1926 그림

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int n, m;
int** arr;
bool** visited;
int num = 0, maxNum = 0;
queue<pair<int, int>> qu;

void isNear(int p, int q) {
	if (p < 0 || q < 0 || p >= n || q >= m) return;
	if (arr[p][q] == 1 && visited[p][q] == false) {
		qu.push(make_pair(p, q));
		visited[p][q] = true;
	}
}

void findArea() {
	int area = 0;
	while (!qu.empty()) {
		pair<int, int> cur = qu.front();
		qu.pop();
		area++;
		int p = cur.first;
		int q = cur.second;

		isNear(p, q - 1);
		isNear(p - 1, q);
		isNear(p, q + 1);
		isNear(p + 1, q);
	}
	if (maxNum < area) {
		maxNum = area;
	}
}

int main(void)
{
	ios::sync_with_stdio(false);
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
			cin >> arr[i][j];
			visited[i][j] = false;
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] == 1 && visited[i][j] == false) {
				qu.push(make_pair(i, j));
				visited[i][j] = true;
				num++;
				findArea();
			}
		}
	}

	cout << num << "\n" << maxNum;

	return 0;
}
//BaekJoon 2583 영역 구하기

#include <iostream>
#include <string>
#include <queue>
#include <list>
#include <utility>

using namespace std;

int m, n, k;
int arr[100][100];
bool visited[100][100] = { false, };
list <int> li;
queue<pair<int, int>> qu;
int cnt = 0;

int isNear(int a, int b) {
	if (a < 0 || b < 0 || a >= m || b >= n) return 0;
	if (arr[a][b] == 0 && visited[a][b] == false) {
		qu.push(make_pair(a, b));
		visited[a][b] = true;
		return 1;
	}
	return 0;
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> m >> n >> k;
	for (int i = 0; i < k; i++) {
		int a, b, c, d;
		cin >> b >> a >> d >> c;
		c--; d--;
		for (int j = a; j <= c; j++) {
			for (int t = b; t <= d; t++) {
				arr[j][t] = 1;
			}
		}
	}
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] == 1 || visited[i][j] == true) continue;
			qu.push(make_pair(i, j));
			visited[i][j] = true;
			int numArr = 1;
			cnt++;
			while (!qu.empty()) {
				pair<int, int> cur = qu.front();
				qu.pop();
				int a = cur.first;
				int b = cur.second;
				numArr += isNear(a - 1, b);
				numArr += isNear(a, b + 1);
				numArr += isNear(a + 1, b);
				numArr += isNear(a, b - 1);
			}
			li.push_back(numArr);
		}
	}
	li.sort();
	cout << cnt << "\n";
	list<int>::iterator iter;
	for (iter = li.begin(); iter != li.end(); ++iter) {
		cout << *iter << " ";
	}
	
	return 0;
}
//BaekJoon 2573 빙산

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

const int MAX = 300;
int n, m;
int arr[MAX][MAX] = { 0, };
bool visited[MAX][MAX] = { false, };
int nearNode[MAX][MAX] = { 0, };
int numIce = 0;
int year = 0;
bool isZero = false;
int dx[] = { 0,1,0,-1 };
int dy[] = { -1,0,1,0 };
queue<pair<int, int>> qu;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
		}
	}
	while (!isZero) {
		isZero = true;
		numIce = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				visited[i][j] = false;
				nearNode[i][j] = 0;
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (visited[i][j] == true || arr[i][j] == 0) continue;
				qu.push(make_pair(i, j));
				visited[i][j] = true;

				while (!qu.empty()) {
					pair<int, int> cur = qu.front();
					qu.pop();
					for (int i = 0; i < 4; i++) {
						int x = cur.first + dx[i];
						int y = cur.second + dy[i];
						if (x < 0 || y < 0 || x >= n || y >= m) continue;
						if (arr[x][y] == 0) {
							nearNode[cur.first][cur.second]++;
							continue;
						}
						if (visited[x][y] == true) continue;
						qu.push(make_pair(x, y));
						visited[x][y] = true;
					}
				}
				numIce++;
			}
		}
		if (numIce >= 2) {
			cout << year;
			return 0;  
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] < nearNode[i][j]) arr[i][j] = 0;
				else arr[i][j] -= nearNode[i][j];
			}
		}
		//check if ice all melted
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] != 0) isZero= false;
			}
		}
		year++;
	}
	cout << 0;
	return 0;
}
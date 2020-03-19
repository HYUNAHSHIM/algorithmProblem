//BaekJoon 2468 안전영역

#include <iostream>
#include <string>

using namespace std;

int n;
int num[100] = {0, };
int arr[100][100];
int dfsArr[100][100];
int visited[100][100] = { false, };
int dx[] = { 0, 1, 0, -1 };
int dy[] = { -1, 0, 1, 0 };

void dfs(int a, int b) {
	visited[a][b] = true;
	for (int i = 0; i < 4; i++) {
		int x = a + dx[i];
		int y = b + dy[i];
		if (x < 0 || y < 0 || x >= n || y >= n) continue;
		if (visited[x][y] == false && dfsArr[x][y] == 0) dfs(x, y);
	}

}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n;
	int max = -1;
	//initialize and find the highest area
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
			max = max < arr[i][j] ? arr[i][j] : max;
		}
	}
	for (int i = 1; i <= max; i++) {
		for (int p = 0; p < n; p++) {
			for (int q = 0; q < n; q++) {
				if (arr[p][q] <= i) dfsArr[p][q] = 1; //물에 잠긴부분
				else dfsArr[p][q] = 0; //물에 잠기지 않은 부분
				visited[p][q] = false;
			}
		}
		for (int p = 0; p < n; p++) {
			for (int q = 0; q < n; q++) {
				if (visited[p][q] || dfsArr[p][q] == 1) continue;
				dfs(p, q);
				num[i]++;
			}
		}
	}
	
	int maxArea = 1;
	for (int i = 1; i < max; i++) {
		maxArea = maxArea < num[i] ? num[i] : maxArea;
	}
	cout << maxArea;
	return 0;
}
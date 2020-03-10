//BaekJoon 2667 단지번호 붙이기

#include <iostream>
#include <string>
#include <stdio.h>
#include <queue>
#include <utility>
#include <list>

using namespace std;

int n;
int arr[25][25];
bool visited[25][25] = { false, };
list<int> l;
int num = 0;
int numApt;
pair<int, int> cur;
queue<pair<int, int>> qu;

int isNear(int a, int b){
	if (a < 0 || a >= n || b < 0 || b >= n) {
		return 0;
	}
	if (arr[a][b] == 1 && visited[a][b] == false) {
		qu.push(make_pair(a, b));
		visited[a][b] = true;
		return 1;
	}
	return 0;
}

int main(void)
{
	cin.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] == 1 && visited[i][j] == false) {
				qu.push(make_pair(i, j));
				visited[i][j] = true;
				num++;
				numApt = 1;
				while (!qu.empty()) {
					cur = qu.front();
					qu.pop();
					int a = cur.first;
					int b = cur.second;
					numApt += isNear(a + 1, b);
					numApt += isNear(a, b - 1);
					numApt += isNear(a, b + 1);
					numApt += isNear(a - 1, b);
				}
				l.push_back(numApt);
			}
		}
	}
	l.sort();
	cout << num << "\n";
	list<int>::iterator iter;
	for (iter = l.begin(); iter != l.end(); ++iter) {
		cout << *iter << "\n";
	}
	return 0;
}
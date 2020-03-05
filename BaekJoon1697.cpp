//BaekJoon 1697 ¼û¹Ù²ÀÁú

#include <iostream>
#include <stdio.h>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int n, k;
queue<pair<int, int>> qu;
bool visited[100001] = { false, };
pair<int, int> current;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> k;
	if (n == k) {
		cout << 0;
		return 0;
	}
	qu.push(make_pair(n, 0));
	visited[n] = true;

	while (!qu.empty()) {
		current = qu.front();
		qu.pop();
		int x = current.first;
		int y = current.second;
		if (x - 1 >= 0 && visited[x - 1] == false) {
			if ((x - 1) == k) {
				cout << y + 1;
				return 0;
			}
			qu.push(make_pair(x - 1, y + 1));
			visited[x - 1] = true;
		}
		if (x + 1 <= 100000 && visited[x + 1] == false) {
			if ((x + 1) == k) {
				cout << y + 1;
				return 0;
			}
			qu.push(make_pair(x + 1, y + 1));
			visited[x + 1] = true;
		}
		if (x * 2 <= 100000 && visited[x * 2] == false) {
			if ((x * 2) == k) {
				cout << y + 1;
				return 0;
			}
			qu.push(make_pair(x * 2, y + 1));
			visited[x * 2] = true;
		}
	}
	return 0;
}
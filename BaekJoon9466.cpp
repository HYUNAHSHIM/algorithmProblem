//BaekJoon 9466 텀 프로젝트

#include <iostream>
#include <string>

using namespace std;

const int MAX = 100000 + 1;
int T, n, cnt = 0;
int want[MAX];
int visited[MAX];
int done[MAX];

void dfs(int cur) {
	visited[cur] = true;
	int next = want[cur];
	if (!visited[next])	dfs(next);
	else if (!done[next]) {
		for (int i = next; i != cur; i = want[i]) cnt++;
		cnt++;
	}
	done[cur] = true;
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> T;
	while (T--) {
		cin >> n;
		cnt = 0;
		for (int i = 1; i <= n; i++) {
			visited[i] = false;
			done[i] = false;
		}
		for (int i = 1; i <= n; i++) {
			cin >> want[i];
		}
		for (int i = 1; i <= n; i++) {
			if (!visited[i]) dfs(i);
		}
		cout << n - cnt << "\n";
	}
	return 0;
}
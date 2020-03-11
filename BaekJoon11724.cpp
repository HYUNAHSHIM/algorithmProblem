//BaekJoon 11724 연결 요소의 개수

#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int n, m;
vector<int> arr[1001];
bool visited[1001] = { false, };

int dfs() {
	stack<int> st;
	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (visited[i]) continue;
		st.push(i);
		cnt++;
		visited[i] = true;
		while (!st.empty()) {
			int cur = st.top();
			st.pop();
			for (int j = 0; j < arr[cur].size(); j++) {
				int nxt = arr[cur][j];
				if (visited[nxt]) continue;
				st.push(nxt);
				visited[nxt] = true;
			}
		}
	}
	return cnt;
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> n >> m;
	for (int i = 1; i <= m; i++) {
		int a, b;
		cin >> a >> b;
		arr[a].push_back(b);
		arr[b].push_back(a);
	}
	cout << dfs();
	return 0;
}
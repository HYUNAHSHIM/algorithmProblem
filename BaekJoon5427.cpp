//BaekJoon 5427 불

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

const int MAX = 1000;
const int INF = 2147438647;
int w, h;
int building[MAX][MAX];
queue<pair<int, int>> fire;
queue<pair<pair<int, int>, int>> person;
int fireTime[MAX][MAX];
bool visited[MAX][MAX];;
int dx[] = { 0, 1, 0, -1 };
int dy[] = { -1, 0, 1, 0 };

int movePerson() {
	while (!person.empty()) {
		int tmpx = person.front().first.first;
		int tmpy = person.front().first.second;
		int time = person.front().second;
		person.pop();
		if (tmpx == h - 1 || tmpx == 0 || tmpy == w - 1 || tmpy == 0) return time + 1;
		for (int i = 0; i < 4; i++) {
			int x = tmpx + dx[i];
			int y = tmpy + dy[i];
			if (x < 0 || y < 0 || x >= h || y >= w) continue;
			if (building[x][y] == 0 && visited[x][y] == false) {
				if (fireTime[x][y] > time + 1) {
					person.push(make_pair(make_pair(x, y), time + 1));
					visited[x][y] = true;
				}
			}
		}
	}
	return -1;
}

void getFireMap() {
	while (!fire.empty()) {
		int tmpx = fire.front().first;
		int tmpy = fire.front().second;
		fire.pop();
		for (int i = 0; i < 4; i++) {
			int x = tmpx + dx[i];
			int y = tmpy + dy[i];
			if (x < 0 || y < 0 || x >= h || y >= w) continue;
			if (building[x][y] != 1) {
				if (fireTime[x][y] > fireTime[tmpx][tmpy] + 1) {
					fireTime[x][y] = fireTime[tmpx][tmpy] + 1;
					fire.push(make_pair(x, y));
				}
			}
		}
	}
}

void initialize() {
	while (!fire.empty()) fire.pop();
	while (!person.empty()) person.pop();
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			fireTime[i][j] = INF;
			visited[i][j] = false;
			building[i][j] = 0;
			char tmp;
			cin >> tmp;
			if (tmp == ',') building[i][j] = 0;
			else if (tmp == '#') building[i][j] = 1;
			else if (tmp == '@') {
				building[i][j] = 2;
				person.push(make_pair(make_pair(i, j), 0));
				visited[i][j] = true;
			}
			else if (tmp == '*') {
				building[i][j] = 3;
				fire.push(make_pair(i, j));
				fireTime[i][j] = 0;
			}
		}
	}
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T; cin >> T;
	while (T--) {
		cin >> w >> h;
		initialize();
		getFireMap();
		int result = movePerson();
		if (result == -1) cout << "IMPOSSIBLE" << "\n";
		else cout << result << "\n";
	}
	return 0;
}
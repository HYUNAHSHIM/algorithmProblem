//BaekJoon 9202 boggle

#include <string.h>
#include <iostream>
#include <set>

using namespace std;

const int ALPHABET = 26;
int w, b;
bool visited[4][4];
string map[4];
set<string> res;
int dx[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
int dy[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int score[9] = { 0, 0, 0, 1, 1, 2, 3, 5, 11 };

struct Trie {
	bool isFinish;
	Trie* children[ALPHABET];

	//constructor
	Trie() : isFinish(false) {
		memset(children, 0, sizeof(children));
		this->isFinish = false;
	}

	//destructor
	~Trie() {
		for (int i = 0; i < ALPHABET; i++) {
			if (children[i]) delete this->children[i];
		}
	}

	void insert(const char* key) {
		if (*key == '\0') isFinish = true;
		else {
			int cur = *key - 'A';
			if (children[cur] == NULL) children[cur] = new Trie();
			children[cur]->insert(key + 1);
		}
	}
	//dfs search
	void search(int x, int y, string key) {
		if (key.length() > 8) return;
		visited[x][y] = true;
		key += map[x][y];

		Trie* child = this->children[map[x][y] - 'A'];
		if (child == NULL) {
			visited[x][y] = false;
			return;
		}
		if (child->isFinish) res.insert(key);
		for (int dir = 0; dir < 8; dir++) {
			int ny = y + dy[dir], nx = x + dx[dir];
			if (ny < 0 || ny >= 4 || nx < 0 || nx >= 4) continue;
			if (visited[nx][ny]) continue;
			child->search(nx, ny, key);
		}
		visited[x][y] = false;
	}
};

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	Trie* root = new Trie();
	cin >> w;
	while (w--) {
		char s[10] = {}; cin >> s;
		root->insert(s);
	}
	cin >> b;
	while (b--) {
		for (int i = 0; i < 4; i++) cin >> map[i];
		res.clear();
		for (int x = 0; x < 4; x++) {
			for (int y = 0; y < 4; y++) {
				root->search(x, y, "");
			}
		}
		string longest = "";
		int Max = 0, match = res.size(), scoreSum = 0;
		for (string item : res) {
			if (Max == item.length()) longest = longest < item ? longest : item;
			else if (Max < item.length()) {
				Max = item.length();
				longest = item;
			}
			scoreSum += score[item.length()];
		}
		cout << scoreSum << " " << longest << " " << match << "\n";
	}
	delete root;
	return 0;
}
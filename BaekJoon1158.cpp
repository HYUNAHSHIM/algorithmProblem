//BaekJoon 1158 조세퍼스 문제

#include <iostream>
#include <vector>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	vector<int> arr;
	int n, k;
	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		arr.push_back(i + 1);
	}

	int idx = k - 1;
	cout << "<";
	while (arr.size() > 1) {
		cout << arr[idx] << ", ";
		arr.erase(arr.begin() + idx);
		idx += k - 1;
		idx %= arr.size();//����, �ѹ��� �� ������ ���
	}
	cout << arr[0] << ">" << endl;

	return 0;
}
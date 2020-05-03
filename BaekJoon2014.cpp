//BaekJoon 2014 소수의 곱

#include <string.h>
#include <iostream>
#include <queue>
#include <functional>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int k, n; cin >> k >> n;
	long long input[100];
	priority_queue< long long, vector<long long>, greater<long long> > pq;
	for (int i = 0; i < k; i++) {
		cin >> input[i];
		pq.push(input[i]);
	}
	for (int i = 0; i < n - 1; i++) {
		long long smallest = pq.top();
		pq.pop();

		for (int j = 0; j < k; j++) {
			pq.push(smallest* input[j]);
			if (smallest % input[j] == 0) break;
		}
	}
	long long result = pq.top();
	cout << result;
	return 0;
}
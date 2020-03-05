//BaekJoon 1874 스택 수열

#include <iostream> 
#include <string>

using namespace std;

int stack[100000];
int top = 0;
char* result;
int pointer = 0;

void push(int num) {
	stack[top++] = num;
	result[pointer++] = '+';
}

int pop() {
	result[pointer++] = '-';
	return stack[--top];
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n = 0;
	cin >> n;
	result = new char[n];

	int max = 0;
	while (n--) {
		int tmp = 0;
		cin >> tmp;

		if (max < tmp) {
			for (int i = max + 1; i <= tmp; i++) {
				push(i);
			}
		}
		else {
			if (stack[top - 1] != tmp) {
				cout << "NO" << "\n";
				return 0;
			}
		}
		pop();
		if (max < tmp) max = tmp;
	}

	for (int i = 0; i < pointer; i++) {
		cout << result[i] << "\n";
	}

	return 0;
}
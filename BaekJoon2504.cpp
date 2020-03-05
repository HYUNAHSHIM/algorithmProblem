//BaekJoon 2504 °ýÈ£ÀÇ °ª

#include <iostream>
#include <string>
#include <stack>

using namespace std;

stack<char> stk;
int sum = 0;//result
int mul = 1;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	string input;
	cin >> input;
	int length = input.length();
	for (int i = 0; i < length; i++) {
		if (input[i] == '(') {
			mul *= 2;
			stk.push('(');
		}
		else if (input[i] == '[') {
			mul *= 3;
			stk.push('[');
		}
		else if (input[i] == ')') {
			if (input[i - 1] == '(') {
				sum += mul;
			}
			if (stk.empty()) return !printf("0");
			if (stk.top() == '(') stk.pop();
			mul /= 2;
		}
		else if (input[i] == ']') {
			if (input[i - 1] == '[') {
				sum += mul;
			}
			if (stk.empty()) return !printf("0");
			if (stk.top() == '[') stk.pop();
			mul /= 3;
		}
	}

	//if not empty return 0
	cout << (stk.empty() ? sum : 0);

	return 0;
}
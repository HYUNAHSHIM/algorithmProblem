//BaekJoon 9012 괄호

#include <iostream>
#include <string.h>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int testCase; cin >> testCase;

	while (testCase--) {
		int stack[100];
		int top = -1;
		string input = "";
		cin >> input;
		bool isVPS = true;
		int len = input.length();
		for (int i = 0; i < len; i++) {
			if (input[i] == '(') {
				stack[++top] = 1;
			}
			else {
				if (top == -1) {
					isVPS = false;
					break;;
				}
				else {
					stack[top--];
				}
			}
		}
		if (top != -1) isVPS = false;

		if (isVPS == true) cout << "YES\n";
		else cout << "NO\n";
	}

	return 0;
}
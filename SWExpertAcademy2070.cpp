//SWExpertAcademy 2070 큰놈, 작은 놈, 같은 놈

#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{

		int a, b; cin >> a >> b;
		if (a > b) cout << "#" << test_case << " >\n";
		else if (a == b) cout << "#" << test_case << " =\n";
		else cout << "#" << test_case << " <\n";


	}
	return 0;
}
//SWExpertAcademy 2068 최대수 구하기

#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
		int max = 0;
        for(int i=0;i<10;i++){
            int tmp = 0;
            cin >> tmp;
            if(tmp > max) max = tmp;
        }
        cout << "#" << test_case << " " << max << "\n";
	}
	return 0;
}
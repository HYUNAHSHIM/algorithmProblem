//SW Expert Academy 2071 평균값 구하기

#include <iostream>
#include <math.h>

using namespace std;

int main(void)
{
	int result = 0; //result of calculation
	int n = 0; //number of test cases
	cin >> n;
	float* test = new float[n]; //store result

	for (int i = 0; i < n; i++) {
		result = 0;
		for (int j = 0; j < 10; j++) {
			int tmp = 0;
			cin >> tmp;
			result += tmp;
		}
		test[i] = floor((result + 5) / 10);
	}

	for (int i = 0; i < n; i++) { //print result
		cout << "#" << i + 1 << " " << test[i] << endl;
	}

	return 0;
}
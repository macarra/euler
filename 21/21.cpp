#include <iostream>
#include <math.h>
#include <vector>
#include <map>
#include <string>


using namespace std;

void divide(int N, long* m){
	for(int n = 1; n < N; n++){
		m[n] = 0;
		for(int i = 1; i < n; i++){
			if(n%i == 0){
				m[n]+=i;
			}
		}
	}
}

int main(int argc, char** argv){
	long*  m;
	const long k = 100000;
	m = (long*) malloc(k * sizeof(long));
	divide(k, m);
	int res = 0;
	for(int i = 1; i < k; i++){
		int val = m[i];
		if(val < k && val != i && m[val] == i){
			res += i;
			res += val;
			m[i]= 0;
			m[val] = 0;
		}

	}
	cout << "res: "<< res << "\n";
	return 0;
}

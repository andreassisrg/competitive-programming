#include <bits/stdc++.h>
using namespace std;

int main() {
	long long N; cin >> N;
	bool primo = false;
	for (long long i = 2; i*i <= N; i++) {
		if (N % i == 0) {
			primo = true;
			break;
		}
	}
	if (primo) { cout << "nao" << endl; }
	else { cout << "sim" << endl; }

	return 0;
}


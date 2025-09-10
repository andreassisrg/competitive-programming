#include <bits/stdc++.h>

using namespace std;

int main() {
	int N;
	int n_teste { 1 };

	while(true) {
		cin >> N;
		if (N == 0) { break; }
		
		for (int i = 1; i <= N; i++) {
			int x; cin >> x;
			if (i == x) {
				cout << "Teste " << n_teste << endl;
				cout << x << endl;
				cout << "\n";
			}
		}
		n_teste++;
	}
	
	return 0;
}


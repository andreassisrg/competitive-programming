#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;

    if (n == 0) {
        cout << 1 << endl;
        return 0;
    }

    int result = 1;
    while (n > 0) {
        result *= n; n--;
    }
    
    cout << result << endl;

	return 0;
}


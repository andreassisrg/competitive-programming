#include <bits/stdc++.h>

using namespace std;

int main() {
    int t; cin >> t;
    
    while (t--) {
       int a; int b; cin >> a; cin >> b;

        if (a % b == 0) {
            cout << 0 << endl;
            continue;
        }

        if (a / b >= 1) {
            int teto_divisao = ceil(double(a) / b);
            cout << (teto_divisao * b) - a << endl;
            continue;
        }
        
        if (a / b < 1) {
            cout << b - a << endl;
            continue;
        }
    }    

    return 0;
}


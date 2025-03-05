#include <bits/stdc++.h>

using namespace std;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define f first
#define s second

typedef long long ll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;

int main() { _
    
	int t; cin >> t;
	ll x, n, m;
	while (t--) {
		cin >> x >> n >> m;
		bool possible = true;
		while (x > 0) {
			if (x > 20 && n > 0) {
				x = (floor(x/2)) + 10;
				n--;
			}
			else if (m > 0) {
				x -= 10;
				m--;
			}
			else {
				possible = false;
				break;	
			}
		}
		cout << (possible ? "YES" : "NO") << endl;
	}	

	return 0;
}


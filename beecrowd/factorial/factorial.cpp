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
	ll N; cin >> N;
	ll count = 0;
	while (N > 0) {
		ll curr = 1;
		for (ll i = 1; i <= N; i++) {
			curr *= i;
			if (curr > N) {
				count++;
				N -= (curr/i);
				break;
			}
			if (curr == N) {
				count++;
				N -= curr;
				break;
			}
		}
	}
	cout << count << endl;
	return 0;
}


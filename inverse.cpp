// (a * x) mod m = 1
#include <bits/stdc++.h>
using namespace std;

int modInverse(int a, int m) {
	for(int x = 1; x < m; x++) {
		if(((a % m) * (x % m)) % m == 1) {
			return x;
		}
	}
}

int main() {
	int a, m;
	cin >> a >> m;
	cout << "x la " << modInverse(a, m);
}

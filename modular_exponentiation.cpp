// a^b mod m 
#include <bits/stdc++.h>
using namespace std;

int power(int a, int b, int m) {
	int res = 1;
	while(b > 0) {
		if(b % 2 == 1) {
			res = res * a;
		}
		b = b >> 1;
		a = a * a;
	}
	return res % m;
}

int main() {
	int a, b, m;
	cin >> a >> b >> m;
	cout << "Power = " << power(a, b, m);
}

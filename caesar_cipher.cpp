// ma Caesar
#include <bits/stdc++.h>
using namespace std;

string caesar(string s, int shift) {
	string result = "";
	for(int i = 0; i < s.length(); i++) {
		if(isupper(s[i])) {
			result += char(int(s[i] + shift - 65) % 26 + 65);
		}
		else {
			result += char(int(s[i] + shift - 97) % 26 + 97);
		}
	}
	return result;
}

int main() {	
	string s;
	int shift;
	getline(cin, s);
	cin >> shift;
	cout << "Sau ma hoa Caesar: " << caesar(s, shift);
}

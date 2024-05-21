#include<bits/stdc++.h>
using namespace std;

int gcd(double a, double h) {
    int temp;
    while(1) {
        temp = fmod(a, h);
        if(temp == 0) {
            return h;
        }
        a = h;
        h = temp;
    }
}

bool isPrime(double a) {
    if(a <= 1) return false;
    if(a == 2) return true;
    if(fmod(a, 2) == 0) return false;
    for(double i = 3; i <= sqrt(a); i+=2) {
        if(fmod(a, i) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    double p, q;
    do {
        cout << "Nhap 2 so nguyen to p, q: ";
        cin >> p >> q;
        if(!isPrime(p) || !isPrime(q)) {
            cout << "Yeu cau nhap lai\n";
        }
    } while(!isPrime(p) || !isPrime(q));

    double n = p * q;

    double e = 2;
    double phi = (p - 1) * (q - 1);
    while( e < phi) {
        if(gcd(e, phi) == 1) break;
        else e++;
    }

    int k = 2;
    double d = (1 + (k * phi)) / e;
    double msg;
    cout << "Enter message data: ";
    cin >> msg;

    cout << "Message data = " << msg << "\n";

    double c = pow(msg, e);
    c = fmod(c, n);
    cout << "Encrypted data = " << c << "\n";

    double m = pow(c, d);
    m = fmod(m, n);
    cout << "Original Message Sent = " << m;
}
#include<bits/stdc++.h>
using namespace std;

// set<int> prime;

int public_key;
int private_key;
int n;

// void primeFiller() {
//     vector<bool> seive(250, true);
//     seive[0] = false;
//     seive[1] = false;
//     for(int i = 2; i < 250; i++) {
//         for(int j = i * 2; j < 250; j += i) {
//             seive[j] = false;
//         }
//     }
//     for(int i = 0; i< seive.size(); i++) {
//         if(seive[i]) prime.insert(i);
//     }
// }

// int pickRandomPrime() {
//     int k = rand() % prime.size();
//     auto it = prime.begin();
//     while(k--) {
//         it++;
//     }
//     int ret = *it;
//     prime.erase(it);
//     return ret;
// }

int gcd(int a, int h) {
    int temp;
    while(1) {
        temp = a % h;
        if(temp == 0) {
            return h;
        }
        a = h;
        h = temp;
    }
}

void setKeys(int prime1, int prime2) {
    // int prime1 = pickRandomPrime();
    // int prime2 = pickRandomPrime();

    n = prime1 * prime2;
    int fi = (prime1 - 1) * (prime2 - 1);
    int e = 2;
    while(1) {
        if(gcd(e, fi) == 1) {
            break;
        }
        e++;
    }
    public_key = e;
    int d = 2;
    while(1) {
        if((d * e) % fi == 1) break;
        d++;
    }
    private_key = d;
}

long long int encrypt(int message) {
    int e = public_key;
    long long int encrypted_text = 1;
    while(e--) {
        encrypted_text *= message;
        encrypted_text %= n;
    }
    return encrypted_text;
}

long long int decrypt(int encrypted_text) {
    int d = private_key;
    long long int decrypted = 1;
    while(d--) {
        decrypted *= encrypted_text;
        decrypted %= n;
    }
    return decrypted;
}

vector<int> encoder(string message) {
    vector<int> form;
    for(auto& letter : message) {
        form.push_back(encrypt((int)letter));
    }
    return form;
}

string decoder(vector<int> encoded) {
    string s;
    for(auto& num : encoded) {
        s += decrypt(num);
    }
    return s;
}

bool isPrime(int a) {
    if(a <= 1) return false;
    if(a == 2) return true;
    if(a % 2 == 0) return false;
    for(int i = 3; i <= sqrt(a); i+=2) {
        if(a % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    // primeFiller();
    // setKeys();
    int p, q;
    do {
        cout << "Nhap 2 so nguyen to p, q: ";
        cin >> p >> q;
        if(!isPrime(p) || !isPrime(q)) {
            cout << "Yeu cau nhap lai\n";
        }
    } while(!isPrime(p) || !isPrime(q));
    setKeys(p, q);
    string message;
    cout << "Initial message: ";
    cin.ignore();
    getline(cin, message);
    vector<int> coded = encoder(message);
    cout << "The encoded message(encrypted by public key): ";
    for(auto& p : coded) {
        cout << p;
    }
    cout << "\nThe decoded message(decrypted by private key): " << decoder(coded);
}
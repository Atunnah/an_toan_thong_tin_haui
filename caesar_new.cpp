#include <iostream>
#include <string>
#include <locale>

using namespace std;

// Hàm mã hoá Caesar
string caesarCipherEncrypt(string text, int shift) {
    string result = "";

    for (char& c : text) {
        // Kiểm tra xem ký tự có phải là chữ cái không
        if (isalpha(c, locale())) {
            // Mã hoá ký tự
            char base = isupper(c, locale()) ? 'A' : 'a';
            c = ((c - base + shift) % 26) + base;
        }
        // Thêm ký tự vào kết quả
        result += c;
    }

    return result;
}

// Hàm giải mã Caesar
string caesarCipherDecrypt(string text, int shift) {
    // Sử dụng hàm mã hoá với shift âm để giải mã
    return caesarCipherEncrypt(text, -shift);
}

int main() {
    string plaintext;
    int shift;

    cout << "Nhập văn bản cần mã hoá: ";
    getline(cin, plaintext);

    cout << "Nhập số lượng dịch chuyển (shift): ";
    cin >> shift;

    // Mã hoá văn bản
    string encryptedText = caesarCipherEncrypt(plaintext, shift);
    cout << "Văn bản đã mã hoá: " << encryptedText << endl;

    // Giải mã văn bản
    string decryptedText = caesarCipherDecrypt(encryptedText, shift);
    cout << "Văn bản đã giải mã: " << decryptedText << endl;

    return 0;
}

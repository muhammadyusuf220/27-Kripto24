#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string shiftCipherEncrypt(string text, int key) {
    string result = "";
    for (char &c : text) {
        if (isalpha(c)) {
            char offset = isupper(c) ? 'A' : 'a';
            c = (c - offset + key) % 26 + offset;
        }
        result += c;
    }
    return result;
}

string shiftCipherDecrypt(string text, int key) {
    return shiftCipherEncrypt(text, 26 - key);
}

string readFile(string filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: Tidak dapat membuka file " << filename << endl;
        exit(EXIT_FAILURE);
    }
    string text((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
    file.close();
    return text;
}

void writeFile(string filename, string text) {
    ofstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: Tidak dapat menulis ke file " << filename << endl;
        exit(EXIT_FAILURE);
    }
    file << text;
    file.close();
}

void printMenu() {
    cout << "\n====================================\n";
    cout << "             Shift Cipher             \n";
    cout << "====================================\n";
    cout << "1. Enkripsi Teks\n";
    cout << "2. Dekripsi Teks\n";
    cout << "3. Enkripsi File\n";
    cout << "4. Dekripsi File\n";
    cout << "0. Keluar\n";
    cout << "====================================\n";
}

int main() {
    int choice, key;
    string text, inputFile, outputFile;

    do {
        printMenu();
        cout << "Masukkan pilihan (1-5): ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Masukkan teks: ";
                cin.ignore();
                getline(cin, text);
                cout << "Masukkan key (0-25): ";
                cin >> key;
                if (key < 0 || key > 25) {
                    cerr << "Error: Key harus dalam rentang 0-25." << endl;
                    break;
                }
                cout << "Hasil enkripsi: " << shiftCipherEncrypt(text, key) << endl;
                break;

            case 2:
                cout << "Masukkan teks: ";
                cin.ignore();
                getline(cin, text);
                cout << "Masukkan key (0-25): ";
                cin >> key;
                if (key < 0 || key > 25) {
                    cerr << "Error: Key harus dalam rentang 0-25." << endl;
                    break;
                }
                cout << "Hasil dekripsi: " << shiftCipherDecrypt(text, key) << endl;
                break;

            case 3:
                cout << "Masukkan nama file input: ";
                cin >> inputFile;
                cout << "Masukkan nama file output: ";
                cin >> outputFile;
                cout << "Masukkan key (0-25): ";
                cin >> key;
                if (key < 0 || key > 25) {
                    cerr << "Error: Key harus dalam rentang 0-25." << endl;
                    break;
                }
                text = readFile(inputFile);
                writeFile(outputFile, shiftCipherEncrypt(text, key));
                cout << "File " << inputFile << " telah dienkripsi menjadi " << outputFile << endl;
                break;

            case 4:
                cout << "Masukkan nama file input: ";
                cin >> inputFile;
                cout << "Masukkan nama file output: ";
                cin >> outputFile;
                cout << "Masukkan key (0-25): ";
                cin >> key;
                if (key < 0 || key > 25) {
                    cerr << "Error: Key harus dalam rentang 0-25." << endl;
                    break;
                }
                text = readFile(inputFile);
                writeFile(outputFile, shiftCipherDecrypt(text, key));
                cout << "File " << inputFile << " telah didekripsi menjadi " << outputFile << endl;
                break;

            case 0:
                cout << "Keluar dari program. Terima kasih telah menggunakan aplikasi ini!" << endl;
                break;

            default:
                cerr << "Error: Pilihan tidak valid. Silakan pilih angka antara 0-4." << endl;
        }
    } while (choice != 0);

    return 0;
}

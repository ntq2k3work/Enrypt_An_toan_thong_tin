#include<bits/stdc++.h>

using namespace std;

bool ok = false;

int mod(int a, int m){
	int r = a % m;
	return (r < 0) ? (r + m) : r;
}

int gcd(int a, int m){
	if(m == 0)
		return a;
	return gcd(m, a % m);
}

int ext(int a, int m, int &x, int &y){
	if(m == 0){
		// a.x + m.y = gcd(a, m) <=> a.1 + 0.0 = 1
		x = 1;
		y = 0;
		return a;
	}
	int x1, y1;
	int d = ext(m, a % m, x1, y1);
	x = y1;
	y = x1 - (a / m) * y1;
	return d;
}

int inv(int a, int m){
	int x, y;
	int d = ext(a, m, x, y);
	if(d != 1)
		return -1;
	else
		return (x % m + m) % m;
}

string encrypt(string mess, int k[]){
	string cipher = "";
	for(int i = 0; i < mess.length(); i++){
		if(mess[i] != ' '){
			if(islower(mess[i]))
				cipher += char(((k[0] * (mess[i] - 'a') + k[1]) % 26) + 'a');
			else
				cipher += char(((k[0] * (mess[i] - 'A') + k[1]) % 26) + 'A');
		}
		else
			cipher += mess[i];
	}
	return cipher;
}

string decrypt(string cipher, int k[]){
	string mess = "";
	int a_inv = inv(k[0], 26);
	for(int i = 0; i < cipher.length(); i++){
		if(cipher[i] != ' '){
			if(islower(cipher[i]))
				mess += char(mod((a_inv * mod(((cipher[i] - 'a') - k[1]), 26)), 26) + 'a');
			else
				mess += char(mod((a_inv * mod(((cipher[i] - 'A') - k[1]), 26)), 26) + 'A');
		}
		else
			mess += cipher[i];
	}
	return mess;
}

int main(){
	int k[2];
	do{
		if(ok)
			cout << "Nhap lai khoa k = (a, b) voi gcd(a, 26) = 1: ";
		else
			cout << "Nhap khoa k = (a, b): ";
		for(int i = 0; i < 2; i++)
			cin >> k[i];
		ok = true;
	}while(gcd(k[0], 26) != 1);

	string mess;
	cin.ignore();
	cout << "Nhap thong diep ma hoa: ";			getline(cin, mess);

	string cipher = encrypt(mess, k);
	cout << "Ban ma: " << cipher << endl;

	cout << "Ban ro: " << decrypt(cipher, k) << endl;
	return 0;
}









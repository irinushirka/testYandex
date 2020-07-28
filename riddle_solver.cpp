#include "pch.h"

#include <fstream>
#include <string>
#include <iostream>
using namespace std;

string read_file() {
	string riddle;
	ifstream file("riddle.txt");
	getline(file, riddle, '\n');
	file.close();
	return riddle;
}

string remove_not_letters(string riddle) {
	for (int i = 0; i < riddle.length(); i++) {
		if (!isalpha(riddle[i])) {
			riddle.erase(i, 1);
			i--;
		}
	}
	return riddle;
}

string kr_5(string riddle) {
	for (int i = 0; i < riddle.length(); i++) {
		if (int(riddle[i]) % 5 == 0) {
			riddle.erase(i, 1);
			i--;
		}
	}
	return riddle;
}

string more_33(string riddle) {
	int counter = 0;
	char current_char;
	for (int i = 0; i < riddle.length(); i++) {
		current_char = riddle[i];
		counter = 0;
		for (int j = i; j < riddle.length(); j++) {
			if (riddle[j] == current_char) {
				counter++;
			}
		}
		if (counter >= 33) {
			for (int j = i; j < riddle.length(); j++) {
				if (riddle[j] == current_char) {
					riddle.erase(j, 1);
					j--;
				}
			}
			i--;
		}
	}

	return riddle;
}

string str_to_lower(string riddle) {
	int len = riddle.length();
	string result = "";
	for (int i = 0; i < len; i++) {
		result += tolower(riddle[i]);
	}
	return result;
}

int main()
{
	string riddle = read_file();
	riddle = remove_not_letters(riddle);
	riddle = kr_5(riddle);
	riddle = more_33(riddle);
	riddle = str_to_lower(riddle);
	cout << riddle;
}

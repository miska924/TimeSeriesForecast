#include <iostream>
#include <cstdio>
#include <string>
#include <deque>

using namespace std;

const int DEFAULT_LOG_SIZE = 100;

int main(int argc, char* argv[]) {
	int wanted_log_size;
	if (argc == 2) {
		wanted_log_size = DEFAULT_LOG_SIZE;
	} else if (argc == 3) {
		wanted_log_size = atoi(argv[2]);
	} else {
		cerr << "Usage:\n./cut_log <log_file_name> <wanted_log_size>\n";
		return -1;
	}

	freopen(argv[1], "r", stdin);
	string line;
	deque<string> log;
	while (getline(cin, line)) {
		log.push_back(line);
		if (log.size() > wanted_log_size) {
			log.pop_front();
		}
	}
	fclose(stdin);

	freopen(argv[1], "w", stdout);
	for (const auto& line : log) {
		cout << line << "\n";
	}
	fclose(stdout);

	return 0;
}
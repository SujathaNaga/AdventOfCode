#include "common.h"
using namespace std;
const char* day10input = R"(noop
noop
noop
addx 5
addx 1
addx 4
addx 1
noop
addx 4
noop
addx 1
addx 4
addx 8
addx -7
addx 3
addx 1
noop
addx 4
addx 2
addx 5
addx -1
noop
addx -37
noop
noop
addx 3
addx 2
addx 13
addx 12
addx -15
addx -2
addx 2
addx -11
addx 18
addx 2
addx -15
addx 16
addx 5
addx 2
addx 5
noop
noop
noop
addx 3
addx -2
addx -38
noop
addx 3
addx 4
noop
noop
noop
noop
noop
addx 5
addx 5
noop
noop
addx 21
addx -17
addx 6
noop
noop
noop
noop
addx 5
noop
noop
noop
noop
noop
addx 3
addx 5
addx -38
noop
noop
addx 5
addx -2
addx 1
addx 7
noop
addx 22
addx -18
addx -11
addx 27
addx -13
addx 2
addx 5
addx -8
addx 9
addx 2
noop
addx 7
noop
addx 1
noop
addx -38
noop
addx 2
addx 5
addx -3
noop
addx 8
addx 11
addx -6
noop
addx 24
addx -31
addx 10
addx 2
addx 5
addx 3
noop
addx 2
addx -29
addx 21
addx 11
addx 5
addx -39
addx 4
addx -2
addx 2
addx 7
noop
addx -1
addx 2
noop
addx 4
noop
addx 1
addx 2
addx 5
addx 2
noop
noop
addx -6
addx 9
addx -18
addx 25
addx 3
noop
addx -17
noop)";


vector<string> lines;

int calculate_a(int cycle)
{
	vector<string> subset = vector<string>(lines.begin(), lines.begin() + cycle - 1);
	vector<int> values;
	for (auto line : subset)
	{
		vector<string> words = SplitString(line, ' ');
		if (words.size() == 2)
		{
			values.push_back(atoi(words[1].c_str()));
		}
	}
	auto total = std::accumulate(values.begin(), values.end(), 1);
	total = total * cycle;
	return total;
}
void day10()
{
	string copydata = day10input;
	vector<string> tokensStr = SplitString(copydata, '\n');

	for (int lineindex = 0; lineindex < tokensStr.size(); lineindex++)
	{
		vector<string> words = SplitString(tokensStr[lineindex], ' ');
		if (words[0] == "addx")
		{
			lines.push_back("addx");
		}
		lines.push_back(tokensStr[lineindex]);
	}

	vector<int> cycles{ 20,60,100,140,180,220 };

	int total = 0;
	for (auto cycle : cycles)
	{
		total += calculate_a(cycle);
	}
	cout << total << endl;

	// b
	int x = 1;
	vector<char> crt;
	int currentpix = 0;
	for (auto line : lines)
	{
		vector<string> words = SplitString(line, ' ');
		if (currentpix >= x - 1 && currentpix <= x + 1)
		{
			crt.push_back('#');
		}
		else
		{
			crt.push_back(' ');
		}
		currentpix = (currentpix + 1) % 40;

		// update x in the end
		if (words.size() == 2)
		{
			x += atoi(words[1].c_str());
		}
	}

	for (int row = 0; row < 6; row++)
	{
		string line(crt.begin() + (row * 40), crt.begin() + (row * 40) + 40);
		cout << line << endl;
	}
}

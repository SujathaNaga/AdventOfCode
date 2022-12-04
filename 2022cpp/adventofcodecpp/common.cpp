#include "common.h"
vector<string> SplitString(string str, char delimiter)
{
	vector<string> toks;
	stringstream ss(str);
	string tok;
	while (getline(ss, tok, delimiter))
	{
		toks.push_back(tok);
	}
	return toks;
}

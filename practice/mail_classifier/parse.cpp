#include "parse.hpp"
#include <fstream>
using namespace std;

vector<string>stop_words = {

};

map<string,int> parse(string filepath){
    string key = "!#@$)(*";
    string line;
    ifstream file(filepath);
    int count = 0;
    for

}
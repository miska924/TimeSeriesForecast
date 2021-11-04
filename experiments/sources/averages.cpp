#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <set>

using namespace std;

const int CAREFUL = 1;
double prefSum[100000];

const vector<string> fields = {
    "<TICKER>", "<PER>", "<DATE>", "<TIME>", "<OPEN>", "<HIGH>", "<LOW>", "<CLOSE>", "<VOL>"
};

pair<string, vector<string>> GetSampleLines(ifstream& in) {
    string format;
    in >> format;
    
    vector<string> lines;
    string line;
    while (in >> line) {
        lines.push_back(line);
        cerr << ".";
        cerr.flush();
    }
    cerr << "\nSample size: " << lines.size() << endl;
    return make_pair(format, lines);
}

int GetIndex(const string& str, const string& subStr) {
    int valuePos = 0;
    int iterEnd = 0;
    int iterBegin = 0;
    while (iterEnd <= str.size()) {
        if (iterEnd == str.size() || str[iterEnd] == ';') {
            if (str.substr(iterBegin, iterEnd - iterBegin) == subStr) {
                return valuePos;
            }
            iterBegin = iterEnd + 1;
            valuePos++;
        }
        iterEnd++;
    }
    return -1;
}

string GetValue(const string& str, int pos) {
    int valuePos = 0;
    int iterEnd = 0;
    int iterBegin = 0;
    while (iterEnd <= str.size()) {
        if (iterEnd == str.size() || str[iterEnd] == ';') {
            if (valuePos == pos) {
                return str.substr(iterBegin, iterEnd - iterBegin);
            }
            iterBegin = iterEnd + 1;
            valuePos++;
        }
        iterEnd++;
    }
    return "";
}

vector<double> GetSampleValues(ifstream& in) {
    pair<string, vector<string>> sample = GetSampleLines(in);

    string format = sample.first;
    vector<string> lines = sample.second;
    int valueIndex = GetIndex(format, "<OPEN>");
    if (valueIndex == -1) {
        return vector<double>(0, 0.0);
    }
    vector<double> values;
    for (int i = 0; i < lines.size(); ++i) {
        char* p;
        values.push_back(strtod(GetValue(lines[i], valueIndex).c_str(), &p));
    }
    return values;
}

double GetAvrg(const vector<double> values, int avrg, int index) {
    return (prefSum[index + 1] - prefSum[index - avrg + 1]) / avrg;
    /*if (precalc[index][avrg]) {
        return precalc[index][avrg];
    }
    double sum = 0;
    int cnt = 0;
    for (int i = index; i > max(index - avrg, 0); --i) {
        sum += values[i];
        cnt++;
    }
    return precalc[index][avrg] = sum / cnt;*/
}

int sgn(double x) {
    if (x < 0.0) {
        return -1;
    } else {
        return 1;
    }
}

int main(int argc, char* argv[]) {
    if (argc !=  3) {
        cerr << "Usage example:\n\n   ./averages samples/AFLT.txt 1000\n\nWhere 1000 is your money in rubles" << endl;
        return 0;
    }
    double startMoney = double(atoi(argv[2]));
    cerr << "Start money: " << startMoney << endl;
    
    ifstream in(argv[1]);
   
    vector<double> values = GetSampleValues(in);
    
    double lastLongAvrg = -1;
    double lastShortAvrg = -1;

    vector<double> profits;
    vector<pair<int, int> > periods;
    double bestProfit = -10000;
    pair<int, int> bestPeriods = make_pair(-1, -1);
    int fail = 0;

    for (int i = 1; i < values.size(); ++i) {
        prefSum[i] = prefSum[i - 1] + values[i];
    }

    for (int longPeriod = 30; longPeriod < 31; longPeriod += 5) {
        cerr << longPeriod << "/100" << endl;
        cerr << "Best profit: " << bestProfit << "%\nShort average period: " << bestPeriods.first << "\nLong average period: " << bestPeriods.second << endl;
        for (int shortPeriod = 3; shortPeriod < 4; ++shortPeriod) {
            
            int extremumPeriod = 60 * 3;
            multiset<double> extremumValues;
            
            double money = startMoney;
            int mass = 0;
            double currentMax = startMoney;
            for (int i = 0; i < values.size(); ++i) {
                if (i * 1000 / values.size() != (i + 1) * 1000 / values.size()) {
                    int percents = i * 1000 / values.size();
                    cerr << extremumValues.size() << " " << percents / 100 << percents % 100 / 10 << "." << percents % 10 << "%   " << mass << " " << money << " " << money + values[i] * mass << "   " << endl;
                }
                // cerr << "checkpoint " << i << endl;
                double longAvrg = GetAvrg(values, longPeriod, i);
                double shortAvrg = GetAvrg(values, shortPeriod, i);

                int cntDelta = 0;
                
                if (money + values[i] * mass < currentMax * 0.8) {
                    fail++;
                    cerr << "DEAD ON " << double(i) / values.size() << "%\nPROFIT: " << (values.back() * mass + money - startMoney) * 100 / startMoney << endl;
                    cerr << "CURRENT MAX: " << currentMax << endl;
                    break;
                }    
                /*if (extremumValues.size() == extremumPeriod && values[i] > (*(extremumValues.rbegin()))) {
                    cntDelta = (int((money + values[i] * mass) / values[i]) - mass) / CAREFUL;
                    //cerr << "WOW!" << endl;
                } else if (extremumValues.size() == extremumPeriod && values[i] < (*(extremumValues.begin()))) {
                    cntDelta = -((int((money + values[i] * mass) / values[i]) + mass) / CAREFUL);
                    //cerr << "WOW!" << endl;
                } else */ if (lastLongAvrg != -1 && lastShortAvrg != -1) {
                    if (sgn(lastLongAvrg - lastShortAvrg) == sgn(shortAvrg - longAvrg)) {
                        if (shortAvrg > longAvrg) {
                            cntDelta = (int((money + values[i] * mass) / values[i]) - mass) / CAREFUL;
                            //cerr << "WOW" << endl;
                        } else {
                            cntDelta = -((int((money + values[i] * mass) / values[i]) + mass) / CAREFUL);
                            //cerr << "WOW 1" << endl;
                        }
                    }
                }
                //cerr << mass << " " << cntDelta << "  ::value:: " << values[i] << endl;
                if (cntDelta != 0) {
                    // system("sleep 1");
                }
                money -= values[i] * cntDelta + values[i] * abs(cntDelta) * 0.00025;
                mass += cntDelta;

                currentMax = max(currentMax, money + values[i] * mass);
                /*extremumValues.insert(values[i]);
                if (i - extremumPeriod >= 0) {
                    extremumValues.erase(extremumValues.begin());
                }*/
                lastLongAvrg = longAvrg;
                lastShortAvrg = shortAvrg;
                if (i + 1 == values.size()) {
                    profits.push_back((values.back() * mass + money - startMoney) * 100 / startMoney);
                    periods.push_back(make_pair(shortPeriod, longPeriod));
                    if (bestProfit < profits.back()) {
                        bestProfit = profits.back();
                        bestPeriods = periods.back();
                    }
                }
            }
            // cerr << "Current profit: " << profits.back() << "%\nShort average period: " << periods.back().first << "\nLong average period: " << periods.back().second << endl;
        }
    }
    cerr << "\nBest profit: " << bestProfit << "%\nShort average period: " << bestPeriods.first << "\nLong average period: " << bestPeriods.second << endl;
    cerr << "Fails: " << fail << endl;
    return 0;
}

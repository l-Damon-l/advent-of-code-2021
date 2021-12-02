#include <iostream>
#include <vector>
#include <string>

using namespace std;

int depthIncreases (const vector<int> &depths) {
    const int depthsSize = depths.size();
    int increases = 0;
    for (int i = 0; i < depthsSize - 1; i++) {
        if (depths[i] < depths[i+1]) {
            increases++;
        }
    }
    return increases;
}

int depthIncreasesSlidingWindow(const vector<int> &depths) {
    const int depthsSize = depths.size();
    int increases = 0;
    int prevWindow = (depths[0] + depths[1] + depths[2]);
    for (int i = 2; i < depthsSize - 1; i++) {
        int window = (depths[i-1] + depths[i] + depths[i+1]);
        if (window > prevWindow) {
            increases++;
        }
        prevWindow = window;
    }
    return increases;
}


int main() {

    // get lines from txt file
    vector<int> depths;
    for (string line; getline(std::cin, line);) {
        depths.push_back(stoi(line));
    }
    
    int solution = depthIncreases(depths);
    cout << "First solution: " << solution << endl;

    int solutionTwo = depthIncreasesSlidingWindow(depths);
    cout << "Second solution: "<< solutionTwo << endl;

    return 0;
}

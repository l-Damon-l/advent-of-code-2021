#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> getBinaryStrings() {
    // get lines from txt file
    std::vector<std::string> binaryStrings;
    for (std::string line; std::getline(std::cin, line);) {
        binaryStrings.push_back(line);
    }
    return binaryStrings;
}

std::string getGammaValue(std::vector<std::string>& binaryStrings) {
    std::string gammaVal;
    int numOfZeros = 0;
    int numOfOnes = 0;
    for (int row = 0; row < binaryStrings[0].size(); row++) {
        for (int column = 0; column < binaryStrings.size(); column++) {
            binaryStrings[column][row] == '0' ? numOfZeros++ : numOfOnes++;
        }
        numOfZeros > numOfOnes ? gammaVal.push_back('0')
                               : gammaVal.push_back('1');
        // Reset counts
        numOfZeros = numOfOnes = 0;
    }
    return gammaVal;
}

std::string getEpsilonValueFromGamma(std::string& gamma) {
    std::string epsilonVal;
    for (char bit : gamma) {
        bit == '0' ? epsilonVal.push_back('1') : epsilonVal.push_back('0');
    }
    return epsilonVal;
}

int getPowerConsumptionRate(std::string& gamma, std::string& epsilon) {
    int gammaAsDecimal = std::stoi(gamma, nullptr, 2);
    int epsilonAsDecimal = std::stoi(epsilon, nullptr, 2);
    int powerConsumptionRate = gammaAsDecimal * epsilonAsDecimal;
    return powerConsumptionRate;
}

void printPartOneSolution() {
    std::vector<std::string> binaryStrings = getBinaryStrings();
    std::string gammaVal = getGammaValue(binaryStrings);
    std::string epsilonVal = getEpsilonValueFromGamma(gammaVal);
    int powerConsumptionRate = getPowerConsumptionRate(gammaVal, epsilonVal);
    std::cout << "Solution one: " << powerConsumptionRate << std::endl;
}

int main() { printPartOneSolution(); }

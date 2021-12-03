#include <iostream>
#include <string>
#include <vector>

// get lines from day2_puzzle.txt file as pairs
std::vector<std::pair<std::string, int>> textToPairs()
{
    std::vector<std::pair<std::string, int>> instructions;
    for (std::string line; std::getline(std::cin, line);)
    {
        int spaceIndex = line.find(" ");
        std::string instruction = line.substr(0, spaceIndex);
        int amount = stoi(line.substr(spaceIndex, line.size()));
        std::pair<std::string, int> instructionAndAmount = std::make_pair(instruction, amount);
        instructions.push_back(instructionAndAmount);
    }
    return instructions;
}

class Submarine
{
private:
    int horizontalPos;
    int depth;

public:
    Submarine()
    {
        horizontalPos = 0;
        depth = 0;
    }
    void forward(int amount)
    {
        horizontalPos += amount;
    }
    void down(int amount)
    {
        depth += amount;
    }
    void up(int amount)
    {
        depth -= amount;
    }
    int getHorizontalPosTimesDepth()
    {
        return horizontalPos * depth;
    }
};

class BetterSubmarine
{
private:
    int horizontalPos;
    int depth;
    int aim;

public:
    BetterSubmarine()
    {
        horizontalPos = 0;
        depth = 0;
        aim = 0;
    }
    void forward(int amount)
    {
        horizontalPos += amount;
        depth += (aim * amount);
    }
    void down(int amount)
    {
        aim += amount;
    }
    void up(int amount)
    {
        aim -= amount;
    }
    int getHorizontalPosTimesDepth()
    {
        return horizontalPos * depth;
    }
};

int main()
{
    std::vector<std::pair<std::string, int>> instructions = textToPairs();
    Submarine sub = Submarine();
    BetterSubmarine betterSub = BetterSubmarine();
    for (int i = 0; i < instructions.size(); i++)
    {
        if (instructions[i].first == "forward")
        {
            sub.forward(instructions[i].second);
            betterSub.forward(instructions[i].second);
        }
        if (instructions[i].first == "down")
        {
            sub.down(instructions[i].second);
            betterSub.down(instructions[i].second);
        }
        if (instructions[i].first == "up")
        {
            sub.up(instructions[i].second);
            betterSub.up(instructions[i].second);
        }
    }
    std::cout << "Solution one: " << sub.getHorizontalPosTimesDepth() << std::endl;
    std::cout << "Solution two: " << betterSub.getHorizontalPosTimesDepth() << std::endl;
}

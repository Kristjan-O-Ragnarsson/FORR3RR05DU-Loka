#include <iostream>
#include "LightSegmentTree.h"

using namespace std;

int main() {
    std::cout << "Test" << std::endl;
    int x[4] = {1,2,3,4};
    //cout << sizeof(x) << endl;
    LightSegmentTree l = LightSegmentTree(x, 4);
    return 0;
}
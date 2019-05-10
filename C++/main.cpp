#include <iostream>
#include "LightSegmentTree.h"
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int x[n];
    memset(x, 0, sizeof(x));
    for (int i = 0; i < n; i++){
        cout << x[i] << endl;
    }
    cout << endl;
    LightSegmentTree l = LightSegmentTree(x, n);

    return 0;
}
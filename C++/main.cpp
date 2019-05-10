#include <iostream>
#include "LightSegmentTree.h"
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int x[n];
    memset(x, 0, sizeof(x));
    LightSegmentTree l = LightSegmentTree(x, n);
    for (int i = 0; i < k; i++){
        char command;
        cin >> command;
        if (command == 'F' || command == 'f'){
            int ind;
            cin >> ind;
            l.update(0, 0, n - 1, ind - 1, !l.A[ind - 1]);
        } else {
            int a, b;
            cin >> a >> b;
            cout << l.query(0, 0, n - 1, a - 1, b - 1) << '\n';
        }
    }
    cout << endl;


    return 0;
}
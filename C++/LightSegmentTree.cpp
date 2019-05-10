//
// Created by Lenovo on 19/04/22.
//
#include <bits/stdc++.h>
#include "LightSegmentTree.h"


LightSegmentTree::LightSegmentTree(int X[], int Len) {
    A = X;
    iArr = new STTYPE[4 * Len];
    std::memset(iArr, 0, sizeof(iArr)*4*Len);
    build(1, 0, Len - 1);
    for (int i = 1; i < 16; i++){
        std::cout << iArr[i] << std::endl;
    }
}

LightSegmentTree::~LightSegmentTree() {
    delete []iArr;
}

void LightSegmentTree::build(int ind, int l, int r) {
    if (l == r)
        iArr[ind] = A[l];
    else{
        int mid = (l+r) / 2;
        build(ind *2, l, mid);
        build(ind * 2 + 1, mid +1 , r);
        iArr[ind] = iArr[ind*2] + iArr[ind*2+1];
    }
}

void LightSegmentTree::update(int ind, int l, int r, int idx, int val) {
    if (l == r){

    } else {
        int mid = (l+r) / 2;
        if (idx >= l && idx <= r){
            update(ind * 2, l , mid, idx, val);
        } else {
            update(ind * 2 +1, mid + 1, idx, val);
        }
        iArr[ind] = iArr[ind * 2] +iArr[ind * 2 + 1];
    }
}

int LightSegmentTree::query(int ind, int l, int r, int a, int b) {
    if (r < a || l > b){
        return 0;
    }
    if (l >= a && r <= b){
        return iArr[ind];
    }
    int mid = (l + r) / 2;
    int query1 = query(ind * 2, l, mid, a, b);
    int query2 = query(ind * 2 + 1, mid + 1, r, a, b);
    return query1 + query2;
}


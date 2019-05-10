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
    for (int i = 0; i < Len * 4;i++){
        //std::cout << iArr[i] << std::endl;
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
        build(ind * 2 + 1, l, mid);
        build(ind * 2 + 2, mid +1 , r);
        iArr[ind] = iArr[ind * 2 + 1] + iArr[ind*2 + 2];
    }
}

void LightSegmentTree::update(int ind, int l, int r, int idx, int val) {
    if (l == r){
        iArr[ind] = val;
        A[idx] = val;
    } else {
        int mid = (l+r) / 2;
        if (idx >= l and idx <= mid){
            update(ind * 2 + 1, l , mid, idx, val);
        } else {
            update(ind * 2 + 2, mid + 1, r, idx, val);
        }
        iArr[ind] = iArr[ind * 2 + 1] +iArr[ind * 2 + 2];
    }
}

int LightSegmentTree::query(int ind, int l, int r, int a, int b) {
    if (r < a or l > b){
        return 0;
    }
    if (l >= a and r <= b){
        return iArr[ind];
    }
    int mid = (l + r) / 2;
    int query1 = query(ind * 2 + 1, l, mid, a, b);
    int query2 = query(ind * 2 + 2, mid + 1, r, a, b);
    return query1 + query2;
}


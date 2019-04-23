//
// Created by Lenovo on 19/04/22.
//

#ifndef C_LIGHTSEGMENTTREE_H
#define C_LIGHTSEGMENTTREE_H
#define STTYPE long long

class LightSegmentTree {
public:
    LightSegmentTree(){iArr = new STTYPE[1];}
    LightSegmentTree(int X[], int len);
    ~LightSegmentTree();
    void build(int value, int l, int r);
    void qury();
    void update();

private:
    int *A;
    STTYPE *iArr;
};


#endif //C_LIGHTSEGMENTTREE_H

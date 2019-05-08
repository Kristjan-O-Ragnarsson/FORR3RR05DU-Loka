public class SegmentTree {
    public static void main(Int[] x, int len){
        A = x;
        iArr = new int[len*4-1];
        build(1,0, len - 1);
        for (int i = 1; i < len * 4; i++){

        }
    }
    private static void build(int ind, int l, int r){
        if (l == r){
            iArr[ind] = A[l];
        } else {
            int mid = (l + r) / 2;
            build(ind * 2, l, mid);
            build(ind * 2 + 1, mid, r);
            iArr[ind] = iArr[ind * 2] + iArr[ind*2+1]
        }
    }
}

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
            iArr[ind] = iArr[ind * 2] + iArr[ind*2+1];
        }
    }

    private static void update(int ind, int l, int r, int idx, int val){
        if (l == r){

        } else {
            int mid = (l + r) / 2;
            if (idx >= l && idx <= r){
                update(ind * 2, l, mid, idx, val);
            } else {
                update(ind * 2 + 1, mid + 1, r, idx, val);
            }
            iArr[ind] = iArr[ind * 2] + iArr[ind*2+1];
        }
    }

    private static int query(int ind, int l, int r, int a, int b){
        if (r < a || l > b){
            return 0;
        }
        if (l >= a && r <= b){
            return iArr[ind]
        }
        int mid = (l + r) / 2;
        int query1 = query(ind * 2, l, mid, a, b);
        int query2 = query(ind * 2 + 1, mid, r, a, b);
    }
}

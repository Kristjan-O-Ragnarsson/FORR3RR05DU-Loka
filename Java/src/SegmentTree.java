import java.util.Scanner;


public class SegmentTree {
    static int iArr[];
    //static int A[];
    static int x[];
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String next = sc.nextLine();
	    String nextLineSplit[] = next.split(" ", 0);
	    int n = Integer.parseInt(nextLineSplit[0]);
	    int k = Integer.parseInt(nextLineSplit[1]);
	    x = new int[n];
        //System.out.println(next);
        bu(x, n);
        //for (int i = 0; i<n;i++)
            //System.out.println(x[i]);
        for (int i = 0; i < k; i++){
		    String command = sc.nextLine();
		    String[] cmdList = command.split(" ", 0);
		    //System.out.println(cmdList[0].charAt(0) == 'F');
		    if (cmdList[0].charAt(0) == 'F'){
			    update(1, 0, n - 1, Integer.parseInt(cmdList[1]), (x[Integer.parseInt(cmdList[1])] == 1) ? 0 : 1);
		    }
		    else {
			    System.out.println(query(1, 0, n - 1, Integer.parseInt(cmdList[1]), Integer.parseInt(cmdList[2])));
		    }
        }
    }

    private static void bu(int[] x, int len){
        //int[] A  = x;
        iArr = new int[len*4];
        build(1,0, len - 1);
    }

    private static void build(int ind, int l, int r){
        if (l == r){
            iArr[ind] = x[l];
        } else {
            int mid = (l + r) / 2;
            build(ind * 2, l, mid);
            build(ind * 2 + 1, mid + 1, r);
            iArr[ind] = iArr[ind * 2] + iArr[ind*2+1];
        }
    }

    private static void update(int ind, int l, int r, int idx, int val){
        if (l == r){
            iArr[ind] = val;
            x[idx] = val;
        } else {
            int mid = (l + r) / 2;
            if (idx >= l && idx <= mid){
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
            return iArr[ind];
        }
        int mid = (l + r) / 2;
        int query1 = query(ind * 2, l, mid, a, b);
        int query2 = query(ind * 2 + 1, mid + 1, r, a, b);
	return query1 + query2;
    }

}

"""
Made By Kristjan O. Ragnarsson
github.com/Kristjan-O-Ragnarsson
"""
import math
import sys

class Tree(object):
    """
    The llght version of segment tree
    """
    def __init__(self, _list):
        """
        Time Complexity: O(N)
        init for the Segmet Tree object
        :param _l: List to turn to Segmet tree
        """
        self._len = len(_list)
        self._list = [0] * (self._len * 4)
        self._g_list = _list + _list[:1]
        self.build(1, 0, self._len - 1)
        print self._list[1:]

    def __len__(self):
        """
        For Inbuilt Python len
        :return: Length of the bottom row of the Segment Tree
        """
        return self._len

    def __repr__(self):
        """
        Python inbuilt
        :return: Repr string
        """
        return "{}({})".format(self.__class__.__name__, self._g_list)

    @property
    def get_list(self):
        return self._list[1:]

    @property
    def get_original_list(self):
        return self._g_list

    def build(self, _ind, _l, _r):
        """
        Build function for Segment tree
        Time complexity: O(n)
        :param _ind: Index for the self._list
        :param _l:
        :param _r:
        :return:
        """
        if _l == _r:
            self._list[_ind] = self._g_list[_l]
        else:
            _mid = (_l+_r) / 2
            self.build(_ind * 2, _l, _mid)
            self.build(_ind * 2 + 1, _mid + 1, _r)
            self._list[_ind] = self._list[_ind * 2] + self._list[_ind * 2 + 1]

    def update(self, _ind, _l, _r, idx, _val):
        """

        :param _ind: Index for _list
        :param _l: Left
        :param _r: Right
        :param idx: index for for selecting child
        :param _val: Ralue
        :return: None
        """

        if _l == _r:
            self._list[_ind] = int(_val)
            self._g_list[idx] = int(_val)
        else:
            _mid = (_l+_r) / 2
            if idx >= _l and idx <= _r:
                self.update(_ind * 2, _l, _mid, idx, int(_val))
            else:
                self.update(_ind * 2 + 1, _mid + 1, _r, idx, int(_val))
            self._list[_ind] = self._list[_ind * 2] + self._list[_ind * 2 + 1]

    def query(self, _ind, _l, _r, _a, _b):
        if _l > _b or _r < _a:
            return 0;
        elif _l >= _a and _r <= _b:
            return self._list[_ind];
        else:
            mid = (_l+_r)/2
            query1 = self.query(_ind * 2, _l, mid, _a, _b)
            query2 = self.query(_ind * 2 + 1, mid + 1, _r, _a, _b)
            return query1 + query2; # Change this for diffren query

if __name__ == "__main__":
    x = list(map(int, sys.stdin.readline().strip('\n').split(' ')))
    n = x[0]
    k = int(x[1])
    y = [0] * x[0]
    t = Tree(y)
    for i in range(k):
        cmd = list(map(str, sys.stdin.readline().strip('\n').split(' ')))
        if cmd[0] == 'F':
            print t.get_original_list[int(cmd[1])]
            print int(cmd[1])
            t.update(1, 0, n - 1, int(cmd[1]), not t.get_original_list[int(cmd[1])])
        else:
            sys.stdout.write(str(t.query(1, 0, n - 1, int(cmd[1]), int(cmd[2]))) + '\n')
    



"""
Made By Kristjan O. Ragnarsson
github.com/Kristjan-O-Ragnarsson
"""


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
        self._g_list = _list
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

        :param _ind:
        :param _l:
        :param _r:
        :param idx:
        :param _val:
        :return:
        """

        if _l == _r:
            self._list[_ind] = _val
        else:
            _mid = (_l+_r) / 2
            self.build(_ind * 2, _l, _mid)
            self.build(_ind * 2 + 1, _mid + 1, _r)
            self._list[_ind] = self._list[_ind * 2] + self._list[_ind * 2 + 1]



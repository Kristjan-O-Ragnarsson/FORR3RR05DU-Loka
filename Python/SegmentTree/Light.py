"""
Made By Kristjan O. Ragnarsson
github.com/Kristjan-O-Ragnarsson
"""


class Light(object):
    """
    The llght version of segment tree
    """
    def __init__(self, _list):
        """
        Time Complexity: O(N)
        init for the Segmet Tree object
        :param _l: List to turn to Segmet tree
        """
        self._list = [0] * len(_list)
        self._g_list = _list

    def __len__(self):
        """
        For Inbuilt Python len
        :return: Length of the bottom row of the Segment Tree
        """
        pass

    def __repr__(self):
        """
        Python inbuilt
        :return: Repr string
        """
        return "Light({})".format("Finish Later")  ## !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-! FINISH LATER NOT IMPORTANT

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
            self._g_list[_ind] = self._g_list[_ind * 2] + self._g_list[_ind * 2 + 1]



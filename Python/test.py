"""
Made By Kristjan O. Ragnarsson
github.com/Kristjan-O-Ragnarsson
"""
from sys import stdout, stdin, stderr
import SegmentTree

write, readln, err = stdout.write, stdin.readline, stderr.write

S, I, F, N, W = str, int, float, '\n', ' '


if __name__ == '__main__':
    xl = list((1, 2, 3, 4))
    tree = SegmentTree.Tree(xl)
    print(tree.get_list)
    print repr(tree)
    tree.update()

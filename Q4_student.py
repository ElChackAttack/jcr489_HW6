# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:11:20 2017

@author: Mebius
"""

import random
random.seed(0)

TRI_DEPTH = 5

class Triangle:

    def __init__(self, up_t=None):
        self.up_t = up_t
        self.size = 1 if up_t == None else up_t.get_size() + 1
        self.my_row = [random.randint(0, 20) for i in range(self.size)]
        self.maxsum = []

    def get_size(self):
        return self.size

    def get_maxsum(self):
        #write your code here, and be sure to return what you've done

        return 

def print_triangles(ts):
    for t in ts:
        print(t.my_row)

def print_maxsum(ts):
    for t in ts:
        print(t.maxsum)

def main():
    tri = []
    for i in range(TRI_DEPTH):
        try:
            tri.append(Triangle(tri[i-1]))
        except:
            tri.append(Triangle())

    print("triangle -- ")
    print(tri)
    print_triangles(tri)

    tri[TRI_DEPTH - 1].get_maxsum()
    print("\nmaximum sum -- ");
    print_maxsum(tri)

main()

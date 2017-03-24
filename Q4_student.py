    # -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:11:20 2017

@author: Mebius
"""

import random
random.seed(0)

TRI_DEPTH = 4

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
        maxsum = [0 for i in range(len(self.my_row))]
        if self.get_size() == 1:
            maxsum = self.my_row[:]  
        else:
            temp = self.up_t.get_maxsum()[:]
            temp.extend(self.up_t.get_maxsum())
            for i in range(self.size) :
#           
                to_add = temp[i] + self.my_row[i]
                maxsum[i] = to_add
            print(temp)
        self.maxsum = maxsum
        return self.maxsum
"""
Bruce said this part was redundant

        elif self.get_size() == 2:
            for i in range(2):
                maxsum[i] = self.my_row[i]
        else:
            maxsum[0] = self.up_t.get_maxsum()[:] + self.my_row[0]
            maxsum[-1] = self.up_t.get_maxsum()[-1] + self.my_row[-1]
            for i in range(1,self.size - 1):
                if self.my_row[i] > self.my_row[i+1]:
                    maxsum[i] += self.my_row[i] + (self.up_t.get_maxsum())[i]
                else:
                    maxsum[i] += self.my_row

            self.maxsum = maxsum
"""
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

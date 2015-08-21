'''
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

. . . X . . .
. X . X . . .
. X . X . . X
. X X X . X X
X X X X X X X
1 4 2 5 1 2 3

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

. . . X . . .
. X O X . . .
. X O X O O X
. X X X O X X
X X X X X X X
1 4 2 5 1 2 3

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list, computes the total area of standing water accumulated when water is poured from the top and allowed to run off the sides.

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
'''

def answer(heights):

    totalWater = 0
    left = 0
    length = len(heights)

    if len(heights) < 3:
        return 0

    # start at first column
    while left < length-1:

        print 'starting while loop with left: ', left
        print 'totalWater: ', totalWater

        # from this point till the end
        right = left+1
        for i in range(left+1, length):
            print 'i: ', i
            # if next column is as high or higher than current
            # (definately right side of hutch)
            if heights[i] >= heights[left]:
                # start over at next column
                right = i
                print 'left: ', left
                break

            # if current column is higher than
            if heights[i] > heights[right]:
                right = i
                print 'right: ', right

        # if no more pools of water
        if left == right:
            print 'totalWater: ', totalWater
            return totalWater

        # height of water
        height = min(heights[left], heights[right])

        left += 1
        print 'left: ', left
        while left < right:
            totalWater += height - heights[left]
            left += 1
            print 'left: ', left

        print 'ending while loop with left: ', left
    return totalWater


heights = [1, 4, 2, 5, 2, 3, 1, 2]
print answer(heights)

#       X
#   X . X
#   X . X . x
#   X X X x x . X
# X X X X x X X X
# 1 4 2 5 2 3 1 2
# 0 1 2 3 4 5 6 7

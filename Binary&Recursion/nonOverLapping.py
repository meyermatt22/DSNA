#given an array of integers, return the count of non-overlapping pairs that have the same sum

#[0,1,2,2,1,3,4,0]  --> 3
#pairs are (2,2), (1,3), (4,0)
#[1,2,1,1,2] --> 2
#pairs are (2,1), (1,2)

class Solution(object):

    def nonOver(nums):
        pairs = {}
        for i in range(len(nums)-1):
            pairs[(nums[i], nums[i+1])] = [i, i+1]

        counter = {}
        for key, value in pairs.items():
            sum = pairs[key][0] + pairs[key][1]
            if(counter[sum]):
                counter[sum] += 1
            else:
                counter[sum] = 1

        mostCommon = 0
        for key, value in counter.items():
            
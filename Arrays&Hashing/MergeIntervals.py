# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_int = {
                'start': intervals[i][0],
                'end': intervals[i][1]
            }

            last_int = {
                'start': stack[-1][0],
                'end': stack[-1][1]
            }

            if curr_int['start'] <= last_int['end'] and curr_int['end'] > last_int['end']:
                stack[-1][1] = curr_int['end']
            elif curr_int['start'] > last_int['end']:
                stack.append(intervals[i])

        return stack

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result

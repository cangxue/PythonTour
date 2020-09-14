class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) == 0:
            return []
        for index, item in enumerate(nums):
            for count in range(index + 1, len(nums)):
                if item + nums[count] == target:
                    return [index, count]

    def twoSum1(self, nums, target):
        hashmap = {}
        for index, item in enumerate(nums):
            if item in hashmap:
                return hashmap[item], index
            else:
                hashmap[target - item] = index


solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 13))
print(solution.twoSum1([2, 7, 11, 15], 17))
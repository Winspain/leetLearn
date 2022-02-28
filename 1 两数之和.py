class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = dict()
        for index, value in enumerate(nums):
            diff_value = target - value
            if diff_value not in temp_dict:
                temp_dict[value] = index
            else:
                return [temp_dict[diff_value], index]


if __name__ == '__main__':
    result_list = Solution().twoSum([2, 3, 3], 6)
    pass

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: # if there are less than two numbers 
            return (-1, -1)
        
        number_dict = {} # key: number value: index

        for i in range(len(nums)):# iterate using indexes 
            difference = target - nums[i] # find the difference
            if difference in number_dict: # if the difference exists within the number dictionary
                return (i, number_dict[difference]) # return indices of both values
            number_dict[nums[i]] = i # otherwise add value-index pair to dictionary
        return (-1, -1)

    # Time Complexity: O(N), need to pass through array only once. 
    # Space Complexity: O(1) no extra space needed.
        
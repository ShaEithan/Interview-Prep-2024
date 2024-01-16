class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set() # create an empty set for us 

        for number in nums:
            if number in mySet: # if found duplicate return true 
                return True
            mySet.add(number) # add number to hash set if it's a non duplicate number

        return False
    # Time Complexity: O(N), only need to iterate through the array once.
    # Space Complexity: O(1)
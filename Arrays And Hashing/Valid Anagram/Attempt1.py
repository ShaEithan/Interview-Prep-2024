class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the two strings do not have the same length return false 
            return False

        countS, countT = {}, {} # create a dictionary for each of them 

        for i in range(len(s)): # iterate over each string and get the count for each character
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT # if both dictionaries equal one another then return true
    # Time Complexity: O(N)
    # Space Complexity: O(1)
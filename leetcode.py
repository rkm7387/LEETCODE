# 1:Longest Substring
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left  = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right-left+1)
        return res

# 167:Two Sum II - Input Array Is Sorted
class Solution167:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0 , len(numbers)-1
        while(left<right):
            if (numbers[left] + numbers[right]) > target:
                right = right-1
            elif (numbers[left] + numbers[right]) < target:
                left = left+1
            else:
                return [left+1,right+1]

        return -1

# 128: Longest Consecutive Sequence
class Solution128:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        longest = 1
        st = set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                cnt = 1
                x = it
                while x+1 in st:
                    x = x+1
                    cnt += 1
                longest = max(longest,cnt)
        return longest

# 238: Product of array except self
class Solution238:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i + 1]

        output = []

        for i in range(0,n):
            output.append(left[i] * right [i])

        return output     

# 271: Encode and decode a string
class Solution271:
    def encode(self,strs:list[str]):
        if not strs:
            return chr(256)
        separate = chr(257)
        return separate.join(strs)
    
    def decode(self, s:str):
        if s == chr(258):
            return []
        separate = chr(257)
        return s.split(separate)  
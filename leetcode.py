# 70: Climbing Stairs
class Solution70:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.func(n,dp)

    def func(self,n,dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.func(n-1,dp) + self.func(n-2, dp)
        return dp[n]

# 45: Jump Game 2
class Solution45:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        l, r = 0, 0
        while(r < n-1):
            farthest = 0
            for i in range(l, r+1):
                farthest = max(i+nums[i], farthest)
            l = r + 1
            r = farthest
            jumps += 1
        return jumps

# 5: Longest Pallindrom
class Solution5:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        left,right = 0,0
        for i in range(len(s)):
            len1 = self.checkPallindrom(s,i,i)
            len2 = self.checkPallindrom(s,i,i+1)
            length = max(len1,len2)

            if length > (right - left):
                left = i - (length-1)//2
                right = i + (length)//2
        return s[left:right+1]

    def checkPallindrom(self,s,left,right):
        L,R = left,right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

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
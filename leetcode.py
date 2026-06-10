# 73: Set Matrix Zero
class Solution73:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rowtrack = [0 for _ in range(row)]
        coltrack = [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1
        
        for i in range(row):
            for j in range(col):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0

# 6: zigzag
class Solution6:
    def convert(self, s: str, numRows: int) -> str:
        t = list(range(numRows)) + list(range(numRows-2,0,-1))
        r = [''] * numRows
        for i, char in enumerate(s):
            r[t[i % len(t)]] += char
        return ''.join(r)

# 56: Merge Inteval
class Solution56:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        for i in intervals[1:]:
            if i[0] <= prev[1]:
                prev[1] = max(prev[1],i[1])
            else:
                merged.append(prev)
                prev = i
        merged.append(prev)
        return merged

# 13: Roman to Integer
class Solution13:
    def romanToInt(self, s: str) -> int:
        letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        result = 0
        for i in range(n):
            if i < n - 1 and letters[s[i]] < letters[s[i+1]]:
                result -= letters[s[i]]
            else:
                result += letters[s[i]]
        return result

# 54: Print Spiral Matrix
class Solution54:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])

        top,left = 0,0
        bottom,right = n-1, m-1

        while top <= bottom and left <= right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i  in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans

# 48: Rotate image
class Solution48:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

# 47: Permutation 2
class Solution47:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()

        dfs()
        return res

# 46: Permutation
class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    current.append(nums[i])
                    used[i] = True
                    backtrack(current)
                    used[i] = False
                    current.pop()

        backtrack([])
        return result

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
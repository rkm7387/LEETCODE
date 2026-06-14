# 137: Singel Number II
class Solution:
    def singleNumber137(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(1, n, 3):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        
        return nums[n-1]

# 414: Third Largest
class Solution414:
    def thirdMax(self, nums: List[int]) -> int:
        first,second,third = float('-inf'), float('-inf'), float('-inf')
        
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if num > first:
                third = second
                second = first
                first = num
            
            elif first > num > second:
                third = second
                second = num
            
            elif second > num > third:
                third = num

        return third if third != float('-inf') else first    

# 69: Sqrt(x)
class Solution69:
    def mySqrt(self, x: int) -> int:
        ans = 0
        low,high = 0, x

        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

# 219: Contains Duplicate II
class Solution219:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

# 22. Generate Paranthesis
class Solution22:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0,0)

        return res

# 153:Find Minimum in Rotated Sorted Array
class Solution153:
    def findMin(self, nums: List[int]) -> int:
        low,high = 0, len(nums)-1
        mini = float('inf')

        while low <= high:
            mid = (low + high)//2

            if nums[mid] < nums[high]:
                mini = min(mini, nums[mid])
                high = mid - 1
            else:
                mini = min(mini, nums[low])
                low = mid + 1
        
        return mini
        
# 62: Unique Path
class Solution62:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m-1,n-1,m,n,dp)


    def solve(self,i,j,m,n,dp):
        if i == 0 and j == 0:
            return 1
        
        if i < 0 or  j < 0: 
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        up = self.solve(i-1, j, m, n, dp)
        left = self.solve(i, j-1, m, n, dp)
        dp[i][j] = up + left
        return dp[i][j]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for key,value in nums_dict.items():
            if value == 1:
                return key

# 108: Sorted Array to BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution108:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left > right:
                return None
            mid = (left + right) // 2

            node = TreeNode(val=nums[mid])
            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)

            return node
        
        return helper(0, len(nums)-1)

# 88: Merge Sorted Array
class Solution88:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1] 

# 66. Plus One
class Solution66:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one,i = 1,0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1]

# 17. Letter Combinations of a Phone Number
class Solution17:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curStr + c)

        if digits:
            backtrack(0, "")

        return res
    
# 59: Spiral Matrix 2
class Solution59:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        val = 1

        while left <= right:
            # fill every val in top row
            for c in range(left, right+1):
                mat[top][c] = val
                val += 1
            top += 1

            # fill every val in right col
            for r in range(top, bottom+1):
                mat[r][right] = val
                val += 1
            right -= 1

            # fill every val in bottom row
            for c in range(right, left-1, -1):
                mat[bottom][c] = val
                val += 1
            bottom -= 1

            # fill every val in left col
            for r in range(bottom, top-1, -1):
                mat[r][left] = val
                val += 1
            left += 1

        return mat
  
# 81: Search in Rotated Sorted Array II
class Solution81:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low,high = 0, n-1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
    
# 678: Paranthesis String
class Solution678:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        return self.checkValid(0,0,s,dp)

    def checkValid(self,ind,count,s,dp):
        if count < 0:
            return False
        if ind == len(s):
            return count == 0
        
        if dp[ind][count] != -1:
            return dp[ind][count]

        ans = False

        if s[ind] == '(':
            ans = self.checkValid(ind+1, count+1, s, dp)
        elif s[ind] == ')':
            ans = self.checkValid(ind+1, count-1,s,dp)
        else:
            ans = (self.checkValid(ind + 1, count - 1, s, dp) or 
                   self.checkValid(ind + 1, count, s, dp) or 
                   self.checkValid(ind + 1, count + 1, s, dp))
        dp[ind][count] = ans
        return ans

# 20: Valid Paranthesis
class Solution20:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if (
                    (bracket == ")" and ch == "(")
                    or
                    (bracket == "]" and ch == "[")
                    or
                    (bracket == "}" and ch == "{")):
                    continue
                else:
                    return False
        return len(stack) == 0

# 8: ATOI
class Solution8:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        sign = 1
        index = 0
        result = 0

        while index < n and s[index] == " ":
            index += 1

        if index < n:
            if s[index] == "+":
                sign = 1
                index += 1
            elif s[index] == "-":
                sign = -1
                index += 1
        
        while index < n and s[index].isdigit():
            digit = int(s[index])
            result = (result * 10) + digit
            index += 1
            if result > INT_MAX:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
        
        return result * sign

# 57: Insert Interval
class Solution57:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

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
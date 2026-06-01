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
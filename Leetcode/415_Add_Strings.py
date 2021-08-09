# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        
        while i>=0 or j>=0 or carry>0:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            res += str(carry % 10)
            carry = carry // 10
        return res[::-1]
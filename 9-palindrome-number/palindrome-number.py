class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        reversed_y = y[::-1]
        return y == reversed_y

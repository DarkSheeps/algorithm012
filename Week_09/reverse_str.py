class Solution(object):
    def reverseWords(self, s):
         return " ".join(s[::-1].split(" ")[::-1])

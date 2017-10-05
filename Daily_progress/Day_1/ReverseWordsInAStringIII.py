class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        k = []
        for i in s:
            i = i[::-1]
            k.append(i)
        return ' '.join(k)


ok = Solution()
print(ok.reverseWords("Let's take LeetCode contest"))

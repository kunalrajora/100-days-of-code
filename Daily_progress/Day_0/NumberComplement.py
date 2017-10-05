class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(bin(num)[2:][::-1])
        for i in range(len(num)):
            if num[i] == '1':
                num[i] = '0'
            else:
                num[i] = '1'
        return int(''.join(num[::-1]), 2)

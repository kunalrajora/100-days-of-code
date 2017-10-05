class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numeral_list = list(s)

        num_list = [[mapping[i], -1] for i in numeral_list]
        count = 0
        i = 0
        while(i < len(num_list) - 1):
            if num_list[i] < num_list[i + 1]:
                count += num_list[i + 1][0] - num_list[i][0]
                num_list[i + 1][1] = 1
                num_list[i][1] = 1
                i += 2
            else:
                count += num_list[i][0]
                num_list[i][1] = 1
                i += 1
        if num_list[-1][1] == -1:
            count += num_list[-1][0]
        return count

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        one = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        two = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        three = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'k']
        final = []
        mid = []
        for i in words:
            mid.append(str(i))
        words = mid
        for i in words:
            o1 = 0
            o2 = 0
            o3 = 0
            x = list(set(i.lower()))
            for j in x:
                if j in one:
                    o1 += 1
                if j in two:
                    o2 += 1
                if j in three:
                    o3 += 1
            if o1 == len(x):
                final.append(i)
            if o2 == len(x):
                final.append(i)
            if o3 == len(x):
                final.append(i)
        return final

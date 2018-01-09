class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=""
        if len(strs)==0:
            return pre
        for i in range(len(strs[0])):
            if i>=len(strs[0]):
                return pre
            temp=strs[0][i]
            for j in range(len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=temp:
                    return pre
            pre=pre+temp
        return pre
    
s=Solution()
strs=["abcdefg","abcdefghijk","abcdfghijk","abcef"]
print s.longestCommonPrefix(strs)
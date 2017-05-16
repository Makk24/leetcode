class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lg=len(str(s))
        res=[]
        relres=[]
        for x in range(lg):
            if s[x] in res:
                if len(res)>len(relres):
                    relres=res[:]
                res.pop(0)
                while s[x] in res:
                    res.pop(0)
                res.append(s[x])
            else:
                res.append(s[x])
        if len(res)>len(relres):
            relres=res[:]    
        return len(relres)

if __name__=='__main__':
    a=Solution()
    print(a.lengthOfLongestSubstring('gaeetgdaa'))
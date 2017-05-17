#!c:\python34\python.exe
class Solution(object):
    
    def getResult(self,s):
        l=len(s)
        rel={}
        re=s[0]
        st=''
        if s==s[::-1]:
            return s
        while l>1:
            for x in range(l):
                st=str(st)+s[x]
                if len(st)>1 and st==st[::-1] and len(st)>len(re):
                    re=st
            l=l-1
            s=s[-l:]
            st=''
        return re
    def longestPalindrome(self, s):
        if len(s)==0:
    	    return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue
        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]
if __name__=='__main__':
    a=Solution()
    print(a.longestPalindrome('wreqwrqwerqerqeree'))


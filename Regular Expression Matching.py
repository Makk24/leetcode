#实现与'.'支持的正则表达式匹配.和'*'。
class Solution(object):
    def isMatch(self, s, p):
        return self.helper(s,p,0,0)

    def helper(self,s,p,i,j):
        if j==len(p):
            return i==len(s)
        if j==len(p)-1 or p[j+1]!='*':
            if i==len(s) or s[i]!=p[j] and p[j]!='.': 
                return False
            else:  
                return self.helper(s,p,i+1,j+1)  
        #p.charAt(j+1)=='*'  
        while i<len(s) and (p[j]=='.' or s[i]==p[j]):  
            if self.helper(s,p,i,j+2):  
                return True 
            i=i+1  
        return self.helper(s,p,i,j+2)


if __name__=='__main__':
    a=Solution()
    print(a.isMatch('aaa','a*a'))


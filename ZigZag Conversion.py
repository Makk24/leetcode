class Solution(object):
    def convert(self, s, numRows):
        l=len(s)
        n=int(numRows)
        res=[]
        if l>2 and n>1 and n<l:
            for h in range(n):
                #if h==0 or h==(n-1):
                x=0
                while 1:
                    if (x*(n-1)-h)<=(l-1) and abs(x*(n-1)-h)!=((x-2)*(n-1)+h):
                        res.append(s[abs(x*(n-1)-h)])
                    if (x*(n-1)+h)>(l-1):break
                    if (x*(n-1)+h)<=(l-1) and (x*(n-1)+h)!=abs(x*(n-1)-h):
                        res.append(s[abs(x*(n-1)+h)])
                    x=x+2
                #else:
                #    for x in range(0,l):
                #        if (x*(n-1)+h)>(l-1):continue
                #        str=str+s[x*(n-1)+h]
            return ''.join(res)
        else:
            return s
if __name__=='__main__':
    a=Solution()
    print(a.convert("01234",4))


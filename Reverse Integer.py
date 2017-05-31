class Solution(object):
    def reverse(self, x):
        s= int(str(x)[::-1]) if x>0 else -int(str(abs(x))[::-1])
        return s*(s<2**31 and s>=-2**31)
if __name__=='__main__':
    a=Solution()
    print(a.reverse(-1534236469))
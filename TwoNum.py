class TowNum(object):
    def twonums(self,num,target):
        length=len(num)
        l=num
        for x in range(length):
            for y in range(x+1,length):
                if l[x]+l[y]==target:
                    return [x,y]

if __name__=='__main__':
    a=TowNum()
    print(a.twonums([4,3,4,5],8))
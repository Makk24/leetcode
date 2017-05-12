import sys


class Median(object):
    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j - 1]
                elif j == 0: max_of_left = A[i - 1]
                else: max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    def myown(self, A, B):
        l1 = len(A)
        l2 = len(B)
        l = l1 + l2
        k = l // 2
        if l % 2 == 0:
            return (self.findnum1(A, 0, B, 0, k) + self.findnum1(
                A, 0, B, 0, k + 1)) / 2
        else:
            return self.findnum1(A, 0, B, 0, k + 1)
    #递归实现
    def findnum(self, num1, i1, num2, i2, key):
        if i1 >= len(num1):
            return num2[key - 1 + i2]
        if i2 >= len(num2):
            return num1[key - 1 + i1]
        if key == 1:
            return min(num1[i1], num2[i2])

        k1 = sys.maxsize if (key//2 - 1 + i1) >= len(num1) else num1[key//2  - 1 + i1]
        k2 = sys.maxsize if (key//2  - 1 + i2) >= len(num2) else num2[key//2  - 1 + i2]
        if k1 < k2:
            return self.findnum(num1, i1 + key // 2, num2, i2, key - key // 2)
        else:
            return self.findnum(num1, i1, num2, i2 + key // 2, key - key // 2)
    #循环
    def findnum1(self, num1, i1, num2, i2, key):
        
        while key>1:
            if i1 >= len(num1):
                return num2[key-1  + i2]
            if i2 >= len(num2):
                return num1[key-1  + i1]
            k1 = sys.maxsize if (key//2 - 1 + i1) >= len(num1) else num1[key//2- 1   + i1]
            k2 = sys.maxsize if (key//2- 1   + i2) >= len(num2) else num2[key//2 - 1  + i2]
            if k1 < k2:
                i1,key=i1 + key // 2, key - key // 2
            else:
                i2,key=i2 + key // 2, key - key // 2
        if i1 >= len(num1):
            return num2[key- 1  + i2]
        if i2 >= len(num2):
            return num1[key- 1  + i1]   
        return min(num1[i1], num2[i2])
if __name__ == '__main__':
    a = Median()
    print(a.median([1,2], [3,4]))
    print(a.myown([1,2], [3,4]))

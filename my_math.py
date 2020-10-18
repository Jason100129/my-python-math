import math
class my_math:
    pi = 3.141592653589793
    e = 2.718281828459045
    def ceil(self, x):
        if x == int(x):
            return x
        else:
            x += int(x) - x + 1
            return int(x)
    def floor(self, x):
        x = x//1
        return int(x)
    def pow(self, x, y):
        for i in range(y-1):
            x *= x
        
Math = my_math()
print(Math.pow(3, 2))

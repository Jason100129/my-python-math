e = 2.718281828459045
pi = 3.141592653589793

class my_math:
    global e
    global pi
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
        return x**y
    def exp(self, x):
        return e**x
    def expm1(self, x):
        return e**x-1
    def fabs(self, x):
        if x > 0:
            return float(x)
        elif x < 0:
            x = 0 - x
            return float(x)
        else:
            return 0
    def ldexp(self, x, i):
        return float(x*(2**i))
    def radians(self, x):
        return float(x/180*pi)
    
if __name__ == '__main__':
    math = my_math()





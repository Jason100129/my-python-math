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
    def isnan(self, x):
        if x != x:
            return True
        else:
            return False
    def isinf(self, x):
        if x - x != x - x:
            return True
        else:
            return False
    def isfinite(self, x):
        if x - x != x - x:
            return False
        else:
            return True
    def gcd(self, x, y):
        if x < y:
            i = x
            while i >= 1:
                if x%i == 0 and y%i == 0:
                    return i
                i -= 1
        else:
            i = y
            while i >= 1:
                if x%i == 0 and y%i == 0:
                    return i
                i -= 1
    def trunc(self, x):
        return x.__trunc__()
               
    
if __name__ == '__main__':
    math = my_math()





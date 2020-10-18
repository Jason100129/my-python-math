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
if __name__ == '__name__':
    math = my_math()





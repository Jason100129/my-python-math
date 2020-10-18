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
        
math = my_math()

#未完成

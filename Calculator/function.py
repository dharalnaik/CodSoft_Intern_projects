import math

class Function:
    def add(self, n1, n2):        #to add
        return n1 + n2
        
    def subtract(self, n1, n2):   #to subtract
        return n1 - n2
        
    def multiply(self, n1, n2):   #to multiply
        return n1 * n2
    
    def divide(self, n1, n2):     #to divide
        return n1 / n2
    
    def square_root(self, n):     #to find square root
        return math.sqrt(n)
    
    def cube_root(self, n):       #to find cube root
        return round((n**(1/3)), 0)
    
    def power(self, n1, n2):      #to find power
        return math.pow(n1, n2)
    
    def sin_func(self, n):        #to find sin function
        return math.sin(n)
    
    def cos_func(self, n):        #to find cos function
        return math.cos(n)
    
    def tan_func(self, n):        #to find tan function
        return math.tan(n)
    
    def square(self, n):          #to find square
        return n**2
    
    def cube(self, n):            #to find cube
        return n**3
    
    def exponent_2(self, n):      #to find exponent of base 2
        return 2**n
    
    def modulus(self, n1, n2):    #to find modulus
        return n1 % n2
    
    def plus_minus(self, n):      #to change sign
        if n>0:
            n = -n
        else:
            n = -(n)
        return n
    





class Funzione:

    def __init__(self,f):
        self.f=f
    
    def eval(self,x):
        return self.f(x)

    def integrale(self,a,b,m):
        h=(b-a)/m
        sum=0
        for i in range (0,m):
            variabile=a+i*h
            sum+=self.eval(variabile)

        return sum*h

# class Funz(Funzione):
#     def eval(self,x):
#         return (x**2)-(2*x)
        
#f=lambda x: (x**2)-(2*x)
def f(x):
    return (x**2)-(2*x)



obj=Funzione(f)
print(obj.integrale(0,5,1000))
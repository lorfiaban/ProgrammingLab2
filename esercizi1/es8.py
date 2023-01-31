class Funzione:
    def eval(self,x):
        return x+1

    def integrale(self,a,b,m):
        h=(b-a)/m
        sum=0
        for i in range (0,m):
            variabile=a+i*h
            sum+=self.eval(variabile)

        return sum*h

class Funz(Funzione):
    def eval(self,x):
        return (x**2)-(2*x)


obj=Funz()
print(obj.integrale(0,5,1000))
class Funzione():

    def __init__(self):
        pass

    def eval(self):
        pass

    def stampa(self,a,b):
        for i in range(a,b+1):
            val=int(self.eval(i))
            for j in range(1,val+1):
                if i==0: print("-", end="")
                else: print(" ", end="")
            if val<0: print("")
            else: print("+")
            

            



class Retta(Funzione):

    def __init__(self,m,q):
        super().__init__
        self.m=m
        self.q=q

    def eval(self,x):
        super().eval()
        return self.m*x+self.q

class Parabola(Funzione):

    def __init__(self,a,b,c):
        super().__init__()
        self.a=a
        self.b=b
        self.c=c

    def eval(self,x):
        super().eval()
        # if x<0:
        #     minx=-x
        #     return self.a*(minx**2)+self.b*x+self.c
        return self.a*(x**2)+self.b*x+self.c


parabola=Parabola(0.5,-4,7)
retta=Retta(2,33)
parabola.stampa(-10,15)
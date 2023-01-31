class Funzioni():

    def eval(self):
        pass

    def pendenza(self,a,b):
        if not a<b:
            ap=a
            a=b
            b=ap
        difX=b-a
        difY=self.eval(b)-self.eval(a)
        return difY/difX

    def valore_medio(self,a,b):
        if not a<b:
            ap=a
            a=b
            b=ap
        return (self.eval(b)+self.eval(a))/2

class Retta(Funzioni):

    def __init__(self,m,q):
        self.m=m
        self.q=q

    def eval(self,x):
        super().eval()
        return self.m*x+self.q

class Parabola(Funzioni):

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def eval(self,x):
        super().eval()
        return self.a*(x**2)+self.b*x+self.c





parabola=Parabola(5,2,3)
print(parabola.eval(6))
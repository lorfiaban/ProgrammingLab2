class Forma:
    
    def __init__(self,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3

    def periemtro(self):
        pass
    def area(self):
        pass



class Triangolo(Forma):

    def __init__(self,l1,l2,l3):
        super().__init__(l1,l2,l3)

    def tipo(self):
        if self.l1==self.l2 and self.l2==self.l3:
            print('equilatero')
            pass
        else:
            if self.l1==self.l2 or self.l2==self.l3 or self.l1==self.l3:
                print('isoscele')
                pass
            else:
                print('scaleno')

    def perimetro(self):
        return self.l1+self.l2+self.l3

    # def area(self):
    #     return 



class Rettangolo(Forma):

    def __init__(self,l1,l2):
        super().__init__(l1,l2,None)

    def tipo(self):
        if self.l1==self.l2:
            print('quadrato')
        else:
            print('rettangolo')

    def perimetro(self):
        return 2*(self.l1+self.l2)

    def area(self):
        return self.l1*self.l2



class Cerchio(Forma):

  
    def __init__(self,l1):
        super().__init__(l1,None,None)

    def perimetro(self):
        return 2*3.14*self.l1

    def area(self):
        return 3.14*(self.l1**2)




try:
    cer=Rettangolo(2,12)
    print(cer.area())
except Exception as e:
    print('errore: {}'.format(e))

    
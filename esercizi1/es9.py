class Viaggi():
    # def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio):
    #     self.nome_viaggio=nome_viaggio
    #     self.data_partenza=data_partenza
    #     self.data_ritorno=data_ritorno
    #     self.localita=localita
    #     self.resort=resort
    #     self.prezzo=prezzo
    #     self.partecipanti=partecipanti
    #     self.responsabile_viaggio=responsabile_viaggio
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def stampa():
        pass

    def periodo(self):
        elements=self.a.split('/')
        mese=float(elements[1])
        elements_fine=self.b.split('/')
        mese_fine=float(elements_fine[1])
        giorni_da_mesi=0
        for i in range(mese+1,mese_fine):
            if i%2==0: giorni_da_mesi+=30
            if i%2!=0: giorni_da_mesi+=31
        
        
        

class ViaggiInvernali(Viaggi):
    def __init__(self, a, b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d

    def stampa(self):
        print(self.a, self.b, self.c, self.d)

class ViaggiEstivi(Viaggi):
    def __init__(self,a,b,e,f):
        super().__init__(a,b)
        self.e=e
        self.f=f

    def stampa(self):
        print(self.a, self.b, self.e, self.f)






obj=ViaggiInvernali('12/2/2333','2/6/2333',2,3)
print(obj.stampa())
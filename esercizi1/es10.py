class Primi():
    def __init__(self,fine):
        self.fine=fine
        self.counter=1
        self.n=2

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter>self.fine:
            raise StopIteration
       # print('StO ANALIZZANDO {}'.format(self.n))
        
        x=self.n
        flag=False
        prova=self.n+1
        while flag==False:
            #per ogni prova devo vedere se eè primo, se lo è faccio self.n=prova e flag=True
            trovatodivisore=False
            i=2
            while trovatodivisore==False and i<prova:
                if prova%i==0:
                    trovatodivisore=True
                i+=1
            if i>=prova:
                flag=True
                self.n=prova
            prova+=1
        self.counter+=1
        return x

obj=Primi(10)
my_iter=iter(obj)
#print(next(my_iter))
for x in my_iter:
    print(x)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
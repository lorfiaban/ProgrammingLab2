class ExamException(Exception):
    pass

# raise ExamException('errore,')

class MovingAvarage():

    def __init__(self,lunghezza):
        self.lunghezza=lunghezza
    
    def compute(self,data):
        if len(data)<1:
            raise ExamException('la lista è vuota. impossibile calcolare alcuna media')
        if len(data)<self.lunghezza:
            raise ExamException('errore: lunghezza della finestra è maggiore della lunghezza della lista')
        
        if isinstance(self.lunghezza,float):
            self.lunghezza=int(self.lunghezza)
        if not isinstance(self.lunghezza,int):
            raise ExamException('la lunghezza della finestra non è un valore numerico. nun se po fa')
        try:
            lista_mediata=[]
            for i in range (self.lunghezza-1,len(data)):
                sum_elem=0
            #print('stiamo provando {}'.format(data[i]))
                for j in range(i-(self.lunghezza-1),i+1):
                    if not isinstance(data[j],float) and not isinstance(data[j],int):
                        raise ExamException('alcuni valori della lista non sono valori numerici')
                    sum_elem+=data[j]
                media_mob_parziale=sum_elem/self.lunghezza
                lista_mediata.append(media_mob_parziale)
            #print('sum_elem è {}'.format(sum_elem))
            #print('    la sua media è {}'.format(media_mob_parziale))
            return (lista_mediata)
        except:
            raise ExamException('errore di qualche sorta, boh non so quale sia')

moving_avarage=MovingAvarage(10)
result=moving_avarage.compute([])
print(result)
# lista=['a','v',6]
# print(len(lista))
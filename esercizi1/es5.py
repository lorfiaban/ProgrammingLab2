# class CSVfile():

#     def __init__(self, file_name):
#         if not isinstance(file_name, str):
#             raise Exception('no s è una stringa')
#         self.name=file_name

#     def data():
#         return(True)



class Model():

   # def __init__(self)
    
    def fit(self, data):
        #non è implementata, pk?
        raise NotImplementedError('metodo non implementato')
        

    def Predict(self, data):
        raise NotImplementedError('metodo non implementato')


class IncrementModel(Model):
    
    def predict(self, data):
        for i in range (0,len(data)):
            data[i]=float(data[i])
        if isinstance(data, str):
            raise Exception('l\'input è una stringa, e non va bene.coglione!!')
        try:
            sum_dif=0
            counter=0
            #for i,item in enumerate(data):
            for i in range (len(data)-3, len(data)):
            #for i in range(1,len(data))
                if i>len(data)-3:
                    dif=data[i]-data[i-1]
                    sum_dif+=dif
                    counter+=1
            incr_medio=sum_dif/counter

            prediction=data[-1]+incr_medio
            #print('la predizione di predict è {}'.format(prediction))
            return prediction
        except Exception as e:
            print('errore {}'.format(e))
            pass

    def eval(self,a,data):
        media_scarti1=0
        for i in range(a,len(data)+1):
            x=slice(0,i)
            new_data=data[x]
            pred=self.predict(new_data)
            effettivo=data[a+1]
            scarto=abs(pred-effettivo)
            media_scarti1=media_scarti1+scarto
        media_scarti=media_scarti1/(len(data)-a)
        print('è stata ritornata la media degli scarti. è {}.format(meda_scarti)')
        return media_scarti

class FitIncrementModel(IncrementModel):


    def fit_predict(self, data):   
        for i in range (0,len(data)):
            data[i]=float(data[i]) 
        sumdif=0
        counter=0
        for i in range (0,len(data)-3):
            if i>0:
                dif=data[i]-data[i-1]
                counter=counter+1
                sumdif+=dif
        sumdif=sumdif/counter
        #print('l incremento medio in fit è {}'.format(sumdif))
        predizione=self.predict(data)
        n=predizione-data[-1]
        #print('predict in fit è {}, fixato è {}'.format(predizione,n))
        ris=data[-1]+(sumdif+n)/2
        return ris
        


            

ogg=IncrementModel()
listt=[8,19,31,41,50.0, 52, 60]
ris=ogg.eval(3,listt)
print('{}'.format(ris))
#print(obj.fit(listt))


# from matplotlib import pyplot
# payplot.plot
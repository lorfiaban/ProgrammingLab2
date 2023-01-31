class CSVfile():
    
    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise Exception('no s\'è una stringa')
        self.name=file_name  
        
    def __str__(self):
        return str(self.name)
    
    def get_data(self):
        try:
            my_file=open(self.name,'r')
            lista=[]
            c=0
            for line in my_file:
                line=line[:-1]
                if c!=0:
                    elements=line.split(',')
                    elements[-1]=float(elements[-1])
                    #del elements[1]
                   
                #elements[-1]=elements[-1][:-1]
                #elements.pop(-1)
                    lista.append(elements)
                c+=1
            #print(lista)
            my_file.close()
            return(lista)
        except Exception as e:
            print('hhherrore {}'.format(e))
            pass
        




myfile=CSVfile('shampoo_sales.csv')
print(myfile.name)
l=myfile.get_data()
print(l)
#print('{}'.format(l))

#my_fie=open('shampoo_sales.csw','r')
#pippo=get_data(my_fie)
#print(myfile.lista)
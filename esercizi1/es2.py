
def sum_list(list):
    somma=0
    if len(list)==0:
        return(None)
    else:
        for item in(list):
            somma=somma+item
        return(somma)


list=[]
som=sum_list(list)
print('{}'.format(som))
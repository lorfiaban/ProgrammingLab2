
def sum_list(list):
    somma=0
    for item in(list):
        somma=somma+item
    return(somma)


list=[]
som=sum_list(list)
if len(list)==0:
    print('none')
else:
    print('{}'.format(som))






def mean(lista):
    sum=0
    for element in lista:
        sum+=element
    return sum/len(lista)

def dev_stan(lista, mean):
    sum=0
    for element in lista:
        sum+=(element-mean)**2
    return (sum/len(lista))**0.5



lista=[1,4,8,12,6,0,-2]
print(mean(lista))
print(dev_stan(lista,mean(lista)))

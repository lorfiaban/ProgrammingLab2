def sum_csv(file_name):
    #my_file=open(file_name,'r')
    sum=0
    for line in file_name:
        elements=line.split(',')
        if elements[0] != 'Date':
            value=float(elements[1])
            sum=sum+value
    return(sum)


my_file=open('shampoo_sales.csv', 'r')
pippo=sum_csv(my_file)
print('{}'.format(pippo))
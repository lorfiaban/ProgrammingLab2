def sum_csv(my_file):
    sum=0
    for line in my_file:
        elements=line.split(',')
        if elements[1] != 'Date' and elements[1] != 'Sales\n':
            value=float(elements[1])
            sum=sum+value
    return(sum)


#my_file=open('shampoo_sales.csv','r')
#print('{}'.format(sum_csv(my_file)))
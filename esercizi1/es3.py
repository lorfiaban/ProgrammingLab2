def sum_csv(file_name):
    sum=0
    for line in file_name:
        elements=line.split(',')
        #if elements[0] != 'date':
        value=float(elements[0])
        sum=sum+value
       # else:
        #    value=float(elements[1])
         #   sum=sum+value
    return(sum)
# f=67
# ty=type(f)
# stri='ciao'
# #print(type(ty))
# if not isinstance(stri,ty)
#     print('non va ben')
# else:
#     print('è una stringa')

stri='12, 23    , 34'

stri=stri.replace(' ','')
ris=stri.split(',')
for i in range(0,len(ris)):
    ris[i]=float(ris[i])
stre=[2,   6, 4   ]
#y=[stre[i]*3 for i in range(0,len(stre))]
y=[el**0.5 for el in stre]
#y=list(map(fun,stre))  applicare funzioni a tutti gli el di una lista
print(y)
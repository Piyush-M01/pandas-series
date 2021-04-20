import pandas as pd
#lst=[2,64,32,5]
#lst={"name":"Piyush","class":"fail","coder":"Jo kam hoti nahi woh karte hi q ho"}
#lst1=pd.Series(lst)
#print(lst1)

#reading data from a csv file
#pd.read_csv('')
#to remove header
#print(pd.read_csv('100 Sales Records.csv',header=None,squeeze=True))
s=pd.read_csv('100 Sales Records.csv',squeeze=True,usecols=['Country'])
#print(s.index)
#print(s.is_unique)
#print(s.add_prefix("Panda "))
#print(s.add_suffix(" Panda "))

#mathematics
print(max(s))

#label indexing

temp=[30,40,50,60,70,80,90]
mon=['jan','feb','march','april','may','june','july']
s1=pd.Series(temp,mon)
#print(s1)

#to sort values

#print(s1.sort_values(ascending=False))
lst=list(s1)
dict=dict(s1)
#print(lst)
#print(dict)

#print(s1[0])
print(s1[[2,4,6]])

#no of times each value is  there
print(s1.value_counts())

#converting temp
def convert(temp):
    return ((temp*1.8)+32)
c=s1.apply(convert)
print(c)

#map
mapobj={30:300,40:400,50:500,60:600}
print(s1.map(mapobj))
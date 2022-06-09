#if there are i=5, j=5, k=5 then i=j=k because this is immutable and it fetches less space or storage 
# than the mutable. 

#Tuple
#it holds the collection of values that is immutable

#a=()
#b=tuple()
#print(type(a)), type(b))

#a=('sun', 'mon', 'tue','wed')
#print(a)

#a=('sun', 'mon', 1, 1.1, True)
#print(a)
#print(a[0])

#Tuple is heterogenous
#Tuple is faster than List

#a=('sun', 'mon', 'tue', 'wed', 'thurs', 'fri', 'sat')
#print(a[0:7:2])
#print(a[::2])

#We cannot delete or remove or add or insert values in tuple

#[] List is mutable i.e it changes
#() Tuple is immutable i.e it does not change


#a=[1]
#print(type(a))

#a=('umesh')
#print(type(a))

#a=('umesh',)
#print(type(a))

#a=set()
#a={}
#a={1,2,3,4,5,6,7}
#a={1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5}
#print(type(a))
#print(a)

#a={'Umseh',1, 1.1,True}
#print(a)

#del(a[0])
#print(a)

#a.add('ram')
#print(a)

#a.remove('ram')
#print(a)

#a.discard(1)
#print(a)

#a.clear()
#print(a)

#a={'ram','umesh','shyam'}
#b={'sita','rita','gita','umesh'}
#print(a.union(b))
#print(a.intersection(b))
#print(b.difference(a))    #gives the value which is in 'b' only. 

#List is mutable (It changes the value or it may add or remove values)
#Tuple is immutable (It doesnot changes the value)

#a=[1,2,3,4,5,6,7,8,9]
#print(tuple(a))
#print(set(a))

#a={1,2,3,4,5,6,7,8,9}
#print(list(a))
#print(tuple(a))

#account_type = ('fixed', 'saving', 'current')
#temp = list(account_type)
#temp.append('nari bachat khata')
#temp = tuple(temp)
#account_type = temp

#a=['umesh','satkar','shishir','bryan']
#b=['bhawana','niraj','bryan','umesh']
#print(set(a+b))

#a=['umesh','satkar','shishir']
#a.insert(0, 'ram')
#a.insert(4, 'shyam')
#a.insert(5, 'hari')
#a.append('bharat')
#a.append('charan')
#print(a)
#print(tuple(a))





























#list method practice question
#Q1.create list 3 numbers and and append 99.
number=[10,20,30,]
number.append(99)
print(number)
#Q2.insert 50at index 2
number.insert(2,50)
print(number)
#Q3.merge two list [1,2]and [3,4]
list1=[1,2]
list2=[3,4]
list1.extend(list2)
print(list1)
#remove the number 10
number.remove(10)
print(number)
#pop method
animal=['tiger','lion']
animal.pop(0)
print(animal)
#clear method
animal.clear()
print(animal)
#index
name=['sushant','rahul','sandip']
index=name.index('rahul')
print(index)
#sort
count=[4,2,9,1,]
desceding=sorted(count,reverse=True)
print(desceding)
count.reverse()#reverse
print(count)
count.copy()#copy
print(count)
#count tuples
car=('scropio','mahindra','marcides','jebegurn','mahindra')
counts=car.count('mahindra')
print(counts)
#index couple
find=car.index('mahindra')
print(find)
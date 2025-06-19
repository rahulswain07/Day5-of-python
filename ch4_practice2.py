#Q1.create a list of 5 intiger and print the sum.
int=[5,25,50,100,150]
total=sum(int)
print(total)
#Q2.Add an item to the list using append()
family=['amiya swain','anuswaya swain','sumitra swain']
family.append('rahul swain')#append mean add item to end
print(family)
#Q3.insert a number at index 2 
number=[1,2,4]
number.insert(2,3)#insert 3 index 2
print(number)
#Q4.remove the number 10
number1=[10,20,30,40,]
number1.remove(10)
print(number1)
#Q5.Reverse a list 
list=[10,20,30,40,50,]
list.reverse()
print(list)
#Q6.count How many times number 3 this list
list1=[1,3,3,4,3,5]
counts=list1.count(3)
print(counts)
#Q7.sort a list in desceding order
list2=[1,2,3,4,5,6,7,8,9]
list2.sort(reverse=True)
print(list2)
#practice question tuple
#Q1.create a tuple of 4 element and print each element using loop
tuple=('apple','banana','cherry','orange')
#print each element using loop
for item in tuple:
    print(item)
#Q2.find the index of an element in a tuple
element=('car','bike','mobile','house')
find=element.index('bike')
print(find)
#Q3.count the number of times value appears in a tuple 
value=(10,20,20,30,40,50,30,20,20)
counts=value.count(20)
print(counts)
# Q4. Convert this tuple to list
phones = ('vivo', 'oppo', 'mi', 'poco')
convert=list(phones)
print(convert)
#Q. create a tuple of fruties print the second
fruties1=('apple','mango','orange','banana')
print(fruties1[1])

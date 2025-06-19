#Q1.create a list 0f 
numbers=[1,2,3,4,5,6,7,8]
print(numbers)
#Q2.add a new number to the list
numbers.append(9)
print(numbers)
#Q3.change the second element 25
numbers[1]=25
print(numbers)
#Q4.create a tupple 0f 3 strings and print it
my_tupple=('tiger','lion','dog')
print(my_tupple)
#Q6.sort a list in descending order.
marks=[88,92,75,60,99]
marks.sort(reverse=True)
print(marks)
#Q7.count How many times an item appears in list
fruties=['apple','banana','apple','orange']
print(fruties.count('apple'))
#Q8.convert list to tupple
list1=[1,2,3]
tuple1=tuple(list1)
print(tuple1)
#Q9.Get the last element of a tuple
element=(10,20,30,40)
print(element[-1])
#Q9.check if an item exist in tuple
print(40 in element)
#Q10.Remove duplicate from a list
nums=[1,2,2,3,4,4,5]
unique_nums=list(set(nums))
print(unique_nums)
#11.combine two tuple 
t1=(20,20)
t2=(20,20)
combine=t1+t2
print(combine)
#slice a list
l=[10,20,30,40,50]
t=(40,60,80,90)
print(l[1:4])
print(t[:2])
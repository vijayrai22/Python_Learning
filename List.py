numbers= [5,2,1,7,4,5,6,3,2,7]
unique= []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

#list operations:
# numbers= [5,2,1,7,4,5]
# numbers.append(20) #to append any number in last
# numbers.insert(0,10) #to to insert any number at given index
# numbers.remove(5) #to remove any specified number
# numbers.clear()  #to remove all the numbers from the list
# numbers.pop() #to remove number from last
# print(numbers.index(1)) # to find the index of given number
# print(50 in numbers) #to find whether the given number is present or not it gives boolean value
# print(numbers.count(5)) #to find the count or how many times the number is present
# numbers.sort() # to sort the list ascending order
# numbers.reverse() # to sort the list in descending order
# numbers2= numbers.copy() #to copy the value into another list
# numbers.append(10)
# print(numbers2)
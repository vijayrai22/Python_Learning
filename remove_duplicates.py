numbers= [5,2,1,7,4,5,6,3,2,7]
unique= []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
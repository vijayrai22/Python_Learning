numbers= [5,2,5,2,2]
# for i in numbers:
#         print(i*"X")
#using inner loop
for i in numbers:
        output=''
        for j in range(i):
                output+= 'x'
        print(output)
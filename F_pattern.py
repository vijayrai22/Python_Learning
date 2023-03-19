numbers= [5,2,5,2,2]
# for i in numbers:
#         print(i*"X")
#using inner loop
for i in numbers:
        output=''
        for j in range(i):
                output+= 'x'
        print(output)

#L pattern
# num= [2,2,2,2,5]
# for i in num:
#         output= ''
#         for j in range(i):
#                 output +='*'
#         print(output)
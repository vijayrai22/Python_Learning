#Random Variable

# import random
# for i in range(3):
#     print(random.randint(10,20))
# members= ['john', 'Mary', 'Bob', 'Mosh']
# leader= random.choice(members) # randomly pick one name
# print(leader)
import random
class dice:
    def roll(self):
        first= random.randint(1,6)
        second= random.randint(1,6)
        return (first,second)
#in python to return any tople there is no need of parentesis we can simply return first,second
Dice=dice()
print(Dice.roll())
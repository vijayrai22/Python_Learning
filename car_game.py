command= ''
count_start =0
count_stop =0
while True:
    command = input('>').lower()
    if command == 'start':
        if count_start == 0:
            print('The car started...')
            count_start +=1
        else:
            print('the car is already started')
    elif command == 'stop':
        if count_stop == 0:
            print('the car stopped')
            count_stop += 1
        else:
            print('the car is already stopped')
    elif command == 'help':
        print('''
Start - to start the car
stop - to stop the car
quit - to quit''')
    elif command == 'quit':
        break
    else:
        print("sorry i don't understand")

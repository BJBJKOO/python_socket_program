#17011824_구범준 서버용
import random
from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
count=0##Sets the variable
serverSocket.listen(1)
sample=0##Sets the variable
t=0#Sets the variable
q=0#Sets the variable
print('The server is ready to receive a game request.')
str_num=0#Sets the variable
ball_num=0#Sets the variable
while True:
    connectionSocket, addr = serverSocket.accept()
    message=connectionSocket.recv(2048).decode()
    if (message[0] == 'M' and message[1] == 'A'):#If the message starts with MA
        print('From Client: game_request')
        modifiedMessage = 'MBgame_grant'#make message
        connectionSocket.send(modifiedMessage.encode())
        print('To Client:game_grant')

        all_list = []

        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Store numbers in list in str format
        for i1 in num:  # The process of creating all combinations of numbers.
            for i2 in num:
                if i2 != i1:
                    for i3 in num:
                        if i3 != i1 and i3 != i2:
                            for i4 in num:
                                if i4 != i1 and i4 != i2 and i4 != i3:
                                    all_list.append(i1 + i2 + i3 + i4)


        get_list = list(all_list)  # Generate List
        while True:  # Generate Target Number
            a = random.choice(num)
            b = random.choice(num)
            c = random.choice(num)
            d = random.choice(num)
            if a == b or a == c or a == d or b == c or b == d or c == d:  # If there's a duplicate number, it's over.
                pass
            else:
                target = a + b + c + d  # Otherwise, set target
                break
        print("Answer:" + target)

        while True:
            if count==0:#start first
                sample = random.choice(get_list)#Randomly generate numbers to fit
                message = connectionSocket.recv(2048).decode()
                print('From Client:'+message[2:])
                x=message[3]+message[6]+message[9]+message[12]#Getting information from a message
                str_num = 0
                ball_num = 0
                for i in range(4):  # Determine the number of balls and strikes
                    for j in range(4):
                        if target[i] == x[j] and i == j:  ## If Strike
                            str_num += 1
                        if target[i] == x[j] and i != j:  # If ball
                            ball_num += 1
                message='MC'+'['+str(sample[0])+','+' '+str(sample[1])+','+' '+str(sample[2])+','+' '+str(sample[3])+']'+'/['+str(str_num)+','+' '+str(ball_num)+']'#Generates a message
                print('To Client:'+message[2:])
                connectionSocket.send(message.encode())
                count+=1#add 1 to count
            else:
                message = connectionSocket.recv(2048).decode()
                print('From Client:'+message[2:])
                if(int(message[16])==4and int(message[3])==0 and int(message[6])==0 and int(message[9])==0 and int(message[12])==0):#When the server won!

                    print('Server Win')
                    break
                if(int(message[3])==int(target[0]) and int(message[6])==int(target[1]) and int(message[9])==int(target[2]) and int(message[12])==int(target[3])):#When the server loses or ties
                    q+=1#I'll give you a chance.
                    if q==2:#I'll give you a chance.
                        if int(message[16])!=4 and t==4:#When the server loses

                            print('Server lose!')
                            break
                        if t==4 and int(message[16])==4:#draw case

                            print('Draw!')
                            break

                str_num=int(message[16])##Check the number of strikes in a message
                ball_num=int(message[19])##Check the number of ball in a message
                for a in range(len(get_list)):  # Compare sample numbers with a list of numbers in all cases
                    str_num2 = 0
                    ball_num2 = 0
                    for b in range(4):
                        for c in range(4):
                            if sample[c] == get_list[a][b] and b == c:  # When the number of information is different compared to the sample
                                str_num2 += 1
                            if sample[c] == get_list[a][b] and b != c:# When the number of information is different compared to the sample
                                ball_num2 += 1
                    if str_num2 != str_num or ball_num2 != ball_num:  # If the number is different, replace it with 0.
                        get_list[a] = 0


                get_list = list(set(get_list))   # Delete a value of 0 and remove it from the list
                get_list.remove(0)
                get_list.sort()
                x = message[3] + message[6] + message[9] + message[12]#Getting information from a message
                str_num = 0
                ball_num = 0
                for i in range(4):  # Determine the number of balls and strikes
                    for j in range(4):
                        if target[i] == x[j] and i == j:  # If Strike
                            str_num += 1
                        if target[i] == x[j] and i != j:  # If ball
                            ball_num += 1
                sample = random.choice(get_list)#Randomly generate numbers to fit
                message='MC'+'['+str(sample[0])+','+' '+str(sample[1])+','+' '+str(sample[2])+','+' '+str(sample[3])+']/['+str(str_num)+','+' '+str(ball_num)+']'##Generates a message
                print('To Cilent:'+message[2:])
                t=str_num#Store strike information at value t
                connectionSocket.send(message.encode())











    connectionSocket.close()
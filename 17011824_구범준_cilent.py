#17011824_구범준 클라이언트용
import random
from socket import *
serverName='localhost'
serverPort=12000
count=0#Sets the variable
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect(('localhost',serverPort))
tmp1=0#Sets the variable
tmp2=0#Sets the variable
sample=0#Sets the variable
request=input('Do you want to play a game? (Yes or No)')
if(request=='Yes'):
    message='MAgame_request'
    print('To Server: game_request')
    clientSocket.send(message.encode())
    modifiedMessage=clientSocket.recv(2048)
    if(modifiedMessage.decode()[0]=='M' and modifiedMessage.decode()[1]=='B'):#If the message starts in MB,
        print('From Server:game_grant')
        all_list = []#Sets the LIST

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
        #play_num = 0
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
            str_num=0#Initialize number of strike balls
            ball_num=0

            if(count==0):#If it's the first time,
                sample = random.choice(get_list)#Randomly generate numbers to fit
                massage = 'MC' + '[' + str(sample[0]) + ',' + ' ' + str(sample[1]) + ',' + ' ' + str(sample[2]) + ',' + ' ' + str(sample[3]) + ']' + '/[0, 0]'#Generates a message
                print('To Server:'+massage[2:])
                clientSocket.send(massage.encode())
                message = clientSocket.recv(2048).decode()
                print('From Server:'+message[2:])

                str_num=int(message[16])#Check the number of strikes in a message
                ball_num=int(message[19])#Check the number of ball in a message

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
                get_list = list(set(get_list))  # Delete a value of 0 and remove it from the list
                get_list.remove(0)
                get_list.sort()
                x=message[3]+message[6]+message[9]+message[12]#Getting information from a message

                str_num = 0
                ball_num = 0
                for i in range(4):  # Determine the number of balls and strikes
                    for j in range(4):
                        if target[i] == x[j] and i == j:  # If Strike
                            str_num += 1
                        if target[i] == x[j] and i != j:  # If ball
                            ball_num += 1
                tmp1=str_num#Save strike information to tmp1
                tmp2=ball_num#Save ball information to tmp2

                count += 1#add 1 to count
                if(tmp1==4):# When the server win
                    print('Client Lose!')
                    massage = 'MC[0, 0, 0, 0]/[4, 0]'
                    print('To Server:' + massage[2:])
                    clientSocket.send(massage.encode())
                    break
            else:

                sample = random.choice(get_list)#Randomly generate numbers to fit
                massage = 'MC' + '[' + str(sample[0]) + ',' + ' ' + str(sample[1]) + ',' + ' ' + str(sample[2]) + ',' + ' ' + str(sample[3]) + ']' + '/[' + str(tmp1) + ',' + ' ' + str(tmp2) + ']'#Generates a message
                print('To Server:' + massage[2:])
                clientSocket.send(massage.encode())
                message = clientSocket.recv(2048).decode()
                print('From Server:' + message[2:])
                str_num = int(message[16])#Check the number of strikes in a message
                ball_num = int(message[19])#Check the number of ball in a message
                temp1=str_num
                temp2=ball_num

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
                if(temp1!=4):
                    get_list = list(set(get_list))  # Delete a value of 0 and remove it from the list
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
                tmp1 = str_num #Save strike information to tmp1
                tmp2 = ball_num #Save ball information to tmp2
                if(tmp1==4 and tmp2==0 and temp1!=4):#When the server won!
                    print('Client Lose!')
                    massage = 'MC[0, 0, 0, 0]/[4, 0]'
                    print('To Server:' + massage[2:])
                    clientSocket.send(massage.encode())
                    break
                if(temp1==4 and tmp1!=4):#When the client wins!
                    print('Client Win!')
                    massage = 'MC' + '[' + str(sample[0]) + ',' + ' ' + str(sample[1]) + ',' + ' ' + str(sample[2]) + ',' + ' ' + str(sample[3]) + ']' + '/[' + str(tmp1) + ',' + ' ' + str(tmp2) + ']'

                    print('To server:'+ massage[2:])
                    clientSocket.send(massage.encode())
                    break
                if (temp1 == 4 and tmp1 == 4):#draw
                    print('Draw!')
                    massage = 'MC' + '[' + str(sample[0]) + ',' + ' ' + str(sample[1]) + ',' + ' ' + str(sample[2]) + ',' + ' ' + str(sample[3]) + ']' + '/[' + str(tmp1) + ',' + ' ' + str(tmp2) + ']'

                    print('To server:' + massage[2:])
                    clientSocket.send(massage.encode())
                    break








clientSocket.close()
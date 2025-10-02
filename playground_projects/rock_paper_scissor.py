import time
import random
name = input("Please input your Name: ")
print(f"Welcome {name} , lets begin the game.\nOn the count of 3")
print('1 ')
time.sleep(1)
print('..2 ')
time.sleep(1)
print('..3 ')

ans_pool = ['rock', 'paper', 'scissor']
computer_response = ans_pool[random.randint(0,2)]
#print(computer_response)
while(True):
    response = input("Enter your move to start the game: ")
    response = response.lower()
    #print(response)

    if(response in ans_pool and response != computer_response):
        print(f"My respose is {computer_response}")
        time.sleep(1)
        if(response == 'rock' and computer_response == 'scissor'):
            print("You win.\nRock breaks the scissor\n")
        elif(response == 'rock' and computer_response == 'paper'):
            print("You loose.\nPaper covers the rock.\n")
        elif(response == 'scissor' and computer_response == 'paper'):
            print("You win.\nScissor cuts the paper.\n")
        elif(response == 'scissor' and computer_response == 'rock'):
            print("You loose.\nRock breaks the scissor.\n")
        elif(response == 'paper' and computer_response == 'rock'):
            print("You Win.\nPaper covers the rock.\n")
        elif(response == 'paper' and computer_response == 'scissor'):
            print("You loose.\nScissor cuts the paper.\n")
        break
    
    elif(response in ans_pool and response == computer_response):
        print(f"My respose is {computer_response}")
        time.sleep(1)
        print("It's a draw. Play again.")
        continue
    print("Invalid Move... I can wait, I've got nowhere to go.\n")

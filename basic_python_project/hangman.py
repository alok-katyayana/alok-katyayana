import random
from getpass import getpass
class Game():
    instance_counter = 6
    word = ''
    guess_letter = ''
    incomplete_letter = []

    def toss(self):
        res = random.randint(1,1000)
        if res <= 500:
            print('Head')
        else:
            print('Tail')
    
    def feed(self):
        self.word = getpass("Please Enter a word to start the Game: ")
        #print(self.word)
    
    def draw(self):
        for elm in self.incomplete_letter:
            print(elm,end='')
        print('\n')
        if(self.instance_counter == 5):
            for i in range(7):
                spc = ' '* 60
                print(spc,end='')
                print('|')
        elif(self.instance_counter == 4):
            print(' '*50+'_'*10+";")
            for i in range(7):
                spc = ' '* 60
                print(spc,end='')
                print('|')
        elif(self.instance_counter == 3):
            print(' '*50+'_'*10+";")
            for i in range(2):
                spc = ' '* 50
                print(spc,end='')
                print('|',end='')
                print(' '* 9, end='')
                print('|')
            for i in range(5):
                spc = ' '* 60
                print(spc,end='')
                print('|')
        elif(self.instance_counter == 2):
            print(' '*50+'_'*10+";")
            for i in range(2):
                spc = ' '* 50
                print(spc,end='')
                print('|',end='')
                print(' '* 9, end='')
                print('|')
            print(' '*48+'(-,-)'+' '*7+'|')
        
            for i in range(4):
                spc = ' '* 60
                print(spc,end='')
                print('|')
        elif(self.instance_counter == 1):
            print(' '*50+'_'*10+";")
            for i in range(2):
                spc = ' '* 50
                print(spc,end='')
                print('|',end='')
                print(' '* 9, end='')
                print('|')
            print(' '*48+'(-,-)'+' '*7+'|')
            print(spc+'|'+' '*9+'|')
            for i in range(4):
                spc = ' '* 60
                print(spc,end='')
                print('|')
        elif(self.instance_counter == 0):
            print(' '*50+'_'*10+";")
            for i in range(2):
                spc = ' '* 50
                print(spc,end='')
                print('|',end='')
                print(' '* 9, end='')
                print('|')
            print(' '*48+'(-,-)'+' '*7+'|')
            print(spc+'|'+' '*9+'|')
            print(spc+'^'+' '*9+'|')
            for i in range(4):
                spc = ' '* 60
                print(spc,end='')
                print('|')
    print('\n')


    def start_guess(self):
        self.incomplete_letter = ['-'] * len(self.word)
        self.draw()
        print('\nGo On Guess The letter\n')
        while (self.instance_counter > 0):
            self.guess_letter = input()
            if len(self.guess_letter) != 1:
                print("No Cheating, enter a single letter.")
                continue
            occur = self.word.count(self.guess_letter)
            #print(occur)
            if occur == 0:
                self.instance_counter -= 1
                self.draw()
                if (self.instance_counter == 0):
                    print(f"\n\nI'm Sorry, Better Luck Next Time.\n\nThe word is:  {self.word}\n\n")
                    break
                print('Unlucky, Keep guessing.')
            else:
                print("Excellent Guess")
                inst = []
                val = -1
                for i in range(occur):
                     #print(val)
                     val = self.word.find(self.guess_letter,val+1)
                     #print(val)
                     inst.append(val)
                #print(inst)
                #var_incom_lettr = '-'
                for i in range(len(self.word)):
                    if (i in inst):
                        self.incomplete_letter[i] = self.guess_letter
                    #else:
                    #   var_incom_lettr = var_incom_lettr + '-'
                
                #self.incomplete_letter = var_incom_lettr
                self.draw()
                if '-' not in self.incomplete_letter:
                    print('\n\nCongratulations. You have won the match.\n\n')
                    break
                print("Continue Guessing.")
                #self.instance_counter -= 1
        else:
               #print("\n\nI'm Sorry, Better Luck Next Time.\n\n")
               pass








if __name__ == '__main__':
    strt = Game()
    _ = input("Press Any Key to begin toss.")
    strt.toss()
    _ = input('Press any key to begin the Game.')
    strt.feed()
    strt.start_guess()
    print("Wasn't it a wonderful game.")

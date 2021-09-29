from tkinter import *
import numpy as np
root = Tk()
e = Entry(width=24)
e.grid(row=0,column=0,columnspan=3)

#global entry_val
#global agg_val
#agg_val = 0
lis = list()
#global pointer
#pointer = '+'

def click_number(i):
    val = e.get()
    e.delete(0,END)
    e.insert(0,val+str(i))
    #global entry_val
    #global agg_val
    #entry_val = abs(int(e.get()))
    #if agg_val == None:
    #    agg_val = entry_val

def click_add():
    #global agg_val, pointer
    #pointer = '+'
    lis.append(abs(int(e.get())))
    lis.append('+')        
    e.delete(0,END)

def click_sub():
    #global agg_val, pointer
    #pointer = '-'
    lis.append(abs(int(e.get())))
    lis.append('-')
    e.delete(0,END)



def click_equal():
    #global agg_val
    #if (pointer == '+'):
    #    agg_val = agg_val + abs(int(e.get()))
    #elif (pointer == '-'):
    #    agg_val = agg_val - abs(int(e.get()))
    lis.append(abs(int(e.get())))
    e.delete(0,END)
    for i in range(1,len(lis),2):
        if lis[i] == '-':
            lis[i+1] = -1 * lis[i+1]
            lis[i] = 0
        else:
            lis[i] = 0
    arr = np.array(lis)

    e.insert(0,arr.sum())

def clear_screen():
    lis.clear()
    e.delete(0,END)

for i in range(10):
    button = Button(root,text=str(i),padx=27,command=lambda x=i:click_number(x))
    if i != 0:
        button.grid(row=((9-i)//3 + 1), column = ((i%3)+2)%3)
    else:
        button.grid(row=((9-i)//3 + 1), column = 0)

add_button = Button(root,text = '+', padx=27,command = click_add)
add_button.grid(row=4,column = 1)

minus_button = Button(root,text = '-', padx=27,command = click_sub)
minus_button.grid(row=4,column = 2)

equal_button = Button(root,text = '=', padx=45,command = click_equal)
equal_button.grid(row=5,column =1)

clear_button = Button(root, text = 'CS', padx =36, command = clear_screen)
clear_button.grid(row=5,column=2)

root.mainloop()

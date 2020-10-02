import numpy as np
import math
msg = input("Enter message : ")
keys = input("Enter key : ")
keys = keys.upper()
key = ''
for index,i in enumerate(keys):
    if not i in keys[:index]:
        key = key + i
carr = np.empty((5,5), 'U1')

char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in char:
    if not i in key:
        key = key + i
        
print(key)
k = 0
for i in range(5):
    for j in range(5):
        if key[k] != 'J':
            carr[i][j] = key[k]
            k = k+1
            
        else:
            k = k+1
           
            carr[i][j] = key[k]
            k = k+1

for i in range(5):
    for j in range(5):
        print(carr[i][j]+'   ',end= '')
    print('\n')

txt = ''

def checker(txts,msgs):
    j = 0 
    i = 0
    for i in range(msgs.__len__()//2): 
        if msgs[j] == msgs[j+1]:
            txts = txts + msgs[j] + 'X' + msgs[j+1]
        elif msgs[j] == 'i' and msgs[j+1] == 'j':
            txts = txts + msgs[j] + 'X' + msgs[j+1]
        else:
            txts = txts + msgs[j] + msgs[j+1]
        j = j+2
    
        
    if (msgs.__len__()%2)!=0:
        txts = txts + msgs[msgs.__len__()-1]
    
    t = txts

    if msgs.__len__() < txts.__len__():
        data =  txts
        txts = ''
        
        t = checker(txts,data)

    if (t.__len__()%2)!=0:
        t = t + 'X'

    return t

txtmsg = checker(txt,msg)
print(txtmsg)
j = 0
txtmsg = txtmsg.upper()
print(txtmsg)
e1= ''


#h =np.where(carr == 'R')

#print(h[0])
j = 0
for i in range(txtmsg.__len__()//2):
    loc1 = np.where(carr == txtmsg[j])
    loc2 = np.where(carr == txtmsg[j+1])

    if loc1[0] == loc2[0]:
        if loc1[1][0] == 4:
            e1 = e1 + carr[loc1[0][0],0]
        else:
            e1 = e1 + carr[loc1[0][0],loc1[1][0]+1]
        if loc2[1][0] == 4:
            e1 = e1 + carr[loc1[1][0],0]
        else:
            e1 = e1 + carr[loc2[0][0],loc2[1][0]+1]
    
    elif loc1[1] == loc2[1]:
        if loc1[0][0] == 4:
            e1 = e1 + carr[0,loc1[1][0]]
        else:
            e1 = e1 + carr[loc1[0][0]+1,loc1[1][0]]
        if loc2[0][0] == 4:
            e1 = e1 + carr[0,loc1[1][0]]
        else:
            e1 = e1 + carr[loc2[0][0]+1,loc1[1][0]]

        
    else:
        e1 = e1 + carr[loc1[0][0],loc2[1][0]] + carr[loc2[0][0],loc1[1][0]]
        

    j = j+2

print(e1)
import random
from pynput import keyboard
from datetime import datetime
import pandas as pd
import seaborn as sn    
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------------------------

def login():
    for i in range(0,4):
        if(i==3):
            print("You have reached the limit--\nTry again later ^_^\n")
            return False
        usern =  input("Enter the Username : ")
        passwd = input("Enter the password : ")
        if(usern == "admin" and passwd == "helloworld"):
            print("\nLogin Successfully ^_^\n")
            return True
        else:
            print("The username or password is invalid--\n")
            continue
#------------------------------------------------------------------------------------------------------

def helo():
    print(''' This is cipher is made with the algorithm of ROT13 and our own algorithm 
          of adding numbers and speical characerts in the sequence order of 2 are included in order 
          to increase the complexity and after the enycrption it is saved in the file called cipher.txt and 
          it can be taken or accessed with the username.
        \nAnd enter the password to get administrator access''')
    admin = input("Access : ")
    if(admin == "administrator"):
        with open("filepath/cipher.txt","r") as file:
            print(file.read())
    else:
        print("Invalid authentication--\n")
    return
    
#------------------------------------------------------------------------------------------------------

class cipherprocess:
    def __init__(self):
        pass

    def encrypter(self):
        has =  input("Enter the text    : ")
        hasvalue = []
        alphabetsL = "ABCDEFGHIJKLM"
        alphabetsl = "NOPQRSTUVWXYZ"
        for i in has:
                if(i in alphabetsL):
                    indexx = alphabetsL.index(i)
                    hasvalue.append(alphabetsl[indexx])
                elif(i.swapcase() in alphabetsL):
                    indexx = alphabetsL.index(i.swapcase())
                    hasvalue.append((alphabetsl[indexx]).swapcase())
                elif(i.swapcase() in alphabetsl):
                    indexx = alphabetsl.index(i.swapcase())
                    hasvalue.append((alphabetsL[indexx]).swapcase())
                elif(i in alphabetsl):
                    indexx = alphabetsl.index(i)
                    hasvalue.append(alphabetsL[indexx])
                else:
                    continue
        numbers = "1234567890@#$%^&*"
        for i in range(1,len(hasvalue),2):
            hasvalue.insert(i,random.choice(numbers))
        print("\nEncrypted Successfully ^_^\n")
        hs = ''
        for i in hasvalue:
            hs+=(i)
        return(hs)
    
    def decrypter(self,hasvalue):
        hs = []
        alphabetsl = "ABCDEFGHIJKLM"
        alphabetsL = "NOPQRSTUVWXYZ"
        for i in hasvalue:
            if(i in alphabetsl or i in alphabetsL or i.swapcase() in alphabetsl or i.swapcase() in alphabetsL):
                hs.append(i)
                continue
        hasvalue = []
        hasvalue1 = ''
        for i in hs:
            if(i in alphabetsl):
                indexx = alphabetsl.index(i)
                hasvalue.append(alphabetsL[indexx])
            elif(i.swapcase() in alphabetsl):
                indexx = alphabetsl.index(i.swapcase())
                hasvalue.append((alphabetsL[indexx]).swapcase())
            elif(i.swapcase() in alphabetsL):
                indexx = alphabetsL.index(i.swapcase())
                hasvalue.append((alphabetsl[indexx]).swapcase())
            elif(i in alphabetsL):
                indexx = alphabetsL.index(i)
                hasvalue.append(alphabetsl[indexx])
            else:
                continue
        for i in hasvalue:
            hasvalue1 += i
        return(hasvalue1)
    
    def savefile(self,user,hasvalue,option):
        if(option == 1):
            try:
                with open("filepath/cipher.txt","a+") as file:
                    value = (user+" "+hasvalue)
                    file.write(value+"\n")
                    print("THE FILE HAS BEEN SAVED SUCCESSFULLY !!!!!!!\n")
                return
            except:
                print("The file is not saved!!!\n")
                return
    
        elif(option == 2):
            with open("filepath/cipher.txt","r+") as file:
                for i in file:
                    if(user in i):
                        user,has = i.split(" ",1)
                        return has
        


#----------------------------------------------------------------------------------------------------------
class keyloggers:
    def __init__(self):
        pass

    def onprocess(self):
        self.final = ''
        def process(key):
            if(str(key) == 'Key.enter'):
                value = datetime.now()
                dt = value.replace(microsecond=0)
                d,t = str(dt).split(" ",1)
                value = '['+d+'|'+t+']'+' : '
                value1 = value+self.final
                with open("filepath/kl.txt","a+") as file:
                    file.write(value1+"\n")
                self.final = ''
                return
            else:
                self.final+=str(key)
                return
        listener = keyboard.Listener(on_press=process)
        listener.start()
        input()

#----------------------------------------------------------------------------------------------------------
print("-------------------------CRYPTOGRAPHIC CIPHER------------------------\n")
if(login() == True):
    pass
else:
    exit()
p = cipherprocess()
k = keyloggers()
while(1==1):
    choice = input("\nENCRYPT(e) | DECRYPT(d) | KEYLOGGIN(k) | ANALYSIS(a) | EXIT(ex)\nEnter the action to be done: ")
    if(choice == 'e' or choice == 'E'):
        user = input("Enter the title       : ")
        h = p.encrypter()
        print("\nCIPHER : ",h)
        save = input("\nDo you want to save the action (y or n) : ")
        if(save == 'y'):
            p.savefile(user,h,1)
        else:
            print("\nThe file is not saved\n")
        continue
    elif(choice == 'd' or choice == 'D'):
        choicee = input("1.Username\n2.Decoder\nEnter the action : ")
        if(choicee == '1'):
            usern = input("Enter the Username: ")
            h = p.savefile(user = usern,hasvalue='NULL',option = 2)
        elif(choicee == '2'):
            h = input("Enter the ciphered text : ")
        else:
            print("Invalid\n")
            continue
        h1 = p.decrypter(h)
        print("DECIPHER: ",h1)
        continue
    elif(choice == 'k' or choice == 'K'):
        k.onprocess()
        continue
    elif(choice == 'ex' or choice == 'Ex'):
        break
    elif(choice == 'help'):
        helo()
        continue
    elif(choice == "a" or "A"):
        p.analysisof()
        continue
    else:
        print("Invalid choice of input:(\n")
        continue
print("-----------------------------------------------------------------------")

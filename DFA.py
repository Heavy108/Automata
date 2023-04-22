
#Write a program in Python which takes the transition table of a DFA as input and accepts or rejects a given string
import pandas as pd
#Program to Check  if the given String Accepted or rejected by the DFA
def DFA_checker(input,table,start,final):
    current = start
    for St in input:
        if St  not in table[current]:
            return False
        current = table[current][St]
        
    
    if current in final:
        return True
    return False
#-------------------------------------------------------------------------------------------------------------------
#driver code

temp=[]
States=input("Enter the number of states: ")
Alphabets= int(input("Enter the nummber finite alphabet: "))
for j in range(Alphabets):
    temp.append(input("Enter the  finite alphabets: "))

Start_state = input("Enter the starting state: ")
final_state =input("Enter the Final state: ")
d = {}
size = int(States)
for i in range(size):
   
    
    key1 = input("Enter the states: ")

    d[key1] = {}
    temp[0] = input("Enter the state at FIRST alph:  ")
    temp[1] = input("Enter the state at SECOND alph: ")
    d[key1]["0"] = temp[0]
    d[key1]["1"] = temp[1]
    

df =pd.DataFrame.from_dict(d, orient ="index")
print(df)
input_strings =  '10101010113'
S=DFA_checker(input_strings,d,Start_state,final_state)
if S==True:

    print("ACCEPTED")
else:
    print("REJECTED")

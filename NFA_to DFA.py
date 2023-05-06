#Write a program in Python which takes the transition table of an NFA as input and convert it to its equivalent DFA that accepts the same language accepted by the NFA.
##NAME:- SATYAM SAJAL
#ROLL NO.: - CSB21073
#4TH SEMESTER FLA ASSIGNMENT
import pandas as pd

def DFA_converter(Transition_table, start, accepting, states):
    current = start
    final = accepting
    nfa = Transition_table
    t = states

    new_states_list = []  #holds all the new states created in NFA
    dfa = {}  
    keys_list = list(list(nfa.keys())[0])  # #conatins all the states in nfa plus the states created in dfa are also appended further
    path_list = list(nfa[keys_list[0]].keys())  
    

   # Computing first row of DFA transition table
    dfa[keys_list[0]] = {}                              #creating aa nested dictionary in dfa
    for y in range(len(path_list)):
        var = "".join(nfa[keys_list[0]][path_list[y]])  
        dfa[keys_list[0]][path_list[y]] = var           #assigning the state in DFA table
        if var not in keys_list and var != '':  
            new_states_list.append(var)  
            keys_list.append(var)  

    # Computing the other rows of DFA transition table
    while len(new_states_list) != 0:                     #consition is true only if the new_states_list is not empty
        if len(new_states_list) > 0:
            dfa[new_states_list[0]] = {}  
            for _ in range(len(new_states_list[0])):
                for i in range(len(path_list)):
                    temp = []                             #creating a temporay list
                    for j in range(len(new_states_list[0])):
                        if new_states_list[0][j] not in nfa:
                            temp.append('')
                        else:
                            temp += nfa[new_states_list[0][j]][path_list[i]] 
                    s = set(temp)
                    var = "".join(sorted(s))
                    if var == '':
                        var = '&'           #'&' this represent the trap state
                    dfa[new_states_list[0]][path_list[i]] = var 
                    if var not in keys_list and var != '':  
                        new_states_list.append(var)  
                        keys_list.append(var)  
            new_states_list.pop(0)
    #updating the final states
    dfa_states_list = list(dfa.keys())
    dfa_final_states = []
    for x in dfa_states_list:
        for i in x:
            if i in final:
                dfa_final_states.append(x)
                break
    return dfa,current,dfa_final_states

start = {'A'}
accepting={'B'}
states={'A','B','C'}
NFA ={
    'A':{0:{'A','B'}, 1:{"B"}},
    'B':{0:'C',1:'C'},
    'C':{0:'',1:'C'}        
}
df = pd.DataFrame.from_dict(NFA,orient = 'index')
dfa,df_start,df_final = DFA_converter(NFA, start, accepting, states)
dz = pd.DataFrame.from_dict(dfa,orient = 'index')
print("--------------NFA-------------")
print(df)
print("-----------DFA----------------------")
print(dz)
print(f"start state:- {df_start},final state :{df_final}")

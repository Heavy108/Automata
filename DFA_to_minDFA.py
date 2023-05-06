##NAME:- SATYAM SAJAL
#ROLL NO.: - CSB21073
#4TH SEMESTER FLA ASSIGNMENT
#  Write a program in Python which takes a DFA as input and gives the equivalent minDFA with
#    minimum number of states as output.
import itertools as t
import pandas as pd

# Function to find the final partition of equivalent states
def equi(table,start,accepting):
    final_states =accepting
    non_final_states = set(table.keys()) - final_states
    equivalence_0 =[non_final_states,final_states]      # 0- equivalence
   
    
    Z=Stabilizes(table,equivalence_0)
    min_dfa,min_start,min_final=dfa_converter(table,Z,start,accepting)  
    dz = pd.DataFrame.from_dict(min_dfa,orient = 'index')       #for representing the transition table in tabular form

    print("-----------------MIN_DFA--------------------")
    print(dz)
    print(f"The start_states of min_dfa: {min_start},The final states of min Dfa: {min_final}")
    
def Stabilizes(trans_table, previous_state):
    partition = previous_state
    tab = trans_table
    new_equivalence = []

    for group in partition:
        new_partition = set()
        #checking states two at a time that it is equivalent to other or not
        for pair in t.combinations(group, 2):
            p1 = set(tab[pair[0]].values())
            p2 = set(tab[pair[1]].values())
            

            if set(p1).issubset(group) and set(p2).issubset(group):     #grouping the equivalent states
                new_partition.add(pair[0])
                new_partition.add(pair[1])
                    
        if len(new_partition) > 0:          
            other_partition = set(group) - new_partition
            new_equivalence.append(new_partition)
            new_equivalence.append(other_partition)
        else:
            new_equivalence.append(group)

    if new_equivalence == previous_state:       # base case
        return new_equivalence
    else:
        return Stabilizes(trans_table, new_equivalence)




def dfa_converter(dfa,new_state,start_state,end_state):
    table2 = dfa
    new_states_list =[]
    for ele in new_state:
        var ="".join(sorted(ele))        
        new_states_list.append(var)
        #updating the start state
        if start_state.issubset(ele):                       
            start_state = "".join(sorted(set(var)))
        #updating the end state for min dfa         
        if end_state.issubset(ele):
            end_state = "".join(sorted(set(var)))
        for alpha in ele:
            key_0 = table2[alpha]['0']
            key_1 = table2[alpha]['1']
            for single_el in new_states_list:
                if table2[alpha]['0'] in single_el:
                    key_0 = single_el
                if table2[alpha]['1'] in single_el:
                    key_1 = single_el
            #remove the old states from table2
            del table2[alpha]
        # after removing the old states adding the new states
        
        table2[var]={'0':"".join(sorted(key_0)) , '1':"".join(sorted(key_1))}
     
        
        
        return table2,start_state,end_state




start = {'A'}
accepting = {'E'}
DFA = {                             #transition table of original DFA
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'B', '1': 'D'},
    'C': {'0': 'B', '1': 'C'},
    'D': {'0': 'B', '1': 'E'},
    'E': {'0': 'B', '1': 'C'}
}
df =pd.DataFrame.from_dict(DFA, orient ="index")
print("--------------ORIGINAL DFA---------------------")
print(df)
print(f"start state: {start} accepting states: {accepting}")
equi(DFA, start, accepting)

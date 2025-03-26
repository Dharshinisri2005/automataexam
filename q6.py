def fillStates(dfa, state, input):
    l = []
    for i in dfa[state]:
        if (i, input) in dfa:
            l.append(dfa[(i, input)])
    newEntry = [element for innerList in l for element in innerList]
    newEntry = list(filter(lambda a: a != '', newEntry))
    return newEntry
nfa = {}
n = int(input("Enter number of states in NFA: "))
state = []
for i in range(n):
    state.append(('q'+str(i), 0))
    state.append(('q'+str(i), 1))
for i in state:
    nfa[i] = list(map(str, input(f"Enter transition for state {i} : ").split(' ')))
print("\nTransistion Diagram for NFA : ")
for i in nfa:
    print(i, " : ", nfa[i])

dfa = nfa
states = set()
for i in dfa.keys():
    states.add(i[0])
newDfa = {}
for i in dfa:
    newState = ""
    for j in dfa[i]:
        newState += j
    if newState not in states and newState != "":
        states.add(newState)
        newDfa[(newState, 0)] = fillStates(dfa, i, 0)
        newDfa[(newState, 1)] = fillStates(dfa, i, 1)
for i in newDfa:
    dfa[i] = newDfa[i]
print("\nTransistion Diagram for DFA : ")
for i in dfa:
    print(i, " : ", dfa[i])
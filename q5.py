def add_epsilon_closure(epsilon_nfa, state, temp):
    if state != '':
        temp.add(state)
        for i in epsilon_nfa.get((state, 'E'), []):
            add_epsilon_closure(epsilon_nfa, i, temp)

def calculate_epsilon_closure(epsilon_nfa):
    epsilon_closures = {}
    for state in states:
        temp = set()
        add_epsilon_closure(epsilon_nfa, state, temp)
        epsilon_closures[state] = temp
    return epsilon_closures

def calculate_transitions(epsilon_nfa, epsilon_closures):
    transitions = {}
    for state in states:
        transitions[state] = {}
        for symbol in alphabet:
            reachable_states = set()
            for s in epsilon_closures[state]:
                targets = epsilon_nfa.get((s, symbol), [])
                reachable_states.update(targets)
            closure = set()
            for s in reachable_states:
                if s in epsilon_closures:
                    closure.update(epsilon_closures[s])
            transitions[state][symbol] = closure
    return transitions

def convert_epsilon_nfa_to_nfa(epsilon_nfa):
    epsilon_closures = calculate_epsilon_closure(epsilon_nfa)
    transitions = calculate_transitions(epsilon_nfa, epsilon_closures)
    return transitions

alphabet = ['0', '1']

epsilon_nfa = {}
n = int(input("Enter number of states in Epsilon-NFA: "))
s = []
states = []

for i in range(n):
    s.append(('q'+str(i), 'E'))
    s.append(('q'+str(i), '0'))
    s.append(('q'+str(i), '1'))
    states.append('q'+str(i))

for i in s:
    transitions = list(map(str, input(f"Enter transitions for state {i} : ").split(' ')))
    epsilon_nfa[i] = transitions

print("Epsilon-NFA : ", epsilon_nfa)
print("\nTransition Diagram for Epsilon-NFA : ")
for i in epsilon_nfa:
    print(i, " : ", epsilon_nfa[i])

print(states, alphabet)

nfa = convert_epsilon_nfa_to_nfa(epsilon_nfa)
print("Transition Table for NFA:")
for state, transitions in nfa.items():
    print(f"State {state}: {transitions}")
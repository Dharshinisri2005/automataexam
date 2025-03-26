from collections import defaultdict

class NFA:
    def __init__(self):
        self.transitions = defaultdict(set)
        self.start_state = 0
        self.final_states = set()

    def add_transition(self, from_state, symbol, to_state):
        self.transitions[(from_state, symbol)].add(to_state)

    def add_final_state(self, state):
        self.final_states.add(state)

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            if (state, 'ε') in self.transitions:
                for next_state in self.transitions[(state, 'ε')]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def is_accepted(self, input_string):
        current_states = self.epsilon_closure({self.start_state})

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            current_states = self.epsilon_closure(next_states)

        return any(state in self.final_states for state in current_states)
nfa = NFA()
Q0, Q1, Q2 = 0, 1, 2
nfa.add_transition(Q0, 'a', Q1)
nfa.add_transition(Q1, 'a', Q1)
nfa.add_transition(Q1, 'b', Q2)
nfa.add_transition(Q2, 'b', Q2)
nfa.add_final_state(Q2)
input_string = input("Enter a string: ")
if nfa.is_accepted(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")

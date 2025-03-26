from collections import defaultdict

class Automaton:
    def __init__(self, is_dfa=True):
        self.transitions = defaultdict(set)
        self.start_state = 0
        self.final_states = set()
        self.is_dfa = is_dfa  

    def add_transition(self, from_state, symbol, to_state):
        if self.is_dfa:
            self.transitions[(from_state, symbol)] = {to_state}  
        else:
            self.transitions[(from_state, symbol)].add(to_state)  

    def add_final_state(self, state):
        self.final_states.add(state)

    def is_accepted(self, input_string):
        current_states = {self.start_state}  

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            if not next_states:  
                return False
            current_states = next_states

        return any(state in self.final_states for state in current_states)

automaton_type = input("Choose Automaton Type (DFA/NFA): ").strip().upper()
is_dfa = automaton_type == "DFA"

automaton = Automaton(is_dfa)

Q0, Q1, Q2 = 0, 1, 2

automaton.add_transition(Q0, 'a', Q1)
automaton.add_transition(Q1, 'a', Q1)
automaton.add_transition(Q1, 'b', Q2)
automaton.add_transition(Q2, 'b', Q2)

automaton.add_final_state(Q2)

input_string = input("Enter a string: ")
if automaton.is_accepted(input_string):
    print("String is accepted.")
else:
    print("String is not accepted.")

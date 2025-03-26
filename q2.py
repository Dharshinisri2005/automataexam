def is_accepted(input_str):
    current_states = {0}  
    
    for c in input_str:
        next_states = set()
        
        for state in current_states:
            if state == 0:
                if c == 'a':
                    next_states.add(1)  
                    next_states.add(2)  
            elif state == 1:
                if c == 'b':
                    next_states.add(3)
            elif state == 2:
                if c == 'a':
                    next_states.add(2)
                if c == 'b':
                    next_states.add(3)
            elif state == 3:
                if c == 'a' or c == 'b':
                    next_states.add(3)
        
        current_states = next_states
        if not current_states:
            return False  
    return 3 in current_states

def main():
    input_str = input("Enter a string (only 'a' and 'b' characters): ")
    
    if is_accepted(input_str):
        print("String is ACCEPTED by the NFA")
    else:
        print("String is REJECTED by the NFA")

if __name__ == "__main__":
    main()
class State:
    Q0 = 0
    Q1 = 1
    Q2 = 2

def is_accepted(input_string):
    current_state = State.Q0

    for symbol in input_string:
        if current_state == State.Q0:
            if symbol == 'a':
                current_state = State.Q1
            else:
                return False

        elif current_state == State.Q1:
            if symbol == 'a':
                current_state = State.Q1
            elif symbol == 'b':
                current_state = State.Q2
            else:
                return False

        elif current_state == State.Q2:
            if symbol == 'b':
                current_state = State.Q2
            else:
                return False

    return current_state == State.Q2

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if is_accepted(input_string):
        print("String is accepted.")
    else:
        print("String is not accepted.")

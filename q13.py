def generate_tac(expression):
    tokens = expression.split("+")  
    tokens = [token.strip() for token in tokens]
    tac_code = []
    temp_vars = []
    
    temp_var_count = 1
    t = f"t{temp_var_count} = {tokens[0]} + {tokens[1]}"
    tac_code.append(t)
    temp_vars.append(f"t{temp_var_count}")
    
    for i in range(2, len(tokens)):
        temp_var_count += 1
        t = f"t{temp_var_count} = {temp_vars[-1]} + {tokens[i]}"
        tac_code.append(t)
        temp_vars.append(f"t{temp_var_count}")
    
    tac_code.append(f"x = {temp_vars[-1]}")
    
    return tac_code

expression = input("Enter an arithmetic expression : ")

tac_result = generate_tac(expression)

print("\nThree-Address Code:")
for line in tac_result:
    print(line)

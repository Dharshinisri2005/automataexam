# Simple First and Follow Implementation

# Grammar Rules (Non-Terminal -> Productions)
grammar = {
    'S': ['aAB', 'B'],
    'A': ['b', 'ε'],
    'B': ['c', 'd']
}

# Compute First Set
def first(symbol):
    first_set = set()
    
    # If symbol is terminal, return itself
    if symbol.islower() or symbol == 'ε':
        return {symbol}
    
    # For non-terminals
    for production in grammar[symbol]:
        first_symbol = production[0]
        
        if first_symbol == 'ε':
            first_set.add('ε')
        elif first_symbol.islower():
            first_set.add(first_symbol)
        else:
            first_set.update(first(first_symbol))
    
    return first_set

# Compute Follow Set
def follow(symbol, start_symbol='S'):
    follow_set = set()
    
    if symbol == start_symbol:
        follow_set.add('$')  # End of input
    
    for nt in grammar:  # For each non-terminal
        for production in grammar[nt]:
            if symbol in production:
                idx = production.index(symbol)
                next_idx = idx + 1
                
                # Case 1: A -> αBβ → Follow(B) includes First(β)
                if next_idx < len(production):
                    next_symbol = production[next_idx]
                    if next_symbol.islower():
                        follow_set.add(next_symbol)
                    else:
                        follow_set.update(first(next_symbol) - {'ε'})
                
                # Case 2: A -> αB or A -> αBβ where β => ε → Follow(B) includes Follow(A)
                if next_idx >= len(production) or 'ε' in first(production[-1]):
                    if nt != symbol:  # Avoid infinite recursion
                        follow_set.update(follow(nt))
    
    return follow_set

# Print First and Follow
print("First Sets:")
for nt in grammar:
    print(f"First({nt}) = {first(nt)}")

print("\nFollow Sets:")
for nt in grammar:
    print(f"Follow({nt}) = {follow(nt)}")

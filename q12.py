from collections import defaultdict

class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.first = defaultdict(set)
        self.follow = defaultdict(set)
        self.start_symbol = list(productions.keys())[0]
        self.compute_first()
        self.compute_follow()

    def compute_first(self):
        for non_terminal in self.productions:
            self.first[non_terminal] = self.find_first(non_terminal)

    def find_first(self, symbol):
        if symbol.islower() or symbol in "()+*":
            return {symbol}
        first_set = set()
        for production in self.productions[symbol]:
            if production == "":  # Epsilon case
                first_set.add("ε")
                continue
            for char in production:
                char_first = self.find_first(char)
                first_set.update(char_first - {"ε"})
                if "ε" not in char_first:
                    break
            else:
                first_set.add("ε")
        return first_set

    def compute_follow(self):
        self.follow[self.start_symbol].add("$")
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.productions.items():
                for production in productions:
                    trailer = self.follow[non_terminal].copy()
                    for symbol in reversed(production):
                        if symbol.isupper():
                            if trailer - self.follow[symbol]:
                                self.follow[symbol].update(trailer)
                                changed = True
                            if "ε" in self.first[symbol]:
                                trailer.update(self.first[symbol] - {"ε"})
                            else:
                                trailer = self.first[symbol]
                        else:
                            trailer = {symbol}

    def display_results(self):
        for non_terminal in self.productions:
            print(f"First({non_terminal}) = {self.first[non_terminal]}")
        print()
        for non_terminal in self.productions:
            print(f"Follow({non_terminal}) = {self.follow[non_terminal]}")

if __name__ == "__main__":
    n = int(input("Enter the number of productions: "))
    productions = defaultdict(list)
    for _ in range(n):
        lhs, rhs = input("Enter production (A=xyz format): ").split("=")
        productions[lhs].extend(rhs.split("|"))
    
    grammar = Grammar(productions)
    grammar.display_results()
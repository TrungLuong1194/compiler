class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    def display(self):
        print('_' * 30)
        print('Symbol table:')
        for k, v in self.symbol_table.items():
            print(str(k) + ': <' + str(v.name) + '>')

    def define(self, symbol):
        print('Define: ' + symbol.name)
        self.symbol_table[symbol.name] = symbol

    def lookup(self, symbol):
        print('Lookup: ' + symbol.name)
        symbol = self.symbol_table.get(symbol.name)
        return symbol

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    def __str__(self):
        s = 'Symbols: {symbols}'.format(
            symbols=[value for value in self.symbol_table.values()]
        )
        return s

    def define(self, symbol):
        print('Define: ' + symbol.name)
        self.symbol_table[symbol.name] = symbol

    def lookup(self, symbol):
        print('Lookup: ' + symbol.name)
        symbol = self.symbol_table.get(symbol.name)
        return symbol

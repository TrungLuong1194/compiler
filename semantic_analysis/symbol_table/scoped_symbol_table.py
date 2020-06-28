class ScopedSymbolTable:
    def __init__(self, scope_name, scope_level, enclosing_scope=None):
        self.symbol_table = {}
        self.scope_name = scope_name
        self.scope_level = scope_level
        self.enclosing_scope = enclosing_scope

    def display(self):
        print('\n')
        print('SCOPE (SCOPED SYMBOL TABLE)')
        print('=' * 30)
        print('Scope name: ' + str(self.scope_name))
        print('Scope level: ' + str(self.scope_level))
        if self.enclosing_scope:
            print('Enclosing scope: ' + str(self.enclosing_scope.scope_name))
        else:
            print('Enclosing scope: None')
        print('Scope contents:')
        print('-' * 30)
        for k, v in self.symbol_table.items():
            print(str(k) + ': <name=' + str(v.name) + ', type=' + str(v.typeSymbol) + '>')

    def define(self, symbol):
        print('Define: ' + symbol.name)
        self.symbol_table[symbol.name] = symbol

    def lookup(self, symbol):
        print('Lookup: ' + symbol.name + ' (Scope name: ' + self.scope_name + ')')
        symbol_find = self.symbol_table.get(symbol.name)

        if symbol_find is not None:
            return symbol_find

        # recursively go up the chain and lookup the name
        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup(symbol)

    def lookupCurrent(self, symbol):
        print('Lookup: ' + symbol.name + ' (Scope name: ' + self.scope_name + ')')
        symbol_find = self.symbol_table.get(symbol.name)

        if symbol_find is not None:
            return symbol_find

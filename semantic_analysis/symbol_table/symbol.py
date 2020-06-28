class Symbol:
    def __init__(self, name, typeSymbol=None):
        self.name = name
        self.typeSymbol = typeSymbol


class ProcedureSymbol:
    def __init__(self, name, typeSymbol=None):
        self.name = name
        self.typeSymbol = typeSymbol
        self.block_ast = None

import xml.etree.ElementTree as elementTree


class WriteXml:
    """Write a file xml"""

    def __init__(self, grammar):
        self.grammar = grammar

    def write(self):
        root = elementTree.Element('grammar', {'name': 'G'})

        # write terminal symbols
        terminalsymbols = elementTree.SubElement(root, 'terminalsymbols')

        for i in self.grammar.terminal:
            elementTree.SubElement(terminalsymbols, 'term', {'name': i})

        # write non terminal symbols
        nonterminalsymbols = elementTree.SubElement(root, 'nonterminalsymbols')

        for i in self.grammar.non_terminal:
            elementTree.SubElement(nonterminalsymbols, 'nonterm', {'name': i})

        # write productions
        productions = elementTree.SubElement(root, 'productions')

        for i in range(len(self.grammar.rule)):
            # write production
            production = elementTree.SubElement(productions, 'production')

            # write lhs
            lhs = elementTree.SubElement(production, 'lhs', {'name': self.grammar.rule[i].left_side})

            # write rhs
            rhs = elementTree.SubElement(production, 'rhs')

            # write symbol
            for j in self.grammar.rule[i].right_side:
                if j in self.grammar.terminal:
                    symbol = elementTree.SubElement(rhs, 'symbol', {'type': 'term', 'name': j})
                else:
                    symbol = elementTree.SubElement(rhs, 'symbol', {'type': 'nonterm', 'name': j})

        # write start symbol
        startsymbol = elementTree.SubElement(root, 'startsymbol', {'name': self.grammar.get_start_symbol()})

        e = elementTree.ElementTree(root)
        with open('output.xml', 'wb') as f:
            e.write(f)

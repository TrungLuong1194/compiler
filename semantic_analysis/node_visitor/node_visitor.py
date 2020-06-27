class NodeVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.error_visit)
        return visitor(node)

    def error_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
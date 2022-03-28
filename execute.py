class Execute:
    def __init__(self, tree, env):
        self.env = env
        res = self.parseTree(tree)
        if res is not None and isinstance(res, int):
            print(res)
        elif isinstance(res, str) and res[0] == '"':
            print(res)

    def parseTree(self, node):
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node
        if node is None:
            return None
        if node[0] == 'program':
            if node[1] == None:
                self.parseTree(node[2])
            else:
                self.parseTree(node[1])
                self.parseTree(node[2])
        if node[0] == 'num':
            return node[1]
        if node[0] == 'str':
            return node[1]
        if node[0] == 'add':
            return self.parseTree(node[1]) + self.parseTree(node[2])
        elif node[0] == 'sub':
            return self.parseTree(node[1]) - self.parseTree(node[2])
        elif node[0] == 'mul':
            return self.parseTree(node[1]) * self.parseTree(node[2])
        elif node[0] == 'div':
            return self.parseTree(node[1]) / self.parseTree(node[2])
        if node[0] == 'var_assign':
            self.env[node[1]] = self.parseTree(node[2])
            return node[1]
        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Variable "+ node[1] +" not defined")
                return 0
        

        
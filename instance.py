class Instance:
    def __init__(self, args):
        self.contents = args
        self.processor = args[7]
        self.unique_id = args[16]
        self.general_id = args[15]
        self.child_general_id = args[18]
        self.cost = args[9]
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getRow(self):
        row = None
        if self.children != []:
            row = self.contents 
            for child in self.children:
                row += child.contents
        return row

    

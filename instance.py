class Instance:
    def __init__(self, args):
        self.contents = args
        self.unique_id = args[16]
        self.general_id = args[15]
        self.child_general_id = args[18]
        self.cost = args[9]
        self.children = []

    def addChild(self, child):
        self.child = child

    def getCheapest(self):
        min_price = -1
        min_child = None
        for child in self.children:
            if min_child == None:
                min_child = child.unique_id

            if (min_price > child.price_per_unit):
                min_price = child.price_per_unit
                min_child = child.unique_id

        return (min_child, min_price)

    def getCheapestSameFamily(self):
        min_price = -1
        min_child = None
        for child in self.children:
            if child.instance_family != self.instance_family:
                continue

            if min_child == None:
                min_child = child.unique_id

            if (min_price > child.price_per_unit):
                min_price = child.price_per_unit
                min_child = child.unique_id

        return (min_child, min_price)

    def getRow(self):
        row = None
        if self.child != None:
            row = self.contents + self.child.contents
        return row

    

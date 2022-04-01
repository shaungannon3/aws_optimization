from cgitb import small
from re import I
import sys
from instance import Instance

class DataProcessor:

    def __init__(self, instances, groups):
        self.instances = instances
        self.groups = groups
        self.groupmins = {}

    def process(self):
        # get two lowest cost items for each group
        self.calcGroupMins()

        # process each instance to add two children to its list of children
        # if processor type is Gravitron, then add 2 lowest priced children
        # else, add cheapest option and 1 of same processor type
        for instance in self.instances:
            if instance.child_general_id in self.groupmins:
                cheapest = self.groupmins[instance.child_general_id]
                instance.children = cheapest


    def calcGroupMins(self):
        for group_id, group_instances in self.groups.items():
            self.calcGroupMin(group_id, group_instances)
    
    def calcGroupMin(self, group_id, group_instances):
        if len(group_instances) <= 2:
            self.groupmins[group_id] = group_instances
            return

        smallest = [None, None]

        for instance in group_instances:
            if smallest[0] == None:
                smallest[0] = instance
                continue
            elif smallest[1] == None:
                smallest[1] = instance
                continue

            if instance.cost < smallest[0].cost:
                temp = smallest[0]
                smallest[1] = temp
                smallest[0] = instance
            elif instance.cost < smallest[1].cost:
                smallest[1] = instance

        self.groupmins[group_id] = smallest

        return

    def getCheapestSameProcessor(self, processor, instances):
        min_price = "999999"
        min_child = None

        for instance in instances:
            if instance.processor != processor:
                continue

            if min_child == None:
                min_child = instance

            if (min_price > instance.cost):
                min_child = instance

        return min_child


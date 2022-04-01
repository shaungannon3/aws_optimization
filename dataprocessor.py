from cgitb import small
from re import I
import sys
from instance import Instance

class DataProcessor:
  
    def __init__(self, instances, groups):
        # instances: all AWS machines
        self.instances = instances 
        # groups: key: general id, value: list of machines w/ same general id
        self.groups = groups 
        #groupmins: key: general id, value: 2 cheapest machines w/ same general id
        self.groupmins = {} 

    def process(self):
        # get two lowest cost machines for each group
        self.calcGroupMins()

        # process each instance to add two cheapest children to its list of children
        for instance in self.instances:
            if instance.child_general_id in self.groupmins:
                cheapest = self.groupmins[instance.child_general_id]
                instance.children = cheapest
        return

    # function to loop through groups of machines
    # and call function to calculate 2 cheapest machines in each group
    def calcGroupMins(self):
        for group_id, group_instances in self.groups.items():
            self.calcGroupMin(group_id, group_instances)
    
    # helper function to calculate 2 cheapest machines in a cluster
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
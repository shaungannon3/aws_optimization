import csv
from curses import has_key
import math
from enum import unique
from instance import Instance

def find_min(group):
    min_cost = -1
    min_instance = None
    for instance in group:
        if min_instance == None:
            min_instance = instance
            min_cost = instance.cost
    
    return min_instance

def main(filename):
    instances = []
    groups = {}
    min_groups = {}
    with open(filename, newline ='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader) 
        for row in reader:
            instance = Instance(row)
            instances.append(instance)

            if row[13] == "Host":
                continue

            if not instance.general_id in groups:
                groups[instance.general_id] = [instance]
            else:
                groups[instance.general_id].append(instance)
    
    for id , group in groups.items():
        min_instance = find_min(group)
        min_groups[id] = min_instance

    for instance in instances:
        child = min_groups.get(instance.child_general_id, None)

        if (child == None):
            continue
        else:
            instance.addChild(child)

    print("world")
    output_filename = filename[:-4] + "-output.csv"

    with open(output_filename, 'w', newline = '') as fp:
        writer = csv.writer(fp)
        child_header = ["Down Size - " + item for item in header]
        output_header = header + child_header
        writer.writerow(output_header)
        for instance in instances:
            row = instance.getRow()
            if row != None:
                writer.writerow(row)

    csv_file.close()
    fp.close()


if __name__ == "__main__":
    main("AWS_pricing.csv")










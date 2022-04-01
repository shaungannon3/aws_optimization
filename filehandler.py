import csv
from instance import Instance

class FileHandler:

    def __init__(self, filename):
        self.filename = filename
        self.header = None

    def readFile(self):
        # hold all rows as 'instances'
        instances = []
        # capture as groups all rows which share the same 'general id'
        groups = {}

        # read through file
        with open(self.filename, newline ='') as csv_file:
            reader = csv.reader(csv_file)
            self.header = next(reader) #save header to use for output file

            for row in reader:
                # bypass rows with 'Host' tenancy
                if row[13] == "Host":
                    continue
                # create new instance for the row and append to list of instances
                instance = Instance(row)
                instances.append(instance)

                # create new group with general_id if not existing
                if not instance.general_id in groups:
                    groups[instance.general_id] = [instance]
                else:
                    groups[instance.general_id].append(instance)

            # close file
            csv_file.close()

        return (instances, groups)

    def writeFile(self, instances):
        output_filename = self.filename[:-4] + "-output.csv"

        with open(output_filename, 'w', newline = '') as fp:
            writer = csv.writer(fp)

            # create new header for output which consists of original data plus 2 sets of fields
            # corresponding to 2 potential options for replacement
            child_header1 = ["Down Size 1 - " + item for item in self.header]
            child_header2 = ["Down Size 2 - " + item for item in self.header]
            output_header = self.header + child_header1 + child_header2
            writer.writerow(output_header)
            for instance in instances:
                print(len(instance.children))
                row = instance.getRow()
                if row != None:
                    writer.writerow(row)
            fp.close()
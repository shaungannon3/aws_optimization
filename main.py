from instance import Instance
from filehandler import FileHandler
from dataprocessor import DataProcessor

def main(filename):

    fileHandler = FileHandler(filename)
    # read in file, get machine instances and machine groups
    instances, groups = fileHandler.readFile()

    # pass instances and groups to data processor for processing
    dataProcessor = DataProcessor(instances, groups)
    dataProcessor.process()

    # pass instances to writeFile method to write to output csv file
    fileHandler.writeFile(instances)


if __name__ == "__main__":
    main("AWS_pricing.csv")










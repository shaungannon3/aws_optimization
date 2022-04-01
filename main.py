from filehandler import FileHandler
from dataprocessor import DataProcessor

def main(filename):

    # create filehandler to handle I/O
    fileHandler = FileHandler(filename)
    
    # read in file, get instances (rows) and groups (rows with same general id)
    instances, groups = fileHandler.readFile()

    # pass instances and groups to data processor for processing
    dataProcessor = DataProcessor(instances, groups)
    dataProcessor.process()

    # pass instances to writeFile method to write to csv file
    fileHandler.writeFile(instances)


if __name__ == "__main__":
    main("AWS_pricing.csv")










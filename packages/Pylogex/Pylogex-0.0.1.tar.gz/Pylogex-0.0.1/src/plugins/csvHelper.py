
import csv
import logging

"""
This module  serves csv output functionality
"""
class csvOutput:
    def __init__(self,args,output_list) -> None:
        self.args = args
        self.defaultFileName = 'csvOutput.csv'
        self.output_list=output_list

    #Function to save csv output in file
    def csvOutput(self):

        #If list is empty
        if not self.output_list:
            raise Exception("No data found")

        name = str()

        #if output file name is not given
        if(self.args.outfile==None):
            name = self.defaultFileName
        else:
            name = self.args.outfile.name

        keys = self.output_list[0].keys()            
        #Writing in file
        with open(name, 'w', newline='') as outstream:
            writer = csv.DictWriter(outstream, fieldnames=keys)
            writer.writeheader()
            for log in self.output_list:
                writer.writerow(log)
                # print(log)
        logging.info("OUTPUT CSV FILE WRITTEN")
        return writer

    #Function to print csv on command line
    def csvCommandLineOutput(self):

        #If list is empty
        if not self.output_list:
            raise Exception("No data found")
        name = str()

        #If output file name is not provided
        if(self.args.outfile==None):
            name = self.defaultFileName
        else:
            name = self.args.outfile.name
        keys = list(self.output_list[0].keys())
        #Print group names
        print(",".join(keys))
        li = [list(out.values()) for out in self.output_list]
        res=[",".join(elm) for elm in li]
        [print (line) for line in res] 
        
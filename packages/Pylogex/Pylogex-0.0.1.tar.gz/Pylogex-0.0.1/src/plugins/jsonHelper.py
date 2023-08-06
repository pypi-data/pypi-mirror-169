
import json
import logging

"""
This module serves json output functionalities
"""

class jsonOutput:
    def __init__(self,args,output_list) -> None:
        self.args = args
        self.defaultFileName = 'jsonOutput.json'
        self.output_list=output_list

    #Function to save output in json file
    def jsonOutput(self):

        #If dictionary is empty
        if not self.output_list:
            raise Exception("No data found")

        name = str()
        #If output file name is not provided
        if(self.args.outfile==None):
            name = self.defaultFileName
        else:
            name = self.args.outfile.name

        json_object=json.dumps({"data": self.output_list},indent=4)
        #validating json_object creation
        if not (self.validateJSON(json_object)):
            raise Exception("Data not in Json Format")
        with open(name,'w') as fp:
            fp.write(json_object)
        logging.info('OUTPUT JSON FILE WRITTEN')

        return json_object

    #Function to print output on command line
    def jsonCommandLineOutput(self):

        logging.info(f"{self.output_list = }")
        #If dictonary is empty
        if not self.output_list:
            raise Exception("No data found")

        name = str()
        #If name of output file is not provided
        if(self.args.outfile==None):
            name = self.defaultFileName
        else:
            name = self.args.outfile.name

        json_object=json.dumps({"data": self.output_list},indent=4)
        #Checking validation of json_object created
        if not (self.validateJSON(json_object)):
            raise Exception("Data not in Json Format")

        logging.info(f"{json_object = }")

    #Function for validating Json Output
    def validateJSON(self,jsonData):
        try:
            json.loads(jsonData)
        except ValueError as err:
            return False
        return True
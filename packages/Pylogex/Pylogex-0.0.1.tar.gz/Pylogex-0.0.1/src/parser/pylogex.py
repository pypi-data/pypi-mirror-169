import argparse
import os
from sys import stdin
import sys
import logging
import regex
import pathlib
import output.csvHelper as csvHelper
import output.jsonHelper as jsonHelper
from utility_component import check_validity
logging.basicConfig(level=logging.INFO)

def main():

    parser = argparse.ArgumentParser(description="Utility to filter textual input stream based on regular expression pattern")
    parser.add_argument("REGEX", type=str, help="extract patterns matching this regular expressions from the input stream")
    parser.add_argument("-i", "--input=", dest="infile", type=open, help="read input (logs) from <INFILE>")
    parser.add_argument("-o", "--output=", dest="outfile", type=argparse.FileType('w', encoding='latin-1'), help="save the extracted data to <OUTFILE>")

    output_format_group = parser.add_mutually_exclusive_group()
    output_format_group.add_argument("-j", "--json", dest="j",  action="store_true", help="generate output in JSON format")
    output_format_group.add_argument("-c", "--csv", dest="c", action="store_true", help="generate output in CSV format (default)")
    
    #Extract cli argument passed
    input_filename = sys.argv[3]
    #check for valid file path
    check_file_path(input_filename)
    args = parser.parse_args()
    
    #checking for valid regex,i/p and o/p format
    check_validity(args)
    
    logging.info(f"CLI arguments are {args = }")
    print('1')
    process_input(args)
    print('2')

def check_file_path(filename):
    """
    This function checks if a file exists for reading the logs
    from with the given file path.
    """
    
    filename=f'{filename}'
    flag = os.path.exists(filename)
    print(flag)
    if flag is False:
        raise ValueError('''\033[1;31mInput File Path is wrong or file does not
             exist and please put full file name in quotation\033[00m''')

def process_input(args):
    
    if not args.infile:
        user_input = sys.stdin.read()
    else:
        with args.infile as file:
            user_input = file.read()
    
    logging.info(f"{user_input = }")

    #Output_dict is list of dictionaries
    output_dict=regex.regex_matcher(user_input, args.REGEX)  
    #if regex doesn't find matching pattern
    if(len(output_dict)==0):
        sys.exit('\033[1;31mGiven Regular Expression did not match with any line\nExiting...\033[00m')  

    #If output format expected is json
    if args.j:
        json_object = jsonHelper.jsonOutput(args, output_dict)
        if not args.outfile:
            json_object.jsonCommandLineOutput()
        else:
            json_object.jsonOutput()
    #If output format expected is csv
    else:
        csv_object = csvHelper.csvOutput(args, output_dict)
        #If output is expected in file
        if not args.outfile:
            csv_object.csvCommandLineOutput()
        #If output is expected on command line
        else:
            csv_object.csvOutput()


if __name__ == "__main__":
    main()

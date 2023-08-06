import re
import sys
from check_format import FileFormat

def check_validity(args):
    #checking validity of regex given
    try:
        re.compile(args.REGEX)
    except:
        sys.exit('\033[1;31mPlease Write valid Regex\033[00m')

    #checking validity of input file if provided
    if(args.infile):
        val = FileFormat.format(args.infile)
        if(val == False):

            sys.exit('\033[1;31mPlease Enter valid Input File format\033[00m')


    #checking validity of output file if generated
    if(args.outfile):
        val = FileFormat.format(args.outfile)
        if(val == False):
            sys.exit('\033[1;31mPlease Enter valid Output File format\033[00m')

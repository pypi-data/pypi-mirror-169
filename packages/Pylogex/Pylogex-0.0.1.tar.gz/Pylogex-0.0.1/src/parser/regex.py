import re
import logging
logging.basicConfig(level=logging.INFO)

"""
Functionality for regular expression matching
"""
def regex_matcher(text, regex):
    
    #List to store dictionaries
    output_list=[]
    try:
        pattern = re.compile(regex, re.VERBOSE)
        matches = re.finditer(pattern, text)
        for match in matches:
            record=match.groupdict()
            logging.info(f"Matched {record = }")
            output_list.append(record)
    except:
        raise TypeError("regex_matcher function arguments must be strings")
    
    return output_list
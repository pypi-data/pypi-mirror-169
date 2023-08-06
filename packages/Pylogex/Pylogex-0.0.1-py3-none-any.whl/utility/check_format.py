
"""
This module checks if the given file has a valid format
"""
class FileFormat:

    #This is a class for checking valid file format.
    def format(file_name) -> bool:
        
        #This function checks if the extension of a file is valid.
        valid_formats = ['.log','.csv','.dat','.json','.txt']
        for format in valid_formats:
            if file_name.name[-len(format):] == format:
                return True
        return False
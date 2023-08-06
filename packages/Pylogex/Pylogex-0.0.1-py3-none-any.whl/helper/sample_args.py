"""
Class for providing arguments to test functions
"""

class Args:
    def __init__(self,REGEX,infile,outfile,j,c) -> None:
        self.REGEX=REGEX
        self.infile=infile
        self.outfile=outfile
        self.j=j
        self.c=c


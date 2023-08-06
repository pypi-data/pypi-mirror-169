import unittest
import pylogex.output.csvHelper as csvHelper
import logging
import argparse
import sample_args
logging.basicConfig(level=logging.INFO)

"""
 To run all test files starting with test_ in tests/ directory,
run command: python3 -m unittest discover -s tests
"""

class TestCsvConverter(unittest.TestCase):

    """
    Test if output is none
    """
    def test_output_none(self):

        test_dict=[{
            "resource":"news",
            "id":"100"
        }]

        #Sample command line arguments
        args=sample_args.Args('(?P<resource>\w+)/(?P<id>\d+)',None,None,False,True)
        logging.info(args)
        csv_output=csvHelper.csvOutput(args,test_dict)
        csv_test_object=csv_output.csvOutput()
        logging.info(csv_test_object)
        self.assertIsNone(csv_test_object)

    def test_output_not_none(self):
        
        """
        Test if output is not none
        """
        #Dictionary for testing csv conversion
        test_dict=[{
            "resource":"news",
            "id":"100"
        }]
        args=sample_args.Args('(?P<resource>\w+)/(?P<id>\d+)',None,None,False,True)
        logging.info(args)
        csv_output=csvHelper.csvOutput(args,test_dict)
        csv_test_object=csv_output.csvOutput()
        logging.info(csv_test_object)
        self.assertIsNotNone(csv_test_object)

if __name__=='__main__':
    unittest.main()

import unittest
import pylogex.output.jsonHelper as jsonHelper
import logging
import sample_args
logging.basicConfig(level=logging.INFO)

"""
 To run all test files starting with test_ in tests/ directory,
run command: python3 -m unittest discover -s tests
"""


class TestJsonConverter(unittest.TestCase):
    
    def test_output_none(self):

        #Sample dictionary
        test_dict=[{
            "name":"python",
            "work":"project"
        }]

        #Sample command line arguments
        args=sample_args.Args('(?P<resource>\w+)/(?P<id>\d+)',None,None,True,False)
        json_output=jsonHelper.jsonOutput(args,test_dict)
        json_test_object=json_output.jsonOutput()
        logging.info(json_test_object)
        self.assertIsNone(json_test_object)

    def test_output_not_none(self):
        test_dict=[{
            "resouce":"news",
            "id":"100"
        }]
        args=sample_args.Args('(?P<resource>\w+)/(?P<id>\d+)',None,None,True,False)
        json_output=jsonHelper.jsonOutput(args,test_dict)
        json_test_object=json_output.jsonOutput()
        logging.info(json_test_object)
        self.assertIsNotNone(json_test_object)
        



if __name__=='__main__':
    unittest.main()


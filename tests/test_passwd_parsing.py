
from parsing import Parsing
import json

__author__ = 'Mohit Gadkari'

class Test_Parser:


    @classmethod
    def setup_class(cls):
        pass

    def test_with_valid_JSON_output(self):
        json_output = Parsing()
        assert json_output is not None


    def test_with_invalid_JSON(self):
        invalid_json = {
            "nobody": {
                "username": "Anobody",
                "uid": "-56",
                "full_name": "Unprivileged User",
                "groups": ""
            }}
        json_output = Parsing()
        assert json_output != invalid_json



# Count of user names in passwd file should match json file
# Error handling test case
# cron job










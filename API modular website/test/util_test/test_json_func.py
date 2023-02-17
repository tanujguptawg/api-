from util import json_functions

def test_readfile_correct_path():
    correct_path = "database/userdata.json"
    try:
        json_functions.JsonClass.read_json(correct_path)
        assert True
    except:
        assert False

def test_readfile_incorrect_path():
    correct_path = "userdata.json"
    try:
        json_functions.JsonClass.read_json(correct_path)
        assert False
    except:
        assert True
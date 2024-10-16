import json
def MainValues():
    with open('values.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    return json_object
badThings = 0
values = MainValues()
round = 1
ecology = values["begEcology"]
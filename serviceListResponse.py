from pprint import pprint


class serviceListResponse:
    def __init__(self,json_str):
        self.json_str=json_str
    def print_data(self):
        pprint(self.json_str)


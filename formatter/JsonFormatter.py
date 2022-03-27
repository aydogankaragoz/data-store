from formatter import Formatter
import json

class JsonFormatter(Formatter.Formatter):
    def serialize(self, data):
       return json.dumps(data)

    def deserialize(self, str):
       return json.loads(strs)
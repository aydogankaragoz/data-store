from destination import Destination
import json

class LocalDestination(Destination.Destination):
    def read(self):
       print("json serialize")

    def write(self, str):
        text_file = open("data.data", "w")
        text_file.write(str)
        text_file.close()
# Yes, built-in types are inherently thread-safe:
# http://docs.python.org/glossary.html#term-global-interpreter-lock


class DataStore:

    def __init__(self, formatter, destination):
        self.__formatter = formatter
        self.__destination = destination
        self.__data = {}

    def insert(self, *records):
        for record in records:
            key = record[0]
            value = record[1]
            self.__data[key] = value
        self.__commit()

    def retrieve(self, key): 
        return self.__data[key]

    def query(self, val, limit=0, offset=0):  # limit & offset
        result = list(filter(lambda key: (self.__data[key] == val), self.__data))
        if offset == 0:
            return result
        else:
            return result[offset:offset+limit]

    def update(self, record):
        key = record[0]
        value = record[1]
        self.__data[key] = value
        self.__commit()

    def delete(self, key):
        del self.__data[key]
        self.__commit()

    def __commit(self):
        self.__destination.write(
            self.__formatter.serialize(self.__data))





import abc
class Destination(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read') and
                callable(subclass.read) and
                hasattr(subclass, 'write') and
                callable(subclass.write) or
                NotImplemented)

    @abc.abstractmethod
    def read(self):
        raise NotImplementedError

    @abc.abstractmethod
    def write(self, str):
        raise NotImplementedError
import abc
class Formatter(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'serialize') and
                callable(subclass.serialize) and
                hasattr(subclass, 'deserialize') and
                callable(subclass.deserialize) or
                NotImplemented)

    @abc.abstractmethod
    def serialize(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def deserialize(self, str):
        raise NotImplementedError
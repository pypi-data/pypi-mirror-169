import boto3

class SingletonBaseClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonBaseClass, cls).__new__(cls)
        return cls.instance

class Boto3SessionSingleton(SingletonBaseClass):
    """
    example usage: `singletons.Boto3SessionSingleton().get_session()`

    Extends: SingletonBaseClass
    Args: N/A
    """

    def __init__(self):
        self.session = boto3.session.Session()

    def get_session(self):
        return self.session
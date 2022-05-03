# When to use class methods and when to use static methods?
# @staticmethod -> when we want to de something that should not be unique per instance
# @classmethod -> we need it for c instances from a structure data that we own
class Item:
    @staticmethod
    def it_integer(num):
        pass
    '''
    This should do something that has a relationship with the class
    '''
    @classmethod
    def instantiate_from_something(cls):
        pass
    '''
    This should also do something that has a relationship with the class,
    but usually, those are used to manipulate different structures of data to 
    instantiate objects, like we have done with CSV
    '''


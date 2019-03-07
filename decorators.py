'''
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass
    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
'''

def print_dec(f):
    def func_to_return(*args, **kwargs):
        print("args: {}; kwargs: {}".format(args, kwargs))
        val = f(*args, **kwargs)
        print("return: {}".format(val))
        return val
    return func_to_return

@print_dec
def foo(a):
    return a+1


result = foo(2)
print("Got the result: {}".format(result))
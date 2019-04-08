import time

class timing(object):

    def __init__(self, func):
        self.f = func
        
    def __call__(self, *args, **kwargs):
        
        start_time = time.time()

        if len(args) == 0 and len(kwargs) == 0:
            print("none")
            self.f()
        elif len(args) != 0 and len(kwargs) == 0:
            print("args")
            self.f(*args)
        elif len(args) == 0 and len(kwargs) != 0:
            print("kwargs")
            self.f(*kwargs)
        else:
            print("both")
            self.f(*args, **kwargs)

        # Print out statistics
        end_time = time.time()
        total_time = end_time - start_time
        print("Total runtime: {0:.4f}s".format(total_time))

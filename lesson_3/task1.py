import time

def decorator(number=3):

    def actual_decorator(func):

        def wrapper():
            Call = []
            i = 0
            sum_ = 0
            for i in range(number):
                start_time = time.time()
                result = func()
                end_time = time.time()
                Call.append(end_time - start_time)
                sum_ += (end_time - start_time)
            res = {
                'Every_Call': Call,
                'Total_Time': sum_,
                'Name': func.__name__,
                'Result': func()
            }
            return res
        return wrapper

    return actual_decorator
from datetime import datetime


def timer(func_name: str = ""):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = function(*args, **kwargs)
            end = datetime.now()
            print(
                "function {name} execution time: {time.seconds}s, {time.microseconds}ms".format(
                    name=func_name,
                    time=end - start
                )
            )
            return result
        return wrapper
    return decorator



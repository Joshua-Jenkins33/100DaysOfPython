def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function_arguments = [arg for arg in args]
        function_name = function.__name__
        function_output = function(*args)
        print(f"Function {function_name.upper()}{args}")
        print(f"And returned: {function_output}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c
    
a_function(1, 2, 3)
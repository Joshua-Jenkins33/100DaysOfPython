# import time
# current_time = time.time()
# print(current_time)

# def speed_calc_decorator(function):
#     def time_to_run():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} took {end_time - start_time} seconds to run.")
#     return time_to_run


# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
        
        
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

# fast_function()
# slow_function()

def make_bold(function):
    def add_b_tags():
        bold_html = f"<b>{function()}</b>"
        return bold_html
    return add_b_tags
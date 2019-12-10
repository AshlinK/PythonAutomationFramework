# import contextvars

""" This module provides to manage, store and access context-local state.
The ContextVar class is used to declare context variables"""

str_execution_id = None
str_output_log_folder_path = None
str_working_dir = None
dict_test_params = {}
arg_driver = None


# dict_test_params=contextvars.ContextVar("dict_test_params")


def add_to_dict_test(key, value):
    dict_test_params[key] = value


def get_dict_test_param(key):
    return dict_test_params.get(key)


def set_driver(driver):
    global arg_driver
    arg_driver = driver


def get_driver():
    return arg_driver


if __name__ == '__main__':
    pass

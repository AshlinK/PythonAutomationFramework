"""
Written by Ashlin Karkada
This is the main class which will be called first.
It will initialize and setup all the project configuration
required for the test run.

"""
import main.mainTest.MyLogger as mylogger
import main.store.Properties as property
from main.store.Constants import *

global Log
Log = mylogger.get_module_logger(__name__)


def initialize_html_reporting():
    pass


def final_tear_down():
    print("*" * 20, 'Tear down', "*" * 20)
    pass


def main_executor_runner(str_environment, str_test_type=None, str_functionality=None, str_num_of_sets=None):
    try:
        Log.info("Beginning execution of Automation")
        Log.info("Following is the config details of execution -")

        property.dict_test_params[Constants.PARAM_TEST_TYPE] = str_test_type
        property.dict_test_params[Constants.PARAM_NUM_OF_SETS] = str_num_of_sets
        property.dict_test_params[Constants.PARAM_COUNTRY] = str_environment
        property.dict_test_params[Constants.PARAM_FUNCTIONALITY] = str_functionality

        Log.info(property.dict_test_params)

        if property.dict_test_params['isActive'] == "true":
            pass
    except Exception as e:
        Log.critical("Exception occurred in main executor runner method ", e)


if __name__ == '__main__':
    main_executor_runner(str_environment='fenix_ZAMBIA-INT')

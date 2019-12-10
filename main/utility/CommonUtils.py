from datetime import datetime
from main.store.Constants import *
import os
import sys
import main.store.Configuration as config
import main.store.Properties as property
import main.mainTest.MyLogger as mylogger
from inspect import stack
from sys import argv

""" This is where common and frequently used project configuration methods will be available.
For example, take screen shot, timestamp, create output folder """

Log = mylogger.get_module_logger(__name__)


def get_current_timestamp(str_format):
    if str_format is not None:
        now = datetime.now()
        dt_string = now.strftime(str_format)
        return dt_string
    else:
        print("Date format not provided!!")


def create_output_folder():
    try:
        str_time_stamp = get_current_timestamp(Constants.FILE_SUFFIX_DATE_FORMAT_NO_SPACE)
        property.str_execution_id = str_time_stamp

        str_folder_name = Constants.LOG_FOLDER_PREFIX + "_" + str_time_stamp
        property.str_working_dir = Constants.USER_DIR
        property.str_output_log_folder_path = property.str_working_dir + "\\" + str_folder_name

        if not os.path.exists(property.str_output_log_folder_path):
            os.makedirs(property.str_output_log_folder_path)
            print("************** \t Output directory created \t ******************")
            obj_screenshots_folder = property.str_output_log_folder_path + "\\" + Constants.SCREENSHOT_FOLDER
            if not os.path.exists(obj_screenshots_folder):
                os.makedirs(obj_screenshots_folder)
                print("************** \t Screenshots folder is created \t***************")
                return property.str_output_log_folder_path, property.str_execution_id

            else:
                print("Failed to create screenshots folder")
                sys.exit(0)
        else:
            print("Failed to create TestOutputFolder!!")

    except Exception as e:
        print(e)


def transform_json_config_to_dict(str_environment) -> dict:
    if str_environment is not None:
        return config.get_config_as_dict(str_environment)
    else:
        print("Environment is not provided!!")


def log_start_test_case(str_testcase_name):
    Log.info("*" * 90)
    Log.info("\t \t \t \t" + str_testcase_name)
    Log.info("*" * 90)


def log_end_test_case(str_testcase_name):
    Log.info("*" * 90)
    Log.info("\t \t Execution completed for [{0}]".format(str_testcase_name))
    Log.info("*" * 90)


def take_screenshot(self, str_msg, driver):
    Log.info("Entering method: [{0}]".format(stack()[0][3]))
    str_time_stamp = get_current_timestamp(Constants.FILE_SUFFIX_DATE_FORMAT_NO_SPACE)
    driver.save_screenshot(
        property.str_output_log_folder_path + "\\" + Constants.SCREENSHOT_FOLDER + "\\" + str_msg + "_" + str_time_stamp + ".png")


def read_config(str_environment):
    """ This dictionary will hold you config parameters.(config.json). It will create a dict from config.json"""
    try:
        property.dict_test_params = transform_json_config_to_dict(str_environment)
    except Exception as e:
        Log.error("Exception occurred in read config method ", e)


def get_environment():
    environment = sys.argv[1].split('=')[1].split('_')[1].split()[0]
    return environment


def get_num_of_sets():
    num_of_sets = int(sys.argv[1].split('=')[1].split('_')[1].split()[1])
    return num_of_sets


if __name__ == '__main__':
    transform_json_config_to_dict()

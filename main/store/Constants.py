import os


class Constants:
    FILE_SUFFIX_DATE_FORMAT_NO_SPACE = "%d%m%Y%H%M%S"
    FILE_SUFFIX_DATE_FORMAT = "%d-%m-%Y- %H:%M:%S"
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    MAIN_DIR = os.path.dirname(FILE_DIR)
    USER_DIR = os.path.dirname(MAIN_DIR)
    LOG_FOLDER_PREFIX = "TestOutput\\TestOutput"
    SCREENSHOT_FOLDER = "screenshot"
    INPUT_DATA_FOLDER = "\\inputData\\"
    RESOURCES_FOLDER="\\resources\\"
    CONFIG_FILE = "\\config.json"
    CHROMEDRIVER_WIN = "\\chromedriver.exe"

    PARAM_TEST_TYPE = "test_type"
    PARAM_FUNCTIONALITY = "functionality"
    PARAM_NUM_OF_SETS = "numOfSets"
    PARAM_COUNTRY = "country"
    PARAM_ENVIRONMENT="environment"

    RESULT_FAIL="FAIL"
    RESULT_PASS="PASS"


if __name__ == '__main__':
    print(Constants.USER_DIR)

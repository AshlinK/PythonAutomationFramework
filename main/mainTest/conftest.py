from main.mainTest.MyLogger import *
import allure,allure_commons
from allure_commons.model2 import Status
from main.mainTest.TestExecutor import TestExecutor
from main.utility.CommonUtils import read_config, Constants, create_output_folder
import main.mainTest.MyLogger as my_logger
import pytest
from main.store.Properties import *

"""
Written by Ashlin Karkada
This is the file which will be run after the ini file
It will initialize and setup all the project configuration
required for the test run. It will also contain the code to control the before and after test run. 

"""

Log = my_logger.get_module_logger(__name__)


@pytest.fixture(name='setup', autouse=True, scope='session')
def before_test(pytestconfig):
    """ A session scope fixture named setup.
    It will run the steps before test execution until yield is encountered.
    After the test cases have ran successfully it will execute the steps after yield."""

    try:
        Log.info("Beginning execution of Automation")

        set_test_params(pytestconfig)
        str_environment = property.dict_test_params.get(Constants.PARAM_ENVIRONMENT)
        read_config(str_environment)

        Log.info("Following is the config details of execution -")
        Log.info(property.dict_test_params)

        Log.info("Log file configured at: {0}".format(pytestconfig.getoption("--log-file")))
        Log.info("Allure dir configured at: {0}".format(pytestconfig.getoption("--alluredir")))

        test_execute = TestExecutor()
        test_execute.test_set_up()

        yield  # This is where testing happens

        print("*" * 80)
        import os
        # command1 = "cd {}".format(pytestconfig.getoption("--alluredir"))
        # command2 = "allure generate {}".format(pytestconfig.getoption("--alluredir"))
        #
        # p = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
        # output, err = p.communicate()
        # p_status = p.wait()
        # p = subprocess.Popen(command2, stdout=subprocess.PIPE, shell=True)
        # output, err = p.communicate()
        # p_status = p.wait()
        # Teardown:
        print("Done executing tests")
    except Exception as e:
        print(e)


def set_test_params(pytestconfig):
    """This method will set the values of dict_test_params which will be used in the overall project"""

    functionality = pytestconfig.args[0].split('_')[0]
    environment, no_of_sets = tuple(get_environment(pytestconfig).split())

    add_to_dict_test(Constants.PARAM_NUM_OF_SETS, no_of_sets)
    add_to_dict_test(Constants.PARAM_FUNCTIONALITY, functionality)
    add_to_dict_test(Constants.PARAM_ENVIRONMENT, environment)


def get_environment(pytestconfig) -> str:
    """ This method returns the value assigned to the command line argument 'environment' """

    pytest.environment = pytestconfig.getoption("--environment")
    return pytest.environment


@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    """ Register argparse-style options and ini-style config values.
     Explicitly sets an additional command line argument called --environment"""

    parser.addoption("--environment", action="store", default="NONE", type=str,
                     help="Arguments required while running the test")


def pytest_cmdline_preparse(config, args):
    """  This method will parse the ini file then find and replace the values of add opts to dynamically
    report create folder and log file inside TestOutput folder"""
    print("**************\tCommand line preparser called \t **************")

    output_folder, execution_id = create_output_folder()
    my_logger.initialize_logging()
    args[args.index("--log-file=dummy")] = "--log-file=" + output_folder + "\\log_" + execution_id + ".log"
    args[args.index("--alluredir=dummy")] = "--alluredir=" + output_folder + "\\Reports\\"


#
# @pytest.fixture(scope='session')
# def logger_init() -> None:
#     parser = argparse.ArgumentParser()
#     parser.add_argument(name='--log-file', default=str_output_folder + "\\log_" + str_execution_id + ".log")
#     parser.parse_args()

def attach_file(request):
    allure.attach(source='', attachment_type=allure.attachment_type.TEXT)
    request.addfinalizer()


class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
            pass

    def emit(self, record):
        if record.levelname.lower() == 'error':
            @allure_commons.hookimpl(hookwrapper=True)
            def stop_step(self, uuid):
                self.allure_logger.stop_step(uuid,
                                             status=Status.FAILED)
        self.log("({}) -> {}".format(record.levelname, record.getMessage()))


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield

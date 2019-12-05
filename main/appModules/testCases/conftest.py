from main.mainTest.TestExecutor import TestExecutor
from main.mainTest.conftest import *
from main.utility.CommonUtils import read_config, Constants, create_output_folder
import subprocess
import main.mainTest.MyLogger as my_logger
import pytest
from main.store.Properties import *

global Log
Log = my_logger.get_module_logger(__name__)


@pytest.fixture(name='setup', autouse=True, scope='session')
def before_test(pytestconfig):
    print("Enter")
    """ A session scope fixture named setup.
    It will run the steps before test execution until yield is encountered.
    After the test cases have ran successfully it will execute the steps after yield."""

    try:
        # Before testing

        set_test_params(pytestconfig)
        str_environment = property.dict_test_params.get(Constants.PARAM_ENVIRONMENT)
        read_config(str_environment)

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

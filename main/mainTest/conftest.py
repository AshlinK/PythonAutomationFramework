from main.mainTest.MyLogger import *
import pytest
import allure
import allure_commons
from allure_commons.model2 import Status


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

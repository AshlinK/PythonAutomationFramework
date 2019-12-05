from main.appModules.functionalActions.FulfilmentHelper import FulfilmentHelper
import pytest
from main.mainTest.MyLogger import get_module_logger
from main.mainTest.TestExecutor import TestExecutor
from main.utility import CommonUtils
from main.utility.CommonUtils import log_start_test_case, log_end_test_case
from main.utility.ExcelUtils import *

Log = get_module_logger(__name__)


class TestFulfilment(TestExecutor):

    @pytest.mark.parametrize(argnames="key", argvalues=ExcelUtils.get_input_rows(__name__), scope='session')
    def test_execute(self, key):
        log_start_test_case(key['Testcasename'])

        if TestExecutor.i_count == 0:
            global obj_helper
            CommonUtils.log_start_test_case("Login to Application")
            obj_helper = FulfilmentHelper()
            # obj_helper.login_to_application(TestExecutor.str_user_name, TestExecutor.str_password)
        try:
            # obj_helper.do_something()
            # obj_helper.now_what()
            log_end_test_case(key['Testcasename'])
        except Exception as e:
            Log.error(e)
        finally:
            TestExecutor.i_count += 1

from inspect import stack
from main.mainTest.MyLogger import get_module_logger
from main.store.Properties import dict_test_params, get_dict_test_param
from main.store.Constants import *
from main.utility.WebDriverAdapter import WebDriverAdapter

Log = get_module_logger(__name__)


class TestExecutor:
    """ This class contains the setup and tear down of the test case
     execution."""

    obj_webdriver_adapter = None
    str_URL = None
    str_user_name = None
    str_password = None
    str_country = None
    str_browser = None
    obj_driver = None
    str_test_result = Constants.RESULT_FAIL
    i_count = 0

    @classmethod
    def test_set_up(cls):
        Log.info("Entering method: [{0}]".format(stack()[0][3]))
        try:
            cls.str_browser = get_dict_test_param('browser')
            cls.str_URL = get_dict_test_param('aut_url')
            cls.str_user_name = get_dict_test_param('aut_user')
            cls.str_password = get_dict_test_param('aut_pass')

            obj_webdriver_adapter = WebDriverAdapter()
            obj_webdriver_adapter.init_browser(cls.str_browser)
            obj_driver = obj_webdriver_adapter.get_obj_driver()
            obj_driver.get(cls.str_URL)

            Log.info("Beginning Setup for {0}".format(cls.str_browser))
        except Exception as e:
            Log.error(e)
        finally:
            pass

    def tear_down(self):
        Log.info("Entering method: [{0}]".format(stack()[0][3]))
        pass

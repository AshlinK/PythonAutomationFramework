from inspect import stack

import main.mainTest.MyLogger as mylogger
from main.utility.WebDriverAdapter import WebDriverAdapter

Log = mylogger.get_module_logger(__name__)


class FulfilmentHelper(WebDriverAdapter):

    def __init__(self):
        pass

    def login_to_application(self, str_username, str_password):
        Log.info("Entering method: [{0}]".format(stack()[0][3]))
        try:
            self.enter_text_box_value(str_element="txtUsername", str_data=str_username)
            self.enter_text_box_value(str_element="txtPassword", str_data=str_password)
        except Exception as e:
            print(e)
            Log.error("Error occurred during login to application ")
        finally:
            pass

    def now_what(self):
        pass

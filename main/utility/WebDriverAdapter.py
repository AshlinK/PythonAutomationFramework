from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

from main.mainTest.MyLogger import get_module_logger
from main.store.Constants import *
from main.store.Properties import set_driver, get_driver
from main.utility.ObjectRepoUtils import get_element_properties


class WebDriverAdapter:
    global log, driver
    log = get_module_logger(__name__)

    def init_browser(self, str_browser):

        if str_browser.casefold() == "chrome".casefold():

            options = webdriver.ChromeOptions()
            capabilities = options.to_capabilities()
            self.driver = webdriver.Chrome(
                executable_path=Constants.USER_DIR + Constants.RESOURCES_FOLDER + Constants.CHROMEDRIVER_WIN,
                desired_capabilities=capabilities)

            self.driver.maximize_window()
        elif str_browser.casefold() == "firefox".casefold():

            options = webdriver.FirefoxOptions()
            # options.add_argument()
            # options.add_argument()

            capabilities = options.to_capabilities()

            self.driver = webdriver.Firefox(desired_capabilities=capabilities)

        elif str_browser.casefold() == "ie".casefold():
            self.driver = webdriver.ie
        else:
            log.error("Browser not configured in setup!!")

        self.driver.maximize_window()
        # driver.set_page_load_timeout()
        # driver.set_script_timeout()
        # driver.implicitly_wait()
        set_driver(self.driver)

    @classmethod
    def get_obj_driver(cls):
        return get_driver()

    @staticmethod
    def enter_text_box_value(str_element, str_data):
        try:
            if str_data is not None:
                by, value = WebDriverAdapter.get_element(str_element)
                element = get_driver().find_element(by, value)
                log.info("Found textbox:[{0}]".format(str_element))
                element.clear()
                element.send_keys(str_data)

            else:
                log.info("No data for element:[{0}]".format(str_element))

        except Exception as e:
            log.error("Exception occurred ", e)


    @staticmethod
    def get_element(str_element):
        obj_element_properties = get_element_properties(str_element)
        if obj_element_properties is not None:
            str_by = obj_element_properties.get('by')
            str_identifier = obj_element_properties.get('identifier')
            value = str_identifier
            if value is not None:
                if str_by.lower() == "css":
                    return By.CSS_SELECTOR, value
                elif str_by.lower() == "xpath":
                    return By.XPATH, value
                elif str_by.lower() == "name":
                    return By.NAME, value
                elif str_by.lower() == "linktext":
                    return By.LINK_TEXT, value
                elif str_by.lower() == "id":
                    return By.ID, value
                elif str_by.lower() == "classname":
                    return By.CLASS_NAME, value
                elif str_by.lower() == "tagname":
                    return By.TAG_NAME, value
                elif str_by.lower() == "partiallinktext":
                    return By.PARTIAL_LINK_TEXT, value
                else:
                    log.error("Invalid element")
            else:
                log.error("Cannot find identifier named {0} in OR.xml".format(str_element))

        else:
            log.error("XML Element properties dict is NULL")
        return None


if __name__ == '__main__':
    pass

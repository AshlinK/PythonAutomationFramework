"""
Written by Ashlin Karkada

This file contains a method which is used to store the element properties
in a dict.

"""

import xml.etree.ElementTree as element_tree
import main.mainTest.MyLogger as my_logger
from main.store.Constants import *

root = element_tree.parse(source=Constants.USER_DIR + Constants.RESOURCES_FOLDER + "OR_FENIX.xml").getroot()
Log = my_logger.get_module_logger(__name__)


def get_element_properties(str_element_name) -> dict:
    if str_element_name is not None:
        dict_element = {}
        found = False
        if '.' in str_element_name:
            page_name, element_name = tuple(str_element_name.split('.'))
            for page in root.findall('.//page'):
                if page.get('name') == page_name:
                    found = True
                    for element in root.findall(".//page[@name='" + page_name + "']/element"):
                        dict_element['name'] = element.get('name')
                        dict_element['by'] = element.get('by')
                        dict_element['identifier'] = element.get('identifier')
                        break

        else:
            for element in root.findall(".//element"):
                if element.get('name') == str_element_name:
                    found = True
                    dict_element['name'] = element.get('name')
                    dict_element['by'] = element.get('by')
                    dict_element['identifier'] = element.get('identifier')
                    break

        if not found:
            print("Invalid element name or element name not present in DOM")
            return None
        else:
            return dict_element
    else:
        Log.error("Element name is none")


if __name__ == '__main__':
    pass

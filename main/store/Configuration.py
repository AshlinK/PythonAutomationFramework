import json
from main.store.Constants import *
import main.mainTest.MyLogger as mylogger

""" This file contains methods which convert json to a dict """

str_config_file_path = Constants.USER_DIR + Constants.RESOURCES_FOLDER + Constants.CONFIG_FILE


def get_config_as_dict(str_environment):
    global log
    log = mylogger.get_module_logger(__name__)

    output_dict = {}
    if str_environment is not None:
        with open(str_config_file_path, 'r') as f:
            dict_config = json.load(f)
        for environments in dict_config.keys():
            if isinstance(dict_config[environments], list):
                for value in dict_config[environments]:
                    if isinstance(value, dict):
                        if value.get('environment')==str_environment:
                            for child_value in value:
                                if isinstance(value[child_value], str):
                                    output_dict[child_value] = value[child_value]
                                elif isinstance(value[child_value], dict):
                                    for keys, values in zip(value[child_value].keys(), value[child_value].values()):
                                        output_dict[keys] = values

    if output_dict is not None:
        log.info("Converted json to dict")
        return output_dict


if __name__ == '__main__':
    pass

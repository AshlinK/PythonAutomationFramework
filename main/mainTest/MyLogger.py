import logging
import importlib
import main.store.Properties as property

importlib.reload(property)


def initialize_logging():
    if property.str_output_log_folder_path is not None and property.str_execution_id is not None:
        logging.basicConfig(
            filename=property.str_output_log_folder_path + "\\log_" + property.str_execution_id + ".log",
            format='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG)
        global console
        #console = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
                                      datefmt='%Y-%m-%d:%H:%M:%S')
        #console.setFormatter(formatter)


def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    return logger


if __name__ == '__main__':
    pass

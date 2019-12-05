import xlrd
import main.mainTest.MyLogger as my_logger
from main.store.Constants import *
from main.utility.CommonUtils import get_environment,get_num_of_sets


class ExcelUtils:
    """This class contains excel related methods used for reading from or writing to a file."""

    global log
    log = my_logger.get_module_logger(__name__)

    def __init__(self):
        pass

    @staticmethod
    def get_input_rows(functionality: str) -> dict:
        """
        This method opens an excel file and validates it.

        :param functionality: This parameter is the name of the file which will be derived from the class name.
        :return: It will return each row as a dict as a generator
        """
        try:

            functionality = functionality.split(".")[3].title().replace('_', '')

            file_path = Constants.USER_DIR + Constants.INPUT_DATA_FOLDER + "Data_" + functionality + ".xls"
            log.info("Reading data file...")
            with xlrd.open_workbook(file_path) as work_book:
                if work_book is not None:
                    log.info("Workbook object created...")

                    str_sheet_name = get_environment()

                    if str_sheet_name is not None:
                        if '_' in str_sheet_name:
                            str_sheet_name = str_sheet_name.split('_')[1].upper()
                            print(work_book.sheet_names())
                    else:
                        log.error("Sheet name is None")

                    sheet = work_book.sheet_by_name(str_sheet_name)
                    if sheet is None:
                        log.error("Sheet not found. Proceeding with default sheet.")
                        sheet = work_book.sheet_by_index(0)

                    num_rows = sheet.nrows
                    num_columns = sheet.ncols

                    i_required_rows = get_num_of_sets()

                    keys_header = [sheet.cell_value(0, cell).title() for cell in range(num_columns)]
                    # log.info("Keys are ", keys_header)

                    log.info("Available Rows:[" + str(num_rows) + "] # Required Rows:[" + str(i_required_rows) + "]")

                    for row in range(1, i_required_rows + 1):
                        row_cell = [
                            None if str(sheet.cell_value(row, col)).strip() == '' else sheet.cell_value(row, col)
                            for col in range(num_columns)]
                        yield dict(zip(keys_header, row_cell))

        except Exception as e:
            print("Exception occurred while reading excel file ", e)

    @staticmethod
    def get_column_names(functionality: str) -> list:
        """
             This method opens an excel file and returns the column names

             :param functionality: This parameter is the name of the file which will be derived from the class name.
             :return: It will return the column names in a list
             """
        try:
            str_file_path = Constants.USER_DIR + Constants.INPUT_DATA_FOLDER + "Data_" + functionality + ".xls"

            # ExcelUtils.log.info("Reading data file...")
            work_book = xlrd.open_workbook(str_file_path)

            if work_book is not None:
                print("Workbook object created...")

                str_sheet_name = "ZAMBIA-QA"  # dict_test_params.get('environment', None)

                if str_sheet_name is not None:
                    if '_' in str_sheet_name:
                        str_sheet_name = str_sheet_name.split('_')[1].upper()
                        print(work_book.sheet_names())

                sheet = work_book.sheet_by_name(str_sheet_name)
                if sheet is None:
                    print("Sheet not found. Proceeding with default sheet.")
                    sheet = work_book.sheet_by_index(0)

                num_columns = sheet.ncols

                keys_header = [sheet.cell_value(0, cell).title() for cell in range(num_columns)]

                return keys_header

        except Exception as e:
            print("Exception occurred while reading excel file ", e)


if __name__ == '__main__':
    print(ExcelUtils.get_input_rows("FulfilmentTest"))

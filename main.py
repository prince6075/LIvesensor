from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
from sensor.utilis import dump_csv_file_to_mongodb



# def test_exception():
#     try:
#         logging.info("error occur here diveded by zero")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)




if __name__ == "__main__":
    file_path = "C:/Users/princ/ML Project/LIvesensor/aps_failure_training_set1.csv"
    database_name = "ineuron"
    collection_name = "sensor"
    dump_csv_file_to_mongodb(file_path,database_name,collection_name)




    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)

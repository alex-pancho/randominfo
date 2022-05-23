import logging
import os
import sys
# import unittest
# from io import StringIO

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test_result.log')
logging.basicConfig(
    level=logging.DEBUG,
    filename=filename,
    filemode='w',
    format="%(asctime)s [%(levelname)s](%(funcName)s) %(message)s",  # :%(lineno)s
    datefmt="%Y-%m-%d %H:%M:%S")

log = logging.getLogger()
# stream_handler = logging.StreamHandler(sys.stdout)
# log.addHandler(stream_handler)
file_handler = logging.FileHandler(filename, encoding='utf8')
log.addHandler(file_handler)

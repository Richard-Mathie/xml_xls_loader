from nose.tools import assert_equal
from datetime import datetime

from xml_xls_loader import xmlxls_to_pd
import os


def test_load():
    fixture = os.path.join(os.path.dirname(__file__), 'test_file.xls')
    dat = xmlxls_to_pd(fixture)

    assert_equal(dat['Multi Line Column'][0], 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5')
    assert_equal(dat['Some Date'][0], datetime(2017,5,31,10,50,59))

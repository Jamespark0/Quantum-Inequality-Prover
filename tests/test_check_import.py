import sys

sys.path.insert(0, ".")

from classical import check_import


def test_msg():
    assert check_import.msg == "Hello world!"
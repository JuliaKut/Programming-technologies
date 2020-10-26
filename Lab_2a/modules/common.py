import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def func(x):
    if x:
        for x in range (0,101,2):
            print(x, end=" ")
    else:
        for x in range (1,100,2):
            print(x, end=" ")



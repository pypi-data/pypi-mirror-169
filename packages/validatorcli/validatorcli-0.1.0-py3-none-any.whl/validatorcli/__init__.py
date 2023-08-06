"""
    I provide the directory loader for validatorcli.

    My goal in life is to allow abtracted class/method loading.
"""


import pkg_resources


__version__ = pkg_resources.get_distribution('validatorcli').version

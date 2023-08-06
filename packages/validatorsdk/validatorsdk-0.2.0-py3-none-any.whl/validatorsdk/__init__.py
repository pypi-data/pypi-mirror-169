"""
    I provide the directory loader for prucloudsdk.

    My goal in life is to allow abtracted class/method loading.

    The problem I solve is how do we structure a SDK to allow it to not be
    limited to the validator but have an iterative growth path.
"""


import pkg_resources


__version__ = pkg_resources.get_distribution('validatorsdk').version

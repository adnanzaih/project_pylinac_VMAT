
import sys

__version__ = '2.2.6'
__version_info__ = (2, 2, 6)

# check python version
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    raise ValueError("Pylinac is only supported on Python 3.6+. Please update your environment.")

# import shortcuts

from pylinac.core import decorators, geometry, vmatIMAGE, io, mask, profile, roi, utilities
from pylinac.core.utilities import clear_data_files, assign2machine

from pylinac.vmat import DRMLC, DRGS


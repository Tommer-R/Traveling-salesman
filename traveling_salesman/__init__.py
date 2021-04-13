#  Copyright (c) 2021. | by: Tommer Rissin | github: github.com/Tommer-R
from datetime import date

from TSM_class import TSM
from __about__ import (__version__, __package_name__, __url__, __title__,
                       __author__, __copyright__, __description__)

__date__ = str(date.today())
__all__ = [
    'TSM',
    '__author__',
    '__version__',
    '__package_name__',
    '__url__',
    '__title__',
    '__copyright__',
    '__description__',
]

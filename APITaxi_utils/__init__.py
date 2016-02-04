# -*- coding: utf-8 -*-
VERSION = (0, 1, 0)
__author__ = 'Vincent Lara'
__contact__ = "vincent.lara@data.gouv.fr"
__homepage__ = "https://github.com/"
__version__ = ".".join(map(str, VERSION))
__doc__ = "A set of utils function used by APITaxi"


from .mixins import (AsDictMixin, HistoryMixin, unique_constructor,
        MarshalMixin, FilterOr404Mixin)
from .populate_obj import create_obj_from_json
from .request_wants_json import request_wants_json

get_columns_names = lambda m: [c.name for c in m.__table__.columns]

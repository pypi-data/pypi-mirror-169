#-*- coding:utf-8 -*-
#
# database/pickle_field.py
#
# This file is part of the NNGT project, a graph-library for standardized and
# and reproducible graph analysis: generate and analyze networks with your
# favorite graph library (graph-tool/igraph/networkx) on any platform, without
# any change to your code.
# Copyright (C) 2015-2022 Tanguy Fardet
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

""" Pickle field for peewee """

import sqlite3
import pickle

from playhouse.fields import BlobField


class PickledField(BlobField):

    def python_value(self, value):
        if isinstance(value, (bytearray, sqlite3.Binary)):
            value = bytes(value)
        return pickle.loads(value)

    def db_value(self, value):
        return sqlite3.Binary(pickle.dumps(value, 2))

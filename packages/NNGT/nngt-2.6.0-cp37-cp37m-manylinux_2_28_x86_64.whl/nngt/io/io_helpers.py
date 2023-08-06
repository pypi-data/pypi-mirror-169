#-*- coding:utf-8 -*-
#
# io/io_helpers.py
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

""" IO helpers """

import nngt
from nngt.lib import InvalidArgument


# ------------ #
# Saving tools #
# ------------ #

def _get_format(fmt, filename):
    if fmt == "auto":
        if filename.endswith('.gml'):
            fmt = 'gml'
        elif filename.endswith('.graphml') or filename.endswith('.xml'):
            fmt = 'graphml'
        elif filename.endswith('.dot'):
            fmt = 'dot'
        elif (filename.endswith('.gt') and
              nngt._config["backend"] == "graph-tool"):
            fmt = 'gt'
        elif filename.endswith('.nn'):
            fmt = 'neighbour'
        elif filename.endswith('.el'):
            fmt = 'edge_list'
        else:
            raise InvalidArgument('Could not determine format from filename '
                                  'please specify `fmt`.')
    return fmt


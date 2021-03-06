#
# Copyright 2003-2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

# The presence of this file turns this directory into a Python package

"""
Core contents.
"""

# This is the main GNU Radio python module.
# We pull the swig output and the other modules into the gnuradio.gr namespace

from runtime_swig import *
from exceptions import *
from top_block import *
from hier_block2 import *
from tag_utils import *
from gateway import basic_block, sync_block, decim_block, interp_block

# Force the preference database to be initialized
prefs = prefs.singleton

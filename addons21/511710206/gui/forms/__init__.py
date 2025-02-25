# -*- coding: utf-8 -*-
#
# field-autocomplete Add-on for Anki
# Copyright (C)  2025 RisingOrange
#
# This file was automatically generated by Anki Add-on Builder v1.0.0-dev.5
# It is subject to the same licensing terms as the rest of the program
# (see the LICENSE file which accompanies this program).
#
# WARNING! All changes made in this file will be lost!

"""
Shim that imports forms corresponding to runtime Qt version
"""

from typing import TYPE_CHECKING

from aqt.qt import qtmajor

if TYPE_CHECKING or qtmajor >= 6:
    from .qt6 import *  # noqa: F401
else:
    from .qt5 import *  # noqa: F401

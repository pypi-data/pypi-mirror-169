#!/usr/bin/python
########################################################################################################################
#
# Copyright (c) 2014, Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
#   disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#    following disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################################################################
"""
This module implements interface with BAG in skill language
"""
import laygo2.interface

def export(db, filename, cellname, scale=1e-3, reset_library=False, tech_library=None):
    skill_str=laygo2.interface.skill.export(db, filename, cellname, scale, reset_library, tech_library)
    """
    Export design(s) to BAG2.

    Parameters
    ----------
    db: laygo2.database.Library
        The library database to be exported.
    filename: str, optional
        The path of the intermediate skill scipt file.
    cellname: str or List[str]
        The name(s) of cell(s) to be exported.
    scale: float
        The scaling factor between laygo2's integer coordinats actual physical coordinates.
    reset_library: bool, optional
        If True, the library to export the cells is reset.
    tech_library: str, optional
        The name of technology library to be attached to the resetted library.

    Returns
    -------
    str: the string object contains corresponding skill scripts.
    """

    import bag
    prj=bag.BagProject()
    prj.impl_db._eval_skill('load("'+filename+'");1\n')
    print("Your design was generated in Virtuoso.")

    return skill_str


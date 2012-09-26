#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
# EID   : rp22566
# CSID  : rprater
# CS373 - Downing - Project #2
# ---------------------------

"""
To run the program
    % python RunPFD.py < RunPFD.in > RunPFD.out
    % chmod ugo+x RunPFD.py
    % RunPFD.py < RunPFD.in > RunPFD.out

To document the program
    % pydoc -w PFD
"""

# -------
# imports
# -------

import sys

from PFD import PFD_solve

# ----
# main
# ----

PFD_solve(sys.stdin, sys.stdout)

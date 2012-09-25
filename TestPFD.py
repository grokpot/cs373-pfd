#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
# EID   : rp22566
# CSID  : rprater
# CS373 - Downing - Project #2 - PFD
# ---------------------------

"""
To test the program:
    % python TestPFD.py >& TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_read_metadata, pfd_read_line, pfd_print, pfd_build_independents, pfd_build_output

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :

    # ----
    # read_metadata
    # ----
    def test_read_metadata1 (self) :
        r = StringIO.StringIO("5 4\n")
        a = [0, 0]
        b = pfd_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 5)
        self.assert_(a[1] == 4)

    def test_read_metadata2 (self) :
        r = StringIO.StringIO("0 0\n")
        a = [-1, -1]
        b = pfd_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_metadata3 (self) :
        r = StringIO.StringIO("1 2\n")
        a = [0, 0]
        b = pfd_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 2)

    def test_read_metadata4 (self) :
        r = StringIO.StringIO("100 100\n")
        a = [0, 0]
        b = pfd_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 100)

    def test_read_metadata5 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = pfd_read_metadata(r, a)
        self.assert_(b    == False)


    # ----
    # read_line
    # ----
    def test_read_line1 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("3 2 1 5\n")
        b = pfd_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[3] == [1,5])

    def test_read_line2 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("2 2 5 3\n")
        b = pfd_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[2] == [3,5])

    def test_read_line3 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("4 1 3\n")
        b = pfd_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[4] == [3])

    def test_read_line4 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("5 1 1\n")
        b = pfd_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[5] == [1])


    # ----
    # build_independents
    # ----
    def test_build_independents1 (self) :
        vertex_list = [[], [], [], [], [], []]
        independent_list    = [0, 0, 0, 0, 0, 0]
        pfd_build_independents(vertex_list, independent_list)
        self.assert_(vertex_list        == [[], [], [], [], [], []])
        self.assert_(independent_list   == [1, 1, 1, 1, 1, 1])

    def test_build_independents2 (self) :
        vertex_list = [[1, 2], [], [], [1], [], [1, 2, 3]]
        independent_list    = [0, 0, 0, 0, 0, 0]
        pfd_build_independents(vertex_list, independent_list)
        self.assert_(vertex_list        == [[1, 2], [], [], [1], [], [1, 2, 3]])
        self.assert_(independent_list   == [0, 1, 1, 0, 1, 0])

    def test_build_independents3 (self) :
        vertex_list = [[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5], [1,2,3]]
        independent_list    = [1, 1, 1, 1, 1, 1]
        pfd_build_independents(vertex_list, independent_list)
        self.assert_(vertex_list        == [[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5], [1,2,3]])
        self.assert_(independent_list   == [1, 1, 1, 1, 1, 1])


    # ----
    # eval
    # ----

#    def test_eval_1 (self) :
#        v = collatz_eval(1, 10)
#        self.assert_(v == 20)
#
#    def test_eval_2 (self) :
#        v = collatz_eval(100, 200)
#        self.assert_(v == 125)
#
#    def test_eval_3 (self) :
#        v = collatz_eval(201, 210)
#        self.assert_(v == 89)
#
#    def test_eval_4 (self) :
#        v = collatz_eval(900, 1000)
#        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        a = [0, 0, 0, 0]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "0 0 0 0")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        a = [1, 2, 3, 4]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "1 2 3 4")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        a = [1]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "1")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        a = [1, 2]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "1 2")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        a = [100, 100, 100, 100, 100, 100, 100, 100]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "100 100 100 100 100 100 100 100")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        a = []
        pfd_print(w, a)
        self.assert_(w.getvalue() == "")

    # -----
    # solve
    # -----

#    def test_solve1 (self) :
#        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
#        w = StringIO.StringIO()
#        collatz_solve(r, w)
#        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
#
#    def test_solve2 (self) :
#        r = StringIO.StringIO("1 1\n2 2\n1 2\n2 1\n")
#        w = StringIO.StringIO()
#        collatz_solve(r, w)
#        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n1 2 2\n2 1 2\n")
#
#    def test_solve3 (self) :
#        r = StringIO.StringIO("1 9999\n9999 10001\n99999 100000\n999999 1000000\n")
#        w = StringIO.StringIO()
#        collatz_solve(r, w)
#        self.assert_(w.getvalue() == "1 9999 262\n9999 10001 180\n99999 100000 227\n999999 1000000 259\n")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."

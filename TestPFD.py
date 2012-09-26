#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
#         Jose A Fernandez Jr
# EID   : rp22566
#         jaf2568
# CSID  : rprater
#         josef
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

from PFD import PFD_read_metadata, PFD_read_line, PFD_print, PFD_build_independents, PFD_build_output, PFD_solve

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
        b = PFD_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 5)
        self.assert_(a[1] == 4)

    def test_read_metadata2 (self) :
        r = StringIO.StringIO("0 0\n")
        a = [-1, -1]
        b = PFD_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_metadata3 (self) :
        r = StringIO.StringIO("1 2\n")
        a = [0, 0]
        b = PFD_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 2)

    def test_read_metadata4 (self) :
        r = StringIO.StringIO("100 100\n")
        a = [0, 0]
        b = PFD_read_metadata(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 100)

    def test_read_metadata5 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = PFD_read_metadata(r, a)
        self.assert_(b    == False)


    # ----
    # read_line
    # ----
    def test_read_line1 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("3 2 1 5\n")
        b = PFD_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[3] == [1,5])

    def test_read_line2 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("2 2 5 3\n")
        b = PFD_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[2] == [3,5])

    def test_read_line3 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("4 1 3\n")
        b = PFD_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[4] == [3])

    def test_read_line4 (self) :
        vertex_list = [[], [], [], [], [], []]
        r = StringIO.StringIO("5 1 1\n")
        b = PFD_read_line(r, vertex_list)
        self.assert_(b    == True)
        self.assert_(vertex_list[5] == [1])


    # ----
    # build_independents
    # ----
    def test_build_independents1 (self) :
        vertex_list = [[], [], [], [], [], []]
        independent_list    = [0, 0, 0, 0, 0, 0]
        PFD_build_independents(vertex_list, independent_list)
        self.assert_(vertex_list        == [[], [], [], [], [], []])
        self.assert_(independent_list   == [1, 1, 1, 1, 1, 1])

    def test_build_independents2 (self) :
        vertex_list = [[1, 2], [], [], [1], [], [1, 2, 3]]
        independent_list    = [0, 0, 0, 0, 0, 0]
        PFD_build_independents(vertex_list, independent_list)
        self.assert_(vertex_list        == [[1, 2], [], [], [1], [], [1, 2, 3]])
        self.assert_(independent_list   == [0, 1, 1, 0, 1, 0])

    def test_build_independents3 (self) :
        vertex_list = [[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5], [1,2,3]]
        independent_list    = [1, 1, 1, 1, 1, 1]
        PFD_build_independents(vertex_list, independent_list)
        self.assert_(vertex_list        == [[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5], [1,2,3]])
        self.assert_(independent_list   == [1, 1, 1, 1, 1, 1])


    # ----
    # build_output
    # ----
    def test_build_output1 (self) :
        vertex_list = [[], [], [], []]
        independent_list    = [1, 1, 1, 1]
        output_list = PFD_build_output(vertex_list, independent_list)
        self.assert_(vertex_list        == [[], [], [], []])
        self.assert_(independent_list   == [-1, -1, -1, -1])
        self.assert_(output_list        == [0, 1, 2, 3])

    def test_build_output2 (self) :
        vertex_list = [[], [], [1], [1, 2], [2], [3]]
        independent_list    = [1, 1, 0, 0, 0, 0]
        output_list = PFD_build_output(vertex_list, independent_list)
        self.assert_(vertex_list        == [[], [], [], [], [], []])
        self.assert_(independent_list   == [-1, -1, -1, -1, -1, -1])
        self.assert_(output_list        == [0, 1, 2, 3, 4, 5])

    def test_build_output3 (self) :
        vertex_list = [[], [2,4], [], [1,2,4], [2]]
        independent_list    = [1, 0, 1, 0, 0]
        output_list = PFD_build_output(vertex_list, independent_list)
        self.assert_(vertex_list        == [[], [], [], [], []])
        self.assert_(independent_list   == [-1, -1, -1, -1, -1])
        self.assert_(output_list        == [0, 2, 4, 1, 3])

    def test_build_output3 (self) :
        vertex_list = [[], [], [3,5], [1,5], [3], [1]]
        independent_list    = [1, 1, 0, 0, 0, 0]
        output_list = PFD_build_output(vertex_list, independent_list)
        self.assert_(vertex_list        == [[], [], [], [], [], []])
        self.assert_(independent_list   == [-1, -1, -1, -1, -1, -1])
        self.assert_(output_list        == [0, 1, 5, 3, 2, 4])

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        a = [0, 0, 0, 0, 0]
        PFD_print(w, a)
        self.assert_(w.getvalue() == "0 0 0 0")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        a = [0, 1, 2, 3, 4]
        PFD_print(w, a)
        self.assert_(w.getvalue() == "1 2 3 4")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        a = [0, 1]
        PFD_print(w, a)
        self.assert_(w.getvalue() == "1")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        a = [0, 1, 2]
        PFD_print(w, a)
        self.assert_(w.getvalue() == "1 2")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        a = [0, 100, 100, 100, 100, 100, 100, 100, 100]
        PFD_print(w, a)
        self.assert_(w.getvalue() == "100 100 100 100 100 100 100 100")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        a = []
        PFD_print(w, a)
        self.assert_(w.getvalue() == "")

        # -----
        # solve
        # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4")

        r = StringIO.StringIO("5 0\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 2 3 4 5")

        r = StringIO.StringIO("2 1\n2 1 1")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 2")



# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
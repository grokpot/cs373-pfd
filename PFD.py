#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
# EID   : rp22566
# CSID  : rprater
# CS373 - Downing - Project #2
# ---------------------------

# ------------
# pfd_read_metadata
# ------------
def pfd_read_metadata (r, a) :
    """
    reads the metadata header (line 0) from PFD input, indicating number of tasks and lines
    r is a reader
    a is an array of int
    a[0] will be num_tasks
    a[1] will be num_lines
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > -1
    assert a[1] > -1
    return True

# ------------
# pfd_read_lines
# ------------
def pfd_read_lines (r, vertex_list) :
    """
    reads a line of vertex (dependency) input
    r is a reader
    a is an array of ints, our graph vertex array
    The vertex array is ordered as an adjacency list such that access is constant time and each value is a list of dependencies
    """
    s = r.readline()
    if s == "" :
        return False
    l           = s.split()
    vertex      = int(l[0])
    num_preds   = int(l[1])
    preds_list  = []

    # Iterate through predecessors and add them to the vertex's list
    for index in range(2, 2 + num_preds):
        pred    = int(l[index])
        preds_list.append(pred)

    preds_list.sort()

    # add that predecessor list to the vertex in vertex_list
    vertex_list[vertex] =  preds_list

    return True



# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # pre-condition assertions
    assert i > 0
    assert j > 0
    # Make sure we're getting ints
    assert isinstance(i, int)
    assert isinstance(j, int)


    # post-condition assertions
    assert max_cycle_length > 0

    return max_cycle_length

# -------------
# pfd_print
# -------------

def pfd_print (w, output_list) :
    """
    prints the values of output_list
    w is a writer
    output_list is the list of dependencies in order of when they should be loaded
    """
    if len(output_list) > 0:
        for dependency in range(0, len(output_list)-1):
            w.write(str( output_list[dependency] ) + " ")
        w.write( str( output_list[len(output_list)-1] ) )
    else:
        w.write("")

# -------------
# PFD_solve
# -------------

def PFD_solve (r, w) :
    """
    read header, read lines, eval, print loop
    r is a reader
    w is a writer
    """

    PFD_read_metadata(r, a)
    try:
        num_tasks = a[0]
        num_lines = a[1]
    except Exception:
        print "There was a problem reading the metadata of your input."




    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)

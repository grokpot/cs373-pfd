#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
# EID   : rp22566
# CSID  : rprater
# CS373 - Downing - Project #2
# ---------------------------


"""
example independent list:
        [0, 1, 0, 0, 1, 1, 0]

example vertex_list:
        [ [], [1, 5, 7], [], [], [3, 6], [1, 3, 5, 6] ]
"""


# ------------
# pfd_read_metadata
# ------------
def pfd_read_metadata (r, metadata) :
    """
    reads the metadata header (line 0) from PFD input, indicating number of tasks and lines
    r is a reader
    a is an array of int
    a[0] will be num_tasks
    a[1] will be num_lines
    """
    input = r.readline()
    if input == "" :
        return False
    split_input = input.split()
    metadata[0] = int(split_input[0])
    metadata[1] = int(split_input[1])
    assert input[0] > -1
    assert input[1] > -1
    return True


# ------------
# pfd_read_line
# ------------
def pfd_read_line (r, vertex_list) :
    """
    reads a line of vertex (dependency) input
    r is a reader
    a is an array of ints, our graph vertex array
    The vertex array is ordered as an adjacency list such that access is constant time and each value is a list of dependencies
    """
    input = r.readline()
    if input == "" :
        return False
    split_input = input.split()
    vertex      = int(split_input[0])
    num_preds   = int(split_input[1])
    preds_list  = []

    # Iterate through predecessors and add them to the vertex's list
    for index in range(2, 2 + num_preds):
        pred    = int(split_input[index])
        preds_list.append(pred)

    # else sort and add that predecessor list to the vertex in vertex_list
    else:
        preds_list.sort()
        vertex_list[vertex] =  preds_list

    return True


def pfd_build_independents(vertex_list, independent_list):
    # TODO: write method description
    assert len(vertex_list) > 0
    assert len(independent_list) > 0

    for index, vertex in enumerate(vertex_list):
        # if the vertex has no predecessors, add it to the independent list
        if vertex == []:
            independent_list[index] = 1


def pfd_build_output(vertex_list, independent_list):
    """
    Processes the task graph and returns a list of tasks which can be loaded in sequential order according to their dependencies.
    vertex_list is a list of tasks and their predecessors
    independent_list is a list of tasks with no predecessors

    Step 1: Find a vertex with no predecessors
    Step 2: The next vertex is a node with all predecessors satisfied
    Step 3: Upon a choice of verticies, choose the one with a smaller value (number)
    """
    ADDED       = -1
    DEPENDENT   = 0
    INDEPENDENT = 1


    output_list = []

    # We'll be done processing when our independent_list is clear
    cleared = False
    while cleared == False:

        # Find the lowest task in independent_list (the lowest task with no/satisfied predecessors)
        task = -1

        try:
            # Finds the lowest independent index
            task = independent_list.index(INDEPENDENT)
# TODO: use start parameter for enumerate to bypass 0 index
#        for independent_index, status in enumerate(independent_list):
#            if status == INDEPENDENT:
#                task = independent_index
            output_list.append(task)
            independent_list[task] = ADDED

            # Iterate through vertex list and remove dependency from other tasks' predecessors lists
            for vertex_index, pred_list in enumerate(vertex_list):
                try:
                    # Remove the dependency
                    pred_list.remove(task)

                    # If the task has no more predecessors
                    if pred_list == []:
                        # Add it to the independent list & sort
                        independent_list[vertex_index] = 1
                except Exception:
                    pass
        except:
            # TODO: do something here
            pass
        if DEPENDENT not in independent_list and INDEPENDENT not in independent_list:
            cleared = True

    return output_list



# ------------
# collatz_eval
# ------------

#def collatz_eval (i, j) :
#    """
#    i is the beginning of the range, inclusive
#    j is the end       of the range, inclusive
#    return the max cycle length in the range [i, j]
#    """
#    # pre-condition assertions
#    assert i > 0
#    assert j > 0
#    # Make sure we're getting ints
#    assert isinstance(i, int)
#    assert isinstance(j, int)
#
#
#    # post-condition assertions
#    assert max_cycle_length > 0
#
#    return max_cycle_length


# -------------
# collatz_eval2
# -------------
#def pfd_eval():
#
#    # example list
#    m = [[], [2, 4], [0, 4], [2], [0]]
#
#    # initialize array
#    mSize = [0]*(len(m))
#
#    a = ""
#
#    i =0
#    while(i<len(m)):
#        mSize[i] = len(m[i])
#        i+=1
#
#
#    x = 0
#    j = 0
#    while(j<len(m)):
#        temp = len(m)
#        nextN = len(m)
#        i = 0
#        while(i<len(m)):
#            x = 0
#
#            if(mSize[i]==0):
#                temp = i
#
#                if(temp<nextN):
#                    print temp
#                    nextN = temp
#            i+=1
#
#            if(i == len(m)):
#
#
#                while(x < len(m)):
#
#                    #print nextN
#                    if((nextN) in m[x]):
#                        #print nextN
#                        mSize[x] -= 1
#                    x+=1
#
#        j+=1
#        mSize[nextN] -=1
#        print mSize
#
#
#        a += str(nextN)
#
#    print a



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
        # Because of n being 1..n, we don't output the 0 index
        for task in range(1, len(output_list)-1):
            w.write(str( output_list[task] ) + " ")
        w.write( str( output_list[len(output_list)-1] ) )
    else:
        w.write("")

# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
    """
    read header, read lines, eval, print loop
    r is a reader
    w is a writer
    """

    # Read metadata (number of tasks and number of lines)
    metadata    = [-1, -1]
    pfd_read_metadata(r, metadata)
    num_tasks   = -1
    num_lines   = -1
    try:
        num_tasks = metadata[0]
        num_lines = metadata[1]
    except Exception:
        print "There was a problem reading the metadata of your input."

    # Assert that we received valid input
    assert num_tasks > 0
    assert num_lines > 0

    # Instantiate our graph lists
    vertex_list     = [[]]*(num_tasks + 1)
    independent_list = [0]*(num_tasks + 1)

    # Read vertex data and build graph
    for line in range(0, num_lines):
        pfd_read_line(r, vertex_list)

    # Instantiate the independent list
    pfd_build_independents(vertex_list, independent_list)

    # Build output
    output_list = pfd_build_output(vertex_list, independent_list)

    # Print output
    pfd_print(w, output_list)


